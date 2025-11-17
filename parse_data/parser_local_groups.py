import logging
from collections import defaultdict
from pathlib import Path

from model import ADUser
from parse_data.parser_ad_users import ParserADUsers
from parse_data.parser_ldap import ParserLDAP
from parse_data.translations import FR_TO_EN


class ParserLocGroups(ParserLDAP):
    IGNORED_MEMBERS = ("INTERACTIVE", "Authenticated Users")

    def __init__(self, path_machine_dir: Path, domain_name: str = None) -> None:
        super().__init__(path_machine_dir, "localGroups")
        self.domain_name = domain_name if domain_name else None

    def parse(self) -> tuple[dict[str, list[str]], list[str], list[ADUser]]:
        """Returns a tuple [local_groups, nt_users_discovered, ad_users_discovered].

        local_groups is a dictionary where keys are group names and values are lists of member names.

        nt_users_discovered is a list of local users that are NT users (i.e., their names contain "NT " or " NT") like NT AUTHORITY or NT SERVICE.

        ad_users_discovered is a list of ad users discovered (i.e., their names contain self.domain_name).
        """
        nt_users_discovered = []
        ad_users_discovered = []
        local_groups = defaultdict(list)
        short_domain_name = (
            self.domain_name.split(".")[0].upper() if self.domain_name else None
        )
        # if len(self.json_data) != 1:
        #     logging.warning(
        #         f"found list of {len(self.json_data)} local users, expected 1. "
        #     )
        for val in self.json_data:
            logging.debug(f"Parsing local group: {val} with {self.domain_name=}")
            raw_members_name = [member["Name"] for member in val.get("Members", [])]
            members_name = []
            for member in raw_members_name:
                member_split = member.split("\\")
                member_to_add = ""
                if len(member_split) > 2:
                    raise ValueError(
                        f"Unexpected format for member {member}. "
                        "Expected format is 'domain\\username' or 'username' or 'NT xx\\username'."
                    )
                elif len(member_split) == 2:
                    # This is a local user e.g. 'NT AUTHORITY' or 'AUTHORITE NT'
                    if ("NT " in member or " NT" in member) and "\\" in member:
                        # TODO sometimes "NT " is a local group e.g. AUTORITE NT\\Utilisateurs authentifiés
                        nt_users_discovered.append(member)
                    elif short_domain_name == member_split[0]:
                        # TODO member here could be an AD group.
                        #  Currently we always set it as an AD user while its false
                        logging.debug(f"found AD User {member_split}")
                        ad_users_discovered.append(
                            ADUser(
                                name=member_split[1],
                                id_domain=self.domain_name,
                                password=ParserADUsers.default_password,
                            )
                        )
                    else:
                        member_to_add = member_split[1]
                else:
                    member_to_add = member_split[0]

                member_to_add = FR_TO_EN.get(member_to_add, member_to_add)
                if member_to_add != "" and member_to_add not in self.IGNORED_MEMBERS:
                    members_name.append(member_to_add)

            local_group_name = val["Name"]
            # logging.debug(f"{local_group_name=}")
            if local_group_name in FR_TO_EN.keys():
                local_group_name = FR_TO_EN[local_group_name]
            local_groups[local_group_name] = members_name
            logging.debug(
                f"Members of local group {local_group_name}: {local_groups[local_group_name]}"
            )

        logging.debug(f"{nt_users_discovered=}")
        return local_groups, nt_users_discovered, ad_users_discovered


if __name__ == "__main__":

    def safe_parse_todell(parser_callable, *args, default=None, **kwargs):
        """Utility to call .parse() on a parser, handling FileNotFoundError."""
        try:
            return parser_callable(*args, **kwargs).parse()
        except FileNotFoundError as e:
            logging.warning(str(e))
            return default

    path_machine = Path(
        "/home/manuel/Documents/mantis_amossys/dataamossys/collect_companyA_250716/cleaned/CN=PC-DR38,OU=pc-dr,OU=PC-2025,OU=Amossys,DC=dr,DC=amossys,DC=fr"
    )
    import os

    logging.getLogger().setLevel(logging.DEBUG)
    print(os.getcwd())
    p = ParserLocGroups(path_machine)
    print(p.parse())
    # p2 = safe_parse_todell(ParserLocGroups, path_machine, domain_name="ad2016.local", default=({}, [], []))
    # print(p2)
