from enum import IntFlag
from dataclasses import dataclass, field
from pathlib import PureWindowsPath


# https://learn.microsoft.com/fr-fr/windows/win32/api/wbemcli/ne-wbemcli-wbem_security_flags
# https://learn.microsoft.com/en-us/windows/win32/wmisdk/access-to-wmi-namespaces
class Wbem_Security_Flags(IntFlag):
    Enable = 0x1
    MethodExecute = 0x2
    FullWrite = 0x4
    PartialWrite = 0x8
    ProviderWrite = 0x10
    RemoteAccess = 0x20
    Subscribe = 0x40
    Publish = 0x80
    ReadSecurity = 0x20000
    WriteSecurity = 0x40000


# https://learn.microsoft.com/en-us/previous-versions/windows/desktop/secrcw32prov/win32-ace
class AceFlags(IntFlag):
    ObjectInherit = 1
    ContainerInherit = 2
    NoPropagateInherit = 4
    InheritOnly = 8
    InheritanceFlags = 15  # ObjectInherit | ContainerInherit | NoPropagateInherit | InheritOnly
    Inherited = 16
    SuccessfulAccess = 64
    FailedAccess = 128
    AuditFlags = 192  # SuccessfulAccess | FailedAccess


@dataclass
class Win32_Account:
    Caption: str 
    Description: str
    Domain: str
    InstallDate: str 
    LocalAccount: bool
    Name: str
    SID: str
    SIDType: int
    Status: str

@dataclass
class Win32_Service:
    AcceptPause: bool
    AcceptStop: bool
    Caption: str | None
    CheckPoint: int | None
    CreationClassName: str | None
    DelayedAutoStart: bool
    Description: str | None
    DesktopInteract: bool
    DisplayName: str | None
    ErrorControl: str | None
    ExitCode: int | None
    InstallDate: str | None
    Name: str | None
    PathName: str | None
    ProcessId: int | None
    ServiceSpecificExitCode: int | None
    ServiceType: str | None
    Started: bool
    StartMode: str | None
    StartName: str | None
    State: str | None
    Status: str | None
    SystemCreationClassName: str | None
    SystemName: str | None
    TagId: int | None
    WaitHint: int | None


@dataclass
class RSOP_GPO:
    id: str
    name: str = ""
    guidName: str = ""
    version: int = 0
    enabled: bool = True
    securityDescriptor: list[int] = field(default_factory=list)
    fileSystemPath: str = ""
    accessDenied: bool = False
    filterId: str = ""
    filterAllowed: bool = True
    extensionIds: list[str] = field(default_factory=list)


@dataclass
class RSOP_PolicySetting:
    id: str = None
    precedence: int = None
    name: str = ""
    GPOID: str = ""
    SOMID: str = ""
    creationTime: str = None


# https://learn.microsoft.com/en-us/previous-versions/aa375066(v=vs.85)
@dataclass
class RSOP_SecuritySettings(RSOP_PolicySetting):
    ErrorCode: int = 0
    Status: int = 0


# https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/rsop-registrypolicysetting
@dataclass
class RSOP_RegistryPolicySetting(RSOP_PolicySetting):
    command: str = ""
    deleted: str = ""
    registryKey: str = ""
    value: list[int] = field(default_factory=list)
    valueName: str = ""
    valueType: int = None


# https://learn.microsoft.com/en-us/previous-versions/aa375064(v=vs.85)
@dataclass
class RSOP_SecuritySettingNumeric(RSOP_SecuritySettings):
    KeyName: str = None
    precedence: int = None
    Setting: int = None


# https://learn.microsoft.com/en-us/previous-versions/aa375068(v=vs.85)
@dataclass
class RSOP_SecuritySettingString(RSOP_SecuritySettings):
    KeyName: str = None
    precedence: int = None
    Setting: int = None


@dataclass
class RSOP_SecuritySettingBoolean(RSOP_SecuritySettings):
    KeyName: str = ""
    Setting: str = ""


# https://learn.microsoft.com/en-us/previous-versions/aa375059(v=vs.85)
@dataclass
class RSOP_SecurityEventLogSettingNumeric(RSOP_SecuritySettings):
    KeyName: str = None
    precedence: int = None
    Setting: int = None
    Type: str = None


# https://learn.microsoft.com/en-us/previous-versions/aa375058(v=vs.85)
@dataclass
class RSOP_SecurityEventLogSettingBoolean(RSOP_SecuritySettings):
    KeyName: str = None
    precedence: int = None
    Setting: int = None
    Type: str = None


@dataclass
class RSOP_UserPrivilegeRight(RSOP_SecuritySettings):
    AccountList: list[str] = field(default_factory=list)
    precedence: int = None
    UserRight: str = None


# https://learn.microsoft.com/en-us/previous-versions/aa375076(v=vs.85)
@dataclass
class RSOP_SystemService(RSOP_SecuritySettings):
    precedence: int = None
    SDDLString: str = None
    Service: str = None
    StartupMode: int = None


# https://learn.microsoft.com/en-us/previous-versions/aa374873(v=vs.85)
@dataclass
class RSOP_AuditPolicy(RSOP_SecuritySettings):
    Category: str = None
    Failure: bool = None
    precedence: str = None
    success: bool = None


# https://learn.microsoft.com/en-us/previous-versions/aa375048(v=vs.85)
@dataclass
class RSOP_RegistryKey(RSOP_SecuritySettings):
    Mode: int = None
    Path: str = None
    precedence: int = None
    SDDLString: str = None


# https://learn.microsoft.com/en-us/previous-versions/aa375052(v=vs.85)
@dataclass
class RSOP_RegistryValue(RSOP_SecuritySettings):
    Data: str = None
    Path: str = None
    precedence: int = None
    type: int = None


# Get-CimClass -Namespace root/RSOP/computer -ClassName RSOP_File | Select-Object -ExpandProperty CimClassProperties
@dataclass
class RSOP_File(RSOP_SecuritySettings):
    Mode: int = None
    OriginalPath: str = None
    Path: str = None
    SDDLString: str = None


# Get-CimClass -Namespace root/RSOP/computer -ClassName RSOP_RestrictedGroupEx | Select-Object -ExpandProperty CimClassProperties
@dataclass
class RSOP_RestrictedGroupEx(RSOP_SecuritySettings):
    GroupName: str = None
    Members: list[str] = field(default_factory=list)
    MembersOf: list[str] = field(default_factory=list)


#  Get-CimClass -Namespace root/RSOP/computer -ClassName RSOP_RestrictedGroup | Select-Object -ExpandProperty CimClassProperties
@dataclass
class RSOP_RestrictedGroup(RSOP_SecuritySettings):
    GroupName: str = None
    Members: list[str] = field(default_factory=list)

def wmi_access_mask_to_str_list(mask: int) -> list:
    """
    Convert a WMI AccessMask int to a list of permission names.

    Args:
        mask (int): AccessMask with WMI namespace permissions.

    Returns:
        list[str]: Names of permissions set in the mask.
    """
    return [flag.name for flag in Wbem_Security_Flags if mask & flag]


def aceflags_to_list(mask: int) -> list[str]:
    return [flag.name for flag in AceFlags if mask & flag]

def get_valid_absolute_service_paths(services: list[Win32_Service]) -> list[Win32_Service]:
    """
    Extract valid absolute `.exe` paths from a list of Win32_service objects.

    For example: 
        - "C:\\Windows\\system32\\msiexec.exe \\V";
        - "C:\Windows\system32\svchost.exe -k BcastDVRUserService".
    These kinds of paths should be ignored.

    Args:
        services (list[Win32_Service]): List of services with a `PathName` attribute.

    Returns:
        list[str]: Cleaned executable paths, excluding ones with arguments or malformed suffixes.
    """
    valid_services = []
    for service in services:
        if not hasattr(service, "PathName") or service.PathName is None:
            continue
        path = service.PathName
        
        if "\"" in path:
            path = path.split("\"")[1]
        pr = PureWindowsPath(path)
        
        if pr.suffix.lower() == ".exe":
            valid_services.append(service)
    
    return valid_services