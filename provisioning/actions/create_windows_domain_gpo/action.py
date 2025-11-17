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
from provisioning.data_model.gpo.WindowsDomainGPO import WindowsDomainGPO
from provisioning.Targets import Targets


class CreateWindowsDomainGPO(Action):
    def __init__(self, targets: Targets, gpo: WindowsDomainGPO) -> None:
        super().__init__(targets=targets)
        self.gpo = gpo

    def __str__(self) -> str:
        return "Create GPO ('{}') on targets '{}'".format(self.gpo.name, self.targets)

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        script = PowerShellScript()
        script += (
            "Import-GPO -BackupGpoName "
            + self.gpo.name
            + " -Path C:\\Temp\\gpo -TargetName "
            + self.gpo.name
            + " -createIfNeeded ;"
        )
        script += (
            "New-GPLink -Name " + self.gpo.name + ' -Target "' + self.gpo.link + '";'
        )

        for gppermission in self.gpo.gppermission:
            script += (
                "Set-GPPermission -Name "
                + self.gpo.name
                + ' -TargetName "'
                + gppermission.name
                + '" -TargetType '
                + gppermission.targetType
                + " -PermissionLevel "
                + gppermission.permission
                + ";"
            )

        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Copy backup",
                        "win_copy": {
                            "src": self.gpo.local_path,
                            "dest": "C:\\Temp\\gpo",
                        },
                    },
                    {"name": "Import GPO", "win_shell": script.content},
                    {
                        "name": "Delete backup",
                        "win_file": {"path": "C:\\Temp\\gpo", "state": "absent"},
                    },
                ],
            }
        ]
