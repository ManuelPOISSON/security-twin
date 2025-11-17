from pathlib import Path

from parse_data.parser_ldap import ParserLDAP
from parse_data.utils import clean_sp_name


class ParserWMI(ParserLDAP):
    def __init__(self, path_machine_dir: Path) -> None:
        super().__init__(path_machine_dir, "wmi")

    def parse(
        self,
    ) -> tuple[dict[str, list[str]], dict[str, list[str]], list[str]]:
        """Returns tuple (dict {security_principal: [permissions]}, dict {group_name: list_members}, nt_local_users)"""
        rootcimv2_rights = {}
        extra_local_group = {}
        nt_local_user = []
        for val in self.json_data:
            raw_sp_name = val["Name"]
            sp_name = clean_sp_name(raw_sp_name)
            if ("NT " in raw_sp_name or " NT" in raw_sp_name) and "\\" in raw_sp_name:
                nt_local_user.append(sp_name)

            if sp_name == "Administrators":
                extra_local_group["Administrators"] = []
                sp_name = "Administrators"
            elif sp_name == "Users":
                extra_local_group["Users"] = []
                sp_name = "Users"

            rootcimv2_rights[sp_name] = (
                val["Permission"]
                if isinstance(val["Permission"], list)
                else [val["Permission"]]
            )
        return rootcimv2_rights, extra_local_group, nt_local_user
