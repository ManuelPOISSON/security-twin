from dataclasses import dataclass, field

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
"""


@dataclass
class LdapObject:
    distinguishedName: str = field(metadata={"private": True, "store": "distinguishedName"})


@dataclass
class AdObject(LdapObject):
    objectGUID: str = field(metadata={"privacy": "guid"})


@dataclass
class AdSecurityPrincipal(AdObject):
    objectSid: str = field(metadata={"privacy": "sid"})
    sAMAccountName: str = field(
        default="", metadata={"private": True, "store": "userWorkstations", "func_store": lambda x: x.rstrip("$")}
    )


@dataclass(kw_only=True)
class AdUser(AdSecurityPrincipal):
    memberOf: list[str] = field(default_factory=lambda: [], metadata={"resolve": "distinguishedName"})
    userWorkstations: str | list[str] = field(default="", metadata={"resolve": "userWorkstations"})
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
    member: list[str] = field(default_factory=lambda: [], metadata={"resolve": "distinguishedName"})
    memberOf: list[str] = field(default_factory=lambda: [], metadata={"resolve": "distinguishedName"})
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
    name: str = field(default="")
    dNSHostName: str = field(
        default="",
        metadata={"private": True, "store": "userWorkstations", "func_store": lambda x: x.split(".")[0].lower()},
    )


@dataclass(kw_only=True)
class AdOu(AdObject):
    gPLink: str = ""
    ou: str


@dataclass(kw_only=True)
class AdData:
    domain_name: str
    ous: list[AdOu]
    users: list[AdUser]
    computers: list[AdComputer]
    gpos: list[AdGpo]
    groups: list[AdGroup]

    @classmethod
    def from_dict(cls, domain_name: str, data: dict[str, AdObject]):
        """
        Return an instance of the class from a dictionnary.
        """
        return cls(
            domain_name=domain_name,
            ous=[item for _, item in data.items() if isinstance(item, AdOu)],
            users=[item for _, item in data.items() if isinstance(item, AdUser)],
            computers=[item for _, item in data.items() if isinstance(item, AdComputer)],
            gpos=[item for _, item in data.items() if isinstance(item, AdGpo)],
            groups=[item for _, item in data.items() if isinstance(item, AdGroup)],
        )
