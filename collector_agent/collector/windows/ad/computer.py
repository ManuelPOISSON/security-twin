from dataclasses import dataclass

from collector.model.exporter import JsonExporter
from collector.model.local_windows import LocalComputerData
from collector.model.post_processor import LocalPostProcessor


@dataclass
class Computer:
    """
    Dataclass to represent a Computer
    """

    distinguished_name: str
    ip_addr: str
    username: str
    password: str
    hostname: str
    exporter: JsonExporter
    anonymiser: LocalPostProcessor | None
    local_data: LocalComputerData | None = None
