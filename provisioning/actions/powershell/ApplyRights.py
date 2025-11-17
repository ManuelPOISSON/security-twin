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
import textwrap

from provisioning.actions.powershell.PowerShellScript import PowerShellScript


class ApplyRights(PowerShellScript):
    def __init__(self) -> None:
        self._script = textwrap.dedent(
            """
            #Requires -Version 4.0

            # -- Parameters --

            Param(
                [Parameter(Mandatory=$true)]
                [String]
                $DomainNetBiosName,
                [Parameter(Mandatory=$true)]
                [String]
                $SharingName,
                [Parameter(Mandatory=$true)]
                [String]
                $SharingPath,
                [Parameter(Mandatory=$true)]
                [String]
                $CsvPath
            )

            """
            + self._GLOBAL_POWERSHELL_BEHAVIOR
            + """

            $SharingPath = $SharingPath.Trim()
            $CsvPath = $CsvPath.Trim()

            # -- Functions --

            function Disable-Inheritance([String]$path) {
                $acl = Get-Acl -Path $path
                $acl.SetAccessRuleProtection($true, $true)
                (Get-Item -Path $path).SetAccessControl($acl)
            }

            function Set-Rights([String]$path, [String]$identity,
                                [System.Security.AccessControl.FileSystemRights]$rights,
                                [System.Security.AccessControl.AccessControlType]$type) {
                $acl = Get-Acl -Path $path
                $item = Get-Item -Path $path
                if ($item -is [System.IO.DirectoryInfo]) {
                    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule($identity, $rights,
                        ([System.Security.AccessControl.InheritanceFlags]::ContainerInherit -bor
                        [System.Security.AccessControl.InheritanceFlags]::ObjectInherit),
                        [System.Security.AccessControl.PropagationFlags]::None, $type)
                }
                else {
                    $rule = New-Object System.Security.AccessControl.FileSystemAccessRule($identity, $rights, $type)
                }
                $acl.AddAccessRule($rule)
                $item.SetAccessControl($acl)
            }

            function RemoveMatchingAccessRules([String]$path, [ScriptBlock]$scriptBlock) {
                $acl = Get-Acl -Path $path
                $accessRules = $acl.Access | Where-Object $scriptBlock
                $accessRules | ForEach-Object {
                    $acl.RemoveAccessRule($_) | Out-Null
                }
                (Get-Item -Path $path).SetAccessControl($acl)
            }

            function AggregateRights([String[]]$rights) {
                $accumulator = $null
                $rights.Split("|") | ForEach-Object {
                    if ($accumulator -eq $null) {
                        $accumulator = [System.Enum]::Parse([System.Security.AccessControl.FileSystemRights], $_, $true)
                    }
                    else {
                        $accumulator = $accumulator -bor
                            [System.Enum]::Parse([System.Security.AccessControl.FileSystemRights], $_, $true)
                    }
                }
                return $accumulator
            }

            # -- Main --

            Disable-Inheritance $SharingPath

            RemoveMatchingAccessRules $SharingPath {
                $_.IdentityReference -notlike "CREATEUR PROPRIETAIRE" -and
                $_.IdentityReference -notlike "*Système" -and
                $_.IdentityReference -notlike "*Administrateurs"
            }

            Set-Rights $SharingPath "$($DomainNetBiosName)\\Utilisateurs du domaine" `
                    ([System.Security.AccessControl.FileSystemRights]::Read) `
                    ([System.Security.AccessControl.AccessControlType]::Allow)

            Get-SmbShareAccess -Name $SharingName | ForEach-Object {
                Revoke-SmbShareAccess -Name $SharingName -AccountName $_.AccountName -Force | Out-Null
            }

            Grant-SmbShareAccess -Name $SharingName -AccountName "$($DomainNetBiosName)\\Utilisateurs du domaine" `
                                -AccessRight Full -Force | Out-Null

            Import-Csv -Path $CsvPath | ForEach-Object {
                $path = Join-Path -Path $SharingPath -ChildPath $_.Path
                Disable-Inheritance $path
                RemoveMatchingAccessRules $path {
                    $_.IdentityReference -notlike "CREATEUR PROPRIETAIRE" -and
                    $_.IdentityReference -notlike "*Système" -and
                    $_.IdentityReference -notlike "*Administrateurs"
                }
                $rights = AggregateRights $_.Rights
                if ($rights -eq $null) {
                    continue
                }
                $access = [System.Enum]::Parse([System.Security.AccessControl.AccessControlType], $_.Access, $true)
                Set-Rights $path $_.Identity $rights $access
            }
            """
        )

    @staticmethod
    def name() -> str:
        return f"{ApplyRights.__name__}.ps1"

    @staticmethod
    def call(
        path_script: str,
        domain_netbios_name: str,
        sharing_name: str,
        sharing_path: str,
        csv_path: str,
    ) -> str:
        return '{} "{}" "{}" "{} " "{} "'.format(
            path_script, domain_netbios_name, sharing_name, sharing_path, csv_path
        )
