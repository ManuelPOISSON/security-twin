import json
import logging
import traceback

from abc import ABC, abstractmethod
from typing import Any


logger = logging.getLogger(__name__)


class Importer(ABC):
    @abstractmethod
    def load(self, filename: str) -> Any | None: ...


class JsonImporter(Importer):
    def load(self, filename: str) -> Any | None:
        try:
            with open(filename, "r") as fd:
                obj = json.load(fd)
            return obj
        except Exception as e:
            logger.error(f"Cannot load json file {filename}, get: {e}")
            traceback.print_exc()
            return None
