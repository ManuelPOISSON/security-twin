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
from typing import List

from provisioning.Target import Target


class Targets(object):
    def __init__(self, targets_list: List[Target] = None) -> None:
        """A group of target objects (Targets) represent machines or virtual machines
        that have the same role.

        """
        if targets_list is None:
            targets_list = []

        self.targets_list: List[Target] = []
        for target in targets_list:
            self.add_target(target)

    # Targets handling
    def add_target(self, target: Target, silent: bool = False) -> None:
        for tmp_target in self.targets_list:
            if tmp_target.name == target.name:
                if not silent:
                    raise Exception(
                        "Cannot add target '{}', as it is already present in targets list".format(
                            target
                        )
                    )
                else:
                    return
        self.targets_list.append(target)

    def __str__(self) -> str:
        return str(self.targets_list).strip("[]").replace("'", "")
