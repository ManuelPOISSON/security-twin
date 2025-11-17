from dataclasses import dataclass
from typing import Literal


@dataclass
class NetworkInterface:
    interface_name: str
    mac_address: str
    ipv4_address: str
    ipv4_netmask: str
    net_name: str
    gateway: str
    dhcp: bool = False


@dataclass
class HostDTO:
    id: str
    vcpu: str
    name: str
    vmem: str
    disk_size: str
    os_type: Literal["windows", "linux"]
    os: str
    version: str
    interfaces: list[NetworkInterface]

    # Workaround to works with something like "HostDTO(**host)"
    def __post_init__(self):
        self.interfaces = [NetworkInterface(**interface) for interface in self.interfaces]
