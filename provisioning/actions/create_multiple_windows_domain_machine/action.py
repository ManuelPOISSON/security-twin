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
from typing import List

from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.data_model.account.WindowsDomainAccount import WindowsDomainAccount
from provisioning.data_model.ou.WindowsDomainOU import WindowsDomainOU
from provisioning.Targets import Targets


class CreateMultipleWindowsDomainMachine(Action):
    def __init__(
        self,
        targets: Targets,
        accounts: List[WindowsDomainAccount],
        ou_list: List[WindowsDomainOU],
        domain_name: str,
    ) -> None:
        super().__init__(targets=targets)
        self.accounts = accounts
        self.ou_list = ou_list
        self.domain_name = domain_name

    def __str__(self) -> str:
        return "Create fake machine on targets '{}'".format(self.targets)

    def generate_resources(self, path: str) -> None:
        script = PowerShellScript()

        for account in self.accounts:
            name = account.name.upper() + "-PC"
            dns_name = name.lower() + "." + self.domain_name
            ou = random.choice(self.ou_list)
            ou_name = "ou=" + ou.name + ", " + ou.path
            script += (
                '$pass = ConvertTo-SecureString "'
                + account.machine_password
                + '" -AsPlainText -Force;'
            )
            script += (
                'New-ADComputer -Name "'
                + name
                + '" -SamAccountName "'
                + name
                + '" -Path "'
                + ou_name
                + '" -AccountPassword $pass -KerberosEncryptionType RC4,AES128,AES256 -DisplayName "'
                + name
                + '" '
                + '-DNSHostName "'
                + dns_name
                + '" -OperatingSystem "Windows 7 Entreprise" -OperatingSystemServicePack "Service pack 1" -OperatingSystemVersion "3.1 (7601)";'
            )
            script += (
                'Set-ADComputer -Identity "'
                + name
                + '" -ServicePrincipalNames @{Add="WSMAN/'
                + name.lower()
                + '","WSMAN/'
                + dns_name
                + '","RestrictedKrbHost/'
                + dns_name
                + '","HOST/'
                + dns_name
                + '","RestrictedKrbHost/'
                + name
                + '","HOST/'
                + name
                + '"}; '
            )

        script.save_as(path + "/create_computers.ps1")

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        script = "C:\\Users\\Administrateur\\Documents\\create_computers.ps1"
        raise NotImplementedError(
            "TODO not necessarily 'Administrateur', the script path is hardcoded: "
            + script
        )
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Copy CSV for fake machine",
                        "win_copy": {"src": "./create_computers.ps1", "dest": script},
                        "retries": 2,
                    },
                    {"name": "Create fake machine", "win_shell": script},
                    {
                        "name": "Delete CSV for fake machine",
                        "win_file": {"path": script, "state": "absent"},
                        "retries": 2,
                    },
                ],
            }
        ]
