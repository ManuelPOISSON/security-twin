import json
import os
from dataclasses import asdict, fields, is_dataclass
from typing import Any


class JsonExporter:
    def __init__(self, out_dir: str, indent: int = 2, ensure_ascii: bool = False, privacy: bool = False):
        self.out_dir = out_dir
        self.indent = indent
        self.ensure_ascii = ensure_ascii
        self.privacy = privacy

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

            return {k: self._to_serializable(v) for k, v in asdict(obj).items()}  # type: ignore
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
