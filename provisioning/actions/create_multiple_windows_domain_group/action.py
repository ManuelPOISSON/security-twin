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
import csv
from typing import List

from model import ADGroup
from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.Targets import Targets


class CreateMultipleWindowsDomainGroup(Action):
    def __init__(
        self,
        targets: Targets,
        groups: List[ADGroup],
        admin_username: str,
        domain_name: str,
    ) -> None:
        super().__init__(targets=targets)
        self.admin_username = admin_username
        self.domain_name = domain_name
        if self.domain_name.count(".") != 1:
            raise ValueError(
                "Domain name must be in the form 'domain.local' (with exactly one dot)"
            )
        self.groups = groups
        self.script = PowerShellScript()
        self.script += (
            'Import-Csv "C:\\Users\\'
            + admin_username
            + '\\Documents\\groups.csv" | ForEach-Object {'
            + "New-ADGroup -Name $_.Name "
            + '-SamAccountName $_."SamAccountName" '
            + '-GroupCategory $_."GroupCategory" '
            + '-GroupScope  $_."GroupScope"  '
            + '-DisplayName  $_."DisplayName"  '
            + '-Description  $_."Description"  '
            + '-Path $_."Path" '
            + "}"
        )

    def __str__(self) -> str:
        return "Create groups: {}".format(", ".join([g.name for g in self.groups]))

    def generate_resources(self, path: str) -> None:
        with open(path + "/groups.csv", "w", encoding="utf-8") as csvfile:
            fieldnames = [
                "Name",
                "SamAccountName",
                "GroupCategory",
                "GroupScope",
                "DisplayName",
                "Path",
                "Description",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for group in self.groups:
                writer.writerow(
                    {
                        "Name": group.name,
                        "SamAccountName": group.name,
                        "GroupCategory": "Security",
                        "GroupScope": "DomainLocal",
                        "DisplayName": group.name,
                        "Path": f"CN=Users, DC={self.domain_name.split('.')[0]}, DC={self.domain_name.split('.')[1]}",
                        "Description": "",
                    }
                )

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Copy group CSV",
                        "win_copy": {
                            "src": "./groups.csv",
                            "dest": "C:\\Users\\{}\\Documents\\groups.csv".format(
                                self.admin_username
                            ),
                        },
                        "retries": 2,
                    },
                    {"name": "Add group from csv", "win_shell": self.script.content},
                    {
                        "name": "Remove CSV",
                        "win_file": {
                            "path": "C:\\Users\\{}\\Documents\\groups.csv".format(
                                self.admin_username
                            ),
                            "state": "absent",
                        },
                        "retries": 2,
                    },
                ],
            }
        ]
