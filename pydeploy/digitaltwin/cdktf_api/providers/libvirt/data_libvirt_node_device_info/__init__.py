r"""
# `data_libvirt_node_device_info`

Refer to the Terraform Registry for docs: [`data_libvirt_node_device_info`](https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info).
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


class DataLibvirtNodeDeviceInfo(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.dataLibvirtNodeDeviceInfo.DataLibvirtNodeDeviceInfo",
):
    """Represents a {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info libvirt_node_device_info}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        capability: typing.Optional[typing.Union["DataLibvirtNodeDeviceInfoCapability", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info libvirt_node_device_info} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#name DataLibvirtNodeDeviceInfo#name}.
        :param capability: capability block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#capability DataLibvirtNodeDeviceInfo#capability}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#id DataLibvirtNodeDeviceInfo#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ac9662e67bae5f2d90b1ac5dd6d5a6363bbed51398f3203d968706934f83dfc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataLibvirtNodeDeviceInfoConfig(
            name=name,
            capability=capability,
            id=id,
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
        """Generates CDKTF code for importing a DataLibvirtNodeDeviceInfo resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataLibvirtNodeDeviceInfo to import.
        :param import_from_id: The id of the existing DataLibvirtNodeDeviceInfo that should be imported. Refer to the {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataLibvirtNodeDeviceInfo to import is found.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__999ad5b0c42a1cb55e8f1bb3c1c6a893066801705441845144d4f539dae6aa84)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putCapability")
    def put_capability(
        self,
        *,
        address: typing.Optional[builtins.str] = None,
        block: typing.Optional[builtins.str] = None,
        bus: typing.Optional[builtins.str] = None,
        capability: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        class_: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        device: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        drive_type: typing.Optional[builtins.str] = None,
        drm_type: typing.Optional[builtins.str] = None,
        features: typing.Optional[typing.Sequence[builtins.str]] = None,
        firmware: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        function: typing.Optional[builtins.str] = None,
        hardware: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        host: typing.Optional[builtins.str] = None,
        interface: typing.Optional[builtins.str] = None,
        iommu_group: typing.Optional[typing.Union["DataLibvirtNodeDeviceInfoCapabilityIommuGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        link: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        logical_block_size: typing.Optional[builtins.str] = None,
        lun: typing.Optional[builtins.str] = None,
        model: typing.Optional[builtins.str] = None,
        number: typing.Optional[builtins.str] = None,
        num_blocks: typing.Optional[builtins.str] = None,
        product: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        protocol: typing.Optional[builtins.str] = None,
        scsi_type: typing.Optional[builtins.str] = None,
        serial: typing.Optional[builtins.str] = None,
        size: typing.Optional[builtins.str] = None,
        slot: typing.Optional[builtins.str] = None,
        subclass: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        unique_id: typing.Optional[builtins.str] = None,
        vendor: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        """
        :param address: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#address DataLibvirtNodeDeviceInfo#address}.
        :param block: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#block DataLibvirtNodeDeviceInfo#block}.
        :param bus: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#bus DataLibvirtNodeDeviceInfo#bus}.
        :param capability: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#capability DataLibvirtNodeDeviceInfo#capability}.
        :param class_: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#class DataLibvirtNodeDeviceInfo#class}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#description DataLibvirtNodeDeviceInfo#description}.
        :param device: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#device DataLibvirtNodeDeviceInfo#device}.
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#domain DataLibvirtNodeDeviceInfo#domain}.
        :param drive_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#drive_type DataLibvirtNodeDeviceInfo#drive_type}.
        :param drm_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#drm_type DataLibvirtNodeDeviceInfo#drm_type}.
        :param features: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#features DataLibvirtNodeDeviceInfo#features}.
        :param firmware: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#firmware DataLibvirtNodeDeviceInfo#firmware}.
        :param function: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#function DataLibvirtNodeDeviceInfo#function}.
        :param hardware: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#hardware DataLibvirtNodeDeviceInfo#hardware}.
        :param host: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#host DataLibvirtNodeDeviceInfo#host}.
        :param interface: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#interface DataLibvirtNodeDeviceInfo#interface}.
        :param iommu_group: iommu_group block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#iommu_group DataLibvirtNodeDeviceInfo#iommu_group}
        :param link: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#link DataLibvirtNodeDeviceInfo#link}.
        :param logical_block_size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#logical_block_size DataLibvirtNodeDeviceInfo#logical_block_size}.
        :param lun: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#lun DataLibvirtNodeDeviceInfo#lun}.
        :param model: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#model DataLibvirtNodeDeviceInfo#model}.
        :param number: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#number DataLibvirtNodeDeviceInfo#number}.
        :param num_blocks: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#num_blocks DataLibvirtNodeDeviceInfo#num_blocks}.
        :param product: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#product DataLibvirtNodeDeviceInfo#product}.
        :param protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#protocol DataLibvirtNodeDeviceInfo#protocol}.
        :param scsi_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#scsi_type DataLibvirtNodeDeviceInfo#scsi_type}.
        :param serial: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#serial DataLibvirtNodeDeviceInfo#serial}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#size DataLibvirtNodeDeviceInfo#size}.
        :param slot: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#slot DataLibvirtNodeDeviceInfo#slot}.
        :param subclass: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#subclass DataLibvirtNodeDeviceInfo#subclass}.
        :param target: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#target DataLibvirtNodeDeviceInfo#target}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#type DataLibvirtNodeDeviceInfo#type}.
        :param unique_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#unique_id DataLibvirtNodeDeviceInfo#unique_id}.
        :param vendor: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#vendor DataLibvirtNodeDeviceInfo#vendor}.
        """
        value = DataLibvirtNodeDeviceInfoCapability(
            address=address,
            block=block,
            bus=bus,
            capability=capability,
            class_=class_,
            description=description,
            device=device,
            domain=domain,
            drive_type=drive_type,
            drm_type=drm_type,
            features=features,
            firmware=firmware,
            function=function,
            hardware=hardware,
            host=host,
            interface=interface,
            iommu_group=iommu_group,
            link=link,
            logical_block_size=logical_block_size,
            lun=lun,
            model=model,
            number=number,
            num_blocks=num_blocks,
            product=product,
            protocol=protocol,
            scsi_type=scsi_type,
            serial=serial,
            size=size,
            slot=slot,
            subclass=subclass,
            target=target,
            type=type,
            unique_id=unique_id,
            vendor=vendor,
        )

        return typing.cast(None, jsii.invoke(self, "putCapability", [value]))

    @jsii.member(jsii_name="resetCapability")
    def reset_capability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapability", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="capability")
    def capability(self) -> "DataLibvirtNodeDeviceInfoCapabilityOutputReference":
        return typing.cast("DataLibvirtNodeDeviceInfoCapabilityOutputReference", jsii.get(self, "capability"))

    @builtins.property
    @jsii.member(jsii_name="devnode")
    def devnode(self) -> "DataLibvirtNodeDeviceInfoDevnodeList":
        return typing.cast("DataLibvirtNodeDeviceInfoDevnodeList", jsii.get(self, "devnode"))

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="xml")
    def xml(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "xml"))

    @builtins.property
    @jsii.member(jsii_name="capabilityInput")
    def capability_input(
        self,
    ) -> typing.Optional["DataLibvirtNodeDeviceInfoCapability"]:
        return typing.cast(typing.Optional["DataLibvirtNodeDeviceInfoCapability"], jsii.get(self, "capabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e703c96134b435c0e6797ea48796183dced723cc4bf81f499dac68f8135c4523)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11bdaea52e2376c15b62e9593ecde5bce64a7e51d8296bd09f20e120ad97afde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.dataLibvirtNodeDeviceInfo.DataLibvirtNodeDeviceInfoCapability",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "block": "block",
        "bus": "bus",
        "capability": "capability",
        "class_": "class",
        "description": "description",
        "device": "device",
        "domain": "domain",
        "drive_type": "driveType",
        "drm_type": "drmType",
        "features": "features",
        "firmware": "firmware",
        "function": "function",
        "hardware": "hardware",
        "host": "host",
        "interface": "interface",
        "iommu_group": "iommuGroup",
        "link": "link",
        "logical_block_size": "logicalBlockSize",
        "lun": "lun",
        "model": "model",
        "number": "number",
        "num_blocks": "numBlocks",
        "product": "product",
        "protocol": "protocol",
        "scsi_type": "scsiType",
        "serial": "serial",
        "size": "size",
        "slot": "slot",
        "subclass": "subclass",
        "target": "target",
        "type": "type",
        "unique_id": "uniqueId",
        "vendor": "vendor",
    },
)
class DataLibvirtNodeDeviceInfoCapability:
    def __init__(
        self,
        *,
        address: typing.Optional[builtins.str] = None,
        block: typing.Optional[builtins.str] = None,
        bus: typing.Optional[builtins.str] = None,
        capability: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        class_: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        device: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        drive_type: typing.Optional[builtins.str] = None,
        drm_type: typing.Optional[builtins.str] = None,
        features: typing.Optional[typing.Sequence[builtins.str]] = None,
        firmware: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        function: typing.Optional[builtins.str] = None,
        hardware: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        host: typing.Optional[builtins.str] = None,
        interface: typing.Optional[builtins.str] = None,
        iommu_group: typing.Optional[typing.Union["DataLibvirtNodeDeviceInfoCapabilityIommuGroup", typing.Dict[builtins.str, typing.Any]]] = None,
        link: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        logical_block_size: typing.Optional[builtins.str] = None,
        lun: typing.Optional[builtins.str] = None,
        model: typing.Optional[builtins.str] = None,
        number: typing.Optional[builtins.str] = None,
        num_blocks: typing.Optional[builtins.str] = None,
        product: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        protocol: typing.Optional[builtins.str] = None,
        scsi_type: typing.Optional[builtins.str] = None,
        serial: typing.Optional[builtins.str] = None,
        size: typing.Optional[builtins.str] = None,
        slot: typing.Optional[builtins.str] = None,
        subclass: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        unique_id: typing.Optional[builtins.str] = None,
        vendor: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        """
        :param address: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#address DataLibvirtNodeDeviceInfo#address}.
        :param block: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#block DataLibvirtNodeDeviceInfo#block}.
        :param bus: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#bus DataLibvirtNodeDeviceInfo#bus}.
        :param capability: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#capability DataLibvirtNodeDeviceInfo#capability}.
        :param class_: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#class DataLibvirtNodeDeviceInfo#class}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#description DataLibvirtNodeDeviceInfo#description}.
        :param device: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#device DataLibvirtNodeDeviceInfo#device}.
        :param domain: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#domain DataLibvirtNodeDeviceInfo#domain}.
        :param drive_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#drive_type DataLibvirtNodeDeviceInfo#drive_type}.
        :param drm_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#drm_type DataLibvirtNodeDeviceInfo#drm_type}.
        :param features: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#features DataLibvirtNodeDeviceInfo#features}.
        :param firmware: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#firmware DataLibvirtNodeDeviceInfo#firmware}.
        :param function: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#function DataLibvirtNodeDeviceInfo#function}.
        :param hardware: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#hardware DataLibvirtNodeDeviceInfo#hardware}.
        :param host: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#host DataLibvirtNodeDeviceInfo#host}.
        :param interface: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#interface DataLibvirtNodeDeviceInfo#interface}.
        :param iommu_group: iommu_group block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#iommu_group DataLibvirtNodeDeviceInfo#iommu_group}
        :param link: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#link DataLibvirtNodeDeviceInfo#link}.
        :param logical_block_size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#logical_block_size DataLibvirtNodeDeviceInfo#logical_block_size}.
        :param lun: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#lun DataLibvirtNodeDeviceInfo#lun}.
        :param model: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#model DataLibvirtNodeDeviceInfo#model}.
        :param number: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#number DataLibvirtNodeDeviceInfo#number}.
        :param num_blocks: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#num_blocks DataLibvirtNodeDeviceInfo#num_blocks}.
        :param product: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#product DataLibvirtNodeDeviceInfo#product}.
        :param protocol: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#protocol DataLibvirtNodeDeviceInfo#protocol}.
        :param scsi_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#scsi_type DataLibvirtNodeDeviceInfo#scsi_type}.
        :param serial: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#serial DataLibvirtNodeDeviceInfo#serial}.
        :param size: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#size DataLibvirtNodeDeviceInfo#size}.
        :param slot: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#slot DataLibvirtNodeDeviceInfo#slot}.
        :param subclass: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#subclass DataLibvirtNodeDeviceInfo#subclass}.
        :param target: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#target DataLibvirtNodeDeviceInfo#target}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#type DataLibvirtNodeDeviceInfo#type}.
        :param unique_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#unique_id DataLibvirtNodeDeviceInfo#unique_id}.
        :param vendor: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#vendor DataLibvirtNodeDeviceInfo#vendor}.
        """
        if isinstance(iommu_group, dict):
            iommu_group = DataLibvirtNodeDeviceInfoCapabilityIommuGroup(**iommu_group)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32de968585e941ab2fed142ead422c4efe0499800e1e7b822913848fb525dae0)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument block", value=block, expected_type=type_hints["block"])
            check_type(argname="argument bus", value=bus, expected_type=type_hints["bus"])
            check_type(argname="argument capability", value=capability, expected_type=type_hints["capability"])
            check_type(argname="argument class_", value=class_, expected_type=type_hints["class_"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument device", value=device, expected_type=type_hints["device"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument drive_type", value=drive_type, expected_type=type_hints["drive_type"])
            check_type(argname="argument drm_type", value=drm_type, expected_type=type_hints["drm_type"])
            check_type(argname="argument features", value=features, expected_type=type_hints["features"])
            check_type(argname="argument firmware", value=firmware, expected_type=type_hints["firmware"])
            check_type(argname="argument function", value=function, expected_type=type_hints["function"])
            check_type(argname="argument hardware", value=hardware, expected_type=type_hints["hardware"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument interface", value=interface, expected_type=type_hints["interface"])
            check_type(argname="argument iommu_group", value=iommu_group, expected_type=type_hints["iommu_group"])
            check_type(argname="argument link", value=link, expected_type=type_hints["link"])
            check_type(argname="argument logical_block_size", value=logical_block_size, expected_type=type_hints["logical_block_size"])
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument model", value=model, expected_type=type_hints["model"])
            check_type(argname="argument number", value=number, expected_type=type_hints["number"])
            check_type(argname="argument num_blocks", value=num_blocks, expected_type=type_hints["num_blocks"])
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument scsi_type", value=scsi_type, expected_type=type_hints["scsi_type"])
            check_type(argname="argument serial", value=serial, expected_type=type_hints["serial"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument slot", value=slot, expected_type=type_hints["slot"])
            check_type(argname="argument subclass", value=subclass, expected_type=type_hints["subclass"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument unique_id", value=unique_id, expected_type=type_hints["unique_id"])
            check_type(argname="argument vendor", value=vendor, expected_type=type_hints["vendor"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if address is not None:
            self._values["address"] = address
        if block is not None:
            self._values["block"] = block
        if bus is not None:
            self._values["bus"] = bus
        if capability is not None:
            self._values["capability"] = capability
        if class_ is not None:
            self._values["class_"] = class_
        if description is not None:
            self._values["description"] = description
        if device is not None:
            self._values["device"] = device
        if domain is not None:
            self._values["domain"] = domain
        if drive_type is not None:
            self._values["drive_type"] = drive_type
        if drm_type is not None:
            self._values["drm_type"] = drm_type
        if features is not None:
            self._values["features"] = features
        if firmware is not None:
            self._values["firmware"] = firmware
        if function is not None:
            self._values["function"] = function
        if hardware is not None:
            self._values["hardware"] = hardware
        if host is not None:
            self._values["host"] = host
        if interface is not None:
            self._values["interface"] = interface
        if iommu_group is not None:
            self._values["iommu_group"] = iommu_group
        if link is not None:
            self._values["link"] = link
        if logical_block_size is not None:
            self._values["logical_block_size"] = logical_block_size
        if lun is not None:
            self._values["lun"] = lun
        if model is not None:
            self._values["model"] = model
        if number is not None:
            self._values["number"] = number
        if num_blocks is not None:
            self._values["num_blocks"] = num_blocks
        if product is not None:
            self._values["product"] = product
        if protocol is not None:
            self._values["protocol"] = protocol
        if scsi_type is not None:
            self._values["scsi_type"] = scsi_type
        if serial is not None:
            self._values["serial"] = serial
        if size is not None:
            self._values["size"] = size
        if slot is not None:
            self._values["slot"] = slot
        if subclass is not None:
            self._values["subclass"] = subclass
        if target is not None:
            self._values["target"] = target
        if type is not None:
            self._values["type"] = type
        if unique_id is not None:
            self._values["unique_id"] = unique_id
        if vendor is not None:
            self._values["vendor"] = vendor

    @builtins.property
    def address(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#address DataLibvirtNodeDeviceInfo#address}."""
        result = self._values.get("address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def block(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#block DataLibvirtNodeDeviceInfo#block}."""
        result = self._values.get("block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bus(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#bus DataLibvirtNodeDeviceInfo#bus}."""
        result = self._values.get("bus")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capability(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#capability DataLibvirtNodeDeviceInfo#capability}."""
        result = self._values.get("capability")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def class_(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#class DataLibvirtNodeDeviceInfo#class}."""
        result = self._values.get("class_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#description DataLibvirtNodeDeviceInfo#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#device DataLibvirtNodeDeviceInfo#device}."""
        result = self._values.get("device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#domain DataLibvirtNodeDeviceInfo#domain}."""
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def drive_type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#drive_type DataLibvirtNodeDeviceInfo#drive_type}."""
        result = self._values.get("drive_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def drm_type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#drm_type DataLibvirtNodeDeviceInfo#drm_type}."""
        result = self._values.get("drm_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def features(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#features DataLibvirtNodeDeviceInfo#features}."""
        result = self._values.get("features")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def firmware(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#firmware DataLibvirtNodeDeviceInfo#firmware}."""
        result = self._values.get("firmware")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def function(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#function DataLibvirtNodeDeviceInfo#function}."""
        result = self._values.get("function")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hardware(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#hardware DataLibvirtNodeDeviceInfo#hardware}."""
        result = self._values.get("hardware")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#host DataLibvirtNodeDeviceInfo#host}."""
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interface(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#interface DataLibvirtNodeDeviceInfo#interface}."""
        result = self._values.get("interface")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iommu_group(
        self,
    ) -> typing.Optional["DataLibvirtNodeDeviceInfoCapabilityIommuGroup"]:
        """iommu_group block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#iommu_group DataLibvirtNodeDeviceInfo#iommu_group}
        """
        result = self._values.get("iommu_group")
        return typing.cast(typing.Optional["DataLibvirtNodeDeviceInfoCapabilityIommuGroup"], result)

    @builtins.property
    def link(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#link DataLibvirtNodeDeviceInfo#link}."""
        result = self._values.get("link")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def logical_block_size(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#logical_block_size DataLibvirtNodeDeviceInfo#logical_block_size}."""
        result = self._values.get("logical_block_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lun(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#lun DataLibvirtNodeDeviceInfo#lun}."""
        result = self._values.get("lun")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#model DataLibvirtNodeDeviceInfo#model}."""
        result = self._values.get("model")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def number(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#number DataLibvirtNodeDeviceInfo#number}."""
        result = self._values.get("number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_blocks(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#num_blocks DataLibvirtNodeDeviceInfo#num_blocks}."""
        result = self._values.get("num_blocks")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def product(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#product DataLibvirtNodeDeviceInfo#product}."""
        result = self._values.get("product")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#protocol DataLibvirtNodeDeviceInfo#protocol}."""
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scsi_type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#scsi_type DataLibvirtNodeDeviceInfo#scsi_type}."""
        result = self._values.get("scsi_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def serial(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#serial DataLibvirtNodeDeviceInfo#serial}."""
        result = self._values.get("serial")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#size DataLibvirtNodeDeviceInfo#size}."""
        result = self._values.get("size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slot(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#slot DataLibvirtNodeDeviceInfo#slot}."""
        result = self._values.get("slot")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subclass(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#subclass DataLibvirtNodeDeviceInfo#subclass}."""
        result = self._values.get("subclass")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#target DataLibvirtNodeDeviceInfo#target}."""
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#type DataLibvirtNodeDeviceInfo#type}."""
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unique_id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#unique_id DataLibvirtNodeDeviceInfo#unique_id}."""
        result = self._values.get("unique_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vendor(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#vendor DataLibvirtNodeDeviceInfo#vendor}."""
        result = self._values.get("vendor")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLibvirtNodeDeviceInfoCapability(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


@jsii.data_type(
    jsii_type="libvirt.dataLibvirtNodeDeviceInfo.DataLibvirtNodeDeviceInfoCapabilityIommuGroup",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataLibvirtNodeDeviceInfoCapabilityIommuGroup:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLibvirtNodeDeviceInfoCapabilityIommuGroup(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DataLibvirtNodeDeviceInfoCapabilityIommuGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.dataLibvirtNodeDeviceInfo.DataLibvirtNodeDeviceInfoCapabilityIommuGroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a1b159ec7790466557ee1ec71fd5d606feb86210d07e6d51f042378ed1bf7b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="addresses")
    def addresses(self) -> _cdktf_9a9027ec.StringMapList:
        return typing.cast(_cdktf_9a9027ec.StringMapList, jsii.get(self, "addresses"))

    @builtins.property
    @jsii.member(jsii_name="number")
    def number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "number"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataLibvirtNodeDeviceInfoCapabilityIommuGroup]:
        return typing.cast(typing.Optional[DataLibvirtNodeDeviceInfoCapabilityIommuGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataLibvirtNodeDeviceInfoCapabilityIommuGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dcb00ee24397b46fc85e5d8bc35cf8358cf5670258987173bc32ebc8b8c5541)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class DataLibvirtNodeDeviceInfoCapabilityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.dataLibvirtNodeDeviceInfo.DataLibvirtNodeDeviceInfoCapabilityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__11c279a53d005b0b17795859bfc8820ede72709dac01e74da6c0ecd6cd84d6f7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIommuGroup")
    def put_iommu_group(self) -> None:
        value = DataLibvirtNodeDeviceInfoCapabilityIommuGroup()

        return typing.cast(None, jsii.invoke(self, "putIommuGroup", [value]))

    @jsii.member(jsii_name="resetAddress")
    def reset_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddress", []))

    @jsii.member(jsii_name="resetBlock")
    def reset_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlock", []))

    @jsii.member(jsii_name="resetBus")
    def reset_bus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBus", []))

    @jsii.member(jsii_name="resetCapability")
    def reset_capability(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapability", []))

    @jsii.member(jsii_name="resetClass")
    def reset_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClass", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDevice")
    def reset_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevice", []))

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetDriveType")
    def reset_drive_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriveType", []))

    @jsii.member(jsii_name="resetDrmType")
    def reset_drm_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDrmType", []))

    @jsii.member(jsii_name="resetFeatures")
    def reset_features(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFeatures", []))

    @jsii.member(jsii_name="resetFirmware")
    def reset_firmware(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirmware", []))

    @jsii.member(jsii_name="resetFunction")
    def reset_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunction", []))

    @jsii.member(jsii_name="resetHardware")
    def reset_hardware(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHardware", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetInterface")
    def reset_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterface", []))

    @jsii.member(jsii_name="resetIommuGroup")
    def reset_iommu_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIommuGroup", []))

    @jsii.member(jsii_name="resetLink")
    def reset_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLink", []))

    @jsii.member(jsii_name="resetLogicalBlockSize")
    def reset_logical_block_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogicalBlockSize", []))

    @jsii.member(jsii_name="resetLun")
    def reset_lun(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLun", []))

    @jsii.member(jsii_name="resetModel")
    def reset_model(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModel", []))

    @jsii.member(jsii_name="resetNumber")
    def reset_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumber", []))

    @jsii.member(jsii_name="resetNumBlocks")
    def reset_num_blocks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumBlocks", []))

    @jsii.member(jsii_name="resetProduct")
    def reset_product(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProduct", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetScsiType")
    def reset_scsi_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScsiType", []))

    @jsii.member(jsii_name="resetSerial")
    def reset_serial(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSerial", []))

    @jsii.member(jsii_name="resetSize")
    def reset_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSize", []))

    @jsii.member(jsii_name="resetSlot")
    def reset_slot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlot", []))

    @jsii.member(jsii_name="resetSubclass")
    def reset_subclass(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubclass", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetUniqueId")
    def reset_unique_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUniqueId", []))

    @jsii.member(jsii_name="resetVendor")
    def reset_vendor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVendor", []))

    @builtins.property
    @jsii.member(jsii_name="iommuGroup")
    def iommu_group(
        self,
    ) -> DataLibvirtNodeDeviceInfoCapabilityIommuGroupOutputReference:
        return typing.cast(DataLibvirtNodeDeviceInfoCapabilityIommuGroupOutputReference, jsii.get(self, "iommuGroup"))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="blockInput")
    def block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blockInput"))

    @builtins.property
    @jsii.member(jsii_name="busInput")
    def bus_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "busInput"))

    @builtins.property
    @jsii.member(jsii_name="capabilityInput")
    def capability_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "capabilityInput"))

    @builtins.property
    @jsii.member(jsii_name="classInput")
    def class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "classInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceInput")
    def device_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="driveTypeInput")
    def drive_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driveTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="drmTypeInput")
    def drm_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "drmTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="featuresInput")
    def features_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "featuresInput"))

    @builtins.property
    @jsii.member(jsii_name="firmwareInput")
    def firmware_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "firmwareInput"))

    @builtins.property
    @jsii.member(jsii_name="functionInput")
    def function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionInput"))

    @builtins.property
    @jsii.member(jsii_name="hardwareInput")
    def hardware_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "hardwareInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="interfaceInput")
    def interface_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="iommuGroupInput")
    def iommu_group_input(
        self,
    ) -> typing.Optional[DataLibvirtNodeDeviceInfoCapabilityIommuGroup]:
        return typing.cast(typing.Optional[DataLibvirtNodeDeviceInfoCapabilityIommuGroup], jsii.get(self, "iommuGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="linkInput")
    def link_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "linkInput"))

    @builtins.property
    @jsii.member(jsii_name="logicalBlockSizeInput")
    def logical_block_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logicalBlockSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="modelInput")
    def model_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelInput"))

    @builtins.property
    @jsii.member(jsii_name="numberInput")
    def number_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "numberInput"))

    @builtins.property
    @jsii.member(jsii_name="numBlocksInput")
    def num_blocks_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "numBlocksInput"))

    @builtins.property
    @jsii.member(jsii_name="productInput")
    def product_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "productInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="scsiTypeInput")
    def scsi_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scsiTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="serialInput")
    def serial_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serialInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="slotInput")
    def slot_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slotInput"))

    @builtins.property
    @jsii.member(jsii_name="subclassInput")
    def subclass_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subclassInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="uniqueIdInput")
    def unique_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uniqueIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vendorInput")
    def vendor_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "vendorInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06436215e02e95b6a9603f9f5c205fc0ae3f4364cf31a05a458707f3c02536df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="block")
    def block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "block"))

    @block.setter
    def block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb476705c849e9974fa486a35aa507cd70929997e8f749ef5af06fa6080e87f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "block", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="bus")
    def bus(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bus"))

    @bus.setter
    def bus(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4e8c9534ab1e5bc7439bbf43d2d705fc056ffbb74770959601fa26df8ec540e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bus", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="capability")
    def capability(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "capability"))

    @capability.setter
    def capability(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3879119d64d52e35b51329ebfc0655b442099b1c22ceb0b46149c38d924819df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capability", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="class")
    def class_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "class"))

    @class_.setter
    def class_(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8cc2e9cc9180d19afaa58388607e34b7893d733e0c51d95164d2a3e07c24592)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "class", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8532112530d10ee2ec1e63230816c424a1a744b3478bb077f63a91fa5005bae4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="device")
    def device(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "device"))

    @device.setter
    def device(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1338f68d76ff4a340c2f797a8892d3f531934367e41009c720fdfa36b81eebcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "device", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1ab9b0a65b80db268283046b0895b28d5a355edca58345bb39d7a3f2745cdf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="driveType")
    def drive_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driveType"))

    @drive_type.setter
    def drive_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af80a6ebc5e9156093d8c3005f4679c6b63df01a6f24a11f47e96c7d0282d716)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driveType", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="drmType")
    def drm_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "drmType"))

    @drm_type.setter
    def drm_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0d61110aa0fc622ac3eef6416ece427c593f509032b345d69e1e03dbdaa12d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "drmType", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="features")
    def features(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "features"))

    @features.setter
    def features(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__671a0fb0ce0e5d32eafa3aee2df328676ba752c0121cd0c9d76e0f8d1e75554f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "features", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="firmware")
    def firmware(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "firmware"))

    @firmware.setter
    def firmware(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__011f6187364ed326f6fe7af4880779d32240c22deded4a540e97db2c995a7b67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firmware", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="function")
    def function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "function"))

    @function.setter
    def function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a784589f7701003c0d4c3fadab0393016e4ac4dfd4df485d8460fb4b59a41c74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "function", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hardware")
    def hardware(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "hardware"))

    @hardware.setter
    def hardware(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46e9faf684c9f8eed5425c35be8865d063fa0fde85eb4cd0ca3ca06c95938f8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hardware", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4030b5c5b3b81a55d6357a364ed827f8fb6612e352675b57a5e93db63b2fe359)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="interface")
    def interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interface"))

    @interface.setter
    def interface(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ede4ea9a2ef8599bbae95de2cc744290d79b47cee1a03e8e7627452f041532c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interface", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="link")
    def link(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "link"))

    @link.setter
    def link(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c0d08caa27af6b57515c4daa51cc36d1d15ba7163bc7688c0071f0cae748c1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "link", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logicalBlockSize")
    def logical_block_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logicalBlockSize"))

    @logical_block_size.setter
    def logical_block_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__421acc334b595cb36ff0353f2da655e0de05461c65889a70a77aa1bc132fd4ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logicalBlockSize", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9012d1fb02944551f5edc911b149be4a58033c8c5380affb6c29cb649946dae6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="model")
    def model(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "model"))

    @model.setter
    def model(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f056396ad9bf2d54156f9a3d0732898c72a1b7c87ff1bfa398b31fe75107a259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "model", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="number")
    def number(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "number"))

    @number.setter
    def number(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37df24c49c0885b9588ee47b414320ed0ba73809112313d05e34437a2259e5ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "number", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="numBlocks")
    def num_blocks(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "numBlocks"))

    @num_blocks.setter
    def num_blocks(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6b70660dbdaae564781ecdd9daf432c506e781112b3b5622fde874d178fb9a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numBlocks", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "product"))

    @product.setter
    def product(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b586f00e724c86f162b8e65d23b121fbe4a9bcc3528e7751f5e4c5da72b2d69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a02f11477245cd919bd6fc3ff6b07bc7bf59d011b81c3fe3911b4364d0d2d523)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scsiType")
    def scsi_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scsiType"))

    @scsi_type.setter
    def scsi_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63b14058cd110e8375296ebb21bc7c282c526316e1b342e9e4f70c6afe3821a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scsiType", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serial")
    def serial(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serial"))

    @serial.setter
    def serial(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__673bc8faef1b101ef89043d9a943a38735cc22493292fcdd68a57a54bf00b975)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serial", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07a0ff952b443c3e87ceaa75156bd5f300e79960682c3910c3a29b9ba8801ca4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="slot")
    def slot(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slot"))

    @slot.setter
    def slot(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8009d529aed639dbce444d244b3f8c13be9c3febce1109d4feceb17935b375d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slot", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subclass")
    def subclass(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subclass"))

    @subclass.setter
    def subclass(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b04dd98b8e5a576599ff6e01c5f3003b08e7099e99090bd980b39b3e0548208f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subclass", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cde032d3d0d3cdcc7cbfafe6de165a1da6559e312e8bca9530bd1fec9a7b501)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7258542532358f67cdb1bde3545b2d5dce50ef5436d9b466ef66a1cf6ce55df4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="uniqueId")
    def unique_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uniqueId"))

    @unique_id.setter
    def unique_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b19d3f855149c5a006e516601c1c807f9ee12d4c7e67b497e52bb116cbbf069f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uniqueId", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vendor")
    def vendor(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "vendor"))

    @vendor.setter
    def vendor(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__079ed5d6a7b4e6d7c3f6ceecd0f3a1d13b901ec98f24d97284ce928608b9a994)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vendor", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataLibvirtNodeDeviceInfoCapability]:
        return typing.cast(typing.Optional[DataLibvirtNodeDeviceInfoCapability], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataLibvirtNodeDeviceInfoCapability],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bf218f75a8c8ab8743a328fd61f4c49b907cdc007887c8d79a5c8fb144194c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.dataLibvirtNodeDeviceInfo.DataLibvirtNodeDeviceInfoConfig",
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
        "capability": "capability",
        "id": "id",
    },
)
class DataLibvirtNodeDeviceInfoConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        capability: typing.Optional[typing.Union[DataLibvirtNodeDeviceInfoCapability, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#name DataLibvirtNodeDeviceInfo#name}.
        :param capability: capability block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#capability DataLibvirtNodeDeviceInfo#capability}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#id DataLibvirtNodeDeviceInfo#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(capability, dict):
            capability = DataLibvirtNodeDeviceInfoCapability(**capability)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__559e471ec0a46d22e4e5bb4d84fe2bc4e09f0629a6f095e2dba377bd74a12bd7)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument capability", value=capability, expected_type=type_hints["capability"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
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
        if capability is not None:
            self._values["capability"] = capability
        if id is not None:
            self._values["id"] = id

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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#name DataLibvirtNodeDeviceInfo#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capability(self) -> typing.Optional[DataLibvirtNodeDeviceInfoCapability]:
        """capability block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#capability DataLibvirtNodeDeviceInfo#capability}
        """
        result = self._values.get("capability")
        return typing.cast(typing.Optional[DataLibvirtNodeDeviceInfoCapability], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/data-sources/node_device_info#id DataLibvirtNodeDeviceInfo#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLibvirtNodeDeviceInfoConfig(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


@jsii.data_type(
    jsii_type="libvirt.dataLibvirtNodeDeviceInfo.DataLibvirtNodeDeviceInfoDevnode",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataLibvirtNodeDeviceInfoDevnode:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLibvirtNodeDeviceInfoDevnode(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DataLibvirtNodeDeviceInfoDevnodeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.dataLibvirtNodeDeviceInfo.DataLibvirtNodeDeviceInfoDevnodeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3117b6a8958442a8288502aae971156ff5d4375901a16b243028034a5a950632)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataLibvirtNodeDeviceInfoDevnodeOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d557a4cd28d4c3c341ddd0034e8ef60f88d7897b7bd87c68703e9f155cfe0ad9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataLibvirtNodeDeviceInfoDevnodeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__870e0bfd444e185e6c0c7fad176d6e27336ecf245c7a2a5b47c2de202065fb2c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b06a6547930cae960557184f59167542cde5f3c3dcb22f4bb24e1b684f8682c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__649d95eadfe7299f415c02072ea1098c4ec0572805314c3be20f62b145d3bd89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)  # pyright: ignore[reportArgumentType]


class DataLibvirtNodeDeviceInfoDevnodeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.dataLibvirtNodeDeviceInfo.DataLibvirtNodeDeviceInfoDevnodeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8dc0dd8de24492a5563da0072f80fea4c695316048da501fdb041afefc6d4d6f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataLibvirtNodeDeviceInfoDevnode]:
        return typing.cast(typing.Optional[DataLibvirtNodeDeviceInfoDevnode], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataLibvirtNodeDeviceInfoDevnode],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77cec37c2c3aa6343b0e06d2c2888ca7c7caf27985836e32ca69a5bfce03519c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


__all__ = [
    "DataLibvirtNodeDeviceInfo",
    "DataLibvirtNodeDeviceInfoCapability",
    "DataLibvirtNodeDeviceInfoCapabilityIommuGroup",
    "DataLibvirtNodeDeviceInfoCapabilityIommuGroupOutputReference",
    "DataLibvirtNodeDeviceInfoCapabilityOutputReference",
    "DataLibvirtNodeDeviceInfoConfig",
    "DataLibvirtNodeDeviceInfoDevnode",
    "DataLibvirtNodeDeviceInfoDevnodeList",
    "DataLibvirtNodeDeviceInfoDevnodeOutputReference",
]

publication.publish()


def _typecheckingstub__1ac9662e67bae5f2d90b1ac5dd6d5a6363bbed51398f3203d968706934f83dfc(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    capability: typing.Optional[typing.Union[DataLibvirtNodeDeviceInfoCapability, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__999ad5b0c42a1cb55e8f1bb3c1c6a893066801705441845144d4f539dae6aa84(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e703c96134b435c0e6797ea48796183dced723cc4bf81f499dac68f8135c4523(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__11bdaea52e2376c15b62e9593ecde5bce64a7e51d8296bd09f20e120ad97afde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__32de968585e941ab2fed142ead422c4efe0499800e1e7b822913848fb525dae0(
    *,
    address: typing.Optional[builtins.str] = None,
    block: typing.Optional[builtins.str] = None,
    bus: typing.Optional[builtins.str] = None,
    capability: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    class_: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    device: typing.Optional[builtins.str] = None,
    domain: typing.Optional[builtins.str] = None,
    drive_type: typing.Optional[builtins.str] = None,
    drm_type: typing.Optional[builtins.str] = None,
    features: typing.Optional[typing.Sequence[builtins.str]] = None,
    firmware: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    function: typing.Optional[builtins.str] = None,
    hardware: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    host: typing.Optional[builtins.str] = None,
    interface: typing.Optional[builtins.str] = None,
    iommu_group: typing.Optional[typing.Union[DataLibvirtNodeDeviceInfoCapabilityIommuGroup, typing.Dict[builtins.str, typing.Any]]] = None,
    link: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    logical_block_size: typing.Optional[builtins.str] = None,
    lun: typing.Optional[builtins.str] = None,
    model: typing.Optional[builtins.str] = None,
    number: typing.Optional[builtins.str] = None,
    num_blocks: typing.Optional[builtins.str] = None,
    product: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    protocol: typing.Optional[builtins.str] = None,
    scsi_type: typing.Optional[builtins.str] = None,
    serial: typing.Optional[builtins.str] = None,
    size: typing.Optional[builtins.str] = None,
    slot: typing.Optional[builtins.str] = None,
    subclass: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    unique_id: typing.Optional[builtins.str] = None,
    vendor: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1a1b159ec7790466557ee1ec71fd5d606feb86210d07e6d51f042378ed1bf7b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9dcb00ee24397b46fc85e5d8bc35cf8358cf5670258987173bc32ebc8b8c5541(
    value: typing.Optional[DataLibvirtNodeDeviceInfoCapabilityIommuGroup],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__11c279a53d005b0b17795859bfc8820ede72709dac01e74da6c0ecd6cd84d6f7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__06436215e02e95b6a9603f9f5c205fc0ae3f4364cf31a05a458707f3c02536df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fb476705c849e9974fa486a35aa507cd70929997e8f749ef5af06fa6080e87f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c4e8c9534ab1e5bc7439bbf43d2d705fc056ffbb74770959601fa26df8ec540e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3879119d64d52e35b51329ebfc0655b442099b1c22ceb0b46149c38d924819df(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c8cc2e9cc9180d19afaa58388607e34b7893d733e0c51d95164d2a3e07c24592(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8532112530d10ee2ec1e63230816c424a1a744b3478bb077f63a91fa5005bae4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1338f68d76ff4a340c2f797a8892d3f531934367e41009c720fdfa36b81eebcd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f1ab9b0a65b80db268283046b0895b28d5a355edca58345bb39d7a3f2745cdf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__af80a6ebc5e9156093d8c3005f4679c6b63df01a6f24a11f47e96c7d0282d716(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f0d61110aa0fc622ac3eef6416ece427c593f509032b345d69e1e03dbdaa12d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__671a0fb0ce0e5d32eafa3aee2df328676ba752c0121cd0c9d76e0f8d1e75554f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__011f6187364ed326f6fe7af4880779d32240c22deded4a540e97db2c995a7b67(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a784589f7701003c0d4c3fadab0393016e4ac4dfd4df485d8460fb4b59a41c74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__46e9faf684c9f8eed5425c35be8865d063fa0fde85eb4cd0ca3ca06c95938f8d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4030b5c5b3b81a55d6357a364ed827f8fb6612e352675b57a5e93db63b2fe359(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ede4ea9a2ef8599bbae95de2cc744290d79b47cee1a03e8e7627452f041532c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1c0d08caa27af6b57515c4daa51cc36d1d15ba7163bc7688c0071f0cae748c1b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__421acc334b595cb36ff0353f2da655e0de05461c65889a70a77aa1bc132fd4ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9012d1fb02944551f5edc911b149be4a58033c8c5380affb6c29cb649946dae6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f056396ad9bf2d54156f9a3d0732898c72a1b7c87ff1bfa398b31fe75107a259(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__37df24c49c0885b9588ee47b414320ed0ba73809112313d05e34437a2259e5ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c6b70660dbdaae564781ecdd9daf432c506e781112b3b5622fde874d178fb9a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6b586f00e724c86f162b8e65d23b121fbe4a9bcc3528e7751f5e4c5da72b2d69(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a02f11477245cd919bd6fc3ff6b07bc7bf59d011b81c3fe3911b4364d0d2d523(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__63b14058cd110e8375296ebb21bc7c282c526316e1b342e9e4f70c6afe3821a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__673bc8faef1b101ef89043d9a943a38735cc22493292fcdd68a57a54bf00b975(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__07a0ff952b443c3e87ceaa75156bd5f300e79960682c3910c3a29b9ba8801ca4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8009d529aed639dbce444d244b3f8c13be9c3febce1109d4feceb17935b375d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b04dd98b8e5a576599ff6e01c5f3003b08e7099e99090bd980b39b3e0548208f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6cde032d3d0d3cdcc7cbfafe6de165a1da6559e312e8bca9530bd1fec9a7b501(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7258542532358f67cdb1bde3545b2d5dce50ef5436d9b466ef66a1cf6ce55df4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b19d3f855149c5a006e516601c1c807f9ee12d4c7e67b497e52bb116cbbf069f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__079ed5d6a7b4e6d7c3f6ceecd0f3a1d13b901ec98f24d97284ce928608b9a994(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9bf218f75a8c8ab8743a328fd61f4c49b907cdc007887c8d79a5c8fb144194c8(
    value: typing.Optional[DataLibvirtNodeDeviceInfoCapability],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__559e471ec0a46d22e4e5bb4d84fe2bc4e09f0629a6f095e2dba377bd74a12bd7(
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
    capability: typing.Optional[typing.Union[DataLibvirtNodeDeviceInfoCapability, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3117b6a8958442a8288502aae971156ff5d4375901a16b243028034a5a950632(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d557a4cd28d4c3c341ddd0034e8ef60f88d7897b7bd87c68703e9f155cfe0ad9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__870e0bfd444e185e6c0c7fad176d6e27336ecf245c7a2a5b47c2de202065fb2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8b06a6547930cae960557184f59167542cde5f3c3dcb22f4bb24e1b684f8682c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__649d95eadfe7299f415c02072ea1098c4ec0572805314c3be20f62b145d3bd89(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8dc0dd8de24492a5563da0072f80fea4c695316048da501fdb041afefc6d4d6f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__77cec37c2c3aa6343b0e06d2c2888ca7c7caf27985836e32ca69a5bfce03519c(
    value: typing.Optional[DataLibvirtNodeDeviceInfoDevnode],
) -> None:
    """Type checking stubs"""
    pass
