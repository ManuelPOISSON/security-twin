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


# Wallpaper actions disabled in ChronologyFactory
def test_set_wallpaper(basebox_id: str) -> None:
    pytest.skip("Reboot action not used for the moment")
    assert True
    # Step asserts to ensure simu state
