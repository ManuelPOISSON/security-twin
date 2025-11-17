r"""
# `libvirt_network`

Refer to the Terraform Registry for docs: [`libvirt_network`](https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network).
"""

from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class Network(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.Network",
):
    """Represents a {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network libvirt_network}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        autostart: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        bridge: typing.Optional[builtins.str] = None,
        dhcp: typing.Optional[typing.Union["NetworkDhcp", typing.Dict[builtins.str, typing.Any]]] = None,
        dns: typing.Optional[typing.Union["NetworkDns", typing.Dict[builtins.str, typing.Any]]] = None,
        dnsmasq_options: typing.Optional[typing.Union["NetworkDnsmasqOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        domain: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        mtu: typing.Optional[jsii.Number] = None,
        routes: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkRoutes", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        xml: typing.Optional[typing.Union["NetworkXml", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[
            typing.Union[
                typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]],
                typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]],
            ]
        ] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[
            typing.Sequence[
                typing.Union[
                    typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]],
                    typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]],
                    typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]],
                ]
            ]
        ] = None,
    ) -> None:
        """Create a new {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network libvirt_network} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#name Network#name}.
        :param addresses: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#addresses Network#addresses}.
        :param autostart: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#autostart Network#autostart}.
        :param bridge: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#bridge Network#bridge}.
        :param dhcp: dhcp block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#dhcp Network#dhcp}
        :param dns: dns block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#dns Network#dns}
        :param dnsmasq_options: dnsmasq_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#dnsmasq_options Network#dnsmasq_options}
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#domain Network#domain}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#id Network#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#mode Network#mode}.
        :param mtu: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#mtu Network#mtu}.
        :param routes: routes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#routes Network#routes}
        :param xml: xml block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#xml Network#xml}
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c32f55c9289268193f91d86d57e5e098c0eef24a0ecf0689b3d0ae3176d44e06)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkConfig(
            name=name,
            addresses=addresses,
            autostart=autostart,
            bridge=bridge,
            dhcp=dhcp,
            dns=dns,
            dnsmasq_options=dnsmasq_options,
            domain=domain,
            id=id,
            mode=mode,
            mtu=mtu,
            routes=routes,
            xml=xml,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        """Generates CDKTF code for importing a Network resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Network to import.
        :param import_from_id: The id of the existing Network that should be imported. Refer to the {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Network to import is found.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feee1bbb61bdb1a603c00e6cd6370af981d2b66455133bac2615b3c71e1dcf60)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putDhcp")
    def put_dhcp(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        """
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#enabled Network#enabled}.
        """
        value = NetworkDhcp(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putDhcp", [value]))

    @jsii.member(jsii_name="putDns")
    def put_dns(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        forwarders: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkDnsForwarders", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        hosts: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkDnsHosts", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        local_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        srvs: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkDnsSrvs", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
    ) -> None:
        """
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#enabled Network#enabled}.
        :param forwarders: forwarders block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#forwarders Network#forwarders}
        :param hosts: hosts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#hosts Network#hosts}
        :param local_only: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#local_only Network#local_only}.
        :param srvs: srvs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#srvs Network#srvs}
        """
        value = NetworkDns(
            enabled=enabled,
            forwarders=forwarders,
            hosts=hosts,
            local_only=local_only,
            srvs=srvs,
        )

        return typing.cast(None, jsii.invoke(self, "putDns", [value]))

    @jsii.member(jsii_name="putDnsmasqOptions")
    def put_dnsmasq_options(
        self,
        *,
        options: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkDnsmasqOptionsOptions", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
    ) -> None:
        """
        :param options: options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#options Network#options}
        """
        value = NetworkDnsmasqOptions(options=options)

        return typing.cast(None, jsii.invoke(self, "putDnsmasqOptions", [value]))

    @jsii.member(jsii_name="putRoutes")
    def put_routes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkRoutes", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d587a6b4a8a348f4ddb46118b51bf6766c897b8dea20bc03e255978f049ca3cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRoutes", [value]))

    @jsii.member(jsii_name="putXml")
    def put_xml(self, *, xslt: typing.Optional[builtins.str] = None) -> None:
        """
        :param xslt: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#xslt Network#xslt}.
        """
        value = NetworkXml(xslt=xslt)

        return typing.cast(None, jsii.invoke(self, "putXml", [value]))

    @jsii.member(jsii_name="resetAddresses")
    def reset_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddresses", []))

    @jsii.member(jsii_name="resetAutostart")
    def reset_autostart(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutostart", []))

    @jsii.member(jsii_name="resetBridge")
    def reset_bridge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBridge", []))

    @jsii.member(jsii_name="resetDhcp")
    def reset_dhcp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDhcp", []))

    @jsii.member(jsii_name="resetDns")
    def reset_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDns", []))

    @jsii.member(jsii_name="resetDnsmasqOptions")
    def reset_dnsmasq_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsmasqOptions", []))

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetMtu")
    def reset_mtu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMtu", []))

    @jsii.member(jsii_name="resetRoutes")
    def reset_routes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoutes", []))

    @jsii.member(jsii_name="resetXml")
    def reset_xml(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXml", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="dhcp")
    def dhcp(self) -> "NetworkDhcpOutputReference":
        return typing.cast("NetworkDhcpOutputReference", jsii.get(self, "dhcp"))

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> "NetworkDnsOutputReference":
        return typing.cast("NetworkDnsOutputReference", jsii.get(self, "dns"))

    @builtins.property
    @jsii.member(jsii_name="dnsmasqOptions")
    def dnsmasq_options(self) -> "NetworkDnsmasqOptionsOutputReference":
        return typing.cast("NetworkDnsmasqOptionsOutputReference", jsii.get(self, "dnsmasqOptions"))

    @builtins.property
    @jsii.member(jsii_name="routes")
    def routes(self) -> "NetworkRoutesList":
        return typing.cast("NetworkRoutesList", jsii.get(self, "routes"))

    @builtins.property
    @jsii.member(jsii_name="xml")
    def xml(self) -> "NetworkXmlOutputReference":
        return typing.cast("NetworkXmlOutputReference", jsii.get(self, "xml"))

    @builtins.property
    @jsii.member(jsii_name="addressesInput")
    def addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "addressesInput"))

    @builtins.property
    @jsii.member(jsii_name="autostartInput")
    def autostart_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autostartInput"))

    @builtins.property
    @jsii.member(jsii_name="bridgeInput")
    def bridge_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bridgeInput"))

    @builtins.property
    @jsii.member(jsii_name="dhcpInput")
    def dhcp_input(self) -> typing.Optional["NetworkDhcp"]:
        return typing.cast(typing.Optional["NetworkDhcp"], jsii.get(self, "dhcpInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsInput")
    def dns_input(self) -> typing.Optional["NetworkDns"]:
        return typing.cast(typing.Optional["NetworkDns"], jsii.get(self, "dnsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsmasqOptionsInput")
    def dnsmasq_options_input(self) -> typing.Optional["NetworkDnsmasqOptions"]:
        return typing.cast(typing.Optional["NetworkDnsmasqOptions"], jsii.get(self, "dnsmasqOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="mtuInput")
    def mtu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mtuInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="routesInput")
    def routes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkRoutes"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkRoutes"]]], jsii.get(self, "routesInput"))

    @builtins.property
    @jsii.member(jsii_name="xmlInput")
    def xml_input(self) -> typing.Optional["NetworkXml"]:
        return typing.cast(typing.Optional["NetworkXml"], jsii.get(self, "xmlInput"))

    @builtins.property
    @jsii.member(jsii_name="addresses")
    def addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "addresses"))

    @addresses.setter
    def addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f692eab7b59cc5b548231f8710836245224572cf8d0598783d2e29dec84c15a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addresses", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="autostart")
    def autostart(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autostart"))

    @autostart.setter
    def autostart(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcd154f1f44a84add25ae111aa12d9cc7d7a54c466b628a8bd3efad12464048f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autostart", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="bridge")
    def bridge(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bridge"))

    @bridge.setter
    def bridge(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f2066dbb85fb47f01fce1802c4b364a7fa72a61cb3bfa2470b52354485ba46b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bridge", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0303056157b7388279e7bef3e6df738f328eb9d10caad340bbc1b1a2165f361)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b0c1251a5650d984c7418829025382ebca2f69ab7b2fd7182fde48ca0fbd65b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01109477854f68213bbfeece378dea0ff34bc3479015fba28b2ef2a0e098b5a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mtu")
    def mtu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mtu"))

    @mtu.setter
    def mtu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1753235c092a8d3ed7be4f2a6b478634101aa2e6bd79c037e2f63a3cbe19c3f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mtu", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d85c7231bcb2d91e17cb46ad607a9bdb0249958bec90fa569ed4b497347623a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.network.NetworkConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "addresses": "addresses",
        "autostart": "autostart",
        "bridge": "bridge",
        "dhcp": "dhcp",
        "dns": "dns",
        "dnsmasq_options": "dnsmasqOptions",
        "domain": "domain",
        "id": "id",
        "mode": "mode",
        "mtu": "mtu",
        "routes": "routes",
        "xml": "xml",
    },
)
class NetworkConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[
            typing.Union[
                typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]],
                typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]],
            ]
        ] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[
            typing.Sequence[
                typing.Union[
                    typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]],
                    typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]],
                    typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]],
                ]
            ]
        ] = None,
        name: builtins.str,
        addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        autostart: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        bridge: typing.Optional[builtins.str] = None,
        dhcp: typing.Optional[typing.Union["NetworkDhcp", typing.Dict[builtins.str, typing.Any]]] = None,
        dns: typing.Optional[typing.Union["NetworkDns", typing.Dict[builtins.str, typing.Any]]] = None,
        dnsmasq_options: typing.Optional[typing.Union["NetworkDnsmasqOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        domain: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        mtu: typing.Optional[jsii.Number] = None,
        routes: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkRoutes", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        xml: typing.Optional[typing.Union["NetworkXml", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#name Network#name}.
        :param addresses: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#addresses Network#addresses}.
        :param autostart: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#autostart Network#autostart}.
        :param bridge: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#bridge Network#bridge}.
        :param dhcp: dhcp block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#dhcp Network#dhcp}
        :param dns: dns block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#dns Network#dns}
        :param dnsmasq_options: dnsmasq_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#dnsmasq_options Network#dnsmasq_options}
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#domain Network#domain}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#id Network#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#mode Network#mode}.
        :param mtu: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#mtu Network#mtu}.
        :param routes: routes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#routes Network#routes}
        :param xml: xml block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#xml Network#xml}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(dhcp, dict):
            dhcp = NetworkDhcp(**dhcp)
        if isinstance(dns, dict):
            dns = NetworkDns(**dns)
        if isinstance(dnsmasq_options, dict):
            dnsmasq_options = NetworkDnsmasqOptions(**dnsmasq_options)
        if isinstance(xml, dict):
            xml = NetworkXml(**xml)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1be553ccc6d9d8b8109e39972de0ed79073e066872099ac5fa7fecd80f29308)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument addresses", value=addresses, expected_type=type_hints["addresses"])
            check_type(argname="argument autostart", value=autostart, expected_type=type_hints["autostart"])
            check_type(argname="argument bridge", value=bridge, expected_type=type_hints["bridge"])
            check_type(argname="argument dhcp", value=dhcp, expected_type=type_hints["dhcp"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument dnsmasq_options", value=dnsmasq_options, expected_type=type_hints["dnsmasq_options"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument mtu", value=mtu, expected_type=type_hints["mtu"])
            check_type(argname="argument routes", value=routes, expected_type=type_hints["routes"])
            check_type(argname="argument xml", value=xml, expected_type=type_hints["xml"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if addresses is not None:
            self._values["addresses"] = addresses
        if autostart is not None:
            self._values["autostart"] = autostart
        if bridge is not None:
            self._values["bridge"] = bridge
        if dhcp is not None:
            self._values["dhcp"] = dhcp
        if dns is not None:
            self._values["dns"] = dns
        if dnsmasq_options is not None:
            self._values["dnsmasq_options"] = dnsmasq_options
        if domain is not None:
            self._values["domain"] = domain
        if id is not None:
            self._values["id"] = id
        if mode is not None:
            self._values["mode"] = mode
        if mtu is not None:
            self._values["mtu"] = mtu
        if routes is not None:
            self._values["routes"] = routes
        if xml is not None:
            self._values["xml"] = xml

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        """
        :stability: experimental
        """
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        """
        :stability: experimental
        """
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        """
        :stability: experimental
        """
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        """
        :stability: experimental
        """
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        """
        :stability: experimental
        """
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        """
        :stability: experimental
        """
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[
        typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]
    ]:
        """
        :stability: experimental
        """
        result = self._values.get("provisioners")
        return typing.cast(
            typing.Optional[
                typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]
            ],
            result,
        )

    @builtins.property
    def name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#name Network#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#addresses Network#addresses}."""
        result = self._values.get("addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def autostart(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#autostart Network#autostart}."""
        result = self._values.get("autostart")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def bridge(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#bridge Network#bridge}."""
        result = self._values.get("bridge")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dhcp(self) -> typing.Optional["NetworkDhcp"]:
        """dhcp block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#dhcp Network#dhcp}
        """
        result = self._values.get("dhcp")
        return typing.cast(typing.Optional["NetworkDhcp"], result)

    @builtins.property
    def dns(self) -> typing.Optional["NetworkDns"]:
        """dns block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#dns Network#dns}
        """
        result = self._values.get("dns")
        return typing.cast(typing.Optional["NetworkDns"], result)

    @builtins.property
    def dnsmasq_options(self) -> typing.Optional["NetworkDnsmasqOptions"]:
        """dnsmasq_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#dnsmasq_options Network#dnsmasq_options}
        """
        result = self._values.get("dnsmasq_options")
        return typing.cast(typing.Optional["NetworkDnsmasqOptions"], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#domain Network#domain}."""
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#id Network#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#mode Network#mode}."""
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mtu(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#mtu Network#mtu}."""
        result = self._values.get("mtu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def routes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkRoutes"]]]:
        """routes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#routes Network#routes}
        """
        result = self._values.get("routes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkRoutes"]]], result)

    @builtins.property
    def xml(self) -> typing.Optional["NetworkXml"]:
        """xml block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#xml Network#xml}
        """
        result = self._values.get("xml")
        return typing.cast(typing.Optional["NetworkXml"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConfig(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


@jsii.data_type(
    jsii_type="libvirt.network.NetworkDhcp",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class NetworkDhcp:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        """
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#enabled Network#enabled}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f05a5c46191e752f273bff09496af2a3c20b9c14ae8f4111988e45098a954f66)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#enabled Network#enabled}."""
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkDhcp(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class NetworkDhcpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkDhcpOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58b6567a0ba24675036d978f6938a52fb3646abb7f9c39dc5a735d412b94a7d0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35bbed0105d1720b367de0770cb5a73e6471ff6085ef6d770984e6c27b5f75f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkDhcp]:
        return typing.cast(typing.Optional[NetworkDhcp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[NetworkDhcp]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7570076a74a1ae63fe565b5a1a7b7d56e3c562ef323fcfb5f0670236ba0fbd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.network.NetworkDns",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "forwarders": "forwarders",
        "hosts": "hosts",
        "local_only": "localOnly",
        "srvs": "srvs",
    },
)
class NetworkDns:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        forwarders: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkDnsForwarders", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        hosts: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkDnsHosts", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        local_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        srvs: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkDnsSrvs", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
    ) -> None:
        """
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#enabled Network#enabled}.
        :param forwarders: forwarders block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#forwarders Network#forwarders}
        :param hosts: hosts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#hosts Network#hosts}
        :param local_only: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#local_only Network#local_only}.
        :param srvs: srvs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#srvs Network#srvs}
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fa2b0f0a171b4424cde8bbd60f76f8103e2366f49a2dff8a4608c518e7242c7)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument forwarders", value=forwarders, expected_type=type_hints["forwarders"])
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument local_only", value=local_only, expected_type=type_hints["local_only"])
            check_type(argname="argument srvs", value=srvs, expected_type=type_hints["srvs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if forwarders is not None:
            self._values["forwarders"] = forwarders
        if hosts is not None:
            self._values["hosts"] = hosts
        if local_only is not None:
            self._values["local_only"] = local_only
        if srvs is not None:
            self._values["srvs"] = srvs

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#enabled Network#enabled}."""
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def forwarders(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkDnsForwarders"]]]:
        """forwarders block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#forwarders Network#forwarders}
        """
        result = self._values.get("forwarders")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkDnsForwarders"]]], result)

    @builtins.property
    def hosts(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkDnsHosts"]]]:
        """hosts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#hosts Network#hosts}
        """
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkDnsHosts"]]], result)

    @builtins.property
    def local_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#local_only Network#local_only}."""
        result = self._values.get("local_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def srvs(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkDnsSrvs"]]]:
        """srvs block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#srvs Network#srvs}
        """
        result = self._values.get("srvs")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkDnsSrvs"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkDns(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


@jsii.data_type(
    jsii_type="libvirt.network.NetworkDnsForwarders",
    jsii_struct_bases=[],
    name_mapping={"address": "address", "domain": "domain"},
)
class NetworkDnsForwarders:
    def __init__(
        self,
        *,
        address: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param address: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#address Network#address}.
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#domain Network#domain}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aa75610c9ddf533080ebee1cad14f70f67562baa3efaeb0e3b2a95c2a0ed83f)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if address is not None:
            self._values["address"] = address
        if domain is not None:
            self._values["domain"] = domain

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#address Network#address}."""
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#domain Network#domain}."""
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkDnsForwarders(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class NetworkDnsForwardersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkDnsForwardersList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da3ca2ed266bbe294e1e5da5f25f6cf86bdff81f67f45234a41cdc6ad7b2f358)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NetworkDnsForwardersOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bceb90276f7f99db3258d7693808efa42dcc2b902c770a1e5305ff3267bcbdc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkDnsForwardersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cb94436400df302c24e2f6dcd39d3748fb9bfef2c0539ae3f9c0eda2d5f96cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f70ddfdd227bf41dd96927931f804e1c111fb460c1c00b998321510006e31024)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f4daa4126d156576d0863bd8e0041950549b4ebd0e18e57d41184b2ff56e103)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsForwarders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsForwarders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsForwarders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbfef6d0858398607b86c650dcdbcea8a2bbd1a95ed2ddc643bfac34e30bd3a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class NetworkDnsForwardersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkDnsForwardersOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5125c8865ebe7156fd0328136db398e1c693fd5f42c64567b0b4886782b2b8e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAddress")
    def reset_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddress", []))

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce8db89fc9f2861cb6eac28f875087f67e993ca0b9cbf28c190caedfddddec01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b49620ca65f2742096e8bb3c36f7b499d7ad71e6c77ca15ad656979c96bec1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsForwarders]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsForwarders]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsForwarders]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fe3202a2f474a1caa1c084b3bedaaa26c6b8add45abd8c969b9fd2f211a8f49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.network.NetworkDnsHosts",
    jsii_struct_bases=[],
    name_mapping={"hostname": "hostname", "ip": "ip"},
)
class NetworkDnsHosts:
    def __init__(
        self,
        *,
        hostname: typing.Optional[builtins.str] = None,
        ip: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param hostname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#hostname Network#hostname}.
        :param ip: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#ip Network#ip}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5fdeec12143649e2d5fef7059f2c3a4835ac744b9c00175fc7c8f603daa1f83)
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if hostname is not None:
            self._values["hostname"] = hostname
        if ip is not None:
            self._values["ip"] = ip

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#hostname Network#hostname}."""
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#ip Network#ip}."""
        result = self._values.get("ip")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkDnsHosts(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class NetworkDnsHostsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkDnsHostsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66e7de7a92665cb0f4e9f72e1e6a5f6d0cb97ec61790fb91a25bf29a94bb7715)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NetworkDnsHostsOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd449990fc12de39881af96572074551fffc3f9d2d2684c57b66975cb84dbb1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkDnsHostsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b637e966f7e439e1ab524f0826e93e4def3ac8c3944e76a0d878ad1858fc5857)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e9fcca371d0f9653e9268fb0274033825790eb4ee8bb1ed7da50555b5dee146)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43720657779da054e4b015c00a9d17f65dc36ea2efffab8bebeaba62734b8da5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsHosts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsHosts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsHosts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00425f0809eea386b5a7186b3a8b2389e81d7dcba4e135bb8dd9f2c83888cd23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class NetworkDnsHostsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkDnsHostsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc6a6a915d02af5c5d8ecd15157359b99557b62d40985f1e9f3021abd68592e1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetIp")
    def reset_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIp", []))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="ipInput")
    def ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipInput"))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8080f35df4abab1e3ef990f53a5a3e3c552069776558232dd9e34f56ae27930e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__186e29e89a9c8d57126135e26744b46dfb97b64ac5e5de6eb9fa06cb9dc15c95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsHosts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsHosts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsHosts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__448f46d4b8bbe542e723edd546722fc75e551f95fffdc8ba30534ceae6213469)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class NetworkDnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkDnsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39a10239e74861a2734ae9ba395891aebea23b947bb4bc989f113f04ed907cc3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putForwarders")
    def put_forwarders(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkDnsForwarders, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcf69c91e94246f7edaa95ae3312fa79d62673d016e6d4062f239e34c0f6d6a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putForwarders", [value]))

    @jsii.member(jsii_name="putHosts")
    def put_hosts(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkDnsHosts, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa5bcffcb67da8dc3026e26bcf397d7e372dadde96015cac263a6978cacbcdb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHosts", [value]))

    @jsii.member(jsii_name="putSrvs")
    def put_srvs(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkDnsSrvs", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94df9055229ff6fc9ee78200a76af4af30bbaaf8c507c9ee174fcc7de451ae01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSrvs", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetForwarders")
    def reset_forwarders(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwarders", []))

    @jsii.member(jsii_name="resetHosts")
    def reset_hosts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHosts", []))

    @jsii.member(jsii_name="resetLocalOnly")
    def reset_local_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalOnly", []))

    @jsii.member(jsii_name="resetSrvs")
    def reset_srvs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSrvs", []))

    @builtins.property
    @jsii.member(jsii_name="forwarders")
    def forwarders(self) -> NetworkDnsForwardersList:
        return typing.cast(NetworkDnsForwardersList, jsii.get(self, "forwarders"))

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> NetworkDnsHostsList:
        return typing.cast(NetworkDnsHostsList, jsii.get(self, "hosts"))

    @builtins.property
    @jsii.member(jsii_name="srvs")
    def srvs(self) -> "NetworkDnsSrvsList":
        return typing.cast("NetworkDnsSrvsList", jsii.get(self, "srvs"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardersInput")
    def forwarders_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsForwarders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsForwarders]]], jsii.get(self, "forwardersInput"))

    @builtins.property
    @jsii.member(jsii_name="hostsInput")
    def hosts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsHosts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsHosts]]], jsii.get(self, "hostsInput"))

    @builtins.property
    @jsii.member(jsii_name="localOnlyInput")
    def local_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "localOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="srvsInput")
    def srvs_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkDnsSrvs"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkDnsSrvs"]]], jsii.get(self, "srvsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcc133ce7f251a909346e50e3d12851ccce6ef320f52dd665561741521958097)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="localOnly")
    def local_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "localOnly"))

    @local_only.setter
    def local_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f24aae8e88839b0a05fe3cfc26237f20d3cd1d5c22c745198154577872ff8a03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localOnly", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkDns]:
        return typing.cast(typing.Optional[NetworkDns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[NetworkDns]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06451162b2cbb83b2b428ef8896812383744e0da79e98d36b5d0ee7035ee7a4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.network.NetworkDnsSrvs",
    jsii_struct_bases=[],
    name_mapping={
        "domain": "domain",
        "port": "port",
        "priority": "priority",
        "protocol": "protocol",
        "service": "service",
        "target": "target",
        "weight": "weight",
    },
)
class NetworkDnsSrvs:
    def __init__(
        self,
        *,
        domain: typing.Optional[builtins.str] = None,
        port: typing.Optional[builtins.str] = None,
        priority: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        service: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        weight: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#domain Network#domain}.
        :param port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#port Network#port}.
        :param priority: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#priority Network#priority}.
        :param protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#protocol Network#protocol}.
        :param service: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#service Network#service}.
        :param target: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#target Network#target}.
        :param weight: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#weight Network#weight}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaa574c26414436b5a874cd7a24ea7a85e0f08bb4eb18913984d1c0754522fb7)
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if domain is not None:
            self._values["domain"] = domain
        if port is not None:
            self._values["port"] = port
        if priority is not None:
            self._values["priority"] = priority
        if protocol is not None:
            self._values["protocol"] = protocol
        if service is not None:
            self._values["service"] = service
        if target is not None:
            self._values["target"] = target
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#domain Network#domain}."""
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#port Network#port}."""
        result = self._values.get("port")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#priority Network#priority}."""
        result = self._values.get("priority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#protocol Network#protocol}."""
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#service Network#service}."""
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#target Network#target}."""
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weight(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#weight Network#weight}."""
        result = self._values.get("weight")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkDnsSrvs(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class NetworkDnsSrvsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkDnsSrvsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ce3599931d4576f245d989d75d943ef7da5104ed4390124e910888b0e356a32)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NetworkDnsSrvsOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77666b35feefdabddb932d474fb4ee161c7853e516825305f9c1a6abb1d6da40)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkDnsSrvsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e30c52b0fb164433e76c6bbba9d6a26ee87385209c0c9c47028607ad80f283d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c35934c8418e696aec1648c1835d2b7ac93fd8eb9e6d0b249dfa991f86cd296d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__915d4682e3a179992788f8c7bfcdfaa25b4e1a90d749538ba15f4e1658e5bf95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsSrvs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsSrvs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsSrvs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9250c1d22bc8bd650849f127a98878ee30183fe89ff8f5305f8197689cb09f78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class NetworkDnsSrvsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkDnsSrvsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5727e95b2b44483bb42012e950777bb2b32479fa3faab67cd8bd37a839222c1d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a501fb03df9f0e4b304356db01601849bebe43251f74e23dc80029b49e7f57c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "port"))

    @port.setter
    def port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b05527030daacfc52794568ad7d01eca6faa8fc582f51145e85e74b207ea16b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec9ea2338f5c74eb47268f78973d1c0717a64ac4eb3c6f88a021113fe57f5b54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4d9bce8c48101b8f09036c9b19d34e429320bfaf5d4dbce34ef7ca505d42b0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd019852401bc816e477a81f22cbd823c7f81d909c205e32bf1cd790873c230)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9111e96e7a0bf4263efed6e0f294d66fa964f5ba7c5778417fa521511d5b8689)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__921c824db456b4f8f42ad1adcdb6d674febe29d4f66971bf8bbbc4b0435952d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsSrvs]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsSrvs]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsSrvs]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dc0aa2436b605c816bc60f20538a08c91a657c32a0647c4999eadeeca142538)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.network.NetworkDnsmasqOptions",
    jsii_struct_bases=[],
    name_mapping={"options": "options"},
)
class NetworkDnsmasqOptions:
    def __init__(
        self,
        *,
        options: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkDnsmasqOptionsOptions", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
    ) -> None:
        """
        :param options: options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#options Network#options}
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e9da8045200ffa9a02bae5779d3b041bdcd73dccfe1c380e78553cbbf6a2f72)
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if options is not None:
            self._values["options"] = options

    @builtins.property
    def options(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkDnsmasqOptionsOptions"]]]:
        """options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#options Network#options}
        """
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkDnsmasqOptionsOptions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkDnsmasqOptions(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


@jsii.data_type(
    jsii_type="libvirt.network.NetworkDnsmasqOptionsOptions",
    jsii_struct_bases=[],
    name_mapping={"option_name": "optionName", "option_value": "optionValue"},
)
class NetworkDnsmasqOptionsOptions:
    def __init__(
        self,
        *,
        option_name: typing.Optional[builtins.str] = None,
        option_value: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param option_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#option_name Network#option_name}.
        :param option_value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#option_value Network#option_value}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e3bf55d2473ebf4a7d2742a1173e2fe8df6fd862d23e5339f305de83c96a9b2)
            check_type(argname="argument option_name", value=option_name, expected_type=type_hints["option_name"])
            check_type(argname="argument option_value", value=option_value, expected_type=type_hints["option_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if option_name is not None:
            self._values["option_name"] = option_name
        if option_value is not None:
            self._values["option_value"] = option_value

    @builtins.property
    def option_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#option_name Network#option_name}."""
        result = self._values.get("option_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def option_value(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#option_value Network#option_value}."""
        result = self._values.get("option_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkDnsmasqOptionsOptions(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class NetworkDnsmasqOptionsOptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkDnsmasqOptionsOptionsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc768840202d74993817c54f360f73d1c44f77e7445d41178d7b78ab3a28e89e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NetworkDnsmasqOptionsOptionsOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84b4946d0fb05364caf5d1a713a3a5b598fd4b8bafaed10b021d2d1c4b512323)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkDnsmasqOptionsOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80589a99390183821ab9c394983c1af974bc3ff413dc36e911cb2142d002757a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c33ba26084c4a2feea9929de24dabc2962caf6ee35d097361be980a3dc9cf002)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0a5fcc2065d6b7b2ab5e62a1289f8ed59aac1e1aec353761cb0cab50c2f7f5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsmasqOptionsOptions]]]:
        return typing.cast(
            typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsmasqOptionsOptions]]], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsmasqOptionsOptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f3c2f51544062998f48789536205546eca06a88e2e5e599da5f6ff05a8a6e01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class NetworkDnsmasqOptionsOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkDnsmasqOptionsOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bcc95660e3f71e0989db532c0a13edbfa759ff4905233827872fa49196f39e3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetOptionName")
    def reset_option_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptionName", []))

    @jsii.member(jsii_name="resetOptionValue")
    def reset_option_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptionValue", []))

    @builtins.property
    @jsii.member(jsii_name="optionNameInput")
    def option_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "optionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionValueInput")
    def option_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "optionValueInput"))

    @builtins.property
    @jsii.member(jsii_name="optionName")
    def option_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "optionName"))

    @option_name.setter
    def option_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb33e2c7795ca164f88bc7d9655bf88fec2a920c72aa1cf02c943a1dc1a98752)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optionName", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="optionValue")
    def option_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "optionValue"))

    @option_value.setter
    def option_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90bb0efedcc30d4a8eda5cf64e757ace9956b27a6140db2d5bbf802e10b8e072)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optionValue", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsmasqOptionsOptions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsmasqOptionsOptions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsmasqOptionsOptions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7777efc6f53be806a5e6568cc46930957489f3d16dc57ad18bc3aa693bde59a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class NetworkDnsmasqOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkDnsmasqOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b8f1212d9c387edece86bfab0807ce217e23eada1d66da953537861a4240cce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOptions")
    def put_options(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkDnsmasqOptionsOptions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebdacd1c62c041c2f8ad5d3eebc6d8ea8ab0f37ce4a4dce52689c5e40440703e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOptions", [value]))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> NetworkDnsmasqOptionsOptionsList:
        return typing.cast(NetworkDnsmasqOptionsOptionsList, jsii.get(self, "options"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsmasqOptionsOptions]]]:
        return typing.cast(
            typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsmasqOptionsOptions]]], jsii.get(self, "optionsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkDnsmasqOptions]:
        return typing.cast(typing.Optional[NetworkDnsmasqOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[NetworkDnsmasqOptions]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cce7696f242e0b513d183fb1a6d8480d99a19d9a307f1743b8120d72943e4556)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.network.NetworkRoutes",
    jsii_struct_bases=[],
    name_mapping={"cidr": "cidr", "gateway": "gateway"},
)
class NetworkRoutes:
    def __init__(self, *, cidr: builtins.str, gateway: builtins.str) -> None:
        """
        :param cidr: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#cidr Network#cidr}.
        :param gateway: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#gateway Network#gateway}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b7d09ad5e09fdc4daf3f8f8ce2c21b516cd6e18378a99198a8f4248a618698c)
            check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
            check_type(argname="argument gateway", value=gateway, expected_type=type_hints["gateway"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cidr": cidr,
            "gateway": gateway,
        }

    @builtins.property
    def cidr(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#cidr Network#cidr}."""
        result = self._values.get("cidr")
        assert result is not None, "Required property 'cidr' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def gateway(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#gateway Network#gateway}."""
        result = self._values.get("gateway")
        assert result is not None, "Required property 'gateway' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkRoutes(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class NetworkRoutesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkRoutesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9392e4922f83fa16c45ab22d2cd738ba7901d582a00b06a0c14ea5a86bf4f2a4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NetworkRoutesOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__620b1390c53c661fd637085fc98fd8b7989d8c76fdcee560249c6d42c501bcce)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkRoutesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a35de28d34ea58fdf6c9420f1a1eceb704d6346f6d58a9db746e406c48c679d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b26e4da8d6ff2a3bca5e12880ef51ff967605c6c45941b54665b0a795787b3e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88aa3f1739905ec23ddc75538a78f00d2d0299811e484f6421b2baa2faf4274c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkRoutes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkRoutes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkRoutes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f75d04fbc00120befb2563f19b03ffba489170d5d843aa163183a8e77b708ade)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class NetworkRoutesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkRoutesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd5798b15f2e683cee49802132f00bb3835546695b75679a283263da26cce486)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="cidrInput")
    def cidr_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidrInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayInput")
    def gateway_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="cidr")
    def cidr(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidr"))

    @cidr.setter
    def cidr(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__638df04b42b36baa482819f37dd480b48b7551f075800808c719f2c958964c27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidr", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gateway")
    def gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gateway"))

    @gateway.setter
    def gateway(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d043728fd0564b2eac4795d74e36ae33cab9d42d2b6589a150df2b701dcdf88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gateway", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkRoutes]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkRoutes]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkRoutes]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bb27cf39e89b066ff340c2c4689cf5c3765234e90d2489f94a59c545c186c66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.network.NetworkXml",
    jsii_struct_bases=[],
    name_mapping={"xslt": "xslt"},
)
class NetworkXml:
    def __init__(self, *, xslt: typing.Optional[builtins.str] = None) -> None:
        """
        :param xslt: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#xslt Network#xslt}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd905cc07396aa02d353a8f0386a0a2a4fe60b1d9405e1ccbc32c7bb811d6933)
            check_type(argname="argument xslt", value=xslt, expected_type=type_hints["xslt"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if xslt is not None:
            self._values["xslt"] = xslt

    @builtins.property
    def xslt(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/network#xslt Network#xslt}."""
        result = self._values.get("xslt")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkXml(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class NetworkXmlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.network.NetworkXmlOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b99300458eed0debdefc5fd20cf2040a84b0f782f5733534ddc7f58d9ed22917)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetXslt")
    def reset_xslt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXslt", []))

    @builtins.property
    @jsii.member(jsii_name="xsltInput")
    def xslt_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "xsltInput"))

    @builtins.property
    @jsii.member(jsii_name="xslt")
    def xslt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "xslt"))

    @xslt.setter
    def xslt(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6f755c50b1c0c9c26fcda668b8a99f01ca17ee329791c5f3fbd667e1f2ca096)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xslt", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkXml]:
        return typing.cast(typing.Optional[NetworkXml], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[NetworkXml]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aebb502d8a10d86e36d2e41638143e47048562b865a178d09ea15e83b2ea2e2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


__all__ = [
    "Network",
    "NetworkConfig",
    "NetworkDhcp",
    "NetworkDhcpOutputReference",
    "NetworkDns",
    "NetworkDnsForwarders",
    "NetworkDnsForwardersList",
    "NetworkDnsForwardersOutputReference",
    "NetworkDnsHosts",
    "NetworkDnsHostsList",
    "NetworkDnsHostsOutputReference",
    "NetworkDnsOutputReference",
    "NetworkDnsSrvs",
    "NetworkDnsSrvsList",
    "NetworkDnsSrvsOutputReference",
    "NetworkDnsmasqOptions",
    "NetworkDnsmasqOptionsOptions",
    "NetworkDnsmasqOptionsOptionsList",
    "NetworkDnsmasqOptionsOptionsOutputReference",
    "NetworkDnsmasqOptionsOutputReference",
    "NetworkRoutes",
    "NetworkRoutesList",
    "NetworkRoutesOutputReference",
    "NetworkXml",
    "NetworkXmlOutputReference",
]

publication.publish()


def _typecheckingstub__c32f55c9289268193f91d86d57e5e098c0eef24a0ecf0689b3d0ae3176d44e06(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    autostart: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    bridge: typing.Optional[builtins.str] = None,
    dhcp: typing.Optional[typing.Union[NetworkDhcp, typing.Dict[builtins.str, typing.Any]]] = None,
    dns: typing.Optional[typing.Union[NetworkDns, typing.Dict[builtins.str, typing.Any]]] = None,
    dnsmasq_options: typing.Optional[typing.Union[NetworkDnsmasqOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    domain: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    mtu: typing.Optional[jsii.Number] = None,
    routes: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkRoutes, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
    xml: typing.Optional[typing.Union[NetworkXml, typing.Dict[builtins.str, typing.Any]]] = None,
    connection: typing.Optional[
        typing.Union[
            typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]],
            typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]],
        ]
    ] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[
        typing.Sequence[
            typing.Union[
                typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]],
                typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]],
                typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]],
            ]
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__feee1bbb61bdb1a603c00e6cd6370af981d2b66455133bac2615b3c71e1dcf60(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d587a6b4a8a348f4ddb46118b51bf6766c897b8dea20bc03e255978f049ca3cc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkRoutes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0f692eab7b59cc5b548231f8710836245224572cf8d0598783d2e29dec84c15a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dcd154f1f44a84add25ae111aa12d9cc7d7a54c466b628a8bd3efad12464048f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2f2066dbb85fb47f01fce1802c4b364a7fa72a61cb3bfa2470b52354485ba46b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d0303056157b7388279e7bef3e6df738f328eb9d10caad340bbc1b1a2165f361(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0b0c1251a5650d984c7418829025382ebca2f69ab7b2fd7182fde48ca0fbd65b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__01109477854f68213bbfeece378dea0ff34bc3479015fba28b2ef2a0e098b5a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1753235c092a8d3ed7be4f2a6b478634101aa2e6bd79c037e2f63a3cbe19c3f3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8d85c7231bcb2d91e17cb46ad607a9bdb0249958bec90fa569ed4b497347623a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a1be553ccc6d9d8b8109e39972de0ed79073e066872099ac5fa7fecd80f29308(
    *,
    connection: typing.Optional[
        typing.Union[
            typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]],
            typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]],
        ]
    ] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[
        typing.Sequence[
            typing.Union[
                typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]],
                typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]],
                typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]],
            ]
        ]
    ] = None,
    name: builtins.str,
    addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    autostart: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    bridge: typing.Optional[builtins.str] = None,
    dhcp: typing.Optional[typing.Union[NetworkDhcp, typing.Dict[builtins.str, typing.Any]]] = None,
    dns: typing.Optional[typing.Union[NetworkDns, typing.Dict[builtins.str, typing.Any]]] = None,
    dnsmasq_options: typing.Optional[typing.Union[NetworkDnsmasqOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    domain: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    mtu: typing.Optional[jsii.Number] = None,
    routes: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkRoutes, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
    xml: typing.Optional[typing.Union[NetworkXml, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f05a5c46191e752f273bff09496af2a3c20b9c14ae8f4111988e45098a954f66(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__58b6567a0ba24675036d978f6938a52fb3646abb7f9c39dc5a735d412b94a7d0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__35bbed0105d1720b367de0770cb5a73e6471ff6085ef6d770984e6c27b5f75f5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e7570076a74a1ae63fe565b5a1a7b7d56e3c562ef323fcfb5f0670236ba0fbd4(
    value: typing.Optional[NetworkDhcp],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7fa2b0f0a171b4424cde8bbd60f76f8103e2366f49a2dff8a4608c518e7242c7(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    forwarders: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkDnsForwarders, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
    hosts: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkDnsHosts, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
    local_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    srvs: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkDnsSrvs, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7aa75610c9ddf533080ebee1cad14f70f67562baa3efaeb0e3b2a95c2a0ed83f(
    *,
    address: typing.Optional[builtins.str] = None,
    domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__da3ca2ed266bbe294e1e5da5f25f6cf86bdff81f67f45234a41cdc6ad7b2f358(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0bceb90276f7f99db3258d7693808efa42dcc2b902c770a1e5305ff3267bcbdc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6cb94436400df302c24e2f6dcd39d3748fb9bfef2c0539ae3f9c0eda2d5f96cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f70ddfdd227bf41dd96927931f804e1c111fb460c1c00b998321510006e31024(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0f4daa4126d156576d0863bd8e0041950549b4ebd0e18e57d41184b2ff56e103(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dbfef6d0858398607b86c650dcdbcea8a2bbd1a95ed2ddc643bfac34e30bd3a1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsForwarders]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d5125c8865ebe7156fd0328136db398e1c693fd5f42c64567b0b4886782b2b8e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ce8db89fc9f2861cb6eac28f875087f67e993ca0b9cbf28c190caedfddddec01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4b49620ca65f2742096e8bb3c36f7b499d7ad71e6c77ca15ad656979c96bec1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4fe3202a2f474a1caa1c084b3bedaaa26c6b8add45abd8c969b9fd2f211a8f49(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsForwarders]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a5fdeec12143649e2d5fef7059f2c3a4835ac744b9c00175fc7c8f603daa1f83(
    *,
    hostname: typing.Optional[builtins.str] = None,
    ip: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__66e7de7a92665cb0f4e9f72e1e6a5f6d0cb97ec61790fb91a25bf29a94bb7715(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0fd449990fc12de39881af96572074551fffc3f9d2d2684c57b66975cb84dbb1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b637e966f7e439e1ab524f0826e93e4def3ac8c3944e76a0d878ad1858fc5857(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0e9fcca371d0f9653e9268fb0274033825790eb4ee8bb1ed7da50555b5dee146(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__43720657779da054e4b015c00a9d17f65dc36ea2efffab8bebeaba62734b8da5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__00425f0809eea386b5a7186b3a8b2389e81d7dcba4e135bb8dd9f2c83888cd23(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsHosts]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bc6a6a915d02af5c5d8ecd15157359b99557b62d40985f1e9f3021abd68592e1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8080f35df4abab1e3ef990f53a5a3e3c552069776558232dd9e34f56ae27930e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__186e29e89a9c8d57126135e26744b46dfb97b64ac5e5de6eb9fa06cb9dc15c95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__448f46d4b8bbe542e723edd546722fc75e551f95fffdc8ba30534ceae6213469(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsHosts]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__39a10239e74861a2734ae9ba395891aebea23b947bb4bc989f113f04ed907cc3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bcf69c91e94246f7edaa95ae3312fa79d62673d016e6d4062f239e34c0f6d6a7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkDnsForwarders, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__aa5bcffcb67da8dc3026e26bcf397d7e372dadde96015cac263a6978cacbcdb9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkDnsHosts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__94df9055229ff6fc9ee78200a76af4af30bbaaf8c507c9ee174fcc7de451ae01(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkDnsSrvs, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bcc133ce7f251a909346e50e3d12851ccce6ef320f52dd665561741521958097(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f24aae8e88839b0a05fe3cfc26237f20d3cd1d5c22c745198154577872ff8a03(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__06451162b2cbb83b2b428ef8896812383744e0da79e98d36b5d0ee7035ee7a4b(
    value: typing.Optional[NetworkDns],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__eaa574c26414436b5a874cd7a24ea7a85e0f08bb4eb18913984d1c0754522fb7(
    *,
    domain: typing.Optional[builtins.str] = None,
    port: typing.Optional[builtins.str] = None,
    priority: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    service: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
    weight: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7ce3599931d4576f245d989d75d943ef7da5104ed4390124e910888b0e356a32(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__77666b35feefdabddb932d474fb4ee161c7853e516825305f9c1a6abb1d6da40(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7e30c52b0fb164433e76c6bbba9d6a26ee87385209c0c9c47028607ad80f283d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c35934c8418e696aec1648c1835d2b7ac93fd8eb9e6d0b249dfa991f86cd296d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__915d4682e3a179992788f8c7bfcdfaa25b4e1a90d749538ba15f4e1658e5bf95(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9250c1d22bc8bd650849f127a98878ee30183fe89ff8f5305f8197689cb09f78(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsSrvs]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5727e95b2b44483bb42012e950777bb2b32479fa3faab67cd8bd37a839222c1d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8a501fb03df9f0e4b304356db01601849bebe43251f74e23dc80029b49e7f57c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b05527030daacfc52794568ad7d01eca6faa8fc582f51145e85e74b207ea16b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ec9ea2338f5c74eb47268f78973d1c0717a64ac4eb3c6f88a021113fe57f5b54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f4d9bce8c48101b8f09036c9b19d34e429320bfaf5d4dbce34ef7ca505d42b0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0fd019852401bc816e477a81f22cbd823c7f81d909c205e32bf1cd790873c230(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9111e96e7a0bf4263efed6e0f294d66fa964f5ba7c5778417fa521511d5b8689(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__921c824db456b4f8f42ad1adcdb6d674febe29d4f66971bf8bbbc4b0435952d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4dc0aa2436b605c816bc60f20538a08c91a657c32a0647c4999eadeeca142538(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsSrvs]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2e9da8045200ffa9a02bae5779d3b041bdcd73dccfe1c380e78553cbbf6a2f72(
    *,
    options: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkDnsmasqOptionsOptions, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9e3bf55d2473ebf4a7d2742a1173e2fe8df6fd862d23e5339f305de83c96a9b2(
    *,
    option_name: typing.Optional[builtins.str] = None,
    option_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cc768840202d74993817c54f360f73d1c44f77e7445d41178d7b78ab3a28e89e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__84b4946d0fb05364caf5d1a713a3a5b598fd4b8bafaed10b021d2d1c4b512323(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__80589a99390183821ab9c394983c1af974bc3ff413dc36e911cb2142d002757a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c33ba26084c4a2feea9929de24dabc2962caf6ee35d097361be980a3dc9cf002(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a0a5fcc2065d6b7b2ab5e62a1289f8ed59aac1e1aec353761cb0cab50c2f7f5d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9f3c2f51544062998f48789536205546eca06a88e2e5e599da5f6ff05a8a6e01(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkDnsmasqOptionsOptions]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0bcc95660e3f71e0989db532c0a13edbfa759ff4905233827872fa49196f39e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fb33e2c7795ca164f88bc7d9655bf88fec2a920c72aa1cf02c943a1dc1a98752(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__90bb0efedcc30d4a8eda5cf64e757ace9956b27a6140db2d5bbf802e10b8e072(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7777efc6f53be806a5e6568cc46930957489f3d16dc57ad18bc3aa693bde59a0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkDnsmasqOptionsOptions]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9b8f1212d9c387edece86bfab0807ce217e23eada1d66da953537861a4240cce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ebdacd1c62c041c2f8ad5d3eebc6d8ea8ab0f37ce4a4dce52689c5e40440703e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkDnsmasqOptionsOptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cce7696f242e0b513d183fb1a6d8480d99a19d9a307f1743b8120d72943e4556(
    value: typing.Optional[NetworkDnsmasqOptions],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5b7d09ad5e09fdc4daf3f8f8ce2c21b516cd6e18378a99198a8f4248a618698c(
    *,
    cidr: builtins.str,
    gateway: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9392e4922f83fa16c45ab22d2cd738ba7901d582a00b06a0c14ea5a86bf4f2a4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__620b1390c53c661fd637085fc98fd8b7989d8c76fdcee560249c6d42c501bcce(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a35de28d34ea58fdf6c9420f1a1eceb704d6346f6d58a9db746e406c48c679d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b26e4da8d6ff2a3bca5e12880ef51ff967605c6c45941b54665b0a795787b3e9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__88aa3f1739905ec23ddc75538a78f00d2d0299811e484f6421b2baa2faf4274c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f75d04fbc00120befb2563f19b03ffba489170d5d843aa163183a8e77b708ade(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkRoutes]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bd5798b15f2e683cee49802132f00bb3835546695b75679a283263da26cce486(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__638df04b42b36baa482819f37dd480b48b7551f075800808c719f2c958964c27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6d043728fd0564b2eac4795d74e36ae33cab9d42d2b6589a150df2b701dcdf88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1bb27cf39e89b066ff340c2c4689cf5c3765234e90d2489f94a59c545c186c66(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkRoutes]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cd905cc07396aa02d353a8f0386a0a2a4fe60b1d9405e1ccbc32c7bb811d6933(
    *,
    xslt: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b99300458eed0debdefc5fd20cf2040a84b0f782f5733534ddc7f58d9ed22917(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e6f755c50b1c0c9c26fcda668b8a99f01ca17ee329791c5f3fbd667e1f2ca096(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__aebb502d8a10d86e36d2e41638143e47048562b865a178d09ea15e83b2ea2e2c(
    value: typing.Optional[NetworkXml],
) -> None:
    """Type checking stubs"""
    pass
