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


class PowerShellScript:
    """
    Simple PowerShell script wrapper to ensure global behaviour (exit on command failure)
    """

    _GLOBAL_POWERSHELL_BEHAVIOR = '$ErrorActionPreference = "Continue";'

    def __init__(self, command: str = "") -> None:
        self._script = self._GLOBAL_POWERSHELL_BEHAVIOR
        self.append(command)

    def __str__(self) -> str:
        return f"PowerShellScript <{self._script}>"

    def __iadd__(self, command: str) -> "PowerShellScript":
        """
        Append a single command to the script content.
        """
        self._script += command
        if len(self._script) > 0 and self._script[-1] != ";":
            self._script += ";"
        return self

    def append(self, command: str) -> "PowerShellScript":
        """
        Append a command to the script (identic to __iadd__).
        """
        self.__iadd__(command)
        return self

    def save_as(self, filepath: str) -> None:
        """
        Save script in the specified filepath.
        """
        with open(filepath, "w", encoding="cp1252") as file:
            file.write(self.content)

    def _get_script(self) -> str:
        return self._script

    content = property(_get_script)
