import io
import re

import pycdlib


def size_to_bytes(size_str):
    units = {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3, "TB": 1024**4, "PB": 1024**5}

    match = re.match(r"(\d+(?:\.\d+)?)\s*([KMGTPE]?B)", size_str.upper().strip())

    if not match:
        raise ValueError("Invalid size format. Expected format: <number><unit> (e.g., '10GB')")

    size, unit = match.groups()
    return int(float(size) * units[unit])


class ISO:
    def __init__(self, iso_path: str):
        """
        Initializes the ISO editor.

        :param iso_path: Path to the existing ISO file.
        """
        self.iso_path = iso_path
        self.iso = pycdlib.PyCdlib()
        self.iso.new(interchange_level=2)

    def add_file(self, file_path: str, iso_file_name: str):
        """
        Adds a file to the ISO without erasing existing content.

        :param file_path: Path to the file to be added.
        :param iso_file_name: Name under which the file will be stored in the ISO.
        """

        self.iso.add_file(file_path, f"/{iso_file_name.upper()};1")

    def add_string(self, content: str, iso_file_name: str):
        """
        Adds a string as a file to the ISO.

        :param content: String content to be saved as a file.
        :param iso_file_name: Name under which the content will be stored.
        """
        file_obj = io.BytesIO(content.encode("utf-8"))
        self.iso.add_fp(file_obj, len(content), f"/{iso_file_name.upper()};1")

    def write(self):
        """
        Saves the modified ISO to a new file.

        :param output_iso: Path to the output ISO file.
        """
        self.iso.write(self.iso_path)
        self.iso.close()
