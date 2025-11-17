import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass

from impacket.dcerpc.v5.epm import MSRPC_UUID_PORTMAP
from impacket.dcerpc.v5.lsad import (
    MSRPC_UUID_LSAD,
    hLsarEnumerateAccountRights,
    hLsarEnumerateAccounts,
    hLsarOpenPolicy,
)
from impacket.dcerpc.v5.lsat import SID_NAME_USE, hLsarLookupSids2
from impacket.dcerpc.v5.rpcrt import DCERPC_v5, DCERPCException
from impacket.dcerpc.v5.samr import (
    MSRPC_UUID_SAMR,
    hSamrCloseHandle,
    hSamrConnect5,
    hSamrEnumerateAliasesInDomain,
    hSamrEnumerateDomainsInSamServer,
    hSamrEnumerateUsersInDomain,
    hSamrGetMembersInAlias,
    hSamrLookupDomainInSamServer,
    hSamrOpenAlias,
    hSamrOpenDomain,
    hSamrRidToSid,
)
from impacket.dcerpc.v5.transport import DCERPCTransportFactory, SMBTransport

logger = logging.getLogger(__name__)


@dataclass
class LocalUser:
    name: str
    sid: str


@dataclass
class LocalGroup:
    name: str
    sid: str
    members: list


class RpcPing:
    def __init__(self, target, username=None, password=None):
        self.target = target
        self.username = username
        self.password = password

    def ping(self, protocol):
        if protocol == "tcp":
            # TCP direct connection (Endpoint Mapper)
            string_binding = r'ncacn_ip_tcp:{}[135]'.format(self.target)
            rpctransport = DCERPCTransportFactory(string_binding)
            dce = rpctransport.get_dce_rpc()
            dce.connect()
            dce.bind(MSRPC_UUID_PORTMAP)
            dce.disconnect()
            logger.info(f"[+] RPC ping TCP successful on {self.target}")

        elif protocol == "smb":
            # SMB transport (using SMB named pipe for RPC)
            # Example: using srvsvc or svcctl pipe
            string_binding = r'ncacn_np:{}[\PIPE\epmapper]'.format(self.target)
            rpctransport = DCERPCTransportFactory(string_binding)

            # If credentials are provided
            if self.username and self.password:
                rpctransport.set_credentials(self.username, self.password)

            dce = rpctransport.get_dce_rpc()
            dce.connect()
            logger.info(f"[+] RPC ping SMB successful on {self.target}")
            dce.disconnect()
        else:
            raise ValueError("Unsupported protocol. Use 'tcp' or 'smb'.")
       
# NOTE : Should be refactored to avoid duplicate code


# NOTE : Should be refactored to avoid duplicate code


class MS_LSAD:
    def __init__(self):
        self.string_binding = None
        self.dcerpc = None

    def connect(self, host: str, username: str, password: str) -> None:
        self.string_binding = f"ncacn_np:{host}[\\pipe\\lsarpc]"
        rpctransport: SMBTransport = DCERPCTransportFactory(self.string_binding)
        rpctransport.set_dport(445)
        rpctransport.set_credentials(username, password)
        self.dcerpc = DCERPC_v5(rpctransport)
        self.dcerpc.connect()
        self.dcerpc.bind(MSRPC_UUID_LSAD)

    def get_all_user_rights(self) -> list | None:
        policyHandle = hLsarOpenPolicy(self.dcerpc)["PolicyHandle"]
        resp = hLsarEnumerateAccounts(self.dcerpc, policyHandle)
        if resp["ErrorCode"]:
            logger.error("TODO")
            return None

        result = []
        accounts = resp["EnumerationBuffer"]["Information"]
        sids = []

        for account in accounts:
            data = {}

            sid = account["Sid"].formatCanonical()
            data["local_principal"] = {}
            data["local_principal"]["sid"] = sid
            sids.append(sid)

            resp = hLsarEnumerateAccountRights(self.dcerpc, policyHandle, sid)
            if resp["ErrorCode"]:
                logger.error("TODO")
                return None

            data["permissions"] = []
            for user_right in resp["UserRights"]["UserRights"]:
                data["permissions"].append(user_right["Data"])

            # Translate SID to Security Principal name using MS-LSAT.
            # hLsarLookupSids2 accepts a list of SIDs and returns the corresponding names,
            # but the response does not preserve an explicit SID->Name mapping.
            # Instead, it relies on the order of the input list.
            # To avoid edge cases or mismatches, we call the method with a single SID each time.
            # Can be have performance issues

            # NOTE: In the future, consider make one call for efficiency if ordering can be guaranteed.
            resp = hLsarLookupSids2(self.dcerpc, policyHandle, [sid])

            # TODO : Should we return None or pass and have incomplete result ?
            if resp["ErrorCode"]:
                logger.error("TODO")
                return None

            for data_name, data_domain in zip(resp["TranslatedNames"]["Names"], resp["ReferencedDomains"]["Domains"]):
                # We got an int but we want a string
                # For more details see section 2.2.13 of MS-LSAT
                data["sid"] = data_domain["Sid"].formatCanonical()
            result.append(data)
        return result

    def disconnect(self):
        self.dcerpc.disconnect()


class MS_SAMR:
    def __init__(self):
        self.string_binding: str = None
        self.dcerpc: DCERPC_v5 = None
        self.is_connected: bool = False

    def connect(self, host: str, username: str, password: str):
        self.string_binding = f"ncacn_np:{host}[\pipe\samr]"
        rpctransport: SMBTransport = DCERPCTransportFactory(self.string_binding)
        rpctransport.set_dport(445)
        rpctransport.set_credentials(username, password)
        self.dcerpc = DCERPC_v5(rpctransport)
        self.dcerpc.connect()
        self.dcerpc.bind(MSRPC_UUID_SAMR)
        self.is_connected = True

    def get_all_domain_handles(self) -> list | None:
        if not self.is_connected:
            logger.error("Trying to enumerate local users without connection")
            return None
        try:
            resp = hSamrConnect5(self.dcerpc)
        except DCERPCException as e:
            logger.error(f"Cannot connect to SAMR with {self.string_binding}, error: {e}")
            return None
        if resp["ErrorCode"]:
            logger.error(f"Cannot connect to SAMR with {self.string_binding}")
            return None

        server_handle = resp["ServerHandle"]
        resp = hSamrEnumerateDomainsInSamServer(self.dcerpc, server_handle)
        if resp["ErrorCode"]:
            logger.error(f"Cannot enumerate domains on {self.string_binding}, error code : {resp['ErrorCode']}")
            return None

        domain_handles = []
        for rid_enum in resp["Buffer"]["Buffer"]:
            domain_name = rid_enum["Name"]

            resp = hSamrLookupDomainInSamServer(self.dcerpc, server_handle, domain_name)
            if resp["ErrorCode"]:
                logger.error(
                    f"Cannot found the domain ID for {domain_name} on {self.string_binding},"
                    f"error code {resp['ErrorCode']}"
                )
                return None

            domain_id = resp["DomainId"]
            resp = hSamrOpenDomain(self.dcerpc, server_handle, domainId=domain_id)
            if resp["ErrorCode"]:
                logger.error(
                    f"Cannot get the domain handle for {domain_name} on {self.string_binding},"
                    f"error code {resp['ErrorCode']}"
                )
                return None
            domain_handles.append(resp["DomainHandle"])
        hSamrCloseHandle(self.dcerpc, server_handle)
        return domain_handles

    def get_all_local_users(self) -> list | None:
        if not self.is_connected:
            logger.error("Trying to enumerate local users without connection")
            return None

        domain_handles = self.get_all_domain_handles()
        if domain_handles is None:
            logger.error(f"Cannot get local users on {self.string_binding}, due to previous error")
            return None

        local_users = []
        for domain_handle in domain_handles:
            resp = hSamrEnumerateUsersInDomain(self.dcerpc, domain_handle)
            if resp["ErrorCode"]:
                logger.error(
                    f"Cannot enumerate users for {domain_handle} on {self.string_binding}, "
                    f"error_code {resp['ErrorCode']}"
                )
                continue
            for user in resp["Buffer"]["Buffer"]:
                username = user["Name"]
                resp = hSamrRidToSid(self.dcerpc, objectHandle=domain_handle, rid=user["RelativeId"])
                if resp["ErrorCode"]:
                    logger.warning(
                        f"Cannot translate RID for {user} in {domain_handle} on {self.string_binding}, "
                        f"error_code {resp['ErrorCode']}"
                    )
                    sid = None
                else:
                    sid = resp["Sid"].formatCanonical()
                local_users.append({"name": username, "sid": sid})

        if not local_users:
            return None

        return local_users

    def get_all_local_groups(self) -> list | None:
        if not self.is_connected:
            logger.error("Trying to enumerate local users without connection")
            return None

        domain_handles = self.get_all_domain_handles()
        if domain_handles is None:
            logger.error(f"Cannot get local users on {self.string_binding}, due to previous error")
            return None

        local_groups = []
        for domain_handle in domain_handles:
            resp = hSamrEnumerateAliasesInDomain(self.dcerpc, domain_handle)

            for alias in resp["Buffer"]["Buffer"]:
                name_alias = alias["Name"]
                resp = hSamrRidToSid(self.dcerpc, domain_handle, alias["RelativeId"])
                if resp["ErrorCode"]:
                    logger.warning(
                        f"Cannot translate RID for {name_alias} in {domain_handle} on {self.string_binding},"
                        f" error_code {resp['ErrorCode']}"
                    )
                    continue

                sid_alias = resp["Sid"].formatCanonical()
                resp = hSamrOpenAlias(self.dcerpc, domain_handle, aliasId=alias["RelativeId"])
                if resp["ErrorCode"]:
                    logger.error(
                        f"Cannot open alias {name_alias} ({sid_alias}) in {domain_handle} on {self.string_binding}, "
                        f"error_code {resp['ErrorCode']}"
                    )
                    continue

                alias_handle = resp["AliasHandle"]
                resp = hSamrGetMembersInAlias(self.dcerpc, alias_handle)
                if resp["ErrorCode"]:
                    logger.error(
                        f"Cannot get members of alias {name_alias} ({sid_alias}) in {domain_handle} on ",
                        f"{self.string_binding}, error_code {resp['ErrorCode']}",
                    )
                    continue

                members = []
                for sid_obj in resp["Members"]["Sids"]:
                    sid = sid_obj["Data"]["SidPointer"].formatCanonical()
                    members.append(sid)

                local_groups.append({ "name": name_alias,"sid" : sid_alias, "members" : members})

        return local_groups

    def disconnect(self):
        self.dcerpc.disconnect()
        self.is_connected = False
