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
from provisioning.data_model.Organization import Organization
from provisioning.Targets import Targets


class AddExchangeToAD(Action):
    def __init__(
        self, targets: Targets, organization: Organization, hostname: str
    ) -> None:
        super().__init__(targets=targets)
        # TODO(QA): organization.active_directory can be None
        self.ad_ip = organization.active_directory.ad_ip
        self.domain_netbios_name = organization.active_directory.domain_netbios_name
        self.account = organization.active_directory.admin_username
        self.password = organization.active_directory.admin_password
        self.hostname = hostname

        self.ou_list = organization.organizational_units.ou_list
        # TODO(QA): organization.active_directory can be None
        self.domain_name = organization.active_directory.dns_domain_name

    def __str__(self) -> str:
        return "Add Exchange to AD Server"

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        ou = random.choice(self.ou_list)
        ou_name = "ou={}, {}".format(ou.name, ou.path)
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Reboot after time set",
                        "win_reboot": {"reboot_timeout": 120},
                        "retries": 2,
                    },
                    {
                        "name": "Add DNS to client",
                        "win_dns_client": {
                            "adapter_names": "*",
                            "ipv4_addresses": self.ad_ip,
                        },
                        "retries": 2,
                    },
                    {
                        "name": "Add to AD",
                        "win_domain_membership": {
                            "dns_domain_name": self.domain_name,
                            "hostname": self.hostname,
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
                        "retries": 2,
                    },
                ],
            }
        ]
