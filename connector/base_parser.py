from abc import ABC, abstractmethod
from dataclasses import is_dataclass, fields, Field, asdict
import logging
import os
import traceback
import json
from pathlib import Path
from typing import Any, Callable
from connector.importer import Importer, JsonImporter
from connector.model import (
    AdData,
    instanciate,
    LocalComputerData,
    AdObject,
    AdSecurityPrincipal,
    LocalPrincipal,
    LinuxData,
)
from connector.utils import WELLKNOWN_RIDS, WELLKNOWN_SIDS


logger = logging.getLogger(__name__)


class BaseParser(ABC):
    """
    Abstract class that defines interface and attributes

    """

    def __init__(self, filename: Path, importer="json"):
        match importer:
            case "json":
                self.importer: Importer = JsonImporter()
                self.data = self.importer.load(filename)

    @property
    def filename(self):
        pass

    @abstractmethod
    def get_data(self) -> Any: ...


class JsonExporter:
    def __init__(
        self,
        out_dir: str,
        indent: int = 2,
        ensure_ascii: bool = False,
        privacy: bool = False,
    ):
        self.out_dir = out_dir
        self.indent = indent
        self.ensure_ascii = ensure_ascii
        self.privacy = privacy

        # Création du répertoire si inexistant
        os.makedirs(self.out_dir, exist_ok=True)

    def _to_serializable(self, obj: Any):
        if is_dataclass(obj):
            if self.privacy:
                result = {}
                for f in fields(obj):
                    if self.privacy and f.metadata.get("private", False):
                        continue
                    value = getattr(obj, f.name)
                    result[f.name] = self._to_serializable(value)
                return result

            return {k: self._to_serializable(v) for k, v in asdict(obj).items()}
        elif isinstance(obj, dict):
            return {k: self._to_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [self._to_serializable(v) for v in obj]
        else:
            return obj

    def export(self, data: Any, filename: str) -> str:
        filepath = os.path.join(self.out_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(
                self._to_serializable(data),
                f,
                indent=self.indent,
                ensure_ascii=self.ensure_ascii,
            )
        return filepath


class ParserAdData(BaseParser):
    filename = "all.json"

    def __init__(self, dir: Path, importer: str = "json") -> None:
        super().__init__(dir / self.__class__.filename, importer)
        self.map_ref: dict[str, dict[str, Any]] = {}
        self.map_ref["guid"] = {}
        self.map_ref["sid"] = {}

    def __generate_name(self, obj: object, field: Field):
        if not isinstance(obj, AdObject):
            logger.warning(
                f"Trying to generate a name for a non-LdapObject instance, instance type : {type(obj)}"
            )
            return

        if field.name != "name":
            return

        # Is it a deja-vu object with a already name attribute ?
        deja_vu = self.map_ref["guid"].get(obj.objectGUID)
        if deja_vu and hasattr(deja_vu, "name") and deja_vu.name != "":
            obj = deja_vu
            return

        cls = obj.__class__
        if not hasattr(cls, "_counter"):
            cls._counter = 0

        if not hasattr(obj, "objectSid"):
            setattr(obj, field.name, f"{cls.__name__}-{cls._counter}")
            cls._counter += 1
            return

        sid: str = getattr(obj, "objectSid")
        rid = sid.split("-")[-1]

        well_known = WELLKNOWN_RIDS.get(rid)
        if well_known:
            setattr(obj, field.name, well_known[0])
            return
        well_known = WELLKNOWN_SIDS.get(sid)
        if well_known:
            setattr(obj, field.name, well_known[0])
            return

        setattr(obj, field.name, f"{cls.__name__}-{cls._counter}")
        cls._counter += 1
        return

    def __store(self, obj: object, field: Field) -> None:
        store = field.metadata.get("store")
        if not store:
            return
        mapping = self.map_ref.get(store)
        if mapping is None:
            self.map_ref[store] = {}
        value = getattr(obj, field.name)
        if value is None:
            logger.warning(f"Cannot store object '{obj}', '{field.name}' is None ")
            return
        if not self.map_ref[store].get(value):
            self.map_ref[store][value] = obj

    def __resolve2(self, obj: object, value) -> None:
        # TODO: improve this workaround
        resolved_obj: object = self.map_ref["guid"].get(value)
        if not resolved_obj:
            # We try with the mapping distinguished name
            resolved_obj: object = self.map_ref["distinguishedName"].get(value)
            if resolved_obj is None:
                logger.warning(f"Cannot resolve due to unknown dn {value}")
                return "unknown ref"

        # Actually it seems that the database models links with
        # name
        if hasattr(resolved_obj, "name"):
            name = getattr(resolved_obj, "name")
            return name
        else:
            logger.warning("Trying to resolve reference without a name")
            return "error"

    def __walk_dataclass_apply(self, obj: object, apply: Callable):
        for field in fields(obj):
            new_obj = apply(obj, field)

            attr = getattr(obj, field.name)
            if is_dataclass(attr):
                self.__walk_dataclass_apply(attr, apply)
            elif isinstance(attr, list):
                for item in attr:
                    if is_dataclass(item):
                        self.__walk_dataclass_apply(item, apply)
        obj = new_obj

    def __walk_dataclass(self, obj: object):
        if not is_dataclass(obj):
            return

        for field in fields(obj):
            # We want to keep a mapping objectGUID: object
            # As we further try to resolve references
            if field.name == "objectGUID":
                guid = getattr(obj, field.name)
                # We store the object reference
                self.map_ref["guid"][guid] = obj

            attr = getattr(obj, field.name)
            if is_dataclass(attr):
                self.__walk_dataclass(attr)
            elif isinstance(attr, list):
                for item in attr:
                    if is_dataclass(item):
                        self.__walk_dataclass(item)

            self.__generate_name(obj, field)

    def __resolve(self, resolved_obj: object, guid: str):
        resolved_obj: object = self.map_ref["guid"].get(guid)
        if not resolved_obj:
            logger.warning(f"Cannot resolve due to unknown guid {guid}")
            return "unknown ref"
        # Actually it seems that the database models links with
        # name
        if hasattr(resolved_obj, "name"):
            name = getattr(resolved_obj, "name")
            return name
        else:
            logger.warning("Trying to resolve reference without a name")
            return "error"

    def __walk_dataclass_resolve(self, obj: object):
        if not is_dataclass(obj):
            return

        for field in fields(obj):
            attr = getattr(obj, field.name)
            if is_dataclass(attr):
                self.__walk_dataclass_resolve(attr)
            elif isinstance(attr, list):
                for item in attr:
                    if is_dataclass(item):
                        self.__walk_dataclass_resolve(item)

            if field.metadata:
                must_resolve = field.metadata.get("resolve")
                if not must_resolve:
                    continue
                attr_to_resolve = getattr(obj, field.name)
                if isinstance(attr_to_resolve, list):
                    new_value = []
                    for guid in attr_to_resolve:
                        new_value.append(self.__resolve2(obj, guid))
                elif isinstance(attr_to_resolve, str):
                    new_value = self.__resolve2(obj, attr_to_resolve)
                else:
                    logger.warning(
                        f"Trying to resolve unknown datatype: {type(attr_to_resolve)} : {attr_to_resolve}"
                    )
                    continue
                setattr(obj, field.name, new_value)

    def get_data(self) -> AdData | None:
        result: AdData | None = None
        try:
            result = instanciate(AdData, self.data)

            self.__walk_dataclass(result)
            self.__walk_dataclass_apply(result, self.__store)

            self.__walk_dataclass_resolve(result)
            return result

        except Exception as e:
            traceback.print_exception(e)
            return None

    def get_sid_mapping(self):
        return {
            sp.objectSid: sp
            for _, sp in self.map_ref["guid"].items()
            if isinstance(sp, AdSecurityPrincipal)
        }


class ParserComputerData(BaseParser):
    filename = "all.json"

    def __init__(
        self,
        dir: Path,
        mapping_domain_sid: dict[str, AdSecurityPrincipal] = None,
        importer="json",
    ):
        super().__init__(dir / self.filename, importer)
        self.map_ref = {}
        self.map_ref["sid"] = {}
        self.map_ref["domain_sid"] = {}
        if mapping_domain_sid is not None:
            self.map_ref["domain_sid"].update(mapping_domain_sid)

    def __store(self, obj: object, field: Field):
        map_name = field.metadata.get("import", {}).get("store")
        if not map_name:
            return
        mapper = self.map_ref.get(map_name)
        if not mapper:
            self.map_ref[map_name] = {}
        attr = getattr(obj, field.name)

        if not self.map_ref[map_name].get(attr):
            self.map_ref[map_name][attr] = obj

    def __resolve(self, obj: object, field: Field):
        map_name = field.metadata.get("import", {}).get("resolve")
        if not map_name:
            return

        mapper = self.map_ref.get(map_name)
        if not mapper:
            logger.warning(
                f"Trying to resolve {field.name} for instance of class {type(obj)} but no map exist {map_name}"
            )
            return

        attr = getattr(obj, field.name)
        swap = self.map_ref[map_name].get(attr)
        if not swap:
            logger.warning(
                f"Trying to resolve {field.name} for instance of class {type(obj)} but target exist"
            )
            return
        return swap

    def __walk_dataclass(self, obj: object, apply: Callable):
        for field in fields(obj):
            new_obj = apply(obj, field)

            attr = getattr(obj, field.name)
            if is_dataclass(attr):
                self.__walk_dataclass(attr, apply)
            elif isinstance(attr, list):
                for item in attr:
                    if is_dataclass(item):
                        self.__walk_dataclass(item, apply)
        obj = new_obj

    def __resolve_object(self, obj: object):
        if not is_dataclass(obj):
            return obj

        for f in fields(obj):
            attr = getattr(obj, f.name)
            if is_dataclass(attr):
                resolved = self.__resolve_object(attr)
                setattr(obj, f.name, resolved)
            elif isinstance(attr, list):
                resolved_list = []
                for item in attr:
                    if is_dataclass(item):
                        resolved_item = self.__resolve_object(item)
                        resolved_list.append(resolved_item)
                    else:
                        resolved_list.append(item)
                setattr(obj, f.name, resolved_list)
        for f in fields(obj):
            meta = f.metadata.get("import", {})
            map_name = meta.get("resolve")
            if map_name:
                key = getattr(obj, f.name)
                mapper = self.map_ref.get(map_name)
                if mapper and key in mapper:
                    return mapper[key]

        return obj

    def generate_names(self, map: dict[str, LocalPrincipal | AdSecurityPrincipal]):
        if not map:
            return
        for sid, lp in map.items():
            if not hasattr(lp, "name"):
                logger.warning(
                    f"Trying to generate a name, but current object has no attribute called name, type : {type(lp)} "
                )
                continue

            cls = lp.__class__
            if not hasattr(cls, "_counter"):
                cls._counter = 0

            new_name = ""
            well_known = WELLKNOWN_SIDS.get(sid)
            if well_known:
                new_name = well_known[0]
            rid = sid.split("-")[-1]
            well_known = WELLKNOWN_RIDS.get(rid)
            if well_known:
                new_name = well_known[0]

            domain_sp = self.map_ref["domain_sid"].get(sid)
            if domain_sp:
                new_name = domain_sp.name

            if new_name:
                setattr(lp, "name", new_name)
                continue

            name = getattr(lp, "name")
            if name:
                continue

            if not new_name:
                new_name = f"{cls.__name__}-{cls._counter}"
                cls._counter += 1

            setattr(lp, "name", new_name)

    def get_data(self) -> LocalComputerData | None:
        if self.data is None:
            return None
        result = instanciate(LocalComputerData, self.data)
        self.__walk_dataclass(result, self.__store)

        result = self.__resolve_object(result)
        self.generate_names(self.map_ref["sid"])
        return result


class ParserLinux(BaseParser):
    filename = "all.json"

    def __init__(
        self,
        dir: Path,
        importer="json",
    ):
        super().__init__(dir / self.filename, importer)

    def get_data(self) -> LinuxData | None:
        try:
            result = instanciate(LinuxData, self.data)
        except ValueError as e:
            logger.error(e)
            return None
        return result
