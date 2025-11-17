import ast
import json
import logging
import socket
from pathlib import Path

from dpapi_ng import ncrypt_unprotect_secret
from ldap3 import ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, Connection

from collector.dns_context import DNSContext
from collector.model.ad_objects import AdComputer, AdData, AdObject
from collector.model.exporter import JsonExporter
from collector.model.post_processor import AdDomainPostProcessor, LocalPostProcessor
from collector.utils import ADContext
from collector.windows.ad.active_directory_utils import (
    LAPSPasswordBlob,
    LDAPFilter,
    ModelAttributesFilter,
    map_model,
    sanitize_ldap_entry,
)
from collector.windows.ad.computer import Computer
from collector.windows.ad.ldap_authentication import LDAPAuthFactory
from collector.windows.processor import collect_remote_host
from collector.windows.utils import init_krb_context, query_srv_record, resolve_ip

logger = logging.getLogger(__name__)


def get_dict_from_object_class(
    conn: Connection, domain: str, object_class: LDAPFilter, attr_filter: list[str] | None = None
):
    search_base = f"DC={domain.replace('.', ',DC=')}"
    search_filter = object_class

    if attr_filter is None:
        attributes = [ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES]
    else:
        attributes = attr_filter
    conn.search(search_base, str(search_filter), attributes=attributes)

    result = {}
    if conn.entries:
        for entry in conn.entries:
            entry_dict = sanitize_ldap_entry(entry)
            dn = entry_dict.pop("distinguishedName")
            result[dn] = entry_dict
            missing = [k for k, v in result[dn].items() if v is None]
            if missing:
                logger.warning(f"{object_class.value} {entry.entry_dn} : missing fields -> {missing}")
        return result

    return None


def get_ad_obj_list_from_object_class(
    conn: Connection, domain: str, object_class: LDAPFilter, attr_filter: list[str] | None = None
) -> list[AdObject]:
    search_base = f"DC={domain.replace('.', ',DC=')}"
    attributes = attr_filter or [ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES]
    conn.search(search_base, str(object_class), attributes=attributes)

    objects: list[AdObject] = []
    if conn.entries:
        for entry in conn.entries:
            entry_dict = sanitize_ldap_entry(entry)
            entry_dict.pop("distinguishedName", None)
            missing = [k for k, v in entry_dict.items() if v is None]
            if missing:
                logger.warning(f"{object_class.value} {entry.entry_dn} : missing fields -> {missing}")
            try:
                obj = map_model[object_class](**entry_dict)
                objects.append(obj)
            except Exception as e:
                logger.error(f"Does not work {object_class.value} and {entry_dict.items()}")
                logger.error(f"Exception : {e}")
    return objects


def get_ad_obj_from_object_class(
    conn: Connection, domain: str, object_class: LDAPFilter, attr_filter: list[str] | None = None
) -> dict[str, AdObject] | None:
    search_base = f"DC={domain.replace('.', ',DC=')}"
    search_filter = object_class

    if attr_filter is None:
        attributes = [ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES]
    else:
        attributes = attr_filter
    conn.search(search_base, str(search_filter), attributes=attributes)

    result: dict[str, AdObject] = {}
    if conn.entries:
        for entry in conn.entries:
            entry_dict = sanitize_ldap_entry(entry)
            dn = entry_dict.get("distinguishedName")
            missing = [k for k, v in entry_dict.items() if v is None]
            if missing:
                logger.warning(f"{object_class.value} {entry.entry_dn} : missing fields -> {missing}")
            try:
                object = map_model[object_class](**entry_dict)
                result[dn] = object
            except Exception as e:
                logger.error(f"Does not work {object_class.value} and {entry_dict.items()}")
                logger.error(f"Exception : {e}")

        return result

    return None


def get_laps_data(
    conn: Connection, domain: str, dc_ip: str, username: str, password: str
) -> dict[str, str | None] | None:
    # TODO : Refactor this function
    laps_data = get_dict_from_object_class(
        conn, domain, LDAPFilter.COMPUTER_OBJECT, ["distinguishedName", "ms-MCS-AdmPwd"]
    )
    logger.debug("Fetching LAPS legacy attributes returned")
    logger.debug(laps_data)
    is_empty = all(not v for v in laps_data.values())
    flattened: dict[str, str | None]
    if not is_empty:
        # TODO: Can LAPS Legacy attributes coexist with new LAPS attributes ?
        flattened = {k: (v.get("ms-Mcs-AdmPwd") if v else None) for k, v in laps_data.items()}
        logger.debug(f"Laps Legacy password found: \n {laps_data}")
        return flattened
    

    logger.warning("No LAPS Legacy data found, trying with LAPS")
    laps_data = get_dict_from_object_class(
        conn, domain, LDAPFilter.COMPUTER_OBJECT, ["distinguishedName", "msLAPS-Password"]
    )
    is_empty = all(not v for v in laps_data.values())
    if not is_empty:
        flattened = {k: (v.get("msLAPS-Password") if v else None) for k, v in laps_data.items()}
        return flattened

    logger.warning("Cannot get the plain text password, trying to fetch the key")
    laps_data = get_dict_from_object_class(
        conn, domain, LDAPFilter.COMPUTER_OBJECT, ["distinguishedName", "msLAPS-EncryptedPassword"]
    )
    is_empty = all(not v for v in laps_data.values())
    if is_empty:
        logger.error("Cannot get any LAPS attributes")
        return None

    flattened = {k: (v.get("msLAPS-EncryptedPassword") if v else None) for k, v in laps_data.items()}
    for dn, unformated_blob in flattened.items():
        if unformated_blob is None:
            logger.warning(f"Cannot retrieve LAPS attribute for {dn}")
            flattened[dn] = None
            continue
        try:
            binary_blob = ast.literal_eval(unformated_blob)
            laps_encrypted = LAPSPasswordBlob(binary_blob)
            # TODO : Test with Kerberos
            bytes_result = ncrypt_unprotect_secret(
                laps_encrypted.encrypted_password, dc_ip, username, password, auth_protocol="ntlm"
            )
            json_result = bytes_result.decode("utf-16").strip("\x00")
            result: dict = json.loads(json_result)
            flattened[dn] = result.get("p")
        except Exception as e:
            logger.warning(f"Error when decrypted the LAPS key of {dn}: {e}")
            flattened[dn] = None
            continue
    return flattened


def active_directory_collect(context: ADContext) -> int:
    dns_configured = False
    dns_context = DNSContext()
    kdc_ip = None
    try:
        dc_hostname = socket.gethostbyaddr(context.dc_ip)[0]
        dns_configured = True
    except socket.herror:
        logger.info(f"Nameserver are not configured for domain {context.domain}")

    if not dns_configured:
        dc_hostnames = query_srv_record(f"_ldap._tcp.dc._msdcs.{context.domain}", context.dc_ip)
        if dc_hostnames is None:
            logger.error(f"Failed to get the hostname of the domain controller {context.dc_ip}")
            return 1
        # Todo improve this message
        logger.debug(f"Found {dc_hostnames}")
        dc_hostname = dc_hostnames[0].removesuffix(".")
        dns_context.hosts[dc_hostname] = context.dc_ip
        dns_context.init()

    if {context.host_auth_method, context.ldap_auth_method} & {"kerberos", "spnego"}:
        # https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/c1987d42-1847-4cc9-acf7-aab2136d6952
        # We want to get the kdc ip in case of user does not provide it
        kdc_hostnames = query_srv_record(f"_kerberos._tcp.{context.domain}", context.dc_ip)
        if kdc_hostnames is None or not kdc_hostnames:
            logger.error("Cannot resolve KDC hostname")
            return 1
        kdc_ip = resolve_ip(kdc_hostnames[0], context.dc_ip)
        init_krb_context(context.dc_ip, context.domain, kdc_ip, context.output_directory)

    ldap_auth = LDAPAuthFactory.create(
        context.ldap_auth_method, dc_hostname, context.domain, context.username, context.password, kdc_ip
    )
    if ldap_auth is None:
        logger.error("Cannot initialize DC Connection")
        return 1

    conn = ldap_auth.get_ldap_connection()

    if conn is None:
        logger.info(f"Cannot initialize DC Connection with the {context.ldap_auth_method} method")
        return 1

    logger.info("Starting LDAP data collection")

    ad_object: dict = {}
    ldap_filters = [
        LDAPFilter.COMPUTER_OBJECT,
        LDAPFilter.AD_GROUPS_OBJECT,
        LDAPFilter.AD_USER_OBJECT,
        LDAPFilter.GPO_OBJECT,
        LDAPFilter.OU_OBJECT,
        LDAPFilter.FSP_OBJECT,
    ]

    attr_filters = [
        ModelAttributesFilter.COMPUTER.value,
        ModelAttributesFilter.AD_GROUPS.value,
        ModelAttributesFilter.AD_USER.value,
        ModelAttributesFilter.AD_GPO.value,
        ModelAttributesFilter.AD_OU.value,
        ModelAttributesFilter.AD_USER.value,
    ]

    for ldap_filter, attr_filter in zip(ldap_filters, attr_filters):
        data = get_ad_obj_from_object_class(conn, context.domain, ldap_filter, attr_filter)
        if data is not None:
            ad_object.update(data)

    ad_data = AdData.from_dict(context.domain, ad_object)
    data_export = ad_data
    ldap_anonymizer: AdDomainPostProcessor | None = None
    if context.privacy:
        ldap_anonymizer = AdDomainPostProcessor(ad_data)
        data_export = ldap_anonymizer.process()

    export_dir = f"./{context.output_directory}/ad/{context.domain}"
    Path(export_dir).mkdir(parents=True, exist_ok=True)

    ldap_exporter = JsonExporter(f"{export_dir}/", privacy=context.privacy, indent=4)
    for key, data in data_export.__dict__.items():
        ldap_exporter.export(data, f"{key}.json")

    ldap_exporter.export(data_export, "all.json")
    if context.privacy and ldap_anonymizer is not None:
        ldap_exporter.export(ldap_anonymizer.mapping["guid"], "guid_mapping.json")
        ldap_exporter.export(ldap_anonymizer.mapping["sid"], "sid_mapping.json")

    logger.info("End LDAP data collection")

    laps_data: dict[str, str | None] | None = None
    if context.laps:
        logger.info("Starting LAPS collection")
        laps_data = get_laps_data(conn, context.domain, context.dc_ip, context.username, context.password)
        logger.info("End of LAPS collection")

    targets: list[Computer] = []
    ipv4_adrrs = {}
    logger.info("Starting domain name resolution")
    computers: dict[str, AdComputer] = {
        dn: computer for dn, computer in ad_object.items() if isinstance(computer, AdComputer)
    }
    for (dn, computer), anonymous in zip(computers.items(), data_export.computers):
        hostname = computer.dNSHostName
        if hostname is None or not hostname:
            logger.warning(f"Host collection for computer {computer.name} will be skipped due to missing domain name.")
            continue

        ipv4 = resolve_ip(hostname, context.dc_ip)

        dns_context.hosts[hostname] = ipv4
        ipv4_adrrs[computer.name] = ipv4

        dir_name = anonymous.name if context.privacy else computer.name
        local_exporter = JsonExporter(
            f"./{context.output_directory}/computers/{dir_name}", privacy=context.privacy, indent=4
        )

        local_anonymizer: None | LocalPostProcessor = None
        if ldap_anonymizer is not None:
            local_anonymizer = LocalPostProcessor(ldap_anonymizer.mapping["sid"])

        if context.laps and laps_data is not None:
            # FIXME: localization problem
            password = laps_data.get(dn)
            logger.debug(f"[LAPS] password for {computer.dNSHostName} is {password}")
            logger.debug("[LAPS] This message will be erase in the future")
            if password is None:
                logger.warning(f"Skipping {hostname}, LAPS password not found")
                continue
            target = Computer(dn, ipv4, "Administrator", password, hostname.lower(), local_exporter, local_anonymizer)
        else:
            target = Computer(
                dn, ipv4, context.username, context.password, hostname.lower(), local_exporter, local_anonymizer
            )

        targets.append(target)

        logger.debug(f"Found {computer.name}, Hostname: {hostname}, IPv4: {ipv4}")
    logger.info("End domain name resolution")

    with open(f"{export_dir}/ip_addresses.json", "w") as fd:
        json.dump(ipv4_adrrs, fd, default=str, indent=4)

    if context.filter_hosts is not None:
        filter_set = {host.lower() for host in context.filter_hosts}
        filtered_hosts: list[Computer] = []
        for host in targets:
            if host.hostname.lower() in filter_set:
                filtered_hosts.append(host)
            else:
                logger.info(f"Skipping host {host.hostname} (not in filter list")
        targets = filtered_hosts

    if context.host_collection and targets:
        logger.info(f"Starting collection on {len(targets)} remote hosts")
        collect_remote_host(targets, context)
        logger.info("Ending collection on remote hosts")

    logger.info(f"End of collection result are available in {context.output_directory}")
    return 0
