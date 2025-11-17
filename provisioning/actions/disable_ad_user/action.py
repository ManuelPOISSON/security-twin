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
import datetime
from typing import List

from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.data_model.account.WindowsDomainAccount import WindowsDomainAccount
from provisioning.Targets import Targets


class DisableADUser(Action):
    def __init__(
        self,
        targets: Targets,
        account: WindowsDomainAccount,
        domain_netbios_name: str,
        date: datetime.datetime,
    ) -> None:
        super().__init__(targets=targets)

        self.account = account
        self.domain_netbios_name = domain_netbios_name
        self.date = date

    def __str__(self) -> str:
        return "Disable AD user {}".format(self.account.name)

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        script = PowerShellScript()
        script += (
            '$cred = New-Object System.Management.Automation.PSCredential("'
            + self.domain_netbios_name
            + "\\"
            + self.account.name
            + '", $("'
            + self.account.password
            + '" | ConvertTo-SecureString -AsPlainText -Force));'
            + '$ErrorActionPreference = "SilentlyContinue"; Start-Process cmd /c -Credential $cred;'
            + '$ErrorActionPreference = "Stop";'
        )
        script += (
            'Set-ADUser -Identity "'
            + self.account.name
            + '" -AccountExpirationDate "'
            + self.date.isoformat()
            + '"; '
        )
        script += "Disable-ADAccount -Identity " + self.account.name + "; "
        script += (
            'Remove-ADComputer -Identity "'
            + self.account.name.upper()
            + '-PC" -Confirm:$False'
        )

        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Disable user",
                        "win_shell": script.content,
                        "retries": 2,
                    }
                ],
            }
        ]
