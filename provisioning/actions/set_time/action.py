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
from datetime import datetime
from typing import List

from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.Targets import Targets


class SetTime(Action):
    def __init__(self, targets: Targets, timestamp: datetime) -> None:
        super().__init__(targets=targets)
        self.timestamp = timestamp

    def __str__(self) -> str:
        return "SetTime('{}') on targets '{}'".format(self.timestamp, self.targets)

    def generate_yaml(self, gather_facts: bool = True) -> List[dict]:
        windows_timestamp = self.timestamp.strftime("%d/%m/%Y %H:%M:%S")
        linux_timestamp = self.timestamp.strftime("%y%m%d	%H:%M:%S")
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Set time (Windows hosts)",
                        "win_shell": PowerShellScript(
                            'Set-Date -Date "{}"'.format(windows_timestamp)
                        ).content,
                        "retries": 2,
                        "when": "ansible_os_family == 'Windows'",
                    },
                    {
                        "name": "Set time (Linux hosts)",
                        "shell": 'date +%Y%m%d%t%T -s "{}"'.format(linux_timestamp),
                        "retries": 2,
                        "when": "ansible_system == 'Linux'",
                    },
                ],
            }
        ]
