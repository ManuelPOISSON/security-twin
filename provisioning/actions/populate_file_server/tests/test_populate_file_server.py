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

from provisioning.actions.create_file_server.tests.test_create_file_server import (
    REQUIRED_ACTIONS as FILESERVER_ACTIONS,
)
from provisioning.actions.create_multiple_windows_domain_account.tests.test_create_multiple_windows_domain_account import (
    REQUIRED_ACTIONS as ACCOUNTS_ACTIONS,
)
from provisioning.actions.create_multiple_windows_domain_group.tests.test_create_multiple_windows_domain_group import (
    REQUIRED_ACTIONS as GROUPS_ACTIONS,
)
from provisioning.actions.populate_file_server import PopulateFileServer
from provisioning.Chronology import Chronology
from provisioning.ChronologyRunner import ChronologyRunner


REQUIRED_ACTIONS = list(
    set(ACCOUNTS_ACTIONS + GROUPS_ACTIONS + FILESERVER_ACTIONS + [PopulateFileServer])
)


@pytest.fixture()
def required_actions() -> None:
    return REQUIRED_ACTIONS


def test_populate_fileserver(
    required_chronology: Chronology, provisioning_path: str, runner: ChronologyRunner
) -> None:

    required_chronology.generate_ansible_configuration(provisioning_path)
    runner.execute()

    # TODO: ssh/winRM into targets to ensure action worked
    # assert True
