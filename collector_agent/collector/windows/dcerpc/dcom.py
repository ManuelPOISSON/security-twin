import logging
import re
from dataclasses import fields, is_dataclass
from typing import Literal

from impacket.dcerpc.v5.dcom.wmi import (
    CLSID_WbemLevel1Login,
    DCERPCException,
    DCERPCSessionError,
    IID_IWbemLevel1Login,
    IWbemClassObject,
    IWbemLevel1Login,
    IWbemServices,
)
from impacket.dcerpc.v5.dcomrt import DCOMConnection
from impacket.dcerpc.v5.dtypes import NULL

from collector.windows.dcerpc.wmi import (
    Win32_Account,
    Win32_Service,
    aceflags_to_list,
    get_valid_absolute_service_paths,
    wmi_access_mask_to_str_list,
)

WindowsHives = Literal[
    "HKEY_CLASSES_ROOT",
    "HKEY_CURRENT_USER",
    "HKEY_LOCAL_MACHINE",
    "HKEY_USERS",
    "HKEY_CURRENT_CONFIG",
]

HIVES_CONST = {
    "HKEY_CLASSES_ROOT": 2147483648,
    "HKEY_CURRENT_USER": 2147483649,
    "HKEY_LOCAL_MACHINE": 2147483650,
    "HKEY_USERS": 2147483651,
    "HKEY_CURRENT_CONFIG": 2147483653,
}

logger = logging.getLogger(__name__)


class MS_WMI:
    """
        Provides impacket's interfaces methods to query and enumerate security characteristics through remote WMI.

    Notes:
        - This implementation may later be refactored into an abstract base class, since
          different namespaces do not expose the same set of methods.
        - Currently, each method connects to and disconnects from IWbemServices independently,
          because the active namespace cannot be assumed in advance.
        - Furthermore, the current functionning doesn't follow the specification described in 3.1 of MS-WMI
          but it's work well for now.
    """

    def __init__(self):
        self.conn: DCOMConnection = None
        self.iwbem_services = None
        self.iwbem_level_1_login = None

    def connect(self, host: str, username: str, password: str) -> None:
        self.conn = DCOMConnection(host, username, password)
        instance = self.conn.CoCreateInstanceEx(CLSID_WbemLevel1Login, IID_IWbemLevel1Login)
        self.iwbem_level_1_login = IWbemLevel1Login(instance)

    def get_dword_register_value(self, hive: WindowsHives, key_path: str, register: str) -> int | None:
        h_key = HIVES_CONST.get(hive)
        if h_key is None:
            return None
        iwbem_services: IWbemServices = self.iwbem_level_1_login.NTLMLogin("root\\cimv2", NULL, NULL)

        # https://learn.microsoft.com/en-us/previous-versions/windows/desktop/regprov/getdwordvalue-method-in-class-stdregprov
        reg_prov, _ = iwbem_services.GetObject("StdRegProv")
        result = reg_prov.GetDWORDValue(h_key, key_path, register)
        if result.ReturnValue == 0:
            return int(result.uValue)

        iwbem_services.RemRelease()
        return None

    def get_software_installed(self) -> dict[list[dict]]:
        keys = [
            "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall",
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall",
        ]

        softwares_by_key = {}
        for key in keys:
            result = [
                {"name": d["DisplayName"], "version": d["DisplayVersion"]}
                for d in self.enum_registry("HKEY_LOCAL_MACHINE", key)
                if "DisplayName" in d and "DisplayVersion" in d
            ]
            softwares_by_key[f"HKEY_LOCAL_MACHINE\{key}"] = result

        return softwares_by_key

    def enum_registry(self, hive: WindowsHives, key: str) -> list[dict] | None:
        iwbem_services: IWbemServices = self.iwbem_level_1_login.NTLMLogin("root\\cimv2", NULL, NULL)
        reg_prov: IWbemClassObject
        reg_prov, _ = iwbem_services.GetObject("StdRegProv")

        try:
            res = reg_prov.EnumKey(HIVES_CONST[hive], key)
            subkeys = res.sNames
        except AttributeError as e:
            logger.error(f"Unable to enumerate key {hive}\\{key}: {e}")
            return None

        results: list[dict] = []

        # Mapping between registry value types and their corresponding StdRegProv getter
        map_method = {
            1: reg_prov.GetStringValue,  # REG_SZ
            2: reg_prov.GetExpandedStringValue,  # REG_EXPAND_SZ
            3: reg_prov.GetBinaryValue,  # REG_BINARY
            4: reg_prov.GetDWORDValue,  # REG_DWORD
            7: reg_prov.GetMultiStringValue,  # REG_MULTI_SZ
            11: reg_prov.GetQWORDValue,  # REG_QWORD
        }

        for subkey in subkeys:
            try:
                result2 = reg_prov.EnumValues(HIVES_CONST[hive], f"{key}\\{subkey}")
                values = result2.sNames
                if not values:
                    continue
                types = result2.Types
            except Exception as e:
                logger.warning(f"Error reading values from {hive}\\{key}\\{subkey}: {e}")
                continue

            data: dict = {"subkey_name": subkey}

            for reg_name, reg_type in zip(values, types):
                try:
                    # Call the correct method based on the registry value type
                    res: IWbemClassObject = map_method[reg_type](HIVES_CONST[hive], f"{key}\\{subkey}", reg_name)
                    if res.ReturnValue:
                        logger.warning(
                            f"Unable to read {reg_name} ({reg_type}) in {hive}\\{key}\\{subkey}, code: {res.ReturnValue}"
                        )
                        continue

                    # Registry values can be stored either in sValue (strings) or uValue (numeric types)
                    value = getattr(res, "sValue", getattr(res, "uValue", None))
                    data[reg_name] = value
                except AttributeError as e:
                    logger.warning(f"Unable to read {reg_name} in {hive}\\{key}\\{subkey}: {e}")
                    continue

            results.append(data)

        # Release WMI resources
        iwbem_services.RemRelease()
        return results

    def get_wmi_right(self, namespace: str) -> dict | None:
        try:
            iwbem_services: IWbemServices = self.iwbem_level_1_login.NTLMLogin(namespace, NULL, NULL)
            system_sec, _ = iwbem_services.GetObject("__systemsecurity")
            params: IWbemClassObject = system_sec.GetSecurityDescriptor()
            result = None
            if not params.ReturnValue:
                result = self._extract_data_from_security_descriptor(params.Descriptor)
                return result
            else:
                raise DCERPCException(f"Return code {params.ReturnValue}")
        except DCERPCException as e:
            logger.error(f"Cannot get the security descriptor of the namespace : {namespace}")
            logger.error(f"Exception : {e}")
            return None

    def _extract_data_from_security_descriptor(self, security_descriptor: IWbemClassObject) -> dict:
        result = {}
        result["owner"] = {
            "domain": security_descriptor.Owner.Domain,
            "name": security_descriptor.Owner.Name,
            "sid": security_descriptor.Owner.SIDString,
        }
        result["group"] = {
            "domain": security_descriptor.Group.Domain,
            "name": security_descriptor.Group.Name,
            "sid": security_descriptor.Group.SIDString,
        }

        result["dacl"] = []
        for ace in security_descriptor.DACL:
            ace_data = {}
            ace_data["trustee"] = {}
            ace_data["trustee"]["name"] = ace.Trustee.Name
            ace_data["trustee"]["domain"] = ace.Trustee.Domain
            ace_data["trustee"]["sid"] = ace.Trustee.SIDString
            ace_data["access_mask"] = ace.AccessMask
            ace_data["permissions"] = wmi_access_mask_to_str_list(ace.AccessMask)
            ace_data["inherited"] = bool(ace.AceFlags & 0x10)
            ace_data["flags"] = aceflags_to_list(ace.AceFlags)
            result["dacl"].append(ace_data)
        return result

    def get_file_security_descriptor(self, file_path: str) -> dict | None:
        try:
            file_path_escaped = file_path.replace('"', "")
            file_path_escaped = re.sub(r"\\+", r"\\\\", file_path_escaped)
            iwbem_services = self.iwbem_level_1_login.NTLMLogin("root\\cimv2", NULL, NULL)
            resp: IWbemClassObject = iwbem_services.ExecMethod(
                f'Win32_LogicalFileSecuritySetting.Path="{file_path_escaped}"',
                "getSecurityDescriptor",
            )
            result = None
            if not resp.ReturnValue:
                result = self._extract_data_from_security_descriptor(resp.Descriptor)
            # else:
            # logger.error(f"Error while fetching security descriptor of {file_path}, error code :{resp.ReturnValue}")
            resp.RemRelease()
            iwbem_services.RemRelease()
            return result
        except DCERPCSessionError as e:
            # logger.error(f"Error while fetching the security descriptor of {file_path}, exception: {e}")
            return None

    def get_wmi32_account(self) -> list[Win32_Account]:
        iwbem_services = self.iwbem_level_1_login.NTLMLogin("root\\cimv2", NULL, NULL)
        enum = iwbem_services.ExecQuery("SELECT * FROM Win32_Account")
        accounts: list[Win32_Account] = []
        while True:
            try:
                account_obj: IWbemClassObject = enum.Next(0xFFFFFFFF, 1)[0]
                account: Win32_Account = self._dict_to_dataclass(account_obj.__dict__, Win32_Account)
                accounts.append(account)
            except Exception as e:
                break
        enum.RemRelease()
        iwbem_services.RemRelease()
        return accounts

    def __get_sp_from_startName(self, start_name: str, accounts: list[Win32_Account]) -> dict:
        # UPN format
        if "@" in start_name:
            name = start_name.split("@")[0]
        elif "\\" in start_name:
            name = start_name.split("\\")[1]
        else:
            name = start_name

        name = name.lower().replace(" ", "")
        if name == "localsystem":
            return {"name": name, "sid": "S-1-5-18"}
        for account in accounts:
            if name == account.Name.lower().replace(" ", ""):
                return {"name": name, "sid": account.SID}

        logger.warning(f"Cannot translate for startName service {name}")
        return {"name": name, "sid": None}

    def get_service_exec_acl(self) -> list | None:
        services = self._get_services()
        if services is None:
            return None
        service_valid_exec_path = get_valid_absolute_service_paths(services)
        result = []
        accounts = self.get_wmi32_account()
        for service in service_valid_exec_path:
            sd = None
            if service.PathName and service in service_valid_exec_path:
                sd = self.get_file_security_descriptor(service.PathName)
            run_by: None | dict = None
            if service.StartName:
                run_by = self.__get_sp_from_startName(service.StartName, accounts)

            if sd is not None:
                result.append(
                    {
                        "name": service.Name,
                        "path": service.PathName,
                        "security_descriptor": sd,
                        "status": service.Status,
                        "run_by": run_by,
                    }
                )

        return result

    def get_system_account(self) -> list[dict[str, str]] | None:
        iwbem_services = self.iwbem_level_1_login.NTLMLogin("root\\cimv2", NULL, NULL)
        enum = iwbem_services.ExecQuery("SELECT * FROM Win32_Account")
        accounts: list[Win32_Account] = []
        while True:
            try:
                account_obj: IWbemClassObject = enum.Next(0xFFFFFFFF, 1)[0]
                account: Win32_Account = self._dict_to_dataclass(account_obj.__dict__, Win32_Account)
                accounts.append(account)
            except Exception as e:
                break

        enum.RemRelease()
        iwbem_services.RemRelease()

        results = [{"name": account.Name, "sid": account.SID} for account in accounts if account.SIDType == 5]
        return results

    def _get_services(self) -> list[Win32_Service] | None:
        iwbem_services = self.iwbem_level_1_login.NTLMLogin("root\\cimv2", NULL, NULL)
        enum = iwbem_services.ExecQuery("SELECT * FROM Win32_Service")

        # Ugly but it works like that, I think
        services = []
        while True:
            try:
                service_obj: IWbemClassObject = enum.Next(0xFFFFFFFF, 1)[0]
                service = self._dict_to_dataclass(service_obj.__dict__, Win32_Service)
                services.append(service)
                service_obj.RemRelease()
            except Exception as e:
                break

        enum.RemRelease()
        iwbem_services.RemRelease()
        return services

    def _dict_to_dataclass(self, data: dict, cls: type):
        if not is_dataclass(cls):
            raise ValueError(f"{cls} is not a dataclass")

        valid_fields = {f.name for f in fields(cls)}
        filtered = {k: v for k, v in data.items() if k in valid_fields}
        return cls(**filtered)
