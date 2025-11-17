import csv
import uuid
from typing import List

from model import User
from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.Targets import Targets


class CreateMultipleWindowsLocalAccount(Action):
    def __init__(
        self,
        targets: Targets,
        accounts: List[User],
        admin_username: str,
    ) -> None:
        super().__init__(targets=targets)

        self.accounts = accounts
        self.admin_username = admin_username
        self.script = PowerShellScript()
        self.csv_file = f"local_users_{uuid.uuid4()}.csv"
        self.script += (
            'Import-Csv "C:\\Users\\'
            + self.admin_username
            + "\\Documents\\"
            + self.csv_file
            + '" | ForEach-Object {'
            + "$user = $_.Name; "
            + '$fullName = $_."FullName"; '
            + '$description = $_."Description"; '
            + '$password = $_."Password"; '
            + '[ADSI]$adsi = [ADSI]"WinNT://$env:COMPUTERNAME"; '
            + '$newUser = $adsi.Create("User", $user); '
            + "$newUser.FullName = $fullName; "
            + "$newUser.Description = $description; "
            + "$newUser.SetPassword($password); "
            + "$newUser.SetInfo() }"
        )

    def __str__(self) -> str:
        return "Create multiple local accounts on targets '{}'".format(self.targets)

    def generate_resources(self, path: str) -> None:
        with open(path + f"/{self.csv_file}", "w", encoding="utf-8") as csvfile:
            fieldnames = [
                "Name",
                "FullName",
                "Description",
                "Password",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for account in self.accounts:
                writer.writerow(
                    {
                        "Name": account.name,
                        "FullName": account.name,
                        "Description": "TODO description",
                        "Password": account.password,
                    }
                )

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Copy CSV",
                        "win_copy": {
                            "src": f"./{self.csv_file}",
                            "dest": "C:\\Users\\"
                            + self.admin_username
                            + "\\Documents\\"
                            + self.csv_file,
                        },
                        "retries": 2,
                    },
                    {"name": "Run script Add", "win_shell": self.script.content},
                    {
                        "name": "Remove CSV",
                        "win_file": {
                            "path": "C:\\Users\\"
                            + self.admin_username
                            + "\\Documents\\"
                            + self.csv_file,
                            "state": "absent",
                        },
                        "retries": 2,
                    },
                ],
            }
        ]
