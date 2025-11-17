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
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.data_model.updates.kb import KB
from provisioning.data_model.updates.update_files_handler import UpdateFilesHandler
from provisioning.logger import logger
from provisioning.Targets import Targets


class InstallKB(Action):
    __user_folders = ["Desktop", "Documents", "Downloads"]

    def __init__(self, targets: Targets, kb: KB) -> None:
        super().__init__(targets=targets)
        self.kb = kb
        self.dest = "C:\\Temp\\KB\\"

    def __str__(self) -> str:
        return "Install {} on '{}'".format(self.kb, self.targets)

    def generate_resources(self, path: str) -> None:
        for target in self.targets.targets_list:
            folder_path = os.path.join(path, "files", str(target), "KB")
            os.makedirs(folder_path, exist_ok=True)

            files_handler = UpdateFilesHandler()
            kb_path = files_handler.kb_filepath(self.kb.filename)
            print("      [+] Copying '{}' to '{}'".format(kb_path, folder_path))
            if os.path.exists(kb_path):
                shutil.copy(kb_path, folder_path)
            else:
                logger.warning("KB file not found: {}".format(self.kb.filename))

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        copy_tasks = []
        for target in self.targets.targets_list:
            copy_tasks.append(
                {
                    "name": "Copying KB file to {} in {}".format(self.dest, target),
                    "win_copy": {
                        "dest": self.dest,
                        "src": "files/{}/KB/{}".format(target, self.kb.filename),
                    },
                }
            )

        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Install KB",
                        "block": [
                            {
                                "name": "Ensuring that the KB install dir is empty",
                                "win_file": {"path": "C:\\Temp\\KB", "state": "absent"},
                            },
                            *copy_tasks,
                            {
                                "name": "Creating cab subdir",
                                "win_file": {
                                    "path": "C:\\Temp\\KB\\cab",
                                    "state": "directory",
                                },
                            },
                            {
                                "name": "Extracting MSU",
                                "win_shell": PowerShellScript(
                                    "Expand -F:* C:\\Temp\\KB\\* C:\\Temp\\KB\\cab"
                                ).content,
                            },
                            {
                                "name": "Cleaning up extracted files",
                                "win_file": {
                                    "path": "C:\\Temp\\KB\\cab\\WSUSSCAN.cab",
                                    "state": "absent",
                                },
                            },
                            {
                                "name": "Installing KB {}".format(self.kb.name),
                                # This command can return an error code even on success, so "ignore_errors" is needed
                                "win_shell": PowerShellScript(
                                    "DISM.exe /Online /NoRestart /Add-Package /PackagePath:C:\\Temp\\KB\\cab"
                                ).content,
                                "ignore_errors": True,
                            },
                        ],
                        "rescue": [
                            {
                                # This can happen if the KB file could not be copied
                                "debug": {
                                    "msg": "ERROR: Could not install {}, skipping.".format(
                                        self.kb.name
                                    ),
                                }
                            }
                        ],
                        "always": [
                            {
                                "name": "Deleting KB install dir",
                                "win_file": {"path": "C:\\Temp\\KB", "state": "absent"},
                            },
                        ],
                    },
                ],
            }
        ]
