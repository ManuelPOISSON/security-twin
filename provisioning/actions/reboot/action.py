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
from provisioning.Targets import Targets


class Reboot(Action):
    def __init__(self, targets: Targets) -> None:
        super().__init__(targets=targets)

    def __str__(self) -> str:
        return "Reboot on targets '{}'".format(self.targets)

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Rebooting",
                        # timers are needed for ansible
                        "win_shell": PowerShellScript(
                            "sleep 5 ; shutdown /r /f /t 2"
                        ).content,
                    },
                    {
                        "name": "Waiting for reboot completion",
                        "wait_for_connection": {
                            "delay": 60,
                            "sleep": 5,
                            "timeout": 600,
                        },
                    },
                ],
            }
        ]
