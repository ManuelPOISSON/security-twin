import base64
import logging
import json
import typing

import pypsrp
import pypsrp.client
import winrm

from abc import ABC, abstractmethod
from xml.etree import ElementTree as ET

from impacket.dcerpc.v5.dcomrt import DCOMConnection
from impacket.dcerpc.v5.dcom.oaut import (
    IID_IDispatch,
    string_to_bin,
    IDispatch,
    DISPATCH_PROPERTYGET,
    VARIANT,
    VARENUM,
    DISPATCH_METHOD,
    DISPPARAMS,
)
from impacket.dcerpc.v5.dcomrt import (
    OBJREF,
    FLAGS_OBJREF_CUSTOM,
    OBJREF_CUSTOM,
    OBJREF_HANDLER,
    OBJREF_EXTENDED,
    OBJREF_STANDARD,
    FLAGS_OBJREF_HANDLER,
    FLAGS_OBJREF_STANDARD,
    FLAGS_OBJREF_EXTENDED,
    IRemUnknown2,
    INTERFACE,
)
from impacket.dcerpc.v5.dtypes import NULL
from pypsrp.wsman import OptionSet, SelectorSet, NAMESPACES, WSManAction,  WSMan



logger = logging.getLogger(__name__)



def hook_create(
    self,
    resource_uri: str,
    resource: ET.Element,
    option_set: typing.Optional[OptionSet] = None,
    selector_set: typing.Optional[SelectorSet] = None,
    timeout: typing.Optional[int] = None,
) -> ET.Element:

    option_set.add_option("WINRS_NOPROFILE", "1", {"MustComply" : "true"})
    res = self.invoke(WSManAction.CREATE, resource_uri, resource, option_set, selector_set, timeout)
    return res.find("s:Body", namespaces=NAMESPACES)


class CollectionStrategy(ABC):
    @abstractmethod
    def execute_ps_script(self, path: str):
        pass


class Prsp(CollectionStrategy):
    # Todo change type hint protocol to Literal
    # And add new protocols
    def __init__(self, host: str, user: str, password: str, auth: str, logger: logging.Logger, user_profile: bool = False):
        if not user_profile:
            WSMan.create = hook_create
        self.host = host
        self.logger = logger
        self.connection = pypsrp.client.Client(
            server=host, username=user, password=password, ssl=False, cert_validation=False, auth=auth,negotiate_service='http'
        )
        output, streams, errors = self.connection.execute_ps('(New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)')
        if output.lower() == "true":
            self.logger.info(f"Running scripts with administrators privileges on {host}")
        else:
            self.logger.warning(f"Running scripts without administrators privileges on {host}")
       

    def execute_ps_script(self, path: str):
        self.logger.debug(f"Executing script {path} on host {self.host}")
        with open(path, "r") as fd:
            script_name = path.split("/")[-1]
            output, streams, errors = self.connection.execute_ps(fd.read())
            if errors:
                self.logger.warning(f"Script: {script_name} get following errors :")
                for err in streams.error:
                    self.logger.warning(f"{err}")
                    if output is True:
                        return output
                    self.logger.error(f"{script_name} gives no output")
                    return None
            
            for name, stream in streams.__dict__.items():
                if name == "progress":
                    continue
                for value in stream:
                    self.logger.debug(f" {self.host} - {script_name} - {name} - {value}")
        
            return output


    
"""_summary_

    Returns:
        _type_: _description_
"""
class Winrm(CollectionStrategy):
    def __init__(self, host: str, user: str, password: str):
        self.session = winrm.Session(host, auth=(user, password), transport="ntlm")

    def execute_ps_script(self, path: str):
        with open(path, "r") as fd:
            result = self.session.run_ps(fd.read())
            if result.status_code != 0:
                print(result.std_err.decode("utf-8"))
                return None
            return json.loads(result.std_out.decode())


class DCOMMMC20(CollectionStrategy):
    def __init__(
        self,
        username,
        password,
        domain,
        target,
        lmhash="",
        nthash="",
        do_kerberos=False,
    ):
        self.username = username
        self.password = password
        self.domain = domain
        self.target = target
        self.lmhash = lmhash
        self.nthash = nthash
        self.do_kerberos = do_kerberos
        self.dcom = None
        self.pExecuteShellCommand = None
        self.iActiveView = None

    def getInterface(self, interface, resp):
        # Now let's parse the answer and build an Interface instance
        objRefType = OBJREF(b"".join(resp))["flags"]
        objRef = None
        if objRefType == FLAGS_OBJREF_CUSTOM:
            objRef = OBJREF_CUSTOM(b"".join(resp))
        elif objRefType == FLAGS_OBJREF_HANDLER:
            objRef = OBJREF_HANDLER(b"".join(resp))
        elif objRefType == FLAGS_OBJREF_STANDARD:
            objRef = OBJREF_STANDARD(b"".join(resp))
        elif objRefType == FLAGS_OBJREF_EXTENDED:
            objRef = OBJREF_EXTENDED(b"".join(resp))

        return IRemUnknown2(
            INTERFACE(
                interface.get_cinstance(),
                None,
                interface.get_ipidRemUnknown(),
                objRef["std"]["ipid"],
                oxid=objRef["std"]["oxid"],
                oid=objRef["std"]["oxid"],
                target=interface.get_target(),
            )
        )

    def connect(self):

        self.dcom = DCOMConnection(
            self.target,
            self.username,
            self.password,
            self.domain,
            self.lmhash,
            self.nthash,
            self.do_kerberos,
        )

        iInterface = self.dcom.CoCreateInstanceEx(
            string_to_bin("49B2791A-B1AE-4C90-9B8E-E860BA07F889"), IID_IDispatch
        )
        dispParams = DISPPARAMS(None, False)
        dispParams["rgvarg"] = NULL
        dispParams["rgdispidNamedArgs"] = NULL
        dispParams["cArgs"] = 0
        dispParams["cNamedArgs"] = 0
        iMMC = IDispatch(iInterface)
        resp = iMMC.GetIDsOfNames(("Document",))
        resp = iMMC.Invoke(resp[0], 0x409, DISPATCH_PROPERTYGET, dispParams, 0, [], [])
        iDocument = IDispatch(
            self.getInterface(
                iMMC, resp["pVarResult"]["_varUnion"]["pdispVal"]["abData"]
            )
        )
        resp = iDocument.GetIDsOfNames(("ActiveView",))
        resp = iDocument.Invoke(
            resp[0], 0x409, DISPATCH_PROPERTYGET, dispParams, 0, [], []
        )
        # $dcomObject.Document.ActiveView.ExecuteShellCommand("cmd.exe", "", "/c echo Hello > C:\Users\Public\Desktop\test3.txt", "7")

        self.iActiveView = IDispatch(
            self.getInterface(
                iMMC, resp["pVarResult"]["_varUnion"]["pdispVal"]["abData"]
            )
        )
        self.pExecuteShellCommand = self.iActiveView.GetIDsOfNames(
            ("ExecuteShellCommand",)
        )[0]
        return True

    def execute_ps_script(self, script):
        with open(script, "r") as fd:
            data = fd.read()
        encoded_script = base64.b64encode(data.encode(encoding="utf-16le"))
        dispParams = DISPPARAMS(None, False)
        dispParams["rgdispidNamedArgs"] = NULL
        dispParams["cArgs"] = 4
        dispParams["cNamedArgs"] = 0
        arg0 = VARIANT(None, False)
        arg0["clSize"] = 5
        arg0["vt"] = VARENUM.VT_BSTR
        arg0["_varUnion"]["tag"] = VARENUM.VT_BSTR
        arg0["_varUnion"]["bstrVal"]["asData"] = "powershell.exe"

        arg1 = VARIANT(None, False)
        arg1["clSize"] = 5
        arg1["vt"] = VARENUM.VT_BSTR
        arg1["_varUnion"]["tag"] = VARENUM.VT_BSTR
        arg1["_varUnion"]["bstrVal"]["asData"] = ""

        arg2 = VARIANT(None, False)
        arg2["clSize"] = 5
        arg2["vt"] = VARENUM.VT_BSTR
        arg2["_varUnion"]["tag"] = VARENUM.VT_BSTR

        arg2["_varUnion"]["bstrVal"][
            "asData"
        ] = f"-EncodedCommand {encoded_script.decode()}"
        print(f"-EncodedCommand {encoded_script.decode()}")
        arg3 = VARIANT(None, False)
        arg3["clSize"] = 5
        arg3["vt"] = VARENUM.VT_BSTR
        arg3["_varUnion"]["tag"] = VARENUM.VT_BSTR
        arg3["_varUnion"]["bstrVal"]["asData"] = "7"
        dispParams["rgvarg"].append(arg3)
        dispParams["rgvarg"].append(arg2)
        dispParams["rgvarg"].append(arg1)
        dispParams["rgvarg"].append(arg0)
        self.iActiveView.Invoke(
            self.pExecuteShellCommand, 0x409, DISPATCH_METHOD, dispParams, 0, [], []
        )
        print("[*] PowerShell script executed successfully")

    def disconnect(self):
        if self.dcom:
            self.dcom.disconnect()
            print("[*] DCOM connection closed")
