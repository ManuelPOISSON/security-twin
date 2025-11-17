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
from provisioning.data_model.ActiveDirectory import ActiveDirectory
from provisioning.Targets import Targets


class MultipleBadPasswordConnexion(Action):
    def __init__(
        self,
        targets: Targets,
        active_directory: ActiveDirectory,
        accounts: List[WindowsDomainAccount],
    ) -> None:
        super().__init__(targets=targets)
        self.domain_netbios_name = active_directory.domain_netbios_name
        self.accounts = accounts

    def __str__(self) -> str:
        return "Fake connection for all fake users and computers".format()

    def generate_resources(self, path: str) -> None:
        script = PowerShellScript()
        for account in self.accounts:
            script += (
                '$cred = New-Object System.Management.Automation.PSCredential("'
                + self.domain_netbios_name
                + "\\"
                + account.name
                + '", $("'
                + account.password
                + 'a" | ConvertTo-SecureString -AsPlainText -Force));'
                + '$ErrorActionPreference = "SilentlyContinue"; Start-Process cmd /c -Credential $cred;'
                + '$ErrorActionPreference = "Stop";'
            )

        script.save_as(path + "/badconnection.ps1")

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        script = "C:\\Users\\Administrateur\\Documents\\badconnection.ps1"
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Copy bad password script",
                        "win_copy": {"src": "./badconnection.ps1", "dest": script},
                        "retries": 2,
                    },
                    {"name": "Run bad password connection", "win_shell": script},
                    {
                        "name": "Remove bad password script",
                        "win_file": {"path": script, "state": "absent"},
                        "retries": 2,
                    },
                ],
            }
        ]
