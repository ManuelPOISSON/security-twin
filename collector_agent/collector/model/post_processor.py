import logging
import os
import re
import uuid
from collections.abc import Callable
from dataclasses import fields, is_dataclass

from collector.model.ad_objects import AdData, AdObject
from collector.model.local_windows import LocalComputerData

logger = logging.getLogger(__name__)


AD_WELLKNOWN_SIDS = {
    "S-1-0": ("Null Authority", "USER"),
    "S-1-0-0": ("Nobody", "USER"),
    "S-1-1": ("World Authority", "USER"),
    "S-1-1-0": ("Everyone", "GROUP"),
    "S-1-2": ("Local Authority", "USER"),
    "S-1-2-0": ("Local", "GROUP"),
    "S-1-2-1": ("Console Logon", "GROUP"),
    "S-1-3": ("Creator Authority", "USER"),
    "S-1-3-0": ("Creator Owner", "USER"),
    "S-1-3-1": ("Creator Group", "GROUP"),
    "S-1-3-2": ("Creator Owner Server", "COMPUTER"),
    "S-1-3-3": ("Creator Group Server", "COMPUTER"),
    "S-1-3-4": ("Owner Rights", "GROUP"),
    "S-1-4": ("Non-unique Authority", "USER"),
    "S-1-5": ("NT Authority", "USER"),
    "S-1-5-1": ("Dialup", "GROUP"),
    "S-1-5-2": ("Network", "GROUP"),
    "S-1-5-3": ("Batch", "GROUP"),
    "S-1-5-4": ("Interactive", "GROUP"),
    "S-1-5-6": ("Service", "GROUP"),
    "S-1-5-7": ("Anonymous", "GROUP"),
    "S-1-5-8": ("Proxy", "GROUP"),
    "S-1-5-9": ("Enterprise Domain Controllers", "GROUP"),
    "S-1-5-10": ("Principal Self", "USER"),
    "S-1-5-11": ("Authenticated Users", "GROUP"),
    "S-1-5-12": ("Restricted Code", "GROUP"),
    "S-1-5-13": ("Terminal Server Users", "GROUP"),
    "S-1-5-14": ("Remote Interactive Logon", "GROUP"),
    "S-1-5-15": ("This Organization", "GROUP"),
    "S-1-5-17": ("IUSR", "USER"),
    "S-1-5-18": ("Local System", "USER"),
    "S-1-5-19": ("NT Authority", "USER"),
    "S-1-5-20": ("Network Service", "USER"),
    "S-1-5-80-0": ("All Services ", "GROUP"),
    "S-1-5-32-544": ("Administrators", "GROUP"),
    "S-1-5-32-545": ("Users", "GROUP"),
    "S-1-5-32-546": ("Guests", "GROUP"),
    "S-1-5-32-547": ("Power Users", "GROUP"),
    "S-1-5-32-548": ("Account Operators", "GROUP"),
    "S-1-5-32-549": ("Server Operators", "GROUP"),
    "S-1-5-32-550": ("Print Operators", "GROUP"),
    "S-1-5-32-551": ("Backup Operators", "GROUP"),
    "S-1-5-32-552": ("Replicators", "GROUP"),
    "S-1-5-32-554": ("Pre-Windows 2000 Compatible Access", "GROUP"),
    "S-1-5-32-555": ("Remote Desktop Users", "GROUP"),
    "S-1-5-32-556": ("Network Configuration Operators", "GROUP"),
    "S-1-5-32-557": ("Incoming Forest Trust Builders", "GROUP"),
    "S-1-5-32-558": ("Performance Monitor Users", "GROUP"),
    "S-1-5-32-559": ("Performance Log Users", "GROUP"),
    "S-1-5-32-560": ("Windows Authorization Access Group", "GROUP"),
    "S-1-5-32-561": ("Terminal Server License Servers", "GROUP"),
    "S-1-5-32-562": ("Distributed COM Users", "GROUP"),
    "S-1-5-32-568": ("IIS_IUSRS", "GROUP"),
    "S-1-5-32-569": ("Cryptographic Operators", "GROUP"),
    "S-1-5-32-573": ("Event Log Readers", "GROUP"),
    "S-1-5-32-574": ("Certificate Service DCOM Access", "GROUP"),
    "S-1-5-32-575": ("RDS Remote Access Servers", "GROUP"),
    "S-1-5-32-576": ("RDS Endpoint Servers", "GROUP"),
    "S-1-5-32-577": ("RDS Management Servers", "GROUP"),
    "S-1-5-32-578": ("Hyper-V Administrators", "GROUP"),
    "S-1-5-32-579": ("Access Control Assistance Operators", "GROUP"),
    "S-1-5-32-580": ("Access Control Assistance Operators", "GROUP"),
    "S-1-5-32-581": ("System Managed Account Groups", "GROUP"),
    "S-1-5-32-582": ("Storage Replica Administrators", "GROUP"),
    "S-1-5-32-583": ("Device Owners", "GROUP"),
}


LOCAL_WELL_KNOWN = {
    "S-1-15-2-1": ("ALL APPLICATION PACKAGES", "GROUP"),
    "s-1-15-2-2": ("ALL RESTRICTED APPLICATION PACKAGES", "GROUP"),
    "S-1-5-32-544": ("Administrators", "GROUP"),
    "S-1-5-32-545": ("Users", "GROUP"),
    "S-1-5-32-546": ("Guests", "GROUP"),
    "S-1-5-32-547": ("Power Users", "GROUP"),
    "S-1-5-32-548": ("Account Operators", "GROUP"),
    "S-1-5-32-549": ("Server Operators", "GROUP"),
    "S-1-5-32-550": ("Print Operators", "GROUP"),
    "S-1-5-32-551": ("Backup Operators", "GROUP"),
    "S-1-5-32-552": ("Replicators", "GROUP"),
    "S-1-5-32-554": ("Pre-Windows 2000 Compatible Access", "GROUP"),
    "S-1-5-32-555": ("Remote Desktop Users", "GROUP"),
    "S-1-5-32-556": ("Network Configuration Operators", "GROUP"),
    "S-1-5-32-557": ("Incoming Forest Trust Builders", "GROUP"),
    "S-1-5-32-558": ("Performance Monitor Users", "GROUP"),
    "S-1-5-32-559": ("Performance Log Users", "GROUP"),
    "S-1-5-32-560": ("Windows Authorization Access Group", "GROUP"),
    "S-1-5-32-561": ("Terminal Server License Servers", "GROUP"),
    "S-1-5-32-562": ("Distributed COM Users", "GROUP"),
    "S-1-5-32-568": ("IIS_IUSRS", "GROUP"),
    "S-1-5-32-569": ("Cryptographic Operators", "GROUP"),
    "S-1-5-32-573": ("Event Log Readers", "GROUP"),
    "S-1-5-32-574": ("Certificate Service DCOM Access", "GROUP"),
    "S-1-5-32-575": ("RDS Remote Access Servers", "GROUP"),
    "S-1-5-32-576": ("RDS Endpoint Servers", "GROUP"),
    "S-1-5-32-577": ("RDS Management Servers", "GROUP"),
    "S-1-5-32-578": ("Hyper-V Administrators", "GROUP"),
    "S-1-5-32-579": ("Access Control Assistance Operators", "GROUP"),
    "S-1-5-32-580": ("Access Control Assistance Operators", "GROUP"),
    "S-1-5-32-581": ("System Managed Account Groups", "GROUP"),
    "S-1-5-32-582": ("Storage Replica Administrators", "GROUP"),
    "S-1-5-32-583": ("Device Owners", "GROUP"),
}


def unique_guid_generator(existing_guids):
    existing_set = {uuid.UUID(str(g)) for g in existing_guids}
    while True:
        g = uuid.uuid4()
        if g not in existing_set:
            existing_set.add(g)
            yield g


def generate_computer_name():
    i = 0
    while True:
        yield f"ws-{i}"
        i += 1


def to_netbios_name(name: str) -> str:
    """
    Convert a computer name into NetBIOS format (15-char uppercase).
    """
    # Take only the hostname part (strip domain if present)
    short_name = name.split(".")[0]

    # Uppercase
    short_name = short_name.upper()

    # Truncate or pad with spaces to 15 chars
    netbios_name = short_name[:15].ljust(15)

    return netbios_name


def generate_user_name():
    i = 0
    while True:
        yield f"user-{i}"
        i += 1


def generate_group_name():
    i = 0
    while True:
        yield f"group-{i}"
        i += 1


class SID:
    def __init__(self, sid: str):
        self.sid_str = sid
        try:
            parts = sid.split("-")
            if parts[0].upper() == "S":
                parts.pop(0)

            self.revision_level = parts.pop(0)
            self.authority = parts.pop(0)
            self.rid = parts.pop(-1)

            self.sub_authority = parts.pop(0)
        except IndexError:
            pass
        self.others = parts

    def __str__(self):
        return self.sid_str

    def __repr__(self):
        return f"<SID {self.sid_str}>"

    def is_well_known(self):
        return self.sid_str in AD_WELLKNOWN_SIDS.keys()

    def as_dict(self):
        return {
            "revision": self.revision_level,
            "authority": self.authority,
            "sub_authority": self.sub_authority,
            "others": self.others,
            "rid": self.rid,
        }


class SidGenerator:
    def __init__(self):
        self.domain_sid = self._generate_domain_sid()
        self.used_rids: set[int] = set()

        self.new_domain_part = []
        # Generates a domain id
        for _ in range(3):
            self.new_domain_part.append(str(int.from_bytes(os.urandom(32))))

    def _generate_domain_sid(self) -> str:
        parts = ["S", "1", "5", "21"]
        for _ in range(3):
            number = int.from_bytes(os.urandom(4), "big")
            parts.append(str(number))
        return "-".join(parts)

    def generate_rid(self) -> int:
        while True:
            rid = int.from_bytes(os.urandom(4), "big")
            if rid not in self.used_rids:
                self.used_rids.add(rid)
                return rid

    def generate_sid(self, original_sid: str) -> str:
        sid_obj = SID(original_sid)

        if sid_obj and sid_obj.is_well_known():
            return original_sid
        try:
            if int(sid_obj.rid) > 999:
                new_rid = self.generate_rid()
            else:
                new_rid = sid_obj.rid
        except AttributeError:
            logger.warning(f"Cannot Generate new SID for {original_sid}")
            return original_sid
        parts = (
            ["S", sid_obj.revision_level, sid_obj.authority, sid_obj.sub_authority]
            + self.new_domain_part
            + [str(new_rid)]
        )
        return "-".join(parts)


def flatten_dict(d, parent_key="", sep="."):
    """
    TODO : Rewrite this shitty function
    """
    items = {}
    for k, v in d.items():
        new_key = f"{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items


def fqdn_to_netbios(fqdn: str, replace_char: str = "-") -> str:
    if not fqdn or not fqdn.strip():
        return ""

    hostname = fqdn.split(".", 1)[0].strip()

    cleaned = re.sub(r"[^A-Za-z0-9-]", replace_char, hostname)

    cleaned = re.sub(r"-{2,}", "-", cleaned)

    netbios = cleaned[:15]
    return netbios.upper()


def get_new_guid() -> str:
    return "{" + str(uuid.uuid4()) + "}"


class AdDomainPostProcessor:
    def __init__(self, data: AdData):
        self.data = data
        self.sid_generator = SidGenerator()
        self.mapping: dict[str, dict[str, str]] = {}

    def process(self) -> AdData:
        for field in fields(self.data):
            obj_lists = getattr(self.data, field.name)
            if not isinstance(obj_lists, list):
                logger.error("Not implemented")
                continue
            for obj in obj_lists:
                self.__pseudonymise(obj)

        for field in fields(self.data):
            obj_lists = getattr(self.data, field.name)
            if not isinstance(obj_lists, list):
                logger.error("Not implemented")
                continue
            for obj in obj_lists:
                self.__resolve(obj)

        return self.data

    def generate_name(self, cls, sid: str | None = None):
        if not hasattr(cls, "_counter"):
            cls._counter = 0
        if sid is not None:
            name = AD_WELLKNOWN_SIDS.get(sid)
            if name:
                return name[0]
            name = LOCAL_WELL_KNOWN.get(sid)
            if name:
                return name[0]

        cls._counter += 1
        return f"{cls.__name__.lower()}{cls._counter}"

    def __resolve(self, obj: AdObject) -> None:
        if not is_dataclass(obj):
            logger.error(f"{obj.__repr__} is not a dataclass")
            return None

        for field in fields(obj):
            resolve = field.metadata.get("resolve")
            if resolve is None:
                continue
            attr = getattr(obj, field.name)
            if isinstance(attr, list):
                new_list = []
                for item in attr:
                    mapping = self.mapping.get(resolve)
                    if mapping is None:
                        # TODO : Improve error msg
                        logger.error("Cannot find the mapping to resolve blalbla ")
                        continue
                    resolved_obj = mapping.get(item)
                    if resolved_obj is None:
                        logger.error(f"Cannot resolve {item} ")
                        new_list.append(item)
                        continue
                    new_list.append(resolved_obj.objectGUID)
                setattr(obj, field.name, new_list)

    def __pseudonymise(self, obj: object) -> None:
        if not is_dataclass(obj):
            logger.error(f"{obj.__repr__} is not a dataclass")
            return
        for field in fields(obj):
            store_attr = field.metadata.get("store")
            func = field.metadata.get("func_store")
            if store_attr is not None:
                storage = self.mapping.get(store_attr)
                if storage is None:
                    storage = {}
                    self.mapping[store_attr] = storage
                name = getattr(obj, field.name)
                if func is not None:
                    name = func(name)
                storage[name] = obj  # type: ignore

            # If a field have the privacy metadata
            # We need to change it by the result of the associated function
            anon_attr = field.metadata.get("privacy")
            if anon_attr is None:
                continue
            if self.mapping.get(anon_attr) is None:
                self.mapping[anon_attr] = {}

            old_value = getattr(obj, field.name)
            match anon_attr:
                case "guid":
                    new_value = get_new_guid()
                case "sid":
                    new_value = self.sid_generator.generate_sid(old_value)
                case _:
                    logger.warning("Unknown anon_attr")
                    new_value = old_value

            self.mapping[anon_attr][old_value] = new_value
            setattr(obj, field.name, new_value)


def generator_local_username(name: str):
    i = 0
    while True:
        yield f"{name}-localuser-{i}"


def generator_local_group(name: str):
    i = 0
    while True:
        yield f"{name}-localuser-{i}"


class LocalPostProcessor:
    def __init__(self, mapping_sid_domain: dict[str, str], local_data: LocalComputerData | None = None):
        self.mapping = {}
        self.mapping["sid"] = mapping_sid_domain
        self.sid_generator = SidGenerator()
        self.local_data = local_data

    def __pseudonymise(self, obj: object) -> None:
        if not is_dataclass(obj):
            logger.error(f"{obj.__repr__} is not a dataclass")
            return

        for field in fields(obj):
            store_attr = field.metadata.get("store")
            func = field.metadata.get("func_store")
            if store_attr is not None:
                storage = self.mapping.get(store_attr)
                if storage is None:
                    storage = {}
                    self.mapping[store_attr] = storage
                name = getattr(obj, field.name)
                if func is not None:
                    name = func(name)
                storage[name] = obj  # type: ignore

            # If a field have the privacy metadata
            # We need to change it by the result of the associated function
            anon_attr = field.metadata.get("privacy")
            if anon_attr is None:
                continue
            if self.mapping.get(anon_attr) is None:
                self.mapping[anon_attr] = {}

            old_value = getattr(obj, field.name)
            new_value = self.mapping[anon_attr].get(old_value)
            if new_value is None:
                match anon_attr:
                    case "guid":
                        new_value = get_new_guid()
                    case "sid":
                        new_value = self.sid_generator.generate_sid(old_value)
                    case _:
                        logger.warning("Unknown anon_attr")
                        new_value = old_value
                self.mapping[anon_attr][old_value] = new_value
            else:
                # We are in the case where the SID is part of a domain
                # the mapping dict will be map["sid"][sid domain] = anon_sid_domain
                # We must update the mapping as well since we don't want generate a new sid for
                self.mapping[anon_attr][new_value] = new_value
            setattr(obj, field.name, new_value)

    def __walk_dataclass(self, obj: object, callable: Callable):
        if not is_dataclass(obj):
            return

        for field in fields(obj):
            attr = getattr(obj, field.name)
            if is_dataclass(attr):
                self.__walk_dataclass(attr, callable)
            elif isinstance(attr, list):
                for item in attr:
                    if is_dataclass(item):
                        self.__walk_dataclass(item, callable)
            callable(obj)

    def process(self):
        self.__walk_dataclass(self.local_data, self.__pseudonymise)
        return self.local_data
