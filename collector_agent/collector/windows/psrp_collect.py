import base64
import json
import traceback
from itertools import dropwhile, takewhile
from logging import Logger

from collector.model.local_windows import (
    LocalGroup,
    LocalUser,
    RegistryKeyValue,
    SecurityDescriptor,
    Service,
    Software,
)
from collector.utils import get_ressource_path
from collector.windows.ad.computer import Computer
from collector.windows.connection_strategy import Prsp


def handle_user_rights_output(lines: list[str]) -> list[dict]:
    """
    Example of content :
        [Unicode]
        Unicode=yes
        [Privilege Rights]
        SeNetworkLogonRight = *S-1-1-0
        SeBackupPrivilege = *S-1-5-32-544,*S-1-5-20
        [Version]
        signature=\"$CHICAGO$\"
        Revision=1
    """

    # Ignore before lines before "[Privilege Rights]""
    after_privileges = dropwhile(lambda l: l.strip() != "[Privilege Rights]", lines)

    # Ignore "[Privilege Rights]"
    next(after_privileges, None)

    # Ignore after
    rights_section = takewhile(lambda l: l.strip() != "[Version]", after_privileges)

    sid_map: dict[str, list[str]] = {}
    for line in rights_section:
        if "=" not in line:
            continue

        privilege, sids_str = line.split("=", 1)
        privilege = privilege.strip()

        sids = [sid.strip().lstrip("*") for sid in sids_str.split(",")]

        for sid in sids:
            if "-" not in sid:
                # Weird case secedit return the name of group for Guest
                continue
            sid_map.setdefault(sid, []).append(privilege)

    return [{"local_principal": {"sid": sid}, "permissions": permissions} for sid, permissions in sid_map.items()]


def collect(logger: Logger, computer: Computer, auth: str, user_profile: bool) -> dict:
    try:
        logger.debug(
            f"Trying to connect to {computer.hostname} with the {auth} auth method and user {computer.username}"
        )
        winrmco = Prsp(computer.hostname, computer.username, computer.password, auth, logger, user_profile)
    except Exception as e:
        logger.warning(f"Unable to connect to the host {computer.hostname}")
        logger.warning(f"Get the following error: {e}")
        logger.debug(traceback.format_exc())
        return False

    collectables = {
        "fdeny_ts_connections": {
            "script": "collector/windows/tasks/getfDenyTSConnectionsRegisterValue.ps1",
            "type": RegistryKeyValue,
        },
        "services": {"script": "collector/windows/tasks/getServiceExeSdWmi.ps1", "type": list[Service]},
        "root_cimv2_sd": {"script": "collector/windows/tasks/getWMICRight.ps1", "type": SecurityDescriptor},
        "local_users": {"script": "collector/windows/tasks/getLocalUsers.ps1", "type": list[LocalUser]},
        "local_groups": {"script": "collector/windows/tasks/getLocalGroups.ps1", "type": list[LocalGroup]},
        "software_registries": {
            "script": "collector/windows/tasks/getInstalledApplicationsFromRegistry.ps1",
            "type": list[Software],
        },
    }
    raw_output = {}
    local_data = {}
    for collectable, params in collectables.items():
        full_path = get_ressource_path(params["script"])
        output = winrmco.execute_ps_script(full_path)
       
        try:
            data = json.loads(output)
            raw_output[collectable] = data
            local_data[collectable] = data["result"]
        except Exception as e:
            logger.error(f"Cannot unpack {collectable} on {computer.hostname}")
            logger.error(f"Exception : {e}")
            traceback.print_exc()
    full_path = get_ressource_path("collector/windows/tasks/getUAR.ps1")
    output = winrmco.execute_ps_script(full_path)
    raw_output["extra"] = {}
    try:
        data = json.loads(output)
        raw_output["extra"]["user_rights_b64"] = data
        result = base64.b64decode(data["xml_b64encoded"]).decode()

        user_rights = handle_user_rights_output(result.splitlines())
        local_data["user_rights"] = user_rights

    except Exception as e:
        logger.error(f"Cannot decoded user rights on {computer.hostname}")
        logger.error(f"Exception : {e}")
        traceback.print_exc()

    return local_data
