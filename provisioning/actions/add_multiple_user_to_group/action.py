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
from typing import List
from typing import Tuple

from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from model import ADGroup, ADUser
from provisioning.Targets import Targets


class AddMultipleUserToGroup(Action):
    def __init__(
        self,
        targets: Targets,
        accounts_groups: List[Tuple[ADGroup | ADUser, ADGroup]],
        admin_username: str,
    ) -> None:
        """

        :param targets:
        :param accounts_groups: (member, group)
        """
        super().__init__(targets=targets)
        self.accounts_groups = accounts_groups
        self.admin_username = admin_username
        self._PS_SCRIPT_NAME = "add_users_to_group.ps1"

    def __str__(self) -> str:
        return "Add users to group"

    def generate_resources(self, path: str) -> None:
        script = PowerShellScript()

        for item in self.accounts_groups:
            script += (
                'Add-ADGroupMember -Identity "'
                + item[1].name
                + '" -Members "'
                + item[0].name
                + '"; '
            )

        script.save_as(path + f"/{self._PS_SCRIPT_NAME}")

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        # TODO(QA): use a temporary folder to create your scritps
        script = (
            f"C:\\Users\\{self.admin_username}\\Documents\\"  # noqa E231
            + self._PS_SCRIPT_NAME
        )
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Copy CSV for add users to group",
                        "win_copy": {
                            "src": f"./{self._PS_SCRIPT_NAME}",
                            "dest": script,
                        },
                        "retries": 2,
                    },
                    {"name": "Add users to group", "win_shell": script},
                    {
                        "name": "Delete CSV for add users to group",
                        "win_file": {"path": script, "state": "absent"},
                        "retries": 2,
                    },
                ],
            }
        ]
