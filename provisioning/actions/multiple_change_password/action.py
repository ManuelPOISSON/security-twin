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

from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.data_model.account.WindowsDomainAccount import WindowsDomainAccount
from provisioning.Targets import Targets


class MultipleChangePassword(Action):
    def __init__(self, targets: Targets, accounts: List[WindowsDomainAccount]) -> None:
        super().__init__(targets=targets)
        self.accounts = accounts

    def __str__(self) -> str:
        return "Change password for users and computers".format()

    def generate_resources(self, path: str) -> None:
        script = PowerShellScript()
        for account in self.accounts:
            script += (
                "Set-ADUser -Identity "
                + account.name
                + " -PasswordNeverExpires $false ;Set-ADAccountPassword -Identity "
                + account.name
                + ' -NewPassword (ConvertTo-SecureString -AsPlainText "'
                + account.password
                + '" -Force)'
            )

        script.save_as(path + "/changepassword.ps1")

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        script = "C:\\Users\\Administrateur\\Documents\\changepassword.ps1"
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Copy change password script",
                        "win_copy": {"src": "./changepassword.ps1", "dest": script},
                        "retries": 2,
                    },
                    {"name": "Run change password connection", "win_shell": script},
                    {
                        "name": "Remove change password script",
                        "win_file": {"path": script, "state": "absent"},
                        "retries": 2,
                    },
                ],
            }
        ]
