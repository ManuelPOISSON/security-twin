import csv
from typing import List

from model import ADGroup
from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.Targets import Targets


class CreateMultipleWindowsLocalGroup(Action):
    def __init__(
        self,
        targets: Targets,
        groups: List[ADGroup],
        admin_username: str,
    ) -> None:
        super().__init__(targets=targets)

        self.groups = groups
        self.admin_username = admin_username
        self.script = PowerShellScript()
        self.csv_file = "local_groups.csv"
        self.script += (
            'Import-Csv "C:\\Users\\'
            + admin_username
            + "\\Documents\\"
            + self.csv_file
            + " | ForEach-Object {"
            + "New-LocalGroup -Name $_.Name "
            + '-Description $_."Description"}'
        )

    def __str__(self) -> str:
        return "Create multiple local groups on targets '{}'".format(self.targets)

    def generate_resources(self, path: str) -> None:
        with open(path + f"/{self.csv_file}", "w", encoding="utf-8") as csvfile:
            fieldnames = [
                "Name",
                "Description",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for group in self.groups:
                writer.writerow(
                    {
                        "Name": group.name,
                        "Description": group.description,
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
