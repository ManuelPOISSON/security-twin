import logging
from pathlib import Path

from model import ADUser
from parse_data.parser_ldap import ParserLDAP


class ParserADUsers(ParserLDAP):

    default_password = "234P@ss"

    def __init__(self, path_sharphound_folder: Path) -> None:
        super().__init__(path_sharphound_folder, "users")

    def get_users(self) -> list[ADUser]:
        """Returns a list of Machine, ADMachine objects.

        By default, all ADMachines are set to is_dc=False.
        """
        users = []
        for cn, val in self.json_data.items():
            name = val["objectSid"]
            users.append(
                ADUser(
                    name=name,
                    id_domain=self.dir_name,
                    password=ParserADUsers.default_password,
                )
            )
        return users
