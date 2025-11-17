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
import pytest

from provisioning.actions.create_multiple_windows_domain_group.tests.test_create_multiple_windows_domain_group import (
    REQUIRED_ACTIONS as GROUPS_ACTIONS,
)
from provisioning.actions.create_windows_domain_gpo import CreateWindowsDomainGPO
from provisioning.actions.create_windows_domain_ou.tests.test_create_windows_domain_ou import (
    REQUIRED_ACTIONS as OU_ACTIONS,
)
from provisioning.Chronology import Chronology
from provisioning.ChronologyRunner import ChronologyRunner

REQUIRED_ACTIONS = list(set(GROUPS_ACTIONS + OU_ACTIONS + [CreateWindowsDomainGPO]))


@pytest.fixture()
def required_actions() -> None:
    return REQUIRED_ACTIONS


def test_create_windows_domain_gpo(
    required_chronology: Chronology, provisioning_path: str, runner: ChronologyRunner
) -> None:

    required_chronology.generate_ansible_configuration(provisioning_path)
    runner.execute()

    # TODO: ssh/winRM into targets to ensure action worked
    # assert True
