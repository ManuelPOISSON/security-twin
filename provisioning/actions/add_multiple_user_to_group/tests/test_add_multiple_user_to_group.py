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

from provisioning.actions.add_multiple_user_to_group import AddMultipleUserToGroup
from provisioning.actions.create_multiple_windows_domain_account.tests.test_create_multiple_windows_domain_account import (
    REQUIRED_ACTIONS as ACCOUNT_ACTIONS,
)
from provisioning.actions.create_multiple_windows_domain_group.tests.test_create_multiple_windows_domain_group import (
    REQUIRED_ACTIONS as GROUP_ACTIONS,
)
from provisioning.Chronology import Chronology
from provisioning.ChronologyRunner import ChronologyRunner

REQUIRED_ACTIONS = list(set(GROUP_ACTIONS + ACCOUNT_ACTIONS + [AddMultipleUserToGroup]))


@pytest.fixture()
def required_actions() -> List:
    return REQUIRED_ACTIONS


def test_add_multiple_user_to_group(
    required_chronology: Chronology, provisioning_path: str, runner: ChronologyRunner
) -> None:

    required_chronology.generate_ansible_configuration(provisioning_path)
    runner.execute()

    # TODO: ssh/winRM into targets to ensure action worked
    # assert True
