import os
import logging


class Parser:
    def __init__(self, file_path: str):
        self.data = []
        if not os.path.isfile(file_path):
            logging.info(f"No file at {file_path}")
            return
        try:
            with open(file_path, "r") as f:
                self.data = f.readlines()
                logging.debug(
                    "error reading with default encoding, trying to use utf-16..."
                )
        except UnicodeDecodeError:
            with open(file_path, "r", encoding="utf-16") as f:
                self.data = f.readlines()
        if not self.data:
            logging.debug(f"data is empty after reading in file {file_path}")
