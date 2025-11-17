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

from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.data_model.Organization import Organization
from provisioning.Targets import Targets


class CreateADServer(Action):
    def __init__(self, targets: Targets, organization: Organization) -> None:
        super().__init__(targets=targets)
        # TODO(QA): organization.active_directory can be null assert
        self.dns_domain_name = organization.active_directory.dns_domain_name
        self.domain_netbios_name = organization.active_directory.domain_netbios_name
        self.safe_mode_password = organization.active_directory.safe_mode_password
        self.original_admin_password = (
            organization.active_directory.original_admin_password
        )
        self.admin_password = organization.active_directory.admin_password
        self.admin_username = organization.active_directory.admin_username

    def __str__(self) -> str:
        return "CreateADServer on targets '{}'".format(self.targets)

    def generate_yaml(self, gather_facts: bool = True) -> List[dict]:
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Create new Windows domain in a new forest with specific parameters",
                        "win_domain": {
                            "create_dns_delegation": "no",
                            "database_path": "C:\\Windows\\NTDS",
                            "dns_domain_name": self.dns_domain_name,
                            "domain_mode": "Win2012R2",
                            "domain_netbios_name": self.domain_netbios_name,
                            "forest_mode": "Win2012R2",
                            "safe_mode_password": self.safe_mode_password,
                            "sysvol_path": "C:\\Windows\\SYSVOL",
                        },
                    },
                    {
                        "name": "Reboot after installation",
                        "win_reboot": {"reboot_timeout": 240, "post_reboot_delay": 90},
                        "when": "ansible_facts['os_name'] == 'Microsoft Windows Server 2012 R2 Standard'",
                    },
                    {
                        "name": "Reboot after installation",
                        "win_reboot": {"reboot_timeout": 420, "post_reboot_delay": 360},
                        "when": "ansible_facts['os_name'] == 'Microsoft Windows Server 2016 Standard'",
                    },
                    {
                        "name": "Active module",
                        "win_shell": PowerShellScript(
                            "set-aduser -PasswordNeverExpires $true -Identity {}".format(
                                self.admin_username
                            )
                        ).content,
                    },
                    {
                        "name": "Edit password Administrator",
                        "win_shell": PowerShellScript(
                            (
                                "Set-ADAccountPassword -Identity {admin_username} "
                                + "-OldPassword (ConvertTo-SecureString "
                                + '-AsPlainText "{original_admin_password}" -Force) '
                                + "-NewPassword (ConvertTo-SecureString "
                                + '-AsPlainText "{admin_password}" -Force)'
                            ).format(
                                admin_username=self.admin_username,
                                original_admin_password=self.original_admin_password,
                                admin_password=self.admin_password,
                            )
                        ).content,
                    },
                ],
            }
        ]
