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

from model import ADUser
from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.Targets import Targets


class CreateMultipleWindowsDomainAccount(Action):
    def __init__(
        self,
        targets: Targets,
        accounts: List[ADUser],
        admin_username: str,
        domain_name: str,
    ) -> None:
        super().__init__(targets=targets)

        self.accounts = accounts
        self.admin_username = admin_username
        self.domain_name = domain_name
        if self.domain_name.count(".") != 1:
            raise ValueError(
                "Domain name must be in the form 'domain.local' (with exactly one dot)"
            )
        self.script = PowerShellScript()
        self.csv_file = "utilisateurs.csv"
        self.script += (
            'Import-Csv "C:\\Users\\'
            + admin_username
            + "\\Documents\\"
            + self.csv_file
            + '" | ForEach-Object {'
            + "New-ADUser -Name $_.Name "
            + '-GivenName $_."GivenName" '
            + '-Surname $_."Surname" '
            + '-SamAccountName  $_."SamAccountName" '
            + '-UserPrincipalName  $_."UserPrincipalName"  '
            + '-Path $_."Path" '
            + "-PasswordNeverExpires $True "
            + '-AccountPassword (ConvertTo-SecureString $_."Password" -AsPlainText -force) -Enabled $true}'
        )

    def __str__(self) -> str:
        return "Create multiple accounts on targets '{}'".format(self.targets)

    def generate_resources(self, path: str) -> None:
        with open(path + f"/{self.csv_file}", "w", encoding="utf-8") as csvfile:
            fieldnames = [
                "Name",
                "GivenName",
                "Surname",
                "SamAccountName",
                "UserPrincipalName",
                "Path",
                "Password",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for account in self.accounts:
                writer.writerow(
                    {
                        "Name": account.name,
                        "GivenName": account.name,
                        "Surname": account.name,
                        "SamAccountName": account.name,
                        "UserPrincipalName": account.name,
                        "Path": f"CN=Users, DC={self.domain_name.split('.')[0]}, DC={self.domain_name.split('.')[1]}",
                        "Password": account.password,
                    }
                )

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Copy CSV",
                        "win_copy": {
                            "src": f"./{self.csv_file}",
                            "dest": "C:\\Users\\"
                            + self.admin_username
                            + "\\Documents\\"
                            + self.csv_file,
                        },
                        "retries": 2,
                    },
                    {"name": "Run script Add", "win_shell": self.script.content},
                    {
                        "name": "Remove CSV",
                        "win_file": {
                            "path": "C:\\Users\\"
                            + self.admin_username
                            + "\\Documents\\"
                            + self.csv_file,
                            "state": "absent",
                        },
                        "retries": 2,
                    },
                ],
            }
        ]
