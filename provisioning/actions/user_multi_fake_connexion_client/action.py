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
import random
from datetime import datetime
from typing import List

import numpy

from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.data_model.account.WindowsDomainAccount import WindowsDomainAccount
from provisioning.data_model.ActiveDirectory import ActiveDirectory
from provisioning.data_model.ou.WindowsDomainOU import WindowsDomainOU
from provisioning.Targets import Targets


class UserMultiFakeConnexionClient(Action):
    def __init__(
        self,
        targets: Targets,
        active_directory: ActiveDirectory,
        ou_list: List[WindowsDomainOU],
        accounts: List[WindowsDomainAccount],
    ) -> None:
        super().__init__(targets=targets)
        self.ad_ip = active_directory.ad_ip
        self.domain_netbios_name = active_directory.domain_netbios_name
        self.ou_list = ou_list
        self.domain_name = active_directory.domain_name
        self.accounts = accounts

    def __str__(self) -> str:
        return "Fake connection for all fake users and computers".format()

    def generate_resources(self, path: str) -> None:
        script = PowerShellScript()
        for account in self.accounts:
            nb_days = numpy.busday_count(
                account.create_date.date(), datetime.now().date()
            )

            for i in range(0, random.randint(max(nb_days - 300, 0), nb_days)):
                script += (
                    '$cred = New-Object System.Management.Automation.PSCredential("'
                    + self.domain_netbios_name
                    + "\\"
                    + account.name
                    + '", $("'
                    + account.password
                    + '" | ConvertTo-SecureString -AsPlainText -Force));'
                    + '$ErrorActionPreference = "SilentlyContinue"; Start-Process cmd /c -Credential $cred;'
                    + '$ErrorActionPreference = "Stop";'
                )
                script += (
                    '$cred = New-Object System.Management.Automation.PSCredential("'
                    + self.domain_netbios_name
                    + "\\"
                    + account.name
                    + '-pc", $("'
                    + account.machine_password
                    + '" | ConvertTo-SecureString -AsPlainText -Force));'
                    + '$ErrorActionPreference = "SilentlyContinue"; Start-Process cmd /c -Credential $cred;'
                    + '$ErrorActionPreference = "Stop";'
                )

        script.save_as(path + "/fkconnection.ps1")

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        script = "C:\\Users\\Administrateur\\Documents\\fkconnection.ps1"
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Copy fake connection script",
                        "win_copy": {"src": "./fkconnection.ps1", "dest": script},
                        "retries": 2,
                    },
                    {
                        "name": "Run script fake connection",
                        "win_shell": script,
                        # Swithcing to async mode to avoid read timeouts
                        "async": 600,
                        "poll": 5,
                    },
                    {
                        "name": "Remove fake connection script",
                        "win_file": {"path": script, "state": "absent"},
                        "retries": 2,
                    },
                ],
            }
        ]
