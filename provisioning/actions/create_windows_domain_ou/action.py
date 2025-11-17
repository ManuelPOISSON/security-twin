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

from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.data_model.Organizational_units import OrganizationalUnits
from provisioning.Targets import Targets


class CreateWindowsDomainOU(Action):
    def __init__(
        self,
        targets: Targets,
        organization_units: OrganizationalUnits,
        admin_username: str,
    ) -> None:
        super().__init__(targets=targets)

        self.organization_units = organization_units
        self.admin_username = admin_username
        self.script = PowerShellScript()
        self.script += (
            'Import-Csv "C:\\Users\\'
            + admin_username
            + '\\Documents\\ou.csv" | ForEach-Object {'
            + "New-ADOrganizationalUnit $_.Name "
            + '-path $_."Path" }'
        )

    def __str__(self) -> str:
        # TODO(QA): unresolved attribute reference 'ou_list' for class 'WindowsDomainOU'
        return "CreateOU('{}') on targets '{}'".format(
            self.organization_units.ou_list, self.targets
        )

    def generate_resources(self, path: str) -> None:
        with open(path + "/ou.csv", "w", encoding="utf-8") as csvfile:
            fieldnames = ["Name", "Path"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            # TODO(QA): unresolved attribute reference 'ou_list' for class 'WindowsDomainOU'
            for ou in self.organization_units.ou_list:
                writer.writerow({"Name": ou.name, "Path": ou.path})

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Copy OU csv",
                        "win_copy": {
                            "src": "./ou.csv",
                            "dest": "C:\\Users\\{}\\Documents\\ou.csv".format(
                                self.admin_username
                            ),
                        },
                    },
                    {"name": "Add OU from csv", "win_shell": self.script.content},
                    {
                        "name": "Remove CSV",
                        "win_file": {
                            "path": "C:\\Users\\{}\\Documents\\ou.csv".format(
                                self.admin_username
                            ),
                            "state": "absent",
                        },
                    },
                ],
            }
        ]
