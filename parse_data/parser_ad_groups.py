from pathlib import Path

from parse_data.parser_ldap import ParserLDAP


class ParserADGroups(ParserLDAP):

    def __init__(self, path_ad_dir: Path) -> None:
        super().__init__(path_ad_dir, "ad_groups")

    def get_ad_groups_and_members(self) -> dict[str, list[str]]:
        groups = {}
        for cn, val in self.json_data.items():
            name = val["objectSid"]
            members = val.get("member", [])
            if isinstance(members, str):
                members = [members]
            groups[name] = members
        return groups
