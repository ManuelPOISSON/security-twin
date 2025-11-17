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
from abc import ABC
from abc import abstractmethod
from typing import List

from provisioning.Targets import Targets


class Action(ABC):
    def __init__(self, targets: Targets) -> None:
        # A target object represents a machine or virtual machine on
        # which we want to play actions
        self.targets = targets

    def __str__(self) -> str:
        return "Action on targets '{}'".format(self.targets)

    def generate_resources(self, path: str) -> None:
        pass

    @abstractmethod
    def generate_yaml(self, gather_facts: bool) -> List[dict]:
        pass
