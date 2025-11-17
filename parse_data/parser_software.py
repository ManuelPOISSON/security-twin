import logging
from pathlib import Path

from model import ServiceStatus
from parse_data.parser_ldap import ParserLDAP


class ParserSoftware(ParserLDAP):

    DEFAULT_RUN_BY = "NT AUTHORITY\\SYSTEM"
    DEFAULT_STATUS = ServiceStatus.running

    def __init__(self, path_machine_dir: Path) -> None:
        super().__init__(path_machine_dir, "Software")

    def parse(self) -> list[dict[str, str]]:
        """
        Returns a list of software with their attributes, dict of file paths and rights per service).

        """
        softwares: list[dict[str, str]] = []
        if "installed_packages" not in self.json_data.keys():
            logging.warning(
                f"No 'installed_packages' found in {self.dir_name}. "
                f"Skipping software parsing."
            )
            return softwares

        if "installed_packages" not in self.json_data.keys():
            logging.warning(
                f"No 'installed_packages' found in {self.dir_name}. "
                f"Skipping software parsing."
            )
            # logging.debug(f"{self.json_data}")
            return softwares
        for soft in self.json_data["installed_packages"]:
            # if not soft.get("Status") == "Installed":
            #     continue
            softwares.append(
                {
                    "name": soft.get("Name", "Unknown"),
                    "version": soft.get("Version", "Unknown"),
                }
            )
        return softwares


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    path_machine = Path("CN=DESKTOP-BLLSMPA,CN=Computers,DC=surpriz,DC=local")
    parser = ParserSoftware(path_machine)
    software_list = parser.parse()
    logging.info(f"Parsed software: {software_list}")
