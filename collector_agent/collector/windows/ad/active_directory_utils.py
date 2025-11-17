import struct
from dataclasses import fields, is_dataclass
from datetime import datetime, timezone
from enum import Enum

from ldap3 import Entry

from collector.model.ad_objects import AdComputer, AdGpo, AdGroup, AdObject, AdOu, AdUser


class LDAPFilter(Enum):
    COMPUTER_OBJECT = "(objectClass=computer)"
    AD_USER_OBJECT = "(&(objectClass=User)(!(objectClass=Computer)))"
    AD_GROUPS_OBJECT = "(&(objectClass=group)(!(objectClass=Computer)))"
    GPO_OBJECT = "(objectClass=groupPolicyContainer)"
    OU_OBJECT = "(objectClass=organizationalUnit)"
    FSP_OBJECT = "(objectClass=foreignSecurityPrincipal)"

    def __str__(self) -> str:
        return self.value


def asdict_base(obj):
    """Retourne un dict avec uniquement les champs de la classe mère directe du dataclass."""
    # On prend la classe de base directe (juste avant object)
    bases = [b for b in obj.__class__.__bases__ if is_dataclass(b)]
    if not bases:
        # pas de classe mère dataclass
        return {}
    base_cls = bases[0]
    base_fields = {f.name for f in fields(base_cls)}
    return {k: getattr(obj, k) for k in base_fields}


map_model: dict[LDAPFilter, type[AdObject]] = {
    LDAPFilter.COMPUTER_OBJECT: AdComputer,
    LDAPFilter.AD_USER_OBJECT: AdUser,
    LDAPFilter.AD_GROUPS_OBJECT: AdGroup,
    LDAPFilter.GPO_OBJECT: AdGpo,
    LDAPFilter.OU_OBJECT: AdOu,
    LDAPFilter.FSP_OBJECT: AdUser,
}


class ModelAttributesFilter(Enum):
    ALL = ["*", "+"]

    COMPUTER = [
        "distinguishedName",
        "dNSHostName",
        "name",
        "primaryGroupID",
        "operatingSystem",
        "operatingSystemVersion",
        "ObjectGuid",
        "objectSID",
        "sAMAccountName",
    ]
    AD_USER = ["distinguishedName", "name", "userWorkstations", "memberOf", "objectSID", "objectGUID", "sAMAccountName"]
    AD_GROUPS = ["distinguishedName", "objectSID", "member", "memberOf", "name", "objectGUID", "sAMAccountName"]
    AD_OU = ["distinguishedName", "gPLink", "objectGUID", "ou"]
    AD_GPO = [
        "distinguishedName",
        "displayName",
        "gPCFileSysPath",
        "flags",
        "gPCFunctionalityVersion",
        "ntSecurityDescriptor",
        "objectGUID",
    ]


def sanitize_ldap_entry(entry: Entry) -> dict:
    # All ldap attributes are list, even if there is just one element
    entry_dict = {}
    for k, v in entry.entry_attributes_as_dict.items():
        if isinstance(v, list) and len(v) == 0:
            continue
        if isinstance(v, list) and len(v) == 1:
            entry_dict[k] = str(v[0])
        else:
            entry_dict[k] = v
    return entry_dict


class LAPSPasswordBlob:
    HEADER_FORMAT = "<QII"  # Timestamp (8), EncryptedPasswordSize (4), Reserved (4)
    HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
    WINDOWS_TICKS = 10_000_000
    EPOCH_DIFF = 11644473600  # seconds between 1601-01-01 and 1970-01-01

    def __init__(self, raw: bytes):
        self.raw = raw
        self._parse()

    def _parse(self):
        (self._timestamp_raw, self.encrypted_password_size, self.reserved) = struct.unpack_from(
            self.HEADER_FORMAT, self.raw, 0
        )

        self.encrypted_password = self.raw[self.HEADER_SIZE : self.HEADER_SIZE + self.encrypted_password_size]

    @property
    def password_update_timestamp(self) -> datetime:
        """Convert Windows FILETIME → Python datetime (UTC)."""
        return datetime.fromtimestamp(self._timestamp_raw / self.WINDOWS_TICKS - self.EPOCH_DIFF, tz=timezone.utc)

    def __repr__(self):
        return (
            f"<PasswordBlob(timestamp={self.password_update_timestamp}, "
            f"size={self.encrypted_password_size}, reserved={self.reserved})>"
        )
