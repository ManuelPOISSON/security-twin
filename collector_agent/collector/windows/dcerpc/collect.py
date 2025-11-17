import traceback
from logging import Logger

from collector.windows.ad.computer import Computer
from collector.windows.dcerpc.dcom import MS_WMI
from collector.windows.dcerpc.scan_strategy import MS_LSAD, MS_SAMR, RpcPing


def dcerpc_collect(logger: Logger, computer: Computer) -> dict:
    ping = RpcPing(computer.hostname, computer.username, computer.password)

    try:
        logger.debug("Trying to connect to Endpoint Mapper using TCP")
        ping.ping("tcp")
        logger.debug("RPC TCP: Success")

    except Exception as e:
        logger.error(e)
        logger.error(f"Ping RPC failed using TCP and Endpoint Mapper on {computer.hostname}")
        traceback.print_exc()

    try:
        logger.debug("Trying to connect to Endpoint Mapper using SMB")
        ping.ping("smb")
        logger.debug("RPC SMB : Success")
    except Exception as e:
        logger.error(e)
        logger.error(f"Ping RPC failed using SMB and Endpoint Mapper on {computer.hostname}")
        traceback.print_exc()
        return {}

    data = {}
    lsad = MS_LSAD()
    try:
        lsad.connect(computer.hostname, computer.username, computer.password)
        results = lsad.get_all_user_rights()
        data["user_rights"] = results

    except Exception as e:
        logger.warning(f"Cannot enummerate user privileges on {computer.hostname} with account {computer.username}")
        logger.warning(f"Exception: {e}")
        traceback.print_exc()

    samr = MS_SAMR()
    try:
        samr.connect(computer.hostname, computer.username, computer.password)

        results = samr.get_all_local_users()
        data["local_users"] = results
        results = samr.get_all_local_groups()
        data["local_groups"] = results

    except Exception as e:
        logger.warning(
            f"Cannot enummerates local groups and users on {computer.hostname} with account {computer.username}"
        )
        logger.warning(f"Exception: {e}")
        traceback.print_exc()

    try:
        wmi = MS_WMI()
        wmi.connect(computer.hostname, computer.username, computer.password)

        results = wmi.get_service_exec_acl()
        data["services"] = results

        results = wmi.get_wmi_right("root\\cimv2")
        data["root_cimv2_sd"] = results

        results = wmi.get_software_installed()
        data["software_registries"] = results

        has_rdp = wmi.get_dword_register_value(
            "HKEY_LOCAL_MACHINE", "SYSTEM\\CurrentControlSet\\Control\\Terminal Server", "fDenyTSConnections"
        )
        
        data["fdeny_ts_connections"] = {
            "key": "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\\fDenyTSConnections",
            "value": str(has_rdp),
        }

        system_accounts = wmi.get_system_account()
        data["local_users"].extend(system_accounts)
    except Exception as e:
        logger.warning(f"Cannot connect to WMI {computer.hostname} with account {computer.username}")
        logger.warning(f"Exception: {e}")
        traceback.print_exc()
    return data
