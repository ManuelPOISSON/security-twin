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


class BadPasswordConnexion(Action):
    def __init__(
        self,
        targets: Targets,
        active_directory: ActiveDirectory,
        account: WindowsDomainAccount,
    ) -> None:
        super().__init__(targets=targets)
        self.account = account
        self.domain_netbios_name = active_directory.domain_netbios_name

    def __str__(self) -> str:
        return "Bad password connection for {} on targets '{}'".format(
            self.account.name, self.targets
        )

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        script = PowerShellScript()
        script += (
            '$cred = New-Object System.Management.Automation.PSCredential("'
            + self.domain_netbios_name
            + "\\"
            + self.account.name
            + '", $("'
            + self.account.password
            + 'a" | ConvertTo-SecureString -AsPlainText -Force))'
            + ';$ErrorActionPreference = "SilentlyContinue"; Start-Process cmd /c -Credential $cred'
        )

        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Connect user with bad password",
                        "win_shell": script.content,
                    }
                ],
            }
        ]
