import base64
import json
import logging
import subprocess

from collector.utils import WindowsContext, get_ressource_path

logger = logging.getLogger(__name__)


def run_cmd(cmd: str) -> str | None:
    logger.debug(f"Executing {cmd}")
    try:
        process = subprocess.run(["powershell.exe", "-NoProfile", "-Command", cmd], capture_output=True)
    except Exception as e:
        logger.warning(e)
        return None

    if process.returncode == 0:
        stdout = process.stdout.decode()
        stderr = process.stderr.decode()
        logger.debug(f"Stdout: {stdout}")
        if stderr:
            logger.debug(f"Stderr: {stderr}")
        return stdout
    logger.warning(f"Command failed : {cmd}")
    logger.warning(f"Stderr :  {process.stderr.decode()}")
    return None


def run_ps_script(script_path: str) -> str | None:
    logger.debug(f"Executing {script_path}")
    try:
        process = subprocess.run(
            ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", script_path], capture_output=True
        )
    except Exception as e:
        logger.warning(e)
        return None
    if process.returncode == 0:
        stdout = process.stdout.decode()
        stderr = process.stderr.decode()
        logger.debug(f"Stdout: {stdout}")
        if stderr:
            logger.debug(f"Stderr: {stderr}")
        return stdout

    logger.warning(f"Command failed : {script_path}")
    logger.warning(f"Stderr :  {process.stderr.decode()}")
    return None


def local_windows_context(context: WindowsContext):
    info_machine = {}
    version = run_cmd("Write-Host ([System.Environment]::Version)")
    is_admin = run_cmd(
        "(New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent()))"
        ".IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)"
    )
    whoami = run_cmd("whoami")
    hostname = run_cmd("hostname")

    info_machine["powershell_version"] = version
    info_machine["is_admin"] = is_admin
    info_machine["whoami"] = whoami
    info_machine["hostname"] = hostname

    scripts = {
        "hasRDP": "collector/windows/tasks/getfDenyTSConnectionsRegisterValue.ps1",
        "localGroups": "collector/windows/tasks/getLocalGroups.ps1",
        "localUsers": "collector/windows/tasks/getLocalUsers.ps1",
        "SoftwareFromRegistry": "collector/windows/tasks/getInstalledApplicationsFromRegistry.ps1",
        "Software": "collector/windows/tasks/getSoftware.ps1",
        "services": "collector/windows/tasks/getServiceExeModify.ps1",
        "wmi": "collector/windows/tasks/getWMICRight.ps1",
        "GPO": "collector/windows/tasks/getGPO.ps1",
    }
    data = {}
    for script_name, relative_path in scripts.items():
        full_path = get_ressource_path(relative_path)
        output = run_ps_script(full_path)
        if output is None:
            data[script_name] = {"result": "Error"}
        else:
            json_data = json.loads(output)
            data[script_name] = json_data

    outdir = context.output_directory
    for scriptName, value in data.items():
        if scriptName == "GPO":
            xml_b64 = value.get("xml_b64encoded")
            if xml_b64 is not None:
                gpresult_xml = base64.b64decode(value["xml_b64encoded"])
                with open(f"{outdir}/gpresult_computer_xml.xml", "w") as fd:
                    fd.write(gpresult_xml.decode(errors="ignore"))
            continue
        with open(f"{outdir}/{scriptName}.json", "w") as fd:
            fd.write(json.dumps(value, default=str, indent=4))

    with open(f"{outdir}/machine_info.json", "w") as fd:
        fd.write(json.dumps(info_machine, default=str, indent=4))
    return True
