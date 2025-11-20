import argparse
import os
import subprocess
import time
from pathlib import Path
import json
import logging
from typing import Any

from dotenv import load_dotenv

from sqlalchemy import Engine, create_engine

from model.db import engine_base_path
from model.db_connect import connection_cred
from model import Machine, TypeOS
from model.select_in_db import select_all_in_table


ANSIBLE_PASSWORD = "234P@ss"
ANSIBLE_USER = "Administrateur"

MAX_WAIT_TIME = 25  # in minutes, time to wait VM deployment and ip assignment


def load_env_file(path_env_file):
    if not load_dotenv(path_env_file):
        logging.warning(f"Loading env file {path_env_file} failed")


def get_subnet(path_env_file):
    load_env_file(path_env_file)

    subnet = os.getenv("SUBNET", -1)
    if subnet != -1:
        return subnet

    logging.warning(f"Could load SUBNET from .env file {path_env_file}")

    while True:
        raw = input("Please enter the subnet: (enter 177 for ip 192.168.177.x) ")
        try:
            subnet = int(raw)
            break
        except ValueError:
            logging.error(f"Invalid input '{raw}'")
    return subnet


def get_prefix(names: list[str]) -> str:
    if not names:
        return ""
    prefix = names[0]
    for name in names[1:]:
        i = 0
        while i < len(prefix) and i < len(name) and prefix[i] == name[i]:
            i += 1
        prefix = prefix[:i]
        if not prefix:
            break
    if len(prefix) < 1:
        logging.warning(f"Couldn't find similar prefix in {names}")
    return prefix


def gen_hosts_file(
    path_hosts_file: Path, engine: Engine, computers: set[str], ad: bool
):
    """

    :param path_hosts_file:
    :param engine:
    :param computers: if list(computers) == ["all_computers"], all computers are added
    :param ad:
    :return:
    """
    if path_hosts_file.is_file():
        input(
            f"Hosts file {path_hosts_file.resolve()} exists. Press Enter to overwrite or CTRL+C to abort."
        )
    windows_servers = {}
    out_content = ""
    for mach in select_all_in_table(engine, Machine):
        is_server_windows = (
            mach.os_version
            and "server" in mach.os_version.lower()
            and mach.os_type == TypeOS.windows
        )
        if is_server_windows:
            windows_servers[mach.name] = mach
        elif list(computers) == ["all_computers"] or (mach.name in computers):
            if mach.os_type == TypeOS.windows:
                out_content += f"{mach.name};windows,windows10,21H2;40GB\n"  # noqa E231
            elif mach.os_type == TypeOS.linux:
                out_content += f"{mach.name};linux,debian,20250811-2201;20GB\n"  # noqa E231
            else:
                logging.warning(f"Unknown OS type: {mach.os_type}")
    if ad:
        if not windows_servers:
            raise ValueError("No windows server found for AD")
        out_content += f"{windows_servers[list(windows_servers.keys())[0]].name};windows,server19,17763.737;40GB\n"  # noqa E231

    with open(path_hosts_file, "w") as f:
        f.write(out_content)
        logging.info(f"Hosts file {path_hosts_file.resolve()} written")


def ip_match_from_subprocess(
    expected_count: int, subnet_range: int, path_script: Path
) -> list[str]:
    ret = []
    max_wait = int(MAX_WAIT_TIME) * 2
    for wait_idx in range(max_wait):
        out = subprocess.check_output(
            [f"{str(path_script.resolve())}", str(subnet_range)]
        )
        ret = out.decode("utf-8").strip().splitlines()
        if len(ret) > 0:
            if len(ret) != expected_count:
                # wait 60 extra seconds to ensure all VMs are up
                time.sleep(60)
                logging.info("Found IPs, exiting wait loop in 60 seconds")
            return (
                subprocess.check_output(
                    [f"{str(path_script.resolve())}", str(subnet_range)]
                )
                .decode("utf-8")
                .strip()
                .splitlines()
            )
        remaining = (max_wait - wait_idx) / 2
        logging.info(
            f"No IPs found in subnet 192.168.{subnet_range}.x, retrying in 30 seconds...\n"
            f"Remaining wait time before abort: {remaining} minutes"
        )
        time.sleep(30)
    return ret


def get_name_to_ip(
    expected_count: int,
    subnet_range: int = 0,
    path_script: Path = Path("./pydeploy/listips.sh"),
    file_hardcoded_match=None,
) -> dict[str, str]:
    if subnet_range == 0 and file_hardcoded_match is None:
        raise ValueError("Either subnet_range or file_hardcoded_match must be provided")
    if file_hardcoded_match is not None:
        with open(file_hardcoded_match, "r") as f:
            lines = [ll.strip() for ll in f.readlines()]
    else:
        if not path_script.is_file():
            raise FileNotFoundError(f"File {path_script.resolve()} not found")
        logging.info(f"Matching VM names to IPs in subnet 192.168.{subnet_range}.x")
        try:
            lines = ip_match_from_subprocess(expected_count, subnet_range, path_script)
            if not lines:
                return {}
        except Exception as e:
            print(e)
            return {}
    logging.debug(lines)
    return {line.split(" ")[0]: line.split(" ")[1] for line in lines if " " in line}


def gen_inventory(
    hosts_data: dict[str, Any], name_to_ip: dict[str, str], out_path: Path
):
    # Get the path to the default SSH key for Linux hosts
    script_dir = Path(__file__).parent
    ssh_key_path = script_dir.parent / "pydeploy" / "digitaltwin" / "utils" / "id_rsa_linux"
    ssh_key_path_str = str(ssh_key_path.resolve())
    
    hostname_prefix = get_prefix([host["name"] for host in hosts_data["hosts"]])

    def get_ip(host_name: str) -> str:
        ip_list = [ip for name, ip in name_to_ip.items() if host_name in name]
        if not ip_list:
            logging.error(f"host {host_name}: no IP found")
            return "unknown_ip"
        if len(ip_list) > 1:
            logging.warning(
                f"multiple IPs found for host {host_name}: {ip_list}, using the first one"
            )
        return ip_list[0]

    # Separate Windows and Linux hosts
    windows_hosts = []
    linux_hosts = []
    
    for host in hosts_data["hosts"]:
        os_type = host.get("os_type", "").lower()
        if os_type == "windows":
            windows_hosts.append(host)
        elif os_type == "linux":
            linux_hosts.append(host)
        else:
            logging.warning(f"Unknown OS type '{os_type}' for host {host.get('name', 'unknown')}, skipping")

    # Build inventory content
    inventory_content = ""
    
    # Windows section
    if windows_hosts:
        inventory_content += """[windows:vars]
ansible_connection=winrm
ansible_port=5986
ansible_winrm_server_cert_validation=ignore

[windows]
"""
        for host in windows_hosts:
            host_name = host["name"].replace(hostname_prefix, "")
            ip = get_ip(host["name"])
            inventory_content += f"{host_name} ansible_host={ip} ansible_user={ANSIBLE_USER} ansible_password={ANSIBLE_PASSWORD}\n"
        inventory_content += "\n"
    
    # Linux section
    if linux_hosts:
        inventory_content += f"""[linux:vars]
ansible_connection=ssh
ansible_user=root
ansible_ssh_private_key_file={ssh_key_path_str}
ansible_ssh_common_args='-o StrictHostKeyChecking=no'

[linux]
"""
        for host in linux_hosts:
            host_name = host["name"].replace(hostname_prefix, "")
            ip = get_ip(host["name"])
            inventory_content += f"{host_name} ansible_host={ip}\n"
        inventory_content += "\n"
    
    # Add runas_become_plugin section (for Windows)
    inventory_content += """[runas_become_plugin]
password="Here!NotR3alPwd"
"""
    
    with open(out_path, "w") as f:
        f.write(inventory_content)
    logging.info(f"Inventory written to {out_path.resolve()}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Prepare deployment by generating inventory"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--allhosts-file",
        help="Path to all hosts file (when used, no other argument is allowed)",
    )
    group.add_argument("--out-inventory", help="Path to output inventory file")
    parser.add_argument("--in-modeljson", help="Path to input model JSON file")
    parser.add_argument(
        "--in-env", default=".env", help="Path to .env file (default: .env)"
    )
    parser.add_argument(
        "--in-ipmatch",
        default="",
        help="Path to IP match text file (default: empty string)",
    )
    args = parser.parse_args()

    if args.allhosts_file:
        for arg in ["out_inventory", "in_modeljson", "in_ipmatch"]:
            if getattr(args, arg, None):
                parser.error("--allhosts-file cannot be combined with other arguments")

    return args


if __name__ == "__main__":
    args = parse_args()
    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug(args)
    if args.allhosts_file:
        gen_hosts_file(
            Path(args.allhosts_file),
            create_engine(f"{engine_base_path}{connection_cred['db_name']}"),
            {"all_computers"},
            ad=True,
        )
        exit(0)

    with open(args.in_modeljson, "r") as f:
        hosts_data = json.load(f)
    if args.in_ipmatch:
        name_to_ip = get_name_to_ip(
            len(hosts_data["hosts"]), file_hardcoded_match=args.in_ipmatch
        )
    else:
        subnet_range = get_subnet(args.in_env)
        name_to_ip = get_name_to_ip(len(hosts_data["hosts"]), subnet_range=subnet_range)
    
    path_inventory = Path(args.out_inventory)
    gen_inventory(hosts_data, name_to_ip, path_inventory)
