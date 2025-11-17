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
from datetime import datetime
from datetime import time
from typing import List

from provisioning.action import Action
from provisioning.actions.powershell.ApplyRights import ApplyRights
from provisioning.actions.powershell.UpdateFileTimestamps import UpdateFileTimestamps
from provisioning.data_model.file.FileTreeGenerator import FileTreeGenerator
from provisioning.data_model.Organization import Organization
from provisioning.Targets import Targets


class PopulateFileServer(Action):
    def __init__(
        self,
        targets: Targets,
        organization: Organization,
        sharing_name: str,
        file_tree_generator: FileTreeGenerator,
        start_date: datetime,
        end_date: datetime,
        opening_time: time,
        ending_time: time,
    ) -> None:
        super().__init__(targets=targets)
        self.organization = organization
        self.sharing_name = sharing_name
        self.file_tree_generator = file_tree_generator
        self.start_date = start_date
        self.end_date = end_date
        self.opening_time = opening_time
        self.ending_time = ending_time

    def __str__(self) -> str:
        return "PopulateFileServer on targets '{}'".format(self.targets)

    def generate_resources(self, path: str) -> None:
        scripts_dir = os.path.join(path, "scripts")
        os.makedirs(scripts_dir, exist_ok=True)
        UpdateFileTimestamps().save_as(
            os.path.join(scripts_dir, UpdateFileTimestamps.name())
        )
        ApplyRights().save_as(os.path.join(scripts_dir, ApplyRights.name()))
        self.file_tree_generator.generate(path)

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
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
                    {
                        "name": "copy {} script".format(ApplyRights.name()),
                        "win_copy": {
                            "dest": "{{ tempdir.path }}\\",
                            "src": os.path.join("scripts", ApplyRights.name()),
                        },
                    },
                    {
                        "name": "copy rights.csv file",
                        "win_copy": {
                            "dest": "{{ tempdir.path }}\\",
                            "src": "rights.csv",
                        },
                    },
                    {
                        "name": "copy files to samba shared folder",
                        "win_copy": {
                            "dest": "E:\\Shares\\partage\\",
                            "src": "shared_files/",
                        },
                    },
                    {
                        "name": "update files/directories timestamps",
                        "win_shell": UpdateFileTimestamps.call(
                            "{{{{ tempdir.path }}}}\\{}".format(
                                UpdateFileTimestamps.name()
                            ),
                            "E:\\Shares\\partage\\",
                            self.start_date,
                            self.end_date,
                            self.opening_time,
                            self.ending_time,
                        ),
                    },
                    {
                        "name": "apply rights",
                        "win_shell": ApplyRights.call(
                            "{{{{ tempdir.path }}}}\\{}".format(ApplyRights.name()),
                            # TODO(QA): self.organization.active_directory can be null
                            self.organization.active_directory.domain_netbios_name,
                            self.sharing_name,
                            "E:\\Shares\\partage\\",
                            "{{ tempdir.path }}\\rights.csv",
                        ),
                    },
                    {
                        "name": "remove temporary directory",
                        "win_file": {"path": "{{ tempdir.path }}", "state": "absent"},
                    },
                ],
            }
        ]
