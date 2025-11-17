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
from typing import Optional

from provisioning.action import Action
from provisioning.Targets import Targets


class ExecEmptyCommand(Action):
    def __init__(self, targets: Targets) -> None:
        super().__init__(targets=targets)

    def __str__(self) -> str:
        return "ExecEmptyCommand() on targets '{}'".format(self.targets)

    def generate_yaml(self, gather_facts: Optional[bool] = True) -> List[dict]:
        yaml_dict = {
            "hosts": str(self.targets),
            "gather_facts": "yes" if gather_facts else "no",
            "tasks": [
                {"name": "Execute command", "win_command": "whoami"},
            ],
        }

        # Special case for gather_facts
        # It can be explicitly yes, no, or implicit (i.e. use default case depending on ansible.cfg)
        if gather_facts is None:
            del yaml_dict["gather_facts"]

        return [yaml_dict]
