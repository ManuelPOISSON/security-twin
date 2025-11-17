#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.data_model.Organization import Organization
from provisioning.Targets import Targets


class SyncExchangeAccounts(Action):
    def __init__(self, targets: Targets, organization: Organization) -> None:
        super().__init__(targets)
        self.organization = organization
        self._script = PowerShellScript(
            "Add-PSSnapin Microsoft.Exchange.Management.Powershell.E2010"
        )

        self._script += (
            'Get-AdUser -LDAPFilter "(&(name=*)(GivenName=*))" | ForEach-Object {'
            + " $reload = $false;"
            + " $user= $_;"
            + " $mailbox = Get-Mailbox | Where-Object { $_.Name -eq $user.SamAccountName };"
            + " if ($mailbox -eq $null) {"
            + '     Write-Output "Enabling $($user.SamAccountName) mailbox";'
            + "     Enable-Mailbox -Identity $user.SamAccountName;"
            + "     Set-CasMailbox -Identity $user.SamAccountName -PopEnabled $true -ImapEnabled $true;"
            + "     $reload = $true;"
            + " }"
            + "}"
        )

        self._script += (
            "if ($reload) {"
            + ' Write-Output "Restart mail services";'
            + " Restart-Service MSExchangePOP3; Start-Sleep 5;"
            + " Restart-Service MSExchangePOP3BE; Start-Sleep 5;"
            + " Restart-Service MSExchangeIMAP4; Start-Sleep 5;"
            + " Restart-Service MSExchangeIMAP4BE;"
            + "}"
        )

    def __str__(self) -> str:
        return f"SyncExchangeAccounts on targets '{self.targets}'"

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "become": "yes",
                "become_user": f"{self.organization.active_directory.domain_netbios_name}\\"
                + f"{self.organization.active_directory.admin_username}",
                "tasks": [
                    {
                        "name": "Syncing Exchange mailboxes",
                        "win_shell": self._script.content,
                    },
                ],
            }
        ]
