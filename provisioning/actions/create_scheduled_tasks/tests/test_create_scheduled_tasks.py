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
from typing import List

import pytest

from provisioning.actions.add_client_to_ad.tests.test_add_client_to_ad import (
    REQUIRED_ACTIONS as CLIENT_ACTIONS,
)
from provisioning.actions.create_multiple_windows_domain_group.tests.test_create_multiple_windows_domain_group import (
    REQUIRED_ACTIONS as GROUP_ACTIONS,
)
from provisioning.actions.create_multiple_windows_domain_machine.tests.test_create_multiple_windows_domain_machine import (
    REQUIRED_ACTIONS as MACHINE_ACTIONS,
)
from provisioning.actions.create_scheduled_tasks import CreateScheduledTasks
from provisioning.Chronology import Chronology
from provisioning.ChronologyRunner import ChronologyRunner

REQUIRED_ACTIONS = list(
    set(MACHINE_ACTIONS + GROUP_ACTIONS + CLIENT_ACTIONS + [CreateScheduledTasks])
)


@pytest.fixture
def required_actions() -> List:
    return REQUIRED_ACTIONS


# Testing this action does not need any prior provisioning
def test_create_ad_server(
    required_chronology: Chronology, provisioning_path: str, runner: ChronologyRunner
) -> None:

    required_chronology.generate_ansible_configuration(provisioning_path)
    runner.execute()

    # TODO: ssh/winRM into targets to ensure action worked
    # assert True
