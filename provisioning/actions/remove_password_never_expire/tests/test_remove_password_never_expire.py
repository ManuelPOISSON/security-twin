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
from datetime import datetime

import pytest

from provisioning.actions.create_multiple_windows_domain_account.tests.test_create_multiple_windows_domain_account import (
    REQUIRED_ACTIONS as PRIOR_ACTIONS,
)
from provisioning.actions.remove_password_never_expire import RemovePasswordNeverExpire
from provisioning.Chronology import Chronology
from provisioning.ChronologyRunner import ChronologyRunner
from provisioning.Targets import Target
from provisioning.Targets import Targets

REQUIRED_ACTIONS = PRIOR_ACTIONS + [RemovePasswordNeverExpire]


@pytest.fixture()
def required_actions() -> None:
    return REQUIRED_ACTIONS


def test_remove_password_never_expire(
    required_chronology: Chronology, provisioning_path: str, runner: ChronologyRunner
) -> None:

    targets = Targets()
    for node_name in required_chronology.organization.roles["ad"]:
        target = Target(node_name)
        targets.add_target(target)

    date = datetime.now().replace(microsecond=0)
    required_chronology.add_step(date, True)

    accounts = []
    accounts += required_chronology.organization.fake_accounts
    accounts += required_chronology.organization.admin_accounts
    accounts += required_chronology.organization.real_accounts

    for account in accounts:
        required_chronology.add_action(
            date,
            RemovePasswordNeverExpire(targets, account),
        )

    required_chronology.generate_ansible_configuration(provisioning_path)
    runner.execute()

    # TODO: ssh/winRM into targets to ensure action worked
    # assert True
