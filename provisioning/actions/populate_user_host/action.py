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
import random
import shutil
from datetime import datetime
from datetime import time
from typing import Dict
from typing import List

from model import Machine
from provisioning.action import Action
from provisioning.actions.powershell.UpdateFileTimestamps import UpdateFileTimestamps


from provisioning.Target import Target
from provisioning.Targets import Targets


class PopulateUserHost(Action):
    """
    This action populates a user's host with files and directories.
    Copy files from files/{self.target}/{folder} to
        C:\\Users\\{self.machine.account.name}\\{folder} on Windows
        /home/{self.machine.account.name}/{folder} on Linux
    Destination directories must exist to copy files (else the task is skipped).
    """

    __windows_user_folders = ["Desktop", "Documents", "Downloads"]
    __linux_user_folders = ["Documents", "Bureau", "Téléchargements"]

    def __init__(
        self,
        target: Target,
        machine: Machine,
        start_date: datetime,
        end_date: datetime,
        opening_time: time,
        ending_time: time,
    ) -> None:
        super().__init__(Targets([target]))
        self.target = target
        self.machine = machine
        self.start_date = start_date
        self.end_date = end_date
        self.opening_time = opening_time
        self.ending_time = ending_time

    def __str__(self) -> str:
        return "PopulateUserHost on targets '{}'".format(self.targets)

    @staticmethod
    def __pick_entries(entries_list: List[List[Dict]]) -> List[Dict]:
        filenames = []
        n = random.randint(5, 20)

        if not len(entries_list):
            return []
        for i in range(n):
            entries = entries_list[i % len(entries_list)]
            if not len(entries):
                continue
            chosen_entry_index = random.randrange(0, len(entries))
            filenames.append(entries.pop(chosen_entry_index))
        return filenames

    def generate_resources(self, path: str) -> None:
        print("PopulateUserHost.generate_resources\n" "check how it is done")

        # scripts_dir = os.path.join(path, "scripts")
        # os.makedirs(scripts_dir, exist_ok=True)
        # # TODO: file is overwritten multiple times
        # UpdateFileTimestamps().save_as(
        #     os.path.join(scripts_dir, UpdateFileTimestamps.name())
        # )
        # # fetch file entries by patterns
        # files_database = AgingFilesDatabase(provisioning_config["files_path"])
        # file_entries = files_database.sort_by_patterns(
        #     AgingFilesDatabase.FIELD_EXT,
        #     ["doc(?:m|x)?", "odt", "pdf", "ppt(?:m|x)?", "xls(?:m|x)?"],
        #     True,
        # )
        # entries_list = list(file_entries.values())
        #
        # if self.machine.system_type == "windows":
        #     os_user_folders = self.__windows_user_folders
        # elif self.machine.system_type == "linux":
        #     os_user_folders = self.__linux_user_folders
        # else:
        #     raise Exception("system_type '{machine.system_type} not supported'")
        #
        # for folder_name in os_user_folders:
        #     folder_path = os.path.join(path, "files", str(self.target), folder_name)
        #     os.makedirs(folder_path, exist_ok=True)
        #     for entry in self.__pick_entries(entries_list):
        #         if not os.path.exists(
        #             os.path.join(folder_path, entry[AgingFilesDatabase.FIELD_FILENAME])
        #         ):
        #             shutil.copy(files_database.resolve_filepath(entry), folder_path)

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        if self.machine.system_type == "windows":
            return self.generate_yaml_windows(gather_facts=gather_facts)
        elif self.machine.system_type == "linux":
            return self.generate_yaml_linux(gather_facts=gather_facts)
        else:
            raise Exception("system_type '{machine.system_type} not supported'")

    def generate_yaml_windows(self, gather_facts: bool) -> List[dict]:
        copy_tasks = []
        dests = []
        for folder in self.__windows_user_folders:
            dest = "C:\\Users\\{}\\{}\\".format(self.machine.account.name, folder)
            dests.append(dest)
            copy_tasks.extend(
                [
                    {
                        "name": "check if remote dir '{}' exist".format(dest),
                        "win_stat": {
                            "path": dest,
                        },
                        "register": "folder_info",
                    },
                    {
                        "name": "copy files to {}".format(dest),
                        "win_copy": {
                            "dest": dest,
                            "src": "files/{}/{}/".format(str(self.target), folder),
                        },
                        "when": "folder_info.stat.exists",
                    },
                ]
            )
        return [
            {
                "hosts": str(self.target),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Ensure user profile & user home directory exists",
                        "win_user_profile": {
                            "username": f"{self.machine.account.name}",
                            "state": "present",
                        },
                    },
                    {
                        "name": "create temporary directory",
                        "win_tempfile": {"state": "directory"},
                        "register": "tempdir",
                    },
                    {
                        "name": "copy {} script".format(UpdateFileTimestamps.name()),
                        "win_copy": {
                            "dest": "{{ tempdir.path }}\\",
                            "src": os.path.join("scripts", UpdateFileTimestamps.name()),
                        },
                    },
                    *copy_tasks,
                    {
                        "name": "update files/directories timestamps",
                        "win_shell": UpdateFileTimestamps.call(
                            f"{{{{ tempdir.path }}}}\\{UpdateFileTimestamps.name()}",  # noqa E201,202
                            dests,
                            self.start_date,
                            self.end_date,
                            self.opening_time,
                            self.ending_time,
                        ),
                    },
                    {
                        "name": "remove temporary directory",
                        "win_file": {"path": "{{ tempdir.path }}", "state": "absent"},
                    },
                ],
            }
        ]

    def generate_yaml_linux(self, gather_facts: bool) -> List[dict]:
        copy_tasks = []
        dests = []
        for folder in self.__linux_user_folders:
            dest = "/home/{}/{}".format(self.machine.account.name, folder)
            dests.append(dest)
            copy_tasks.extend(
                [
                    {
                        "name": "check if remote dir '{}' exist".format(dest),
                        "stat": {
                            "path": dest,
                        },
                        "register": "folder_info",
                    },
                    {
                        "name": "copy files to {}".format(dest),
                        "copy": {
                            "dest": dest,
                            "src": "files/{}/{}/".format(str(self.target), folder),
                        },
                        "when": "folder_info.stat.exists",
                    },
                ]
            )
        return [
            {
                "hosts": str(self.target),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "create temporary directory",
                        "tempfile": {"state": "directory"},
                        "register": "tempdir",
                    },
                    *copy_tasks,
                    {
                        "name": "remove temporary directory",
                        "file": {"path": "{{ tempdir.path }}", "state": "absent"},
                    },
                ],
            }
        ]
