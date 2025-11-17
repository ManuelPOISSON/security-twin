r"""
# `libvirt_pool`

Refer to the Terraform Registry for docs: [`libvirt_pool`](https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool).
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


class Pool(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.pool.Pool",
):
    """Represents a {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool libvirt_pool}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        allocation: typing.Optional[jsii.Number] = None,
        available: typing.Optional[jsii.Number] = None,
        capacity: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Union["PoolSource", typing.Dict[builtins.str, typing.Any]]] = None,
        target: typing.Optional[typing.Union["PoolTarget", typing.Dict[builtins.str, typing.Any]]] = None,
        xml: typing.Optional[typing.Union["PoolXml", typing.Dict[builtins.str, typing.Any]]] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool libvirt_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#name Pool#name}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#type Pool#type}.
        :param allocation: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#allocation Pool#allocation}.
        :param available: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#available Pool#available}.
        :param capacity: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#capacity Pool#capacity}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#id Pool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#path Pool#path}.
        :param source: source block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#source Pool#source}
        :param target: target block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#target Pool#target}
        :param xml: xml block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#xml Pool#xml}
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b53765ba6ce32ed92ee04258c32b27d85ce8771b5cdc4d5e7b5da02843902576)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PoolConfig(
            name=name,
            type=type,
            allocation=allocation,
            available=available,
            capacity=capacity,
            id=id,
            path=path,
            source=source,
            target=target,
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
        """Generates CDKTF code for importing a Pool resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Pool to import.
        :param import_from_id: The id of the existing Pool that should be imported. Refer to the {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Pool to import is found.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f43b21b5abaed92b36067df3f52c97b951012586e3d21189bb3fbb44e356b3a8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        *,
        device: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PoolSourceDevice", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param device: device block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#device Pool#device}
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#name Pool#name}.
        """
        value = PoolSource(device=device, name=name)

        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(self, *, path: typing.Optional[builtins.str] = None) -> None:
        """
        :param path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#path Pool#path}.
        """
        value = PoolTarget(path=path)

        return typing.cast(None, jsii.invoke(self, "putTarget", [value]))

    @jsii.member(jsii_name="putXml")
    def put_xml(self, *, xslt: typing.Optional[builtins.str] = None) -> None:
        """
        :param xslt: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#xslt Pool#xslt}.
        """
        value = PoolXml(xslt=xslt)

        return typing.cast(None, jsii.invoke(self, "putXml", [value]))

    @jsii.member(jsii_name="resetAllocation")
    def reset_allocation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllocation", []))

    @jsii.member(jsii_name="resetAvailable")
    def reset_available(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailable", []))

    @jsii.member(jsii_name="resetCapacity")
    def reset_capacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacity", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

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
    @jsii.member(jsii_name="source")
    def source(self) -> "PoolSourceOutputReference":
        return typing.cast("PoolSourceOutputReference", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "PoolTargetOutputReference":
        return typing.cast("PoolTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="xml")
    def xml(self) -> "PoolXmlOutputReference":
        return typing.cast("PoolXmlOutputReference", jsii.get(self, "xml"))

    @builtins.property
    @jsii.member(jsii_name="allocationInput")
    def allocation_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "allocationInput"))

    @builtins.property
    @jsii.member(jsii_name="availableInput")
    def available_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "availableInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional["PoolSource"]:
        return typing.cast(typing.Optional["PoolSource"], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional["PoolTarget"]:
        return typing.cast(typing.Optional["PoolTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="xmlInput")
    def xml_input(self) -> typing.Optional["PoolXml"]:
        return typing.cast(typing.Optional["PoolXml"], jsii.get(self, "xmlInput"))

    @builtins.property
    @jsii.member(jsii_name="allocation")
    def allocation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "allocation"))

    @allocation.setter
    def allocation(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b68e589712741b54b55bc8b46f213cce200662ef9ba0a912f5437ea72fec256c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocation", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="available")
    def available(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "available"))

    @available.setter
    def available(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1f60ea691e1b6eaafd14679a4adc3db2a1b676a3c0ed0662650b0c5ad650767)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "available", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26111de0bc99d3f07cde900d7d31989072ed901088a2ad4d80c26085a54a64b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a11259639c838b5ac0ea3c18df553d374a12e6c248b11f2e3cbf10c3303e7e85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5483d35d5ceb5b2accf9072a8ee80e87e1733556bba465823ec1328bf8ec1bb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5112647d87049befde038aa04b1609559ecfec94be8b784e8c36b00354989fd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6c4eb6a5da7eab66c0f8674fbcd70ba16d9d744c8969dab550ce045fa536696)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.pool.PoolConfig",
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
        "type": "type",
        "allocation": "allocation",
        "available": "available",
        "capacity": "capacity",
        "id": "id",
        "path": "path",
        "source": "source",
        "target": "target",
        "xml": "xml",
    },
)
class PoolConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        type: builtins.str,
        allocation: typing.Optional[jsii.Number] = None,
        available: typing.Optional[jsii.Number] = None,
        capacity: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        source: typing.Optional[typing.Union["PoolSource", typing.Dict[builtins.str, typing.Any]]] = None,
        target: typing.Optional[typing.Union["PoolTarget", typing.Dict[builtins.str, typing.Any]]] = None,
        xml: typing.Optional[typing.Union["PoolXml", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#name Pool#name}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#type Pool#type}.
        :param allocation: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#allocation Pool#allocation}.
        :param available: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#available Pool#available}.
        :param capacity: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#capacity Pool#capacity}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#id Pool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#path Pool#path}.
        :param source: source block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#source Pool#source}
        :param target: target block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#target Pool#target}
        :param xml: xml block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#xml Pool#xml}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(source, dict):
            source = PoolSource(**source)
        if isinstance(target, dict):
            target = PoolTarget(**target)
        if isinstance(xml, dict):
            xml = PoolXml(**xml)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0367ca12db51443a12b0e126f29b310c6841a6763dd013e21dba268e36a12cad)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument allocation", value=allocation, expected_type=type_hints["allocation"])
            check_type(argname="argument available", value=available, expected_type=type_hints["available"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument xml", value=xml, expected_type=type_hints["xml"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
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
        if allocation is not None:
            self._values["allocation"] = allocation
        if available is not None:
            self._values["available"] = available
        if capacity is not None:
            self._values["capacity"] = capacity
        if id is not None:
            self._values["id"] = id
        if path is not None:
            self._values["path"] = path
        if source is not None:
            self._values["source"] = source
        if target is not None:
            self._values["target"] = target
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#name Pool#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#type Pool#type}."""
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allocation(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#allocation Pool#allocation}."""
        result = self._values.get("allocation")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def available(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#available Pool#available}."""
        result = self._values.get("available")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def capacity(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#capacity Pool#capacity}."""
        result = self._values.get("capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#id Pool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#path Pool#path}."""
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional["PoolSource"]:
        """source block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#source Pool#source}
        """
        result = self._values.get("source")
        return typing.cast(typing.Optional["PoolSource"], result)

    @builtins.property
    def target(self) -> typing.Optional["PoolTarget"]:
        """target block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#target Pool#target}
        """
        result = self._values.get("target")
        return typing.cast(typing.Optional["PoolTarget"], result)

    @builtins.property
    def xml(self) -> typing.Optional["PoolXml"]:
        """xml block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#xml Pool#xml}
        """
        result = self._values.get("xml")
        return typing.cast(typing.Optional["PoolXml"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PoolConfig(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


@jsii.data_type(
    jsii_type="libvirt.pool.PoolSource",
    jsii_struct_bases=[],
    name_mapping={"device": "device", "name": "name"},
)
class PoolSource:
    def __init__(
        self,
        *,
        device: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PoolSourceDevice", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param device: device block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#device Pool#device}
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#name Pool#name}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2607ac59b4512627ebf964dcdb8670b6111fdba31a6f06fb03bd1272a7ac8af)
            check_type(argname="argument device", value=device, expected_type=type_hints["device"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if device is not None:
            self._values["device"] = device
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def device(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PoolSourceDevice"]]]:
        """device block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#device Pool#device}
        """
        result = self._values.get("device")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PoolSourceDevice"]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#name Pool#name}."""
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PoolSource(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


@jsii.data_type(
    jsii_type="libvirt.pool.PoolSourceDevice",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class PoolSourceDevice:
    def __init__(self, *, path: typing.Optional[builtins.str] = None) -> None:
        """
        :param path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#path Pool#path}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__717d868df676443a3728357add91f486242cd6587fc7aca6724e83c091a6348c)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#path Pool#path}."""
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PoolSourceDevice(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class PoolSourceDeviceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.pool.PoolSourceDeviceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a0a16d53ffea75c4414ccd17368444f9307818bae37e98e458fa37b480b2e1e9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PoolSourceDeviceOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13d8f3553dba1936d0e564c1e36b6e83f8c4e6f2503f468d3299d7ec19d001ac)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PoolSourceDeviceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8ad0705991db7d8747410bdbf0803f2c5bc99adebbd38093536dd612868c0ad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7bbc5bb5f19177b13cb8bf3f4d1c066e40f744635349ebbdaa1973358b6c1787)
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
            type_hints = typing.get_type_hints(_typecheckingstub__80dd9e4b0618b74b28a3c2437bc7cb6fa1850407fa22d78ddafe4079f65bd6cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PoolSourceDevice]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PoolSourceDevice]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PoolSourceDevice]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbbcac87b5e8638e26808840dcc76565d4f5c06d3c378bba10ab6d8bc55e4502)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class PoolSourceDeviceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.pool.PoolSourceDeviceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__14090f566ba3cb8c5d631d1b7d708644394c490d73a115108b44852aa92f69d1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec087e7d6a7486ff9b13e307b4f2695e16e03afdff43050e42ff49545c1f20c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PoolSourceDevice]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PoolSourceDevice]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PoolSourceDevice]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6700a95d10af71278e8ce56c088f12683f34e651f225ac1c23ec9a367adb0b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class PoolSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.pool.PoolSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__55efcdd8d8b66104f153f25b79a3c49cf7a556aefec1158b91aaa6717be1fc0b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDevice")
    def put_device(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PoolSourceDevice, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cdce32ea5533a154e6483ff89fef1f64971fae9b91cd82d67f026ace9b19885)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDevice", [value]))

    @jsii.member(jsii_name="resetDevice")
    def reset_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevice", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="device")
    def device(self) -> PoolSourceDeviceList:
        return typing.cast(PoolSourceDeviceList, jsii.get(self, "device"))

    @builtins.property
    @jsii.member(jsii_name="deviceInput")
    def device_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PoolSourceDevice]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PoolSourceDevice]]], jsii.get(self, "deviceInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4a2e30553b62cabf6d3a4c1cf89410407f3bd19bae6ad26e078b999b1e4bb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PoolSource]:
        return typing.cast(typing.Optional[PoolSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PoolSource]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee1549cef2fee792847c89d1b6d85039d496e52c6875b0c2d51130abee427ef4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.pool.PoolTarget",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class PoolTarget:
    def __init__(self, *, path: typing.Optional[builtins.str] = None) -> None:
        """
        :param path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#path Pool#path}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c924ea09686e5a67cc8c42095bc4dbd5463a86a75d41c38a7404b12214359a32)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#path Pool#path}."""
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PoolTarget(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class PoolTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.pool.PoolTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b6987f7f48fd73601c834051b0f59ed46dafe257b280aa7dabfc0d87664da58e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56a50b2f8f8f17875c47222fb64239f48ea1933fa2135f54428382a6959b951a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PoolTarget]:
        return typing.cast(typing.Optional[PoolTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PoolTarget]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c77c97c6aeb57bd3bf3d5ce7521612826b3c11f2491ad4395dd9e0c87475cab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.pool.PoolXml",
    jsii_struct_bases=[],
    name_mapping={"xslt": "xslt"},
)
class PoolXml:
    def __init__(self, *, xslt: typing.Optional[builtins.str] = None) -> None:
        """
        :param xslt: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#xslt Pool#xslt}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da8e5bd3cf8e553b24641c388c00fc055eb72d9b8e0c761a0ac8347af6e570c7)
            check_type(argname="argument xslt", value=xslt, expected_type=type_hints["xslt"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if xslt is not None:
            self._values["xslt"] = xslt

    @builtins.property
    def xslt(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/pool#xslt Pool#xslt}."""
        result = self._values.get("xslt")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PoolXml(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class PoolXmlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.pool.PoolXmlOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e77324cbffe31076ea6a04910cb03f5ba30486b8e69cd9fa3382b83bec3d5551)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b86030e2937189f1ddd3cd0252c84b6d2b309567a1b0d635124b46eaa274c2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xslt", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PoolXml]:
        return typing.cast(typing.Optional[PoolXml], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PoolXml]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcd0a898b70ae438b274f1501c00a00a0ae29ca7035daa59f7310a501727af15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


__all__ = [
    "Pool",
    "PoolConfig",
    "PoolSource",
    "PoolSourceDevice",
    "PoolSourceDeviceList",
    "PoolSourceDeviceOutputReference",
    "PoolSourceOutputReference",
    "PoolTarget",
    "PoolTargetOutputReference",
    "PoolXml",
    "PoolXmlOutputReference",
]

publication.publish()


def _typecheckingstub__b53765ba6ce32ed92ee04258c32b27d85ce8771b5cdc4d5e7b5da02843902576(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    allocation: typing.Optional[jsii.Number] = None,
    available: typing.Optional[jsii.Number] = None,
    capacity: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    source: typing.Optional[typing.Union[PoolSource, typing.Dict[builtins.str, typing.Any]]] = None,
    target: typing.Optional[typing.Union[PoolTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    xml: typing.Optional[typing.Union[PoolXml, typing.Dict[builtins.str, typing.Any]]] = None,
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


def _typecheckingstub__f43b21b5abaed92b36067df3f52c97b951012586e3d21189bb3fbb44e356b3a8(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b68e589712741b54b55bc8b46f213cce200662ef9ba0a912f5437ea72fec256c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d1f60ea691e1b6eaafd14679a4adc3db2a1b676a3c0ed0662650b0c5ad650767(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__26111de0bc99d3f07cde900d7d31989072ed901088a2ad4d80c26085a54a64b0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a11259639c838b5ac0ea3c18df553d374a12e6c248b11f2e3cbf10c3303e7e85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5483d35d5ceb5b2accf9072a8ee80e87e1733556bba465823ec1328bf8ec1bb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5112647d87049befde038aa04b1609559ecfec94be8b784e8c36b00354989fd4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d6c4eb6a5da7eab66c0f8674fbcd70ba16d9d744c8969dab550ce045fa536696(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0367ca12db51443a12b0e126f29b310c6841a6763dd013e21dba268e36a12cad(
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
    type: builtins.str,
    allocation: typing.Optional[jsii.Number] = None,
    available: typing.Optional[jsii.Number] = None,
    capacity: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    source: typing.Optional[typing.Union[PoolSource, typing.Dict[builtins.str, typing.Any]]] = None,
    target: typing.Optional[typing.Union[PoolTarget, typing.Dict[builtins.str, typing.Any]]] = None,
    xml: typing.Optional[typing.Union[PoolXml, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e2607ac59b4512627ebf964dcdb8670b6111fdba31a6f06fb03bd1272a7ac8af(
    *,
    device: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PoolSourceDevice, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__717d868df676443a3728357add91f486242cd6587fc7aca6724e83c091a6348c(
    *,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a0a16d53ffea75c4414ccd17368444f9307818bae37e98e458fa37b480b2e1e9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__13d8f3553dba1936d0e564c1e36b6e83f8c4e6f2503f468d3299d7ec19d001ac(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c8ad0705991db7d8747410bdbf0803f2c5bc99adebbd38093536dd612868c0ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7bbc5bb5f19177b13cb8bf3f4d1c066e40f744635349ebbdaa1973358b6c1787(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__80dd9e4b0618b74b28a3c2437bc7cb6fa1850407fa22d78ddafe4079f65bd6cc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bbbcac87b5e8638e26808840dcc76565d4f5c06d3c378bba10ab6d8bc55e4502(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PoolSourceDevice]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__14090f566ba3cb8c5d631d1b7d708644394c490d73a115108b44852aa92f69d1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ec087e7d6a7486ff9b13e307b4f2695e16e03afdff43050e42ff49545c1f20c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e6700a95d10af71278e8ce56c088f12683f34e651f225ac1c23ec9a367adb0b0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PoolSourceDevice]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__55efcdd8d8b66104f153f25b79a3c49cf7a556aefec1158b91aaa6717be1fc0b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6cdce32ea5533a154e6483ff89fef1f64971fae9b91cd82d67f026ace9b19885(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PoolSourceDevice, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7f4a2e30553b62cabf6d3a4c1cf89410407f3bd19bae6ad26e078b999b1e4bb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ee1549cef2fee792847c89d1b6d85039d496e52c6875b0c2d51130abee427ef4(
    value: typing.Optional[PoolSource],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c924ea09686e5a67cc8c42095bc4dbd5463a86a75d41c38a7404b12214359a32(
    *,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b6987f7f48fd73601c834051b0f59ed46dafe257b280aa7dabfc0d87664da58e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__56a50b2f8f8f17875c47222fb64239f48ea1933fa2135f54428382a6959b951a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1c77c97c6aeb57bd3bf3d5ce7521612826b3c11f2491ad4395dd9e0c87475cab(
    value: typing.Optional[PoolTarget],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__da8e5bd3cf8e553b24641c388c00fc055eb72d9b8e0c761a0ac8347af6e570c7(
    *,
    xslt: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e77324cbffe31076ea6a04910cb03f5ba30486b8e69cd9fa3382b83bec3d5551(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0b86030e2937189f1ddd3cd0252c84b6d2b309567a1b0d635124b46eaa274c2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bcd0a898b70ae438b274f1501c00a00a0ae29ca7035daa59f7310a501727af15(
    value: typing.Optional[PoolXml],
) -> None:
    """Type checking stubs"""
    pass
