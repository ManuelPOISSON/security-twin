from dataclasses import dataclass
from typing import Literal


@dataclass
class NetworkDTO:
    id: str
    name: str
    mode: Literal["nat", "none", "route", "open", "bridge"]
    addresses: list = None
    dhcp: bool = False
