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
import os
import textwrap
from typing import List

from provisioning.action import Action
from provisioning.Target import Target
from provisioning.Targets import Targets


class SikuliConnection(Action):
    def __init__(self, target: Target, id_simulation: int) -> None:
        super().__init__(Targets([target]))
        self.id_simulation = id_simulation

    def __str__(self) -> str:
        return "SikuliConnection on targets '{}'".format(self.targets)

    def generate_resources(self, path: str) -> None:
        # Content of the open/close session scenario
        yaml_scenario_content = textwrap.dedent(
            """
        name: Open and close session
        target_role: client
        description: >-
          A scenario that open the OS session
        scenario_actions:
          - key: open_session
            action_params:
              - { key: login, value: "VM_USERNAME" }
              - { key: password, value: "VM_PASSWORD" }
          - key: random_sleep
            action_params:
              - { key: min, value: "45" }
              - { key: max, value: "75" }
          - key: close_session
            action_params: []
        """
        )

        # Create scenario dir
        dest_path = os.path.join(path, "scenario")
        os.makedirs(dest_path, exist_ok=True)

        # Write scenario content
        dest_yaml_file = dest_path + os.sep + "scenario-open-close-session.yml"
        with open(dest_yaml_file, "w") as fd:
            fd.write(yaml_scenario_content)

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        return [
            {
                "hosts": str(self.targets),
                "connection": "local",
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Sikuli Connection",
                        "local_action": "shell cyber_range user_activity_play {id_simulation} "
                        "-i scenario/scenario-open-close-session.yml".format(
                            id_simulation=self.id_simulation,
                        ),
                    }
                ],
            }
        ]
