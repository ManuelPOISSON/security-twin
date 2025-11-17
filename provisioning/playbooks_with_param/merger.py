from __future__ import annotations

import shutil
from pathlib import Path


def merge_splits(target_file: Path) -> None:
    """
    Ensure the given target file exists. If it already exists, do nothing.
    Otherwise, concatenate all split chunks (named target_file.name + "_split*")
    in alphabetical order into the target file, then delete the chunks.
    """

    target_path = Path(target_file)
    if target_path.exists():
        return

    split_chunks = sorted(target_path.parent.glob(f"{target_path.name}_split*"))
    if not split_chunks:
        raise FileNotFoundError(
            f"Cannot rebuild {target_path.name}: no split parts found in {target_path.parent}"
        )

    with target_path.open("wb") as merged:
        for chunk_path in split_chunks:
            with chunk_path.open("rb") as chunk:
                shutil.copyfileobj(chunk, merged)

    for chunk_path in split_chunks:
        chunk_path.unlink()

