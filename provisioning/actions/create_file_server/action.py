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
from provisioning.data_model.ActiveDirectory import ActiveDirectory
from provisioning.data_model.ou.WindowsDomainOU import WindowsDomainOU
from provisioning.Targets import Targets


class CreateFileServer(Action):
    def __init__(
        self,
        targets: Targets,
        active_directory: ActiveDirectory,
        ou_list: List[WindowsDomainOU],
        share_name: str,
    ) -> None:
        super().__init__(targets=targets)
        self.ad_ip = active_directory.ad_ip
        self.domain_netbios_name = active_directory.domain_netbios_name
        self.account = active_directory.admin_username
        self.password = active_directory.admin_password
        self.ou_list = ou_list
        self.domain_name = active_directory.dns_domain_name
        self.share_name = share_name

    def __str__(self) -> str:
        return "CreateFileServer on targets '{}'".format(self.targets)

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        targets_str = ",".join([target.name for target in self.targets.targets_list])
        ou = random.choice(self.ou_list)
        ou_name = "ou={}, {}".format(ou.name, ou.path)
        return [
            {
                "hosts": targets_str,
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Reboot after time set",
                        "win_reboot": {"reboot_timeout": 120},
                    },
                    {
                        "name": "Add DNS to client",
                        "win_dns_client": {
                            "adapter_names": "*",
                            "ipv4_addresses": self.ad_ip,
                        },
                    },
                    {
                        "name": "Add to AD",
                        "win_domain_membership": {
                            "dns_domain_name": self.domain_name,
                            "hostname": self.share_name,
                            "domain_admin_user": "{}\\{}".format(
                                self.domain_netbios_name, self.account
                            ),
                            "domain_admin_password": self.password,
                            "domain_ou_path": ou_name,
                            "state": "domain",
                        },
                        "register": "domain_state",
                    },
                    {
                        "name": "Reboot after installation",
                        "win_reboot": {"reboot_timeout": 120},
                    },
                    {
                        "name": "Activate SMB share",
                        "win_shell": PowerShellScript(
                            "Install-WindowsFeature File-Services"
                        ).content,
                    },
                    {
                        "name": "Create share directory",
                        "win_shell": PowerShellScript(
                            (
                                "New-Item -Path E:\\Shares\\{share_name} "
                                + "-Type Directory -Force"
                            ).format(share_name=self.share_name)
                        ).content,
                    },
                    {
                        "name": "Create share",
                        "win_shell": PowerShellScript(
                            (
                                "New-SmbShare -Path E:\\Shares\\{share_name} "
                                + "-Name {share_name} -FolderEnumerationMode AccessBased"
                            ).format(share_name=self.share_name)
                        ).content,
                    },
                ],
            }
        ]
