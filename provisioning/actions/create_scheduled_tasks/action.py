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
import csv
import ntpath
import os
from typing import Dict
from typing import List

from provisioning.action import Action
from provisioning.data_model.account.WindowsDomainAccount import WindowsDomainAccount
from provisioning.data_model.machine.Machine import Machine
from provisioning.Target import Target
from provisioning.Targets import Targets


class CreateScheduledTasks(Action):
    def __init__(
        self,
        target: Target,
        scheduled_tasks: List[Dict],
        domain_netbios_name: str,
        admin_account: WindowsDomainAccount,
        remote_machines: List[Machine],
    ) -> None:
        super().__init__(Targets([target]))
        self.target = target
        self.scheduled_tasks = scheduled_tasks
        self.domain_netbios_name = domain_netbios_name
        self.admin_account = admin_account
        self.remote_machines = remote_machines

    def generate_resources(self, path: str) -> None:
        scheduled_tasks_dir = os.path.join(path, "scheduled_tasks")
        os.makedirs(scheduled_tasks_dir, exist_ok=True)
        for task in self.scheduled_tasks:
            with open(
                "{}.ps1".format(os.path.join(scheduled_tasks_dir, task["name"])),
                "w",
                encoding="cp1252",
            ) as file:
                file.write(task["script"])

        with open(
            os.path.join(path, "RemoteClients.csv"), "w", encoding="cp1252"
        ) as file:
            csv_writer = csv.DictWriter(file, fieldnames=["ComputerName", "UserName"])
            csv_writer.writeheader()
            for m in self.remote_machines:
                # TODO(QA): m.account is not present inside Machine type
                csv_writer.writerow(
                    {
                        "ComputerName": "{}-pc".format(m.account.name),
                        "UserName": m.account.name,
                    }
                )

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        scheduled_task = []
        for i, task in enumerate(self.scheduled_tasks, 1):
            script_path = ntpath.join(
                "C:\\",
                "Users",
                self.admin_account.name,
                "Scripts",
                "{}.ps1".format(task["name"]),
            )
            remote_clients_path = ntpath.join(
                "C:\\", "Users", self.admin_account.name, "RemoteClients.csv"
            )
            scheduled_task.append(
                {
                    "name": "Create scheduled task #{:02d}".format(i),
                    "win_scheduled_task": {
                        "name": task["name"],
                        "logon_type": "password",
                        "username": "{}\\{}".format(
                            self.domain_netbios_name, self.admin_account.name
                        ),
                        "password": self.admin_account.password,
                        "actions": [
                            {
                                "path": "powershell.exe",
                                "arguments": "& '{}' (Import-Csv -Path '{}')".format(
                                    script_path, remote_clients_path
                                ),
                            }
                        ],
                        "triggers": [
                            {
                                "type": "registration",
                                "repetition": {"interval": task["interval"]},
                            }
                        ],
                    },
                }
            )

        return [
            {
                "hosts": str(self.target),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "copy RemoteClients.csv",
                        "win_copy": {
                            "dest": "C:\\Users\\{}\\".format(self.admin_account.name),
                            "src": "RemoteClients.csv",
                        },
                    },
                    {
                        "name": "copy scripts",
                        "win_copy": {
                            "dest": "C:\\Users\\{}\\Scripts".format(
                                self.admin_account.name
                            ),
                            "src": "scheduled_tasks/",
                        },
                    },
                    *scheduled_task,
                ],
            }
        ]
