#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2021 AMOSSYS. All rights reserved.
#
# This file is part of Cyber Range AMOSSYS.
#
# Cyber Range AMOSSYS can not be copied and/or distributed without the express
# permission of AMOSSYS.
#
from provisioning.actions.exec_empty_command.action import ExecEmptyCommand
from provisioning.Chronology import Chronology
from provisioning.ChronologyRunner import ChronologyRunner
from provisioning.Targets import Target
from provisioning.Targets import Targets


# Testing this action does not need any prior provisioning
def test_exec_empty_command(
    chronology: Chronology, provisioning_path: str, runner: ChronologyRunner
) -> None:

    targets = Targets()
    targets.add_target(Target("CLIENT1"))
    date = list(chronology.chronology_steps.keys())[0]

    chronology.add_action(date, ExecEmptyCommand(targets))
    chronology.generate_ansible_configuration(provisioning_path)

    runner.execute()

    # TODO: ssh/winRM into targets to ensure action worked
    # assert True
