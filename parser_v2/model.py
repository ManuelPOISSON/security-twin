from dataclasses import dataclass, field, is_dataclass, fields
from typing import get_origin, get_args


""" 
This module contains an intermediate representation of the database's model used by the collector.
Currently it uses a series of built-in dataclasses to structure the data.
The attribute naming convention follows the Active Directory scheme to facilitate data unpacking.

In several attributes, you can see metadata in the declaration. 
They serve as "decorators" to modify certain behaviors,
regarding how these objects are exported or must undergo specific processing.

Currently, the following decorators or behaviors are implemented:
- private, bool : attribute that will not be exported.
- store, str: the class implementing this behavior will store the current object in a mapping named by the string
- resolve, str: TODO : Finish the documentation


TODO: transfer to a git submodule
"""


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
                new_value = [
                    instanciate(item_type[0], item) if isinstance(item, dict) else item
                    for item in value
                ]
        elif is_dataclass(f.type):
            if isinstance(value, dict):
                new_value = instanciate(f.type, value)
        kwargs[f.name] = new_value
    return cls(**kwargs)


@dataclass(kw_only=True)
class LdapObject:
    distinguishedName: str = field(
        default="", metadata={"private": True, "store": "distinguishedName"}
    )


@dataclass
class AdObject(LdapObject):
    objectGUID: str = field(metadata={"privacy": "guid"})


@dataclass
class AdSecurityPrincipal(AdObject):
    objectSid: str = field(metadata={"privacy": "sid"})
    sAMAccountName: str = field(
        default="",
        metadata={
            "private": True,
            "store": "userWorkstations",
            "func_store": lambda x: x.rstrip("$"),
        },
    )


@dataclass(kw_only=True)
class AdUser(AdSecurityPrincipal):
    memberOf: list[str] = field(
        default_factory=lambda: [], metadata={"resolve": "distinguishedName"}
    )
    userWorkstations: str | list[str] = field(
        default="", metadata={"resolve": "userWorkstations"}
    )
    name: str = field(
        default="",
        metadata={
            "private": True,
        },
    )

    def __post_init__(self):
        if isinstance(self.memberOf, str):
            self.memberOf = [self.memberOf]
        if isinstance(self.userWorkstations, str):
            if self.userWorkstations == "":
                self.userWorkstations = []
            elif "," in self.userWorkstations:
                self.userWorkstations = self.userWorkstations.split(",")
            else:
                self.userWorkstations = [self.userWorkstations]


@dataclass(kw_only=True)
class AdGroup(AdSecurityPrincipal):
    member: list[str] = field(
        default_factory=lambda: [], metadata={"resolve": "distinguishedName"}
    )
    memberOf: list[str] = field(
        default_factory=lambda: [], metadata={"resolve": "distinguishedName"}
    )
    name: str = field(default="", metadata={"private": True})

    def __post_init__(self):
        if isinstance(self.memberOf, str):
            self.memberOf = [self.memberOf]
        if isinstance(self.member, str):
            self.member = [self.member]


@dataclass
class AdGpo(AdObject):
    gPCFunctionalityVersion: str
    displayName: str
    flags: str
    gPCFileSysPath: str
    nTSecurityDescriptor: bytes = b""


@dataclass
class AdComputer(AdSecurityPrincipal):
    operatingSystem: str = ""
    primaryGroupID: str = ""
    operatingSystemVersion: str = ""
    name: str = field(default="", metadata={"private": True})
    dNSHostName: str = field(
        default="",
        metadata={
            "private": True,
            "store": "userWorkstations",
            "func_store": lambda x: x.split(".")[0].lower(),
        },
    )


@dataclass(kw_only=True)
class AdOu(AdObject):
    gPLink: str = ""
    ou: str


@dataclass(kw_only=True)
class AdData:
    # TODO: Change the default value
    domain_name: str
    ous: list[AdOu]
    users: list[AdUser]
    computers: list[AdComputer]
    gpos: list[AdGpo]
    groups: list[AdGroup]

    @classmethod
    def from_dict(cls, domain_name, data: dict[str, AdObject]):
        """
        Return an instance of the class from a dictionnary.
        """
        return cls(
            domain_name=domain_name,
            ous=[item for _, item in data.items() if isinstance(item, AdOu)],
            users=[item for _, item in data.items() if isinstance(item, AdUser)],
            computers=[
                item for _, item in data.items() if isinstance(item, AdComputer)
            ],
            gpos=[item for _, item in data.items() if isinstance(item, AdGpo)],
            groups=[item for _, item in data.items() if isinstance(item, AdGroup)],
        )


@dataclass
class LocalPrincipal:
    sid: str = field(
        default="",
        metadata={"privacy": "sid", "import": {"store": "sid", "resolve": "sid"}},
    )
    name: str = field(default="", metadata={"private": True})


@dataclass
class LocalUser(LocalPrincipal):
    pass


@dataclass
class LocalGroup(LocalPrincipal):
    members: list[LocalPrincipal] = field(
        default_factory=lambda: [], metadata={"import": {"resolve": "sid"}}
    )


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


@dataclass(kw_only=True)
class ModelDTO:
    """Data Transfer Object (DTO) used to encapsulate and transfer
    both Active Directory (AD) and local system data between ORM mapper

    """

    ad_data: AdData
    local_data: dict[str, LocalComputerData]
