import sys
from dataclasses import dataclass
from functools import wraps
from pathlib import Path
from time import perf_counter, time
from typing import Literal

from collector.logger_manager import LoggerManager


def username_to_netbios_format(domain: str, username: str) -> str:
    """
    Normalize a username by ensuring it is prefixed with the given domain and converting it to lowercase.

    :param domain: The domain name to prefix the username with.
    :type domain: str
    :param username: The original username to normalize.
    :type username: str
    :return: The normalized, lowercase username in the format 'domain\\username'.
    :rtype: str
    """
    if not username.lower().startswith(f"{domain.lower()}\\"):
        user = f"{domain}\\{username}"
    else:
        user = username
    return user.lower()


def normalize_to_upn(domain: str, username: str) -> str:
    """
    Normalize a username to UPN (User Principal Name) format: user@domain.
    If the username is already in UPN format, it is returned as-is (lowercased).

    :param domain: The domain to use in the UPN format.
    :type domain: str
    :param username: The original username (can be user, domain\\user, or user@domain).
    :type username: str
    :return: The normalized username in UPN format.
    :rtype: str
    """
    username = username.strip()

    if "@" in username and "\\" not in username:
        return username.lower()

    if "\\" in username:
        _, user = username.split("\\", 1)
    else:
        user = username
    return f"{user}@{domain.upper()}"


def extract_username(identity: str) -> str:
    """
    Extract the bare username from a NetBIOS name (DOMAIN\\username) or a UPN (username@domain).

    :param identity: The full identity (can be NetBIOS, UPN, or plain username).
    :type identity: str
    :return: The extracted username.
    :rtype: str
    """
    identity = identity.strip()

    if "\\" in identity:
        return identity.split("\\", 1)[1]
    elif "@" in identity:
        return identity.split("@", 1)[0]
    else:
        return identity


def get_ressource_path(relative_path: str):
    path = getattr(sys, "_MEIPASS", None)
    if path is None:
        return relative_path
    else:
        return path + "/" + relative_path


@dataclass(kw_only=True)
class BaseContext:
    verbose: int = 0
    log_file: str | None = None
    debug: bool = False
    output_directory: str = ""
    logger_manager: LoggerManager | None = None

    def __post_init__(self):
        if not self.output_directory.strip():
            self.output_directory = f"collector_{str(int(time()))}"
            Path(f"./{self.output_directory}").mkdir(parents=True, exist_ok=True)


@dataclass(kw_only=True)
class ADContext(BaseContext):
    username: str
    password: str
    domain: str
    dc_ip: str
    cache_directory: str = ".caches"
    ldap_auth_method: Literal["simple", "ntlm", "kerberos", "spnego"] = "simple"
    host_auth_method: str = "ntlm"
    username_netbios: str = ""
    username_upn: str = ""
    host_collection: bool = True
    user_profile: bool = False
    workers: int = 0
    filter_hosts: list[str] | None = None
    laps: bool = False
    host_collect_method: str = "psrp"
    privacy: bool = False
    laps_user: str = "Administrator"

    def __post_init__(self):
        super().__post_init__()
        self.username_netbios = username_to_netbios_format(self.domain, self.username)
        self.username_upn = normalize_to_upn(self.domain, self.username)
        self.username = extract_username(self.username)


@dataclass(kw_only=True)
class WindowsContext(BaseContext):
    option1: bool = False


@dataclass()
class LinuxContext(BaseContext):
    hostname: str = ""
    port: int = 22
    key_path: str = ""
    passphrase: str = ""
    username: str = ""
    password: str = ""


def benchmark_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = perf_counter()
        result = func(*args, **kwargs)
        time_end = perf_counter()
        time_duration = time_end - time_start
        print(f"{func.__name__}, args : {args}, kwargs: {kwargs} : Took  {time_duration:.3f} seconds")
        return result

    return wrapper
