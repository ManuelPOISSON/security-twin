import logging
import sys
from collections import defaultdict
from pathlib import Path

from model.db import engine_base_path, reset_db
from model.db_connect import connection_cred

from model.fill_db import DBPopulate
from parse_data.parser_ad_groups import ParserADGroups
from parse_data.parser_ad_users import ParserADUsers
from parse_data.parser_computers import ParserComputers
from parse_data.parser_local_groups import ParserLocGroups
from parse_data.parser_rdp import ParserRDP
from parse_data.parser_services import ParserServices
from parse_data.parser_local_users import ParserLocUsers

from model import ADDomain
from parse_data.parser_software import ParserSoftware
from parse_data.parser_wmi import ParserWMI
from model.select_in_db import select_all_adusers_names


def extend_local_users(local_users: dict[str, str], new_lu_and_rights) -> None:
    """
    Modifies 'local_users' by adding some user/'' (empty pwd) with NT local users.
    """
    local_users.update({ParserServices.DEFAULT_RUN_BY: ""})
    local_users.update(
        {
            sp: ""
            for sp_ace in new_lu_and_rights
            for sp in sp_ace.keys()
            if sp.startswith("NT ") or sp.startswith("APPLICATION PACKAGE AUTHORITY")
        }
    )


def safe_parse(parser_callable, *args, default=None, **kwargs):
    """Utility to call .parse() on a parser, handling FileNotFoundError."""
    try:
        return parser_callable(*args, **kwargs).parse()
    except FileNotFoundError as e:
        logging.warning(str(e))
        return default


def populate_machine(
    db_populate: DBPopulate, path_machine: Path, ad_domain_name: str
) -> None:
    """Populate the database with a machine and its ADMachine."""
    machine_name = path_machine.name.split("CN=")[1].split(",")[0]
    logging.debug(f"Populating machine {machine_name} in domain {ad_domain_name}")

    local_users = safe_parse(ParserLocUsers, path_machine, default={})
    logging.debug(f"{path_machine} Found {len(local_users)} local users")
    local_groups, nt_local_users, ad_users_extra = safe_parse(
        ParserLocGroups,
        path_machine,
        domain_name=ad_domain_name,
        default=(defaultdict(list), [], []),
    )

    local_users.update({nt_user: "" for nt_user in nt_local_users})
    logging.debug(
        f"Extended local users for {machine_name}: {len(local_users)} {local_users}"
    )

    services, files = safe_parse(
        ParserServices,
        path_machine,
        ad_domain_name.split(".")[0].upper(),
        default=([], {}),
    )

    if services:
        extend_local_users(local_users, files.values())
    logging.debug(f"Found {len(services)} services {services}")
    # logging.debug(f"Found files {files}")
    softwares = safe_parse(ParserSoftware, path_machine, default=[])
    logging.debug(f"Found {len(softwares)} sofwares")

    has_rdp = safe_parse(ParserRDP, path_machine, default=False)
    wmi_root_cimv2, local_groups_extra, nt_local_users = safe_parse(
        ParserWMI, path_machine, default=({}, {}, [])
    )
    local_users.update({nt_user: "" for nt_user in nt_local_users})
    local_users.update({"IUSR": ""})  # IUSR is a default local user in Windows

    logging.debug(f"Found WMI root CIMv2 rights: {wmi_root_cimv2}")
    logging.debug(f"{local_groups_extra=}")
    local_groups = {
        **local_groups,
        **{
            lg_name: local_groups[lg_name] + members
            for lg_name, members in local_groups_extra.items()
        },
    }
    DEFAULT_LOCAL_GROUPS = {
        "Users",
    }
    for default_group in DEFAULT_LOCAL_GROUPS:
        if default_group not in local_groups:
            local_groups[default_group] = []
    logging.debug(f"Local groups for {machine_name}: {local_groups}")
    pruned_ad_users_extra = [
        ad_user
        for ad_user in ad_users_extra
        if ad_user.name not in select_all_adusers_names(db_populate.engine)
    ]
    db_populate.add_adusers(pruned_ad_users_extra)
    db_populate.add_localusers(machine_name, local_users)
    db_populate.add_localgroups_current_machine(machine_name, local_groups)
    db_populate.add_service(machine_name, services)
    db_populate.add_files(machine_name, files)
    db_populate.add_all_softwares(machine_name, softwares)
    if has_rdp:
        db_populate.add_rdp(machine_name)
    db_populate.add_psremote(machine_name)
    for ug_rootcim, rights in wmi_root_cimv2.items():
        db_populate.add_root_cimv2(machine_name, ug_rootcim, rights)

    """
        if "saved_creds" in attributes:
            for can_runas, users_impersonated in attributes["saved_creds"].items():
                db_populate.add_runas_creds(
                    win_machine_name, can_runas, users_impersonated
                )
        if "gporesult" in attributes:
            db_populate.add_gporesult(win_machine_name, attributes["gporesult"])
        if "psremote" in attributes and attributes["psremote"]:
            print(f"add psremote to {win_machine_name}")
            db_populate.add_psremote(win_machine_name)
        if "software" in attributes and attributes["software"]:
            db_populate.add_all_softwares(win_machine_name, attributes["software"])
    """


def populate_all_machines(
    db_populate: DBPopulate, dir_ldap: Path, ad_domain_name: str
) -> None:
    """Populate the database with all machines in the directory."""
    for machine_dir in dir_ldap.iterdir():
        if machine_dir.is_dir() and machine_dir.name.startswith("CN="):
            # logging.debug(f"Checking machine directory: {machine_dir}")
            populate_machine(db_populate, machine_dir, ad_domain_name)


def get_dir_ldap() -> Path:
    dir_ldap = None
    if sys.argv and len(sys.argv) > 1:
        dir_ldap = Path(sys.argv[1])

    if not (dir_ldap and dir_ldap.is_dir()):
        raise FileNotFoundError(f"{dir_ldap=} is not a directory.")
    return dir_ldap


if __name__ == "__main__":

    dir_ldap = get_dir_ldap()

    db_name = connection_cred["db_name"]
    db_populate = DBPopulate(engine_base_path, db_name)
    reset_db(db_name)
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger().setLevel(logging.DEBUG)

    parser_computers = ParserComputers(dir_ldap)
    ldap_machines = parser_computers.get_machines()
    ad_users = ParserADUsers(dir_ldap).get_users()
    # TODO modify attribute `is_dc` in ADMachine to be True if the machine is a DC
    ad_domain = ADDomain(name=parser_computers.dir_name)
    ad_domain_name = ad_domain.name
    g_and_members = ParserADGroups(dir_ldap).get_ad_groups_and_members()

    db_populate.add_machines([m[0] for m in ldap_machines])
    logging.info(f"added {len(ldap_machines)} machines to the database")
    logging.debug(
        f"adding adusers {' '.join([adu.name for adu in ad_users])} to the database"
    )
    db_populate.add_ad_adusers_admachines(
        ad_domain, ad_users, [m[1] for m in ldap_machines]
    )
    db_populate.add_all_adgroups(ad_domain_name, g_and_members)
    populate_all_machines(
        db_populate,
        dir_ldap.parent,
        ad_domain_name,
    )
    db_populate.replace_sid_by_name()
    logging.info(f"Populated {db_name} with data from {dir_ldap}")
