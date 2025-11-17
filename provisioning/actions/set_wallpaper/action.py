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
import os
import shutil
from typing import List

from provisioning.action import Action
from provisioning.config import provisioning_config
from provisioning.data_model.account.WindowsDomainAccount import WindowsDomainAccount
from provisioning.Target import Target
from provisioning.Targets import Targets


class SetWallpaper(Action):
    def __init__(self, target: Target, account: WindowsDomainAccount) -> None:
        super().__init__(Targets([target]))
        self.target = target
        self.account = account

    def __str__(self) -> str:
        return "SetWallpaper on targets '{}'".format(self.targets)

    def generate_resources(self, path: str) -> None:
        # fetch file entries by patterns
        # FIXME: allow a random choice from the available wallpapers
        src_path = provisioning_config["wallpapers_path"] / "wallpaper.jpg"

        if not os.path.exists(src_path):
            raise Exception("The path '{}' does not exist".format(src_path))

        dest_path = os.path.join(path, "files", str(self.target))
        os.makedirs(dest_path, exist_ok=True)
        dest_path = os.path.join(dest_path, "TranscodedWallpaper.jpg")
        shutil.copy(src_path, dest_path)

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Check user AppData path exists",
                        "win_stat": {
                            "path": "C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Themes".format(
                                username=self.account.name
                            )
                        },
                        "register": "stat_dir",
                    },
                    {
                        "name": "Copy wallpaper",
                        "win_copy": {
                            "dest": "C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper.jpg".format(
                                username=self.account.name
                            ),
                            "src": "files/{}/TranscodedWallpaper.jpg".format(
                                str(self.target)
                            ),
                        },
                        "when": "stat_dir.stat.exists == True",
                    },
                ],
            }
        ]
