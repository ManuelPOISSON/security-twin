from pathlib import Path

from parse_data.parser_ldap import ParserLDAP


class ParserRDP(ParserLDAP):
    def __init__(self, path_machine_dir: Path) -> None:
        super().__init__(path_machine_dir, "hasRDP")

    def parse(self) -> bool:
        """
        Returns True if the machine has RDP enabled, False otherwise.
        """
        return self.json_data["fDenyTSConnections"] == 0
