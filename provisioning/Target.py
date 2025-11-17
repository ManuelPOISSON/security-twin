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
from typing import Optional


class Target(object):
    def __init__(self, name: str, ip_address: Optional[str] = None) -> None:
        """A target object represents a machine or virtual machine on which
        we want to play actions.

        """
        self.name = name
        self.ip_address = ip_address

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name
