import logging
from pathlib import Path

from model import ADUser
from parse_data.parser_ldap import ParserLDAP


class ParserLocUsers(ParserLDAP):

    default_password = "1234P@ss"

    def __init__(self, path_machine_dir: Path) -> None:
        super().__init__(path_machine_dir, "localUsers")

    def parse(self) -> dict[str, str]:
        """Returns a list of Machine, ADMachine objects.

        By default, all ADMachines are set to is_dc=False.
        """
        loc_users = {}
        # if len(self.json_data) != 1:
        #     logging.warning(
        #         f"found list of {len(self.json_data)} local users, expected 1. "
        #     )
        for val in self.json_data:
            print(val)
            loc_users[val["name"]] = ParserLocUsers.default_password
        return loc_users


if __name__ == "__main__":
    path_machine = Path(
        "/home/manuel/Documents/mantis_amossys/dataamossys/collect_companyA_250716/cleaned/CN=PC-DR74,OU=PC,OU=Amossys,DC=dr,DC=amossys,DC=fr/"
    )
    import os

    logging.getLogger().setLevel(logging.DEBUG)
    print(os.getcwd())
    p = ParserLocUsers(path_machine)
    print(p.parse())
