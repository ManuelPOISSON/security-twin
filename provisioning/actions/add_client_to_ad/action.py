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
import re
from enum import Enum
from typing import List

from model import ADMachine, ADUser, User, ADOU
from provisioning.action import Action
from provisioning.Targets import Targets


class AddClientToAD(Action):
    def __init__(
        self,
        targets: Targets,
        domain_controller: ADMachine,
        user: User,
        ip_dc: str,
        domain_admin: ADUser,
    ) -> None:
        super().__init__(targets=targets)
        # TODO(QA): organization.active_directory can be None
        # TODO need dynamic ip address
        self.ad_ip = ip_dc
        self.domain_netbios_name = domain_controller.id_domain.split(".")[0]
        self.account = domain_admin.name
        self.password = domain_admin.password
        self.user = user

        # TODO(QA): organization.organizational_units can be None
        # TODO(QA): transform 'type' to enum?
        if self.user.type == "admin":
            self.ou_list = [
                ADOU(name="test", path="test"),
                ADOU(name="test0", path="test0"),
            ]
        else:
            self.ou_list = [
                ADOU(name="test1", path="test1"),
                ADOU(name="test2", path="test2"),
            ]
        # TODO(QA): organization.active_directory can be None
        self.domain_name = domain_controller.id_domain

    def __str__(self) -> str:
        return "Add user computer {} to AD Server".format(self.user.name)

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        # ou = random.choice(self.ou_list)
        # ou_name = "ou={}, {}".format(ou.name, ou.path)
        # Les noms standard peuvent contenir des lettres (a-z, A-Z), des chiffres (0-9) et des tirets (-)
        # hostname must have at most 15 characters
        # hostname = re.sub(r"[^a-zA-Z0-9]", "-", self.user.name[:12]) + "-pc"
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
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
                            # "hostname": hostname, # not useful and lead to errors "failed to join domain: Computer 'DESKTOP-TV9P4EJ' was successfully joined to the new domain 'ad2016.local', but renaming it to 'SYSTEMpalais-pc' failed with the following error message: The directory service is busy."
                            "domain_admin_user": "{}\\{}".format(
                                self.domain_netbios_name, self.account
                            ),
                            "domain_admin_password": self.password,
                            # "domain_ou_path": ou_name,
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
