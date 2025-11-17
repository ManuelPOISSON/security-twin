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
from datetime import datetime
from datetime import time
from typing import List
from typing import Union

from provisioning.actions.powershell.PowerShellScript import PowerShellScript


class UpdateFileTimestamps(PowerShellScript):
    def __init__(self) -> None:
        self._script = textwrap.dedent(
            """
            #Requires -Version 4.0

            # -- Parameters --

            Param(
                [Parameter(Mandatory=$true)]
                [String[]]
                $Paths,
                [Parameter(Mandatory=$true)]
                [System.Int32]
                $StartYear,
                [Parameter(Mandatory=$true)]
                [System.Int32]
                $StartMonth,
                [Parameter(Mandatory=$true)]
                [System.Int32]
                $StartDay,
                [Parameter(Mandatory=$true)]
                [System.Int32]
                $EndYear,
                [Parameter(Mandatory=$true)]
                [System.Int32]
                $EndMonth,
                [Parameter(Mandatory=$true)]
                [System.Int32]
                $EndDay,
                [Parameter(Mandatory=$true)]
                [System.Int32]
                $OpeningHour,
                [Parameter(Mandatory=$true)]
                [System.Int32]
                $OpeningMinute,
                [Parameter(Mandatory=$true)]
                [System.Int32]
                $EndingHour,
                [Parameter(Mandatory=$true)]
                [System.Int32]
                $EndingMinute
            )

            """
            + self._GLOBAL_POWERSHELL_BEHAVIOR
            + """

            $args | ForEach-Object { [Console]::Error.WriteLine("arg: $_")}

            $Paths = $Paths | ForEach-Object { $_.Trim() }

            # -- Functions --

            function Generate-Date([DateTime]$startDate, [DateTime]$endDate) {
                $openingDate = Get-Date -Hour $OpeningHour -Minute $OpeningMinute -Second 0 -Millisecond 0
                $endingDate = Get-Date -Hour $EndingHour -Minute $EndingMinute -Second 0 -Millisecond 0

                $date = New-Object DateTime((Get-Random -Minimum $startDate.Ticks -Maximum $endDate.Ticks),
                                            ([DateTimeKind]::Local))
                $range = New-Object DateTime((Get-Random -Minimum $openingDate.Ticks -Maximum $endingDate.Ticks),
                                            ([DateTimeKind]::Local))
                return New-Object DateTime($date.Year, $date.Month, $date.Day, $range.Hour, $range.Minute, $range.Second,
                                        $range.Millisecond, ([DateTimeKind]::Local))
            }

            # -- Main --

            $utcStartDate = New-Object DateTime($StartYear, $StartMonth, $StartDay, 0, 0, 0, 0, ([DateTimeKind]::Utc))
            $utcEndDate = New-Object DateTime($EndYear, $EndMonth, $EndDay, 0, 0, 0, 0, ([DateTimeKind]::Utc))
            $startDate = $utcStartDate.ToLocalTime()
            $startDate = New-Object DateTime($startDate.Year, $startDate.Month, $startDate.Day,
                                            $OpeningHour, $OpeningMinute, 0, 0, ([DateTimeKind]::Local))
            $endDate = $utcEndDate.ToLocalTime()
            $endDate = New-Object DateTime($endDate.Year, $endDate.Month, $endDate.Day,
                                        $EndingHour, $EndingMinute, 0, 0, ([DateTimeKind]::Local))

            Get-ChildItem -Path $Paths -Recurse |
            ForEach-Object {
                $_.CreationTime = Generate-Date $startDate $endDate
                $_.LastWriteTime = Generate-Date $_.CreationTime $endDate
                $_.LastAccessTime = Generate-Date $_.LastWriteTime $endDate
            }
            """
        )

    @staticmethod
    def name() -> str:
        return f"{UpdateFileTimestamps.__name__}.ps1"

    @staticmethod
    def call(
        script_path: str,
        paths: Union[str, List[str]],
        start_date: datetime,
        end_date: datetime,
        opening_time: time,
        ending_time: time,
    ) -> str:
        if isinstance(paths, str):
            paths = [paths]
        return "{} {} {} {} {} {} {} {} {} {} {} {}".format(
            script_path,
            ", ".join(['"{} "'.format(path) for path in paths]),
            start_date.year,
            start_date.month,
            start_date.day,
            end_date.year,
            end_date.month,
            end_date.day,
            opening_time.hour,
            opening_time.minute,
            ending_time.hour,
            ending_time.minute,
        )
