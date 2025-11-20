#!/usr/bin/env python3
import json
from collections import defaultdict
from pathlib import Path
import logging

from sqlalchemy import Engine

from model import File, Service, ADDomain, TypeOS, ADMachine, Machine
from provisioning.generate_yaml import get_admin_creds
from provisioning.path_playbooks import base_playbook_path, playbooks_generated_path
from provisioning.playbooks_with_param.merger import merge_splits
from model.select_in_db import (
    select_all_in_table,
    select_acl,
    select_rootcimv2,
    select_machines_by_name,
    select_saved_creds,
    select_passowrd_for_user,
    select_name_by_id,
    select_softwares_installed_on_machine,
    select_gpo_result,
)


class Cmd:
    def __init__(self, command: list[str], tmpfile: str = None):
        self.val: list[str] = command
        self.tmpfile = tmpfile

    def __str__(self):
        return " ".join(self.val)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(str(self))


def select_in_list(userin: str, list_where_selection_is_made: list[Cmd]) -> list[Cmd]:
    """

    :param userin: indexes and ranges separated by commas (e.g. "1, 3-5, 7" or "1, 3, 5")
    :param list_where_selection_is_made:
    :return: if userin is "1, 3-6, 9, 0" will return list at index 1, 3, 4, 5, 6, 9, 0
    """
    if not all([char in ",- 0987654321" for char in userin]):
        raise ValueError(f"Your input='{userin}' contains invalid characters")
    numbers = userin.replace(" ", "").split(",")
    new_l = []
    for num in numbers:
        if num.isdigit():
            new_l.append(list_where_selection_is_made[int(num)])
        elif num.count("-") == 1:
            start, end = num.split("-")
            print(start, end)
            if start.isdigit() and end.isdigit():
                if int(start) > len(list_where_selection_is_made) or int(end) > len(
                    list_where_selection_is_made
                ):
                    raise IndexError(
                        f"Your input='{userin}' contains indexes out of range {start} or {end}"
                    )
                new_l.extend(list_where_selection_is_made[int(start) : int(end) + 1])
            else:
                raise ValueError(
                    f"One number in range {num} contains invalid characters or negative numbers"
                )
    return new_l


def show_all_commands(all_cmd: list[Cmd]):
    for current_cmd_idx, command in enumerate(all_cmd):
        shorter_cmd = str(command).replace(str(Path(__file__).parent), "...")
        shorter_cmd = shorter_cmd.replace("/playbooks", "")
        print(
            f"command {current_cmd_idx:2d}/{len(all_cmd) - 1} {shorter_cmd}"  # noqa E231
        )


def filter_commands(commands: list[Cmd]) -> list[Cmd]:
    show_all_commands(commands)
    cmd_range_to_use = input(
        "\nEnter the range of commands to execute (e.g. 1, 3-5, 7 for commands [1,3,4,5,7])"
        f"\n{len(commands)=}"
        f"\n(Press enter to execute all): "
    )
    if cmd_range_to_use:
        return select_in_list(cmd_range_to_use, commands)
    return commands


def get_playbooks_no_param() -> list[Cmd]:
    """
    :return: list of playbooks to be run (no extra variables required)
    """
    sorted_playbooks = sorted((playbooks_generated_path).glob("*.yaml"))

    return [Cmd([str(play_path)]) for play_path in sorted_playbooks]


def create_ad(domain: str, adminPasswd: str, netwId: str, target: str) -> Cmd:
    playbook_path = str(base_playbook_path) + "/create_AD/playbook.yaml"
    return Cmd(
        [
            playbook_path,
            "-e",
            f"target='{target}' domain='{domain}' adminPasswd='{adminPasswd}' netwId='{netwId}'",
        ]
    )


def create_file(file_path: str, target: str) -> Cmd:
    file_path = file_path.replace("\\", "\\\\")
    print(f"create file at {file_path}")

    # C:\\Program Files\\Mozilla\\firefox.exe', target='DESKTOP-AONMC63
    playbook_path = (
        str(Path(__file__).parent)
        + "/playbooks_with_param/create_file_windows/playbook.yaml"
    )
    return Cmd(
        [
            playbook_path,
            "-e",
            f"target='{target}' file_path='{file_path}'",
        ]
    )


def create_acl(file_path: str, sp_name, right, target: str) -> Cmd:
    file_path = file_path.replace("\\", "\\\\")
    print(f"Add ACL for file at {file_path}")
    # TODO fix confusion between Domain\Administrateur and Local\Administrateur by default Administrateur is the local one
    print(
        r"\033[91m Warning! confusion between Domain\Administrateur and Local\Administrateur \033[0m"
    )
    # C:\\Program Files\\Mozilla\\firefox.exe', target='DESKTOP-AONMC63
    playbook_path = (
        str(Path(__file__).parent) + "/playbooks_with_param/add_acl/playbook.yaml"
    )
    return Cmd(
        [
            playbook_path,
            "-e",
            f"target='{target}' acl_path='{file_path}' sp_granted='{sp_name}' rights='{right}'",
        ]
    )


def create_service(service_name: str, bin_path: str, target: str) -> Cmd:
    file_path = bin_path.replace("\\", "\\\\")
    print(f"Add service {service_name} executing {bin_path}")
    playbook_path = (
        str(Path(__file__).parent)
        + "/playbooks_with_param/add_windows_service/playbook.yaml"
    )
    return Cmd(
        [
            playbook_path,
            "-e",
            f"target='{target}' service_name='{service_name}' exe_path='{file_path}'",
        ]
    )


def create_wmi_namespace_rights(
    sp_name: str,
    rights: str,
    target: str,
    domain_user: str,
    domain_admin_password: str,
    namespace: str = "root/cimv2",
) -> Cmd:
    playbook_path = (
        str(Path(__file__).parent) + "/playbooks_with_param/wmi_namespace/playbook.yaml"
    )
    return Cmd(
        [
            playbook_path,
            "-e",
            f"target='{target}' user_or_group='{sp_name}' rights_list='{rights}' "
            f"namespace_path='{namespace}' domain_user='{domain_user}' domain_admin_password='{domain_admin_password}'",
        ]
    )


def create_rdp(target: str) -> Cmd:
    playbook_path = (
        str(Path(__file__).parent) + "/playbooks_with_param/enable_rdp/playbook.yaml"
    )
    return Cmd(
        [
            playbook_path,
            "-e",
            f"target='{target}'",
        ]
    )


def create_runas_savedcred(
    target: str,
    impersonator: str,
    impersonator_pwd: str,
    impersonated_user: str,
    impersonated_passwd: str,
) -> Cmd:
    # TODO: modify playbook to avoid required user interaction
    playbook_path = (
        str(Path(__file__).parent) + "/playbooks_with_param/runas/playbook.yaml"
    )
    path_runas_vbs_template = (
        str(Path(__file__).parent)
        + "/playbooks_with_param/runas/first_runas_template.vbs"
    )
    with open(path_runas_vbs_template, "r") as f:
        vbs_script = f.read()
    for to_replace, replacement in (
        ("<impersonated_username>", impersonated_user),
        ("<impersonated_password>", impersonated_passwd),
    ):
        vbs_script = vbs_script.replace(to_replace, replacement)
    with open(
        str(Path(__file__).parent) + "/playbooks_with_param/runas/first_runas.vbs", "w"
    ) as f:
        f.write(vbs_script)
    return Cmd(
        [
            playbook_path,
            "-e",
            f"target='{target}' "
            f"can_runas='{impersonator}' "
            f"can_runas_password='{impersonator_pwd}' ",
        ]
    )


def runas_ask_user_action(cmds: list[Cmd]) -> None:
    for cmd in cmds:
        if "/runas/" in str(cmd):
            str_cmd = str(cmd.val)
            # TODO make script_name dynamic by looking playbook model/provisioning/playbooks_with_param/runas/playbook.yaml
            script_name = "first_runas.vbs"
            target = str(str_cmd.split('target=')[1]).split("'")[1]
            user = str(str_cmd.split('can_runas=')[1]).split("'")[1]
            password = str(str_cmd.split('can_runas_password=')[1]).split("'")[1]
            text = (
                f"Login on {target} "
                f"as user {user} "
                f"with password {password} "
                f"and run the following command: cscript.exe C:\\Users\\Public\\Documents\\{script_name}"  # noqa E231
            )
            print("\033[95m" + f"User manual interaction required\n{text}" + "\033[0m")


def deactivate_firewall(target: str) -> Cmd:
    playbook_path = (
        str(Path(__file__).parent)
        + "/playbooks_with_param/deactivate_firewall/playbook.yaml"
    )
    return Cmd([playbook_path, "-e", f"target='{target}'"])


def deactivate_win_defender(target: str) -> Cmd:
    playbook_path = (
        str(Path(__file__).parent)
        + "/playbooks_with_param/deactivate_win_defender/playbook.yaml"
    )
    return Cmd([playbook_path, "-e", f"target='{target}'"])


def generate_commands_install_software(engine: Engine, target: str) -> list[Cmd]:
    """
    Currently works for WinRar
    :param engine:
    :param target:
    :return:
    """
    softwares_to_install = []
    softwares_machine = select_softwares_installed_on_machine(engine, target)
    for software in softwares_machine:
        logging.debug(f"{target=} {software=}")
        if "winrar" in software.name.lower():
            softwares_to_install.append(install_winrar(target))
        elif "activemq" in software.name.lower():
            softwares_to_install.append(install_activeMQ(target))
        elif "log4j" in software.name.lower():
            softwares_to_install.append(install_log4j(target))
        else:
            print(f"Unknown software {software}")
    # remove duplicates (e.g. ApacheMQ 2.0 and ApacheMQ 4.1, only the ApacheMQ available in playbooks will be installed
    # TODO take into account versions
    uniq_softwares = list(set(softwares_to_install))
    if len(uniq_softwares) != len(softwares_to_install):
        print(
            f"Warning! Duplicates removed in software to install on machine {target} {uniq_softwares}"
        )
    return uniq_softwares


def install_winrar(target: str) -> Cmd:
    playbook_path = (
        Path(__file__).parent
        / "playbooks_with_param"
        / "install_soft_winrar"
        / "playbook.yaml"
    )
    return Cmd([str(playbook_path), "-e", f"target='{target}' "])


def install_activeMQ(target: str) -> Cmd:
    """
    install apache-activeMQ 5.18.0 on target
    vulnerable to CVE-2023-46604
    :param target:
    :return:
    """
    playbook_path = (
        Path(__file__).parent
        / "playbooks_with_param"
        / "install_soft_apacheMQ"
        / "playbook.yaml"
    )
    merge_splits(playbook_path.parent / "jdk-21_windows-x64_bin.exe")
    return Cmd([str(playbook_path), "-e", f"target='{target}' "])




def install_log4j(target: str) -> Cmd:
    """
    install Springboot log4j 1.5 on target
    vulnerable to CVE-2021-44228
    :param target:
    :return:
    """
    playbook_path = (
        Path(__file__).parent
        / "playbooks_with_param"
        / "install_soft_log4j"
        / "playbook.yaml"
    )
    merge_splits(playbook_path.parent / "gradle-7.3.1-bin.zip")
    return Cmd([str(playbook_path), "-e", f"target='{target}' "])


def generate_commands_saved_creds(
    engine: Engine, current_target_name: str
) -> list[Cmd]:
    saved_creds_commands = []
    for a, impersonator, tor_id, impersonated, ted_id in select_saved_creds(
        engine, current_target_name
    ):
        # print(f"saved cread are {select_saved_creds(engine, current_target_name)}")
        pdw_impersonator = select_passowrd_for_user(engine, user_id=tor_id)
        pdw_impersonated = select_passowrd_for_user(engine, user_id=ted_id)
        # add domain to impersonated user name
        ted_name = select_name_by_id(engine, ted_id)
        if "@" in ted_name:
            ted_name = ted_name.split("@")[1] + "\\" + ted_name.split("@")[0]
        saved_creds_commands.append(
            create_runas_savedcred(
                current_target_name,
                impersonator,
                pdw_impersonator,
                ted_name,
                pdw_impersonated,
            )
        )
    return saved_creds_commands


def generate_commands_rootcimv2(
    engine: Engine,
    current_target_name: str,
    domain_admin_name: str,
    domain_admin_passwd: str,
) -> list[Cmd]:
    rootcimv2_commands = []
    for _, _, sp_name, right in select_rootcimv2(engine, current_target_name):
        if sp_name.endswith(f"@{current_target_name}"):
            sp_name = sp_name[: sp_name.rfind("@")]
        if sp_name.startswith("NT AUTHORITY"):
            # skip NT AUTHORITY users
            continue
        rootcimv2_commands.append(
            create_wmi_namespace_rights(
                # 0x5C is backslash \
                f'"{sp_name}"',  # maybe need to add single quotes around
                right,
                current_target_name,
                domain_admin_name,
                domain_admin_passwd,
            )
        )
    return rootcimv2_commands


def get_and_apply_gpo_locally(engine: Engine, target: str) -> Cmd | None:
    mapping = defaultdict(list)
    for _, policy, spname, spid in select_gpo_result(engine, target):
        mapping[policy].append(select_name_by_id(engine, spid, upn_format=False))
    if not mapping:
        print(f"No GPO to apply for {target}")
        return None
    return _apply_gpo_logonright(target, mapping)


def _apply_gpo_logonright(target: str, user_rights: dict) -> Cmd:
    """
    user_rights example:
      {
        "SeInteractiveLogonRight": ["AD2016\\Marchombres"],
        "SeDenyInteractiveLogonRight": ["AD2016\\essindra.essindra", "AD2016\\gHr"]
      }
    """
    playbook_path = (
        Path(__file__).parent / "playbooks_with_param" / "add_gpo" / "playbook.yaml"
    )
    tmp_extra_vars_file = (
        playbook_path.parent / f"tmp_extravars_{target.replace(' ', '_')}"
    )
    mapping = {"target": target, "user_rights_mapping": user_rights}
    with open(tmp_extra_vars_file, "w") as f:
        json.dump(mapping, f)

    return Cmd(
        [
            str(playbook_path),
            "-e",
            f"@{tmp_extra_vars_file}",
        ],
        tmpfile=str(tmp_extra_vars_file),
    )


def generate_all_commands(
    all_targets,
    engine,
    inventory_path,
    filter_service_names: set[str] = None,
    filter_file_paths: set[str] = None,
) -> list[Cmd]:
    all_commands = []

    # Get all machines and filter to only Windows machines that are in the inventory
    all_machines = select_all_in_table(engine, Machine)
    inventory_machine_names = {tar.targets_list[0].name for tar in all_targets.values()}
    windows_machine_names = [
        machine.name 
        for machine in all_machines 
        if machine.os_type == TypeOS.windows and machine.name in inventory_machine_names
    ]
    
    # Only deactivate firewall and Windows Defender on Windows machines in the inventory
    if windows_machine_names:
        all_commands.append(
            deactivate_firewall(",".join(windows_machine_names))
        )
        all_commands.append(
            deactivate_win_defender(",".join(windows_machine_names))
        )

    # TODO take into account when multiple ADmachines are Domain Controllers (DC)
    machine_dc = [
        machine for machine in select_all_in_table(engine, ADMachine) if machine.is_dc
    ][0]
    targetsDC = all_targets[machine_dc.name]

    all_files: list[File] = select_all_in_table(engine, File)
    all_services: list[Service] = select_all_in_table(engine, Service)
    if filter_service_names:
        print(f"Filtering services by {filter_service_names=}")
        all_services = [
            service for service in all_services if service.name in filter_service_names
        ]
    if filter_file_paths:
        filter_file_paths = {path.lower() for path in filter_file_paths}
        all_files = [
            file for file in all_files if file.path.lower() in filter_file_paths
        ]
        print(f"Filtering files by {filter_file_paths=}. {len(all_files)=}")
    domain_name = select_all_in_table(engine, ADDomain)[0].name
    ip_dc = targetsDC.targets_list[0].ip_address
    domain_admin_name, domain_admin_passwd = get_admin_creds(
        inventory_path, targetsDC.targets_list[0].name
    )

    all_commands.append(
        create_ad(
            domain_name,
            "Password1234!",
            ip_dc[: ip_dc.rfind(".")] + ".0/24",
            targetsDC.targets_list[0].name,
        )
    )

    all_commands.extend(get_playbooks_no_param())

    for current_targets in all_targets.values():
        current_target_name = current_targets.targets_list[0].name
        print(f"{current_target_name=}")

        current_vm_files: list[File] = [
            file for file in all_files if file.id_machine == current_target_name
        ]
        current_vm_acls = select_acl(engine, current_target_name)
        if filter_file_paths:
            current_vm_acls = [
                (a, path, b, c)
                for (a, path, b, c) in current_vm_acls
                if path.lower() in filter_file_paths
            ]

        for file_path in current_vm_files:
            all_commands.append(create_file(file_path.path, current_target_name))
        for sp_name, path, rights, machine_name in current_vm_acls:
            if sp_name.endswith(f"@{machine_name}"):
                sp_name = sp_name[: sp_name.rfind("@")]
            if sp_name.startswith("APPLICATION PACKAGE AUTHORITY"):
                continue
            all_commands.append(create_acl(path, sp_name, rights, current_target_name))
        print(tuple((service.id_machine, service.name) for service in all_services))
        for service in [
            service
            for service in all_services
            if service.id_machine == current_target_name
        ]:
            all_commands.append(
                create_service(
                    service.name,
                    service.executable_path,
                    current_target_name,
                )
            )
        machines_windows_list = select_machines_by_name(engine, current_target_name)
        if machines_windows_list is None or len(machines_windows_list) != 1:
            print(
                f"Warning! Found multiple machines with name {current_target_name}: {machines_windows_list=}"
            )
            pass
        else:
            machine_windows = machines_windows_list[0]
            if machine_windows.has_RDP:
                if machine_windows.os_type == TypeOS.windows:
                    print(f"Enable RDP for {machine_windows.name}")
                    all_commands.append(create_rdp(current_target_name))
                else:
                    print(
                        f"{machine_windows.name} has RDP but "
                        f"only {TypeOS.windows} is supported (detected {machine_windows.os_type})"
                    )

        all_commands.extend(
            generate_commands_rootcimv2(
                engine, current_target_name, domain_admin_name, domain_admin_passwd
            )
        )
        all_commands.extend(generate_commands_saved_creds(engine, current_target_name))
        all_commands.extend(
            generate_commands_install_software(engine, current_target_name)
        )
        cmd_apply_gpo = get_and_apply_gpo_locally(engine, current_target_name)
        if cmd_apply_gpo:
            all_commands.append(cmd_apply_gpo)

    return all_commands
