from dataclasses import dataclass, field, fields, is_dataclass
from typing import get_args, get_origin


def find_all_fields_by_type(obj, target_type, found=None):
    if found is None:
        found = []

    if not is_dataclass(obj):
        return found

    for f in fields(obj):
        value = getattr(obj, f.name)

        if isinstance(value, target_type):
            found.append(value)
        elif is_dataclass(value):
            find_all_fields_by_type(value, target_type, found)

    return found


def instanciate(cls, data: dict):
    kwargs = {}
    for f in fields(cls):
        if f.name not in data:
            continue
        value = data[f.name]
        field_type = get_origin(f.type)
        new_value = value
        if field_type is list:
            item_type = get_args(f.type)
            if is_dataclass(item_type[0]):
                new_value = [instanciate(item_type[0], item) if isinstance(item, dict) else item for item in value]
        elif is_dataclass(f.type):
            if isinstance(value, dict):
                new_value = instanciate(f.type, value)
        kwargs[f.name] = new_value
    return cls(**kwargs)


@dataclass
class LocalPrincipal:
    sid: str = field(default="", metadata={"privacy": "sid", "import": {"store": "sid", "resolve": "sid"}})
    name: str = field(default="", metadata={"private": True})


@dataclass
class LocalUser(LocalPrincipal):
    pass


@dataclass
class LocalGroup(LocalPrincipal):
    members: list[LocalPrincipal] = field(default_factory=lambda: [], metadata={})


@dataclass
class Trustee(LocalPrincipal):
    domain: str = ""


@dataclass
class ACE:
    access_mask: int
    trustee: Trustee
    inherited: bool
    permissions: list[str] = field(default_factory=lambda: [])


@dataclass
class SecurityDescriptor:
    owner: Trustee
    group: Trustee
    dacl: list[ACE] = field(default_factory=lambda: [])


@dataclass
class UserRights:
    local_principal: LocalPrincipal
    permissions: list[str] = field(default_factory=lambda: [])


@dataclass
class Software:
    name: str
    version: str = ""


@dataclass
class SoftwareRegistry:
    registry: str
    softwares: list[Software] = field(default_factory=list)


@dataclass
class RegistryKeyValue:
    key: str
    value: str


@dataclass
class Service:
    name: str
    path: str
    status: str
    run_by: LocalPrincipal
    security_descriptor: SecurityDescriptor


@dataclass(kw_only=True)
class LocalComputerData:
    local_users: list[LocalUser]
    local_groups: list[LocalGroup]
    fdeny_ts_connections: RegistryKeyValue
    software_registries: list[SoftwareRegistry]
    user_rights: list[UserRights]
    root_cimv2_sd: SecurityDescriptor
    services: list[Service]
