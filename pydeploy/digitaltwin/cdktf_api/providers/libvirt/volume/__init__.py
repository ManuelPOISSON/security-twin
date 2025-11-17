r"""
# `libvirt_volume`

Refer to the Terraform Registry for docs: [`libvirt_volume`](https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume).
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


class Volume(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.volume.Volume",
):
    """Represents a {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume libvirt_volume}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        base_volume_id: typing.Optional[builtins.str] = None,
        base_volume_name: typing.Optional[builtins.str] = None,
        base_volume_pool: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        pool: typing.Optional[builtins.str] = None,
        size: typing.Optional[jsii.Number] = None,
        source: typing.Optional[builtins.str] = None,
        xml: typing.Optional[typing.Union["VolumeXml", typing.Dict[builtins.str, typing.Any]]] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume libvirt_volume} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#name Volume#name}.
        :param base_volume_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#base_volume_id Volume#base_volume_id}.
        :param base_volume_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#base_volume_name Volume#base_volume_name}.
        :param base_volume_pool: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#base_volume_pool Volume#base_volume_pool}.
        :param format: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#format Volume#format}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#id Volume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param pool: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#pool Volume#pool}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#size Volume#size}.
        :param source: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#source Volume#source}.
        :param xml: xml block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#xml Volume#xml}
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__984c4cbd52dbb10fc4e05b5b7f0fbf7610770ef7aaf8ec1a96bb707140a3093d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VolumeConfig(
            name=name,
            base_volume_id=base_volume_id,
            base_volume_name=base_volume_name,
            base_volume_pool=base_volume_pool,
            format=format,
            id=id,
            pool=pool,
            size=size,
            source=source,
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
        """Generates CDKTF code for importing a Volume resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Volume to import.
        :param import_from_id: The id of the existing Volume that should be imported. Refer to the {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Volume to import is found.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98d7b7606f6062f91ff8fa964b30d0cd0e2ef4e92c6f0b1210704cb8a4c5ebf0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putXml")
    def put_xml(self, *, xslt: typing.Optional[builtins.str] = None) -> None:
        """
        :param xslt: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#xslt Volume#xslt}.
        """
        value = VolumeXml(xslt=xslt)

        return typing.cast(None, jsii.invoke(self, "putXml", [value]))

    @jsii.member(jsii_name="resetBaseVolumeId")
    def reset_base_volume_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseVolumeId", []))

    @jsii.member(jsii_name="resetBaseVolumeName")
    def reset_base_volume_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseVolumeName", []))

    @jsii.member(jsii_name="resetBaseVolumePool")
    def reset_base_volume_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseVolumePool", []))

    @jsii.member(jsii_name="resetFormat")
    def reset_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormat", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPool")
    def reset_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPool", []))

    @jsii.member(jsii_name="resetSize")
    def reset_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSize", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

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
    @jsii.member(jsii_name="xml")
    def xml(self) -> "VolumeXmlOutputReference":
        return typing.cast("VolumeXmlOutputReference", jsii.get(self, "xml"))

    @builtins.property
    @jsii.member(jsii_name="baseVolumeIdInput")
    def base_volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseVolumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="baseVolumeNameInput")
    def base_volume_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseVolumeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="baseVolumePoolInput")
    def base_volume_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseVolumePoolInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="poolInput")
    def pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="xmlInput")
    def xml_input(self) -> typing.Optional["VolumeXml"]:
        return typing.cast(typing.Optional["VolumeXml"], jsii.get(self, "xmlInput"))

    @builtins.property
    @jsii.member(jsii_name="baseVolumeId")
    def base_volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseVolumeId"))

    @base_volume_id.setter
    def base_volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__649409a0192785c03ee241b3d7b88b398a7cd32624f12da4bfe78d7ac53e557d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseVolumeId", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="baseVolumeName")
    def base_volume_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseVolumeName"))

    @base_volume_name.setter
    def base_volume_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b46b2b351e7225789d5d5fe8f0c035ab3d3f55054b0b5eb5c5a8586eb21820c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseVolumeName", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="baseVolumePool")
    def base_volume_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseVolumePool"))

    @base_volume_pool.setter
    def base_volume_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9c95a1303cbd438047400942558eaded30d0fda04d65b0d5484ef0cffd312f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseVolumePool", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ceb713e8bc758102989725d49deb9c190feaabf868d534527bec6145989e2ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f4e97b985637af53293697fa89974beca4fe4ec164bf7e1508dd81145a209c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__111731325d40f813c6dc1a523a14bb2ebe28d390236f2bf802ffddb6159a39c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="pool")
    def pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pool"))

    @pool.setter
    def pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c7d5eefef386aebf7aff652c2a3ab8fe86b822db886462adee3cabd7234dcf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pool", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd534fa2e83d6972e7c4a0f9f9a957db8e2ad1cd53d568f277baefae4a93757e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d060d314872c8ac924b199f65a59501cae57047ee67629582350b7fa81bd02e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.volume.VolumeConfig",
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
        "base_volume_id": "baseVolumeId",
        "base_volume_name": "baseVolumeName",
        "base_volume_pool": "baseVolumePool",
        "format": "format",
        "id": "id",
        "pool": "pool",
        "size": "size",
        "source": "source",
        "xml": "xml",
    },
)
class VolumeConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        base_volume_id: typing.Optional[builtins.str] = None,
        base_volume_name: typing.Optional[builtins.str] = None,
        base_volume_pool: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        pool: typing.Optional[builtins.str] = None,
        size: typing.Optional[jsii.Number] = None,
        source: typing.Optional[builtins.str] = None,
        xml: typing.Optional[typing.Union["VolumeXml", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#name Volume#name}.
        :param base_volume_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#base_volume_id Volume#base_volume_id}.
        :param base_volume_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#base_volume_name Volume#base_volume_name}.
        :param base_volume_pool: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#base_volume_pool Volume#base_volume_pool}.
        :param format: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#format Volume#format}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#id Volume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param pool: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#pool Volume#pool}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#size Volume#size}.
        :param source: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#source Volume#source}.
        :param xml: xml block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#xml Volume#xml}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(xml, dict):
            xml = VolumeXml(**xml)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ae94017523922aad481ad0c3c0dc22359ec5ca5b3d1fb0b18a7a8d730adfdee)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument base_volume_id", value=base_volume_id, expected_type=type_hints["base_volume_id"])
            check_type(argname="argument base_volume_name", value=base_volume_name, expected_type=type_hints["base_volume_name"])
            check_type(argname="argument base_volume_pool", value=base_volume_pool, expected_type=type_hints["base_volume_pool"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument pool", value=pool, expected_type=type_hints["pool"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
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
        if base_volume_id is not None:
            self._values["base_volume_id"] = base_volume_id
        if base_volume_name is not None:
            self._values["base_volume_name"] = base_volume_name
        if base_volume_pool is not None:
            self._values["base_volume_pool"] = base_volume_pool
        if format is not None:
            self._values["format"] = format
        if id is not None:
            self._values["id"] = id
        if pool is not None:
            self._values["pool"] = pool
        if size is not None:
            self._values["size"] = size
        if source is not None:
            self._values["source"] = source
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#name Volume#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_volume_id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#base_volume_id Volume#base_volume_id}."""
        result = self._values.get("base_volume_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def base_volume_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#base_volume_name Volume#base_volume_name}."""
        result = self._values.get("base_volume_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def base_volume_pool(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#base_volume_pool Volume#base_volume_pool}."""
        result = self._values.get("base_volume_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def format(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#format Volume#format}."""
        result = self._values.get("format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#id Volume#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pool(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#pool Volume#pool}."""
        result = self._values.get("pool")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#size Volume#size}."""
        result = self._values.get("size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#source Volume#source}."""
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def xml(self) -> typing.Optional["VolumeXml"]:
        """xml block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#xml Volume#xml}
        """
        result = self._values.get("xml")
        return typing.cast(typing.Optional["VolumeXml"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeConfig(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


@jsii.data_type(
    jsii_type="libvirt.volume.VolumeXml",
    jsii_struct_bases=[],
    name_mapping={"xslt": "xslt"},
)
class VolumeXml:
    def __init__(self, *, xslt: typing.Optional[builtins.str] = None) -> None:
        """
        :param xslt: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#xslt Volume#xslt}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4323a5439c9ff5781acdd03676999333d55fe23d7e17cf85304acc132326571e)
            check_type(argname="argument xslt", value=xslt, expected_type=type_hints["xslt"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if xslt is not None:
            self._values["xslt"] = xslt

    @builtins.property
    def xslt(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/volume#xslt Volume#xslt}."""
        result = self._values.get("xslt")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeXml(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class VolumeXmlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.volume.VolumeXmlOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__224d7de468246ec0bc6e5528643e939248d4f249a5ad8f9cfe5565b672916a3b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__622066113653c761c6d56a7fe726fdf584afab32b54ac955486629e6ab7526ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xslt", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VolumeXml]:
        return typing.cast(typing.Optional[VolumeXml], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VolumeXml]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e698fb9297ef69b74cc8d36da8f8fdd70d1a9b89ba6166fb5876d13a0656e3df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


__all__ = [
    "Volume",
    "VolumeConfig",
    "VolumeXml",
    "VolumeXmlOutputReference",
]

publication.publish()


def _typecheckingstub__984c4cbd52dbb10fc4e05b5b7f0fbf7610770ef7aaf8ec1a96bb707140a3093d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    base_volume_id: typing.Optional[builtins.str] = None,
    base_volume_name: typing.Optional[builtins.str] = None,
    base_volume_pool: typing.Optional[builtins.str] = None,
    format: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    pool: typing.Optional[builtins.str] = None,
    size: typing.Optional[jsii.Number] = None,
    source: typing.Optional[builtins.str] = None,
    xml: typing.Optional[typing.Union[VolumeXml, typing.Dict[builtins.str, typing.Any]]] = None,
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


def _typecheckingstub__98d7b7606f6062f91ff8fa964b30d0cd0e2ef4e92c6f0b1210704cb8a4c5ebf0(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__649409a0192785c03ee241b3d7b88b398a7cd32624f12da4bfe78d7ac53e557d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8b46b2b351e7225789d5d5fe8f0c035ab3d3f55054b0b5eb5c5a8586eb21820c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e9c95a1303cbd438047400942558eaded30d0fda04d65b0d5484ef0cffd312f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2ceb713e8bc758102989725d49deb9c190feaabf868d534527bec6145989e2ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3f4e97b985637af53293697fa89974beca4fe4ec164bf7e1508dd81145a209c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__111731325d40f813c6dc1a523a14bb2ebe28d390236f2bf802ffddb6159a39c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6c7d5eefef386aebf7aff652c2a3ab8fe86b822db886462adee3cabd7234dcf1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dd534fa2e83d6972e7c4a0f9f9a957db8e2ad1cd53d568f277baefae4a93757e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7d060d314872c8ac924b199f65a59501cae57047ee67629582350b7fa81bd02e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8ae94017523922aad481ad0c3c0dc22359ec5ca5b3d1fb0b18a7a8d730adfdee(
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
    base_volume_id: typing.Optional[builtins.str] = None,
    base_volume_name: typing.Optional[builtins.str] = None,
    base_volume_pool: typing.Optional[builtins.str] = None,
    format: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    pool: typing.Optional[builtins.str] = None,
    size: typing.Optional[jsii.Number] = None,
    source: typing.Optional[builtins.str] = None,
    xml: typing.Optional[typing.Union[VolumeXml, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4323a5439c9ff5781acdd03676999333d55fe23d7e17cf85304acc132326571e(
    *,
    xslt: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__224d7de468246ec0bc6e5528643e939248d4f249a5ad8f9cfe5565b672916a3b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__622066113653c761c6d56a7fe726fdf584afab32b54ac955486629e6ab7526ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e698fb9297ef69b74cc8d36da8f8fdd70d1a9b89ba6166fb5876d13a0656e3df(
    value: typing.Optional[VolumeXml],
) -> None:
    """Type checking stubs"""
    pass
