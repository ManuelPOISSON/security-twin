#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2021 AMOSSYS. All rights reserved.
#
# This file is part of Cyber Range AMOSSYS.
#
# Cyber Range AMOSSYS can not be copied and/or distributed without the express
# permission of AMOSSYS.
#
import logging
import shutil
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List
from typing import Tuple, Optional
import yaml
from sqlalchemy import Engine, create_engine

from model.db import engine_base_path
from model.db_connect import connection_cred
from model import ADGroup, ADUser, User, ADMachine, Machine, Group
from provisioning.Target import Target
from provisioning.Targets import Targets
from provisioning.actions.add_client_to_ad import AddClientToAD
from provisioning.actions.add_multiple_user_to_group import AddMultipleUserToGroup
from provisioning.actions.add_multiple_user_to_localgroup import (
    AddMultipleUserToLocalGroup,
)

from provisioning.actions.create_multiple_windows_domain_account import (
    CreateMultipleWindowsDomainAccount,
)
from provisioning.actions.create_multiple_windows_domain_group import (
    CreateMultipleWindowsDomainGroup,
)
from provisioning.actions.create_multiple_windows_local_account.action import (
    CreateMultipleWindowsLocalAccount,
)
from provisioning.actions.create_multiple_windows_local_group import (
    CreateMultipleWindowsLocalGroup,
)
from provisioning.path_playbooks import playbooks_generated_path
from model.select_in_db import (
    select_all_in_table,
    select_adgroup_with_members,
    select_localgroup_with_members,
)


class WindowsDomainAccount:
    def __init__(self, name: str) -> None:
        self.name = name


class WindowsDomainGroup:
    def __init__(self, name: str) -> None:
        self.name = name


def extract_names(path_inventory: str) -> list[str]:
    with open(path_inventory, "r") as f:
        lines = f.readlines()
    return [line.split(" ")[0] for line in lines if "ansible_host" in line]


def extract_ip(path_inventory: str, name: str) -> str:
    with open(path_inventory, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "ansible_host" in line and name in line:
                return line[line.find("ansible_host") + len("ansible_host=") :].split(
                    " "
                )[0]


def get_targets(inventory: Path) -> dict[str, Targets]:
    """
    get targets by reading inventory.ini
    :return:
    """
    return_dict = {}
    for machine_name in extract_names(str(inventory)):
        targets = Targets()
        targets.add_target(
            Target(machine_name, extract_ip(str(inventory), machine_name))
        )
        return_dict[machine_name] = targets
    return return_dict


def check_targets_names(engine: Engine, targets_list: dict[str, Targets]) -> None:
    all_machines_names = [
        machine_obj.name for machine_obj in select_all_in_table(engine, Machine)
    ]
    for targets in targets_list.values():
        for target in targets.targets_list:
            if target.name not in all_machines_names:
                raise ValueError(
                    f"Machine {target.name} detected in inventory "
                    f"not in the information system database ({all_machines_names=})"
                )


def get_admin_creds(inventory: Path, machine_name: str) -> tuple[str, str]:
    """
    get name and password of machine's administrator
    :param inventory:
    :return: username, password
    """
    with open(inventory, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "ansible_user" in line and machine_name in line:
                ret = []
                for search_str in ("ansible_user=", "ansible_password="):
                    ret.append(
                        line[line.find(search_str) + len(search_str) :]
                        .strip()
                        .split(" ")[0]
                    )
                return tuple(ret)


def main(engine: Engine, inventory_path) -> None:

    all_targets = get_targets(inventory_path)

    check_targets_names(engine, all_targets)
    ad_groups = select_all_in_table(engine, ADGroup)
    ad_users = select_all_in_table(engine, ADUser)
    ad_machines = select_all_in_table(engine, ADMachine)
    all_machines = select_all_in_table(engine, Machine)

    members_ad_groups = select_adgroup_with_members(engine)
    localgroup_members: dict[Machine, list[tuple[ADGroup | ADUser | User, Group]]] = {}
    for machine in ad_machines:
        localgroup_members[machine] = select_localgroup_with_members(engine, machine)
    # TODO take into account when multiple ADmachines are Domain Controllers (DC)
    machine_dc: ADMachine = [machine for machine in ad_machines if machine.is_dc][0]
    targetsDC = all_targets[machine_dc.name]
    domain_admin, domain_admin_pwd = get_admin_creds(
        inventory_path, targetsDC.targets_list[0].name
    )

    dom_adm_list = [user for user in ad_users if user.name == domain_admin]
    if len(dom_adm_list) == 1:
        user_domain_admin = dom_adm_list[0]
    else:
        user_domain_admin = ADUser(
            name=domain_admin,
            id_domain=ad_users[0].id_domain,
            password=domain_admin_pwd,
        )
        logging.warning(
            f"Domain admin {domain_admin} not in ADUser table, Using {str(user_domain_admin)=}"
        )

    all_actions = []
    # create ADusers
    all_actions.append(
        CreateMultipleWindowsDomainAccount(
            targetsDC, ad_users, domain_admin, ad_users[0].id_domain
        )
    )
    # create ADgroups
    all_actions.append(
        CreateMultipleWindowsDomainGroup(
            targetsDC, ad_groups, domain_admin, ad_groups[0].id_domain
        )
    )
    # populate ADgroups
    all_actions.append(
        AddMultipleUserToGroup(targetsDC, members_ad_groups, domain_admin)
    )

    for current_targets in (
        targets for targets in all_targets.values() if targets != targetsDC
    ):
        current_admin_creds = get_admin_creds(
            inventory_path, current_targets.targets_list[0].name
        )
        
        # Find the machine in all_machines (includes both Windows and Linux)
        matching_machines = [
            machine
            for machine in all_machines
            if machine.name == current_targets.targets_list[0].name
        ]
        
        if len(matching_machines) == 0:
            logging.error(
                f"Machine {current_targets.targets_list[0].name} not found in database. Skipping."
            )
            continue
        
        current_vm_machine: Machine = matching_machines[0]
        
        # Check if this is an AD machine (Windows) or a regular machine (Linux)
        is_ad_machine = current_vm_machine.name in [m.name for m in ad_machines]
        
        # Only process AD-related actions for Windows machines
        if not is_ad_machine:
            logging.info(
                f"Machine {current_targets.targets_list[0].name} is not an AD machine (likely Linux). "
                f"Skipping AD-related provisioning actions."
            )
            continue

        current_vm_l_users: list[User] = [
            user
            for user in select_all_in_table(engine, User)
            if user.id_machine == current_targets.targets_list[0].name
        ]

        if len(current_vm_l_users) == 0:
            print(
                f"No local user in information system found for machine {current_targets.targets_list[0].name}"
            )
            current_vm_l_users = [User(name="fake", password="123P@ss")]

        ## generate playbooks
        ### join machines to AD
        all_actions.append(
            AddClientToAD(
                current_targets,
                machine_dc,
                current_vm_l_users[0],
                targetsDC.targets_list[0].ip_address,
                user_domain_admin,
            )
        )

        # # create localusers
        # # TODO check if password complexity is not enough (user creation might fail)
        # # TODO check if username is already used (user creation will fail)
        all_actions.append(
            CreateMultipleWindowsLocalAccount(
                current_targets, current_vm_l_users, current_admin_creds[0]
            )
        )
        # # create localgroups
        # all_actions.append(CreateMultipleWindowsLocalGroup(targets, ad_users, domain_admin))
        # populate localgroups
        if current_vm_machine in localgroup_members:
            all_actions.append(
                AddMultipleUserToLocalGroup(
                    current_targets,
                    localgroup_members[current_vm_machine],
                    current_admin_creds[0],
                )
            )
        else:
            logging.warning(
                f"No localgroup members found for machine {current_vm_machine.name}. "
                f"Skipping AddMultipleUserToLocalGroup action."
            )
    # # save creds
    # # TODO not working very well for now

    out_path = playbooks_generated_path
    if out_path.exists():
        shutil.rmtree(out_path)
    out_path.mkdir()
    for idx, action in enumerate(all_actions):
        action.generate_resources(str(out_path.resolve()))
        yaml_dict = action.generate_yaml(gather_facts=False)
        with open(
            out_path / f"{idx:03}_{action.__class__.__name__}.yaml", "w"  # noqa E231
        ) as f:
            f.write("---\n{}".format(yaml.dump(yaml_dict, sort_keys=False)))
    print("playbooks successfully generated")
