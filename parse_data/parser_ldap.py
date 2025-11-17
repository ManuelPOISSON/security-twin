import json
import logging
import os
from pathlib import Path


class ParserLDAP:
    POSSIBLE_OBJECTS: set[str] = {
        "users",
        "ad_groups",
        "computers",
        "localUsers",
        "localGroups",
        "services",
        "hasRDP",
        "wmi",
        "Software",
    }

    def __init__(self, ldap_dir: Path, ad_object: str) -> None:
        if ad_object not in ParserLDAP.POSSIBLE_OBJECTS:
            raise ValueError(
                f"parsers from this class don't parse {ad_object}. Only one of the following is allowed : "
                f"{' '.join(ParserLDAP.POSSIBLE_OBJECTS)}"
            )

        file_path = (
            f"{ldap_dir}/{ParserLDAP.get_correct_file_name(ldap_dir, ad_object)}"
        )
        with open(file_path, "r") as json_file:
            logging.info(f"parsing {file_path}")
            file_content = " ".join(json_file.readlines()).encode().decode("utf-8-sig")
        self.json_data = json.loads(file_content)
        self.dir_name: str = ldap_dir.name

    @staticmethod
    def get_correct_file_name(
        path_sharphound_folder, ad_object: str
    ) -> str | FileNotFoundError:
        for file_name in os.listdir(path_sharphound_folder):
            if file_name.endswith(f"{ad_object}.json"):
                return file_name
        return FileNotFoundError(
            f"No file with its name ending with '{ad_object}.json' found in {path_sharphound_folder}"
        )
