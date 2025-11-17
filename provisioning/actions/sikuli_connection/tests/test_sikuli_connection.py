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


# Sikuli Connexion actions disabled in ChronologyFactory
def test_sikuli_connexion(basebox_id: str) -> None:
    pytest.skip("SikuliConnexion action not used for the moment")
    assert True
    # Step asserts to ensure simu state
