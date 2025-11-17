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


class ChangePassword(Action):
    def __init__(self, targets: Targets, account: WindowsDomainAccount) -> None:
        super().__init__(targets=targets)
        self.account = account

    def __str__(self) -> str:
        return "Change password for {} on targets '{}'".format(
            self.account.name, self.targets
        )

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        script = PowerShellScript()

        script += (
            "Set-ADUser -Identity "
            + self.account.name
            + " -PasswordNeverExpires $false ;Set-ADAccountPassword -Identity "
            + self.account.name
            + ' -NewPassword (ConvertTo-SecureString -AsPlainText "'
            + self.account.password
            + '" -Force)'
        )

        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [{"name": "Connect user", "win_shell": script.content}],
            }
        ]
