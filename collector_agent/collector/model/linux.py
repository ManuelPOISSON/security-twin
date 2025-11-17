from dataclasses import dataclass

from collector.model.local_windows import Software


@dataclass()
class LinuxData:
    machine_name: str
    softwares: list[Software]
