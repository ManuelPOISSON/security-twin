from dataclasses import dataclass
from pathlib import Path
import os


def resolve_env_path(env_var: str, default: str = None) -> str:
    """
    Resolve an environment variable path to an absolute path.
    If the path is relative, it's resolved relative to the pydeploy directory.
    
    :param env_var: Name of the environment variable
    :param default: Default value if env_var is not set
    :return: Absolute path
    """
    path = os.getenv(env_var, default)
    if path is None:
        return None
    
    # If already absolute, return as is
    if os.path.isabs(path):
        return path
    
    # Find pydeploy directory
    # This file is in pydeploy/digitaltwin/utils/config.py
    # So we need to go up 3 levels: utils -> digitaltwin -> pydeploy
    pydeploy_dir = Path(__file__).parent.parent.parent
    # Resolve relative to pydeploy directory
    return str((pydeploy_dir / path).resolve())


# Read-Only classe
# One attribute for the moment
@dataclass(frozen=True)
class Config:
    debug: bool = False
