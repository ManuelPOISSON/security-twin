import uuid
from typing import List
from typing import Tuple

from model import User, ADUser, ADGroup, Group
from provisioning.action import Action
from provisioning.actions.powershell.PowerShellScript import PowerShellScript
from provisioning.Targets import Targets


class AddMultipleUserToLocalGroup(Action):
    def __init__(
        self,
        targets: Targets,
        accounts_groups: List[Tuple[User | ADUser | ADGroup, Group]],
        admin_username: str,
    ) -> None:
        super().__init__(targets=targets)
        self.accounts_groups = accounts_groups
        self._SCRIPT_NAME = f"add_localgroups_{uuid.uuid4()}.ps1"
        self.admin_username = admin_username

    def __str__(self) -> str:
        return "Add security principal to local group"

    def generate_resources(self, path: str) -> None:
        script = PowerShellScript()

        for item in self.accounts_groups:
            # net localgroup Administrators john /add
            script += (
                'net localgroup "' + item[1].name + '" "' + item[0].name + '" /add; '
            )

        script.save_as(path + "/" + self._SCRIPT_NAME)

    def generate_yaml(self, gather_facts: bool = False) -> List[dict]:
        # TODO(QA): use a temporary folder to create your scritps
        script = (
            "C:\\Users\\" + self.admin_username + "\\Documents\\" + self._SCRIPT_NAME
        )
        return [
            {
                "hosts": str(self.targets),
                "gather_facts": "yes" if gather_facts else "no",
                "tasks": [
                    {
                        "name": "Copy CSV for add users to group",
                        "win_copy": {"src": f"./{self._SCRIPT_NAME}", "dest": script},
                        "retries": 2,
                    },
                    {"name": "Add users to group", "win_shell": script},
                    {
                        "name": "Delete CSV for add users to group",
                        "win_file": {"path": script, "state": "absent"},
                        "retries": 2,
                    },
                ],
            }
        ]
