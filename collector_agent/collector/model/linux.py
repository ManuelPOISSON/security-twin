from dataclasses import dataclass

from collector.model.local_windows import Software


@dataclass()
class LinuxUser:
    username: str
    uid: str


@dataclass()
class LinuxData:
    machine_name: str
    softwares: list[Software]
    users: list[LinuxUser]
