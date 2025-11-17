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
from provisioning.Targets import Targets


class ExecCommand(Action):
    def __init__(self, targets: Targets, command: str) -> None:
        super().__init__(targets=targets)
        self.command = command

    def __str__(self) -> str:
        return "ExecCommand('{}') on targets '{}'".format(self.command, self.targets)

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [{"name": "Execute command", "win_command": self.command}],
            }
        ]
