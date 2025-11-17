#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.Targets import Targets

KEYS = [
    ("zeroconfigexchange", 1),
    ("excludelastknowngoodurl", 0),
    ("excludescplookup", 0),
    ("excludehttpsrootdomain", 0),
    ("excludehttpsautodiscoverdomain", 0),
    ("excludehttpredirect", 0),
    ("excludesrvrecord", 0),
    ("excludeexplicito365endpoint", 0),
    ("disableautodiscoverv2service", 0),
]


class OutlookAutoConfig(Action):
    def __init__(self, targets: Targets) -> None:
        super().__init__(targets)
        self._script = PowerShellScript()

        self._script += (
            '$GPOName = "outlook_autoconfig";'
            + "$TargetOU = $(Get-ADDomain -Current LocalComputer).DistinguishedName.ToLower();"
            + "$GPO = New-GPO -Name $GPOName;"
        )

        for key, value in KEYS:

            # Outlook 2016, 2019
            self._script += (
                "Set-GPPrefRegistryValue -Name $GPOName -Action Create,Update "
                + '-Context User -Key "HKCU\\Software\\Policies\\Microsoft\\Office\\16.0\\Outlook\\AutoDiscover" '
                + f'-ValueName "{key}" -Type DWord -Value {value}'
            )
            # Outlook 2013
            self._script += (
                "Set-GPPrefRegistryValue -Name $GPOName -Action Create,Update "
                + '-Context User -Key "HKCU\\Software\\Policies\\Microsoft\\Office\\15.0\\Outlook\\AutoDiscover" '
                + f'-ValueName "{key}" -Type DWord -Value {value}'
            )

        self._script += "New-GPLink -Name $GPOName -Target $TargetOU"

    def __str__(self) -> str:
        return f"OutlookAutoConfig on targets '{self.targets}'"

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Configuring Outlook auto configuration GPO",
                        "win_shell": self._script.content,
                    },
                ],
            }
        ]
