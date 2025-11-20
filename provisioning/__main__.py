import argparse
import logging
import os
import subprocess
import sys
from pathlib import Path
from time import sleep

from sqlalchemy import Engine, create_engine

from model.db import engine_base_path
from model.db_connect import connection_cred
from provisioning import generate_yaml
from provisioning.generate_yaml import get_targets
from provisioning.run_playbook import (
    generate_all_commands,
    filter_commands,
    show_all_commands,
    runas_ask_user_action,
    Cmd,
)


def execute_commands(
    all_cmds: list[Cmd],
    inventory_path: Path,
    batch_AD: bool,
    ignore_errors_cmd_type: str = None,
):
    fail_cmds = []
    for current_cmd_idx, command in enumerate(all_cmds):
        print(f"Running command {current_cmd_idx}/{len(all_cmds) - 1} {command}")
        try:
            subprocess.run(
                ["ansible-playbook", "-i", str(inventory_path.resolve()), "-vvvv"]
                + command.val,
                check=True,
            )
            if "create_AD" in str(command):
                fix_ad_create_timeout(batch_AD)
        except subprocess.CalledProcessError as e:
            if ignore_errors_cmd_type in str(command.val):
                print(f"Error running command {current_cmd_idx}: {e}")
                fail_cmds.append(str(command.val))
            else:
                raise e
        finally:
            if command.tmpfile:
                print(f"Deleting temporary file {command.tmpfile}")
                os.remove(command.tmpfile)
        if fail_cmds:
            print(
                f"{len(fail_cmds)} commands failed to execute: {'\n- '.join(fail_cmds)}"
            )

    runas_ask_user_action(all_cmds)


def fix_ad_create_timeout(batch_AD: bool):
    print("Waiting for Active Directory to be created.")
    if batch_AD:
        minutes_sleep = 15
        print(
            "\033[92m" + f"Batch mode: Sleep for {minutes_sleep} minutes." + "\033[0m"
        )
        print(
            "\033[92m"
            + "Press CTRL+C to skip sleep (when you are sure Domain Controller is fully restarted)"
            + "\033[0m"
        )
        print("Sleeping minutes remaining: ")
        try:
            for remaining_time in range(minutes_sleep * 60, 0, -60):
                print(remaining_time // 60, end=" ", flush=True)
                sleep(60)
            print("\nDone waiting.")
        except KeyboardInterrupt:
            print(
                "\n\033[93mSleep interrupted by user (CTRL+C). Continuing early.\033[0m"
            )
        return

    user_input = ""
    print("\033[91m" + "User input required to avoid timeout error." + "\033[0m")
    while user_input != "ok":
        user_input = input(
            "\033[93m"  # noqa W605
            + "Write ok and press enter when you are sure that the domain controller successfully restarted\n"
            + "\033[0m"
        )
        print(f"{user_input=}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run playbook commands", allow_abbrev=False
    )
    parser.add_argument("action", choices=["exec", "show"], help="Action to perform")
    parser.add_argument(
        "-range", action="store_true", help="Specify a range of commands to execute"
    )
    parser.add_argument(
        "-i",
        "--inventory",
        type=str,
        default="inventory.ini",
        help="Path to inventory file (default: provisioning/inventory.ini)",
    )
    parser.add_argument(
        "--batch-createAD",
        action="store_true",
        help="Playbook when creating AD: 'Sleep 15min' instead of 'Prompt user input'",
    )

    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)
    return parser.parse_args()


def main():
    args = parse_args()
    engine: Engine = create_engine(f"{engine_base_path}{connection_cred['db_name']}")

    # ### start optional arguments, could be set to None ###
    filter_service_names = {
        "Mozilla",
    }
    filter_file_paths = {
        "c:\\program files\\mozilla\\firefox.exe",
    }
    ignore_errors_cmd_type = r"wmi_namespace/playbook.yaml"
    # ### end optional arguments ###

    inventory_path = Path(args.inventory)
    all_targets = get_targets(inventory_path)
    print("Provisioning on ips:")
    for target_obj in all_targets.values():
        print("\n".join(tar.ip_address for tar in target_obj.targets_list))

    generate_yaml.main(engine, inventory_path)
    all_cmds = generate_all_commands(
        all_targets, engine, inventory_path, filter_service_names, filter_file_paths
    )

    if args.action == "exec":
        if args.range:
            all_cmds = filter_commands(all_cmds)
            show_all_commands(all_cmds)
            input("execute these playbooks ok? (CTRL+C to cancel)")
        try:
            execute_commands(
                all_cmds, inventory_path, args.batch_createAD, ignore_errors_cmd_type
            )
        except subprocess.CalledProcessError as e:
            logging.error(f"{e}")
            logging.info(
                f"Maybe VMs were not fully booted. Retry provisionning with {args}"
            )

    elif args.action == "show":
        show_all_commands(all_cmds)


if __name__ == "__main__":
    main()
