r"""
# `libvirt_domain`

Refer to the Terraform Registry for docs: [`libvirt_domain`](https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain).
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


class Domain(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.Domain",
):
    """Represents a {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain libvirt_domain}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        arch: typing.Optional[builtins.str] = None,
        autostart: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        boot_device: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainBootDevice", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        cloudinit: typing.Optional[builtins.str] = None,
        cmdline: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Mapping[builtins.str, builtins.str]]]] = None,
        console: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainConsole", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        coreos_ignition: typing.Optional[builtins.str] = None,
        cpu: typing.Optional[typing.Union["DomainCpu", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        disk: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainDisk", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        emulator: typing.Optional[builtins.str] = None,
        filesystem: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainFilesystem", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        firmware: typing.Optional[builtins.str] = None,
        fw_cfg_name: typing.Optional[builtins.str] = None,
        graphics: typing.Optional[typing.Union["DomainGraphics", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        initrd: typing.Optional[builtins.str] = None,
        kernel: typing.Optional[builtins.str] = None,
        machine: typing.Optional[builtins.str] = None,
        memory: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[builtins.str] = None,
        network_interface: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainNetworkInterface", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        nvram: typing.Optional[typing.Union["DomainNvram", typing.Dict[builtins.str, typing.Any]]] = None,
        qemu_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        running: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["DomainTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        tpm: typing.Optional[typing.Union["DomainTpm", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        vcpu: typing.Optional[jsii.Number] = None,
        video: typing.Optional[typing.Union["DomainVideo", typing.Dict[builtins.str, typing.Any]]] = None,
        xml: typing.Optional[typing.Union["DomainXml", typing.Dict[builtins.str, typing.Any]]] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain libvirt_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#name Domain#name}.
        :param arch: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#arch Domain#arch}.
        :param autostart: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#autostart Domain#autostart}.
        :param boot_device: boot_device block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#boot_device Domain#boot_device}
        :param cloudinit: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#cloudinit Domain#cloudinit}.
        :param cmdline: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#cmdline Domain#cmdline}.
        :param console: console block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#console Domain#console}
        :param coreos_ignition: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#coreos_ignition Domain#coreos_ignition}.
        :param cpu: cpu block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#cpu Domain#cpu}
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#description Domain#description}.
        :param disk: disk block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#disk Domain#disk}
        :param emulator: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#emulator Domain#emulator}.
        :param filesystem: filesystem block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#filesystem Domain#filesystem}
        :param firmware: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#firmware Domain#firmware}.
        :param fw_cfg_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#fw_cfg_name Domain#fw_cfg_name}.
        :param graphics: graphics block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#graphics Domain#graphics}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#id Domain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initrd: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#initrd Domain#initrd}.
        :param kernel: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#kernel Domain#kernel}.
        :param machine: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#machine Domain#machine}.
        :param memory: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#memory Domain#memory}.
        :param metadata: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#metadata Domain#metadata}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#network_interface Domain#network_interface}
        :param nvram: nvram block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#nvram Domain#nvram}
        :param qemu_agent: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#qemu_agent Domain#qemu_agent}.
        :param running: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#running Domain#running}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#timeouts Domain#timeouts}
        :param tpm: tpm block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#tpm Domain#tpm}
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#type Domain#type}.
        :param vcpu: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#vcpu Domain#vcpu}.
        :param video: video block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#video Domain#video}
        :param xml: xml block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#xml Domain#xml}
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f08ce5592300df3006f0dcfcf5ac2fd27b6f0c9fc6ec8053dc56d3f28a2a8e27)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DomainConfig(
            name=name,
            arch=arch,
            autostart=autostart,
            boot_device=boot_device,
            cloudinit=cloudinit,
            cmdline=cmdline,
            console=console,
            coreos_ignition=coreos_ignition,
            cpu=cpu,
            description=description,
            disk=disk,
            emulator=emulator,
            filesystem=filesystem,
            firmware=firmware,
            fw_cfg_name=fw_cfg_name,
            graphics=graphics,
            id=id,
            initrd=initrd,
            kernel=kernel,
            machine=machine,
            memory=memory,
            metadata=metadata,
            network_interface=network_interface,
            nvram=nvram,
            qemu_agent=qemu_agent,
            running=running,
            timeouts=timeouts,
            tpm=tpm,
            type=type,
            vcpu=vcpu,
            video=video,
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
        """Generates CDKTF code for importing a Domain resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Domain to import.
        :param import_from_id: The id of the existing Domain that should be imported. Refer to the {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Domain to import is found.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f07ca475ed20be22d520ab95c8d4b38da5e9eccf638c7b822809cf175b0ca649)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putBootDevice")
    def put_boot_device(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainBootDevice", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce75af6d68e6a26edf8e0240dc67d9b99ab3ac7eff47bc99d416dd1ac2498429)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBootDevice", [value]))

    @jsii.member(jsii_name="putConsole")
    def put_console(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainConsole", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af3f3564a2def969d9f74933d186e37d37ba6221d562696cc7a2d9538dc386d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConsole", [value]))

    @jsii.member(jsii_name="putCpu")
    def put_cpu(self, *, mode: typing.Optional[builtins.str] = None) -> None:
        """
        :param mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#mode Domain#mode}.
        """
        value = DomainCpu(mode=mode)

        return typing.cast(None, jsii.invoke(self, "putCpu", [value]))

    @jsii.member(jsii_name="putDisk")
    def put_disk(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainDisk", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e312859d46d5599c4e456366d708f960ff2fb1780e13e56f5921197aadaaf03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDisk", [value]))

    @jsii.member(jsii_name="putFilesystem")
    def put_filesystem(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainFilesystem", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66a6f9cf9542ccb66d5fca1b18ebf2291ae8d4cde4b7678d9ada05a0afcd292a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilesystem", [value]))

    @jsii.member(jsii_name="putGraphics")
    def put_graphics(
        self,
        *,
        autoport: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        listen_address: typing.Optional[builtins.str] = None,
        listen_type: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        websocket: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param autoport: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#autoport Domain#autoport}.
        :param listen_address: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#listen_address Domain#listen_address}.
        :param listen_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#listen_type Domain#listen_type}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#type Domain#type}.
        :param websocket: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#websocket Domain#websocket}.
        """
        value = DomainGraphics(
            autoport=autoport,
            listen_address=listen_address,
            listen_type=listen_type,
            type=type,
            websocket=websocket,
        )

        return typing.cast(None, jsii.invoke(self, "putGraphics", [value]))

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainNetworkInterface", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4ec0708232225d90dd6eac1b113af66556ccee2b1057f41a7b789a8fd413ea0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterface", [value]))

    @jsii.member(jsii_name="putNvram")
    def put_nvram(
        self,
        *,
        file: typing.Optional[builtins.str] = None,
        template: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param file: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#file Domain#file}.
        :param template: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#template Domain#template}.
        """
        value = DomainNvram(file=file, template=template)

        return typing.cast(None, jsii.invoke(self, "putNvram", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        """
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#create Domain#create}.
        """
        value = DomainTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTpm")
    def put_tpm(
        self,
        *,
        backend_device_path: typing.Optional[builtins.str] = None,
        backend_encryption_secret: typing.Optional[builtins.str] = None,
        backend_persistent_state: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        backend_type: typing.Optional[builtins.str] = None,
        backend_version: typing.Optional[builtins.str] = None,
        model: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param backend_device_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_device_path Domain#backend_device_path}.
        :param backend_encryption_secret: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_encryption_secret Domain#backend_encryption_secret}.
        :param backend_persistent_state: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_persistent_state Domain#backend_persistent_state}.
        :param backend_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_type Domain#backend_type}.
        :param backend_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_version Domain#backend_version}.
        :param model: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#model Domain#model}.
        """
        value = DomainTpm(
            backend_device_path=backend_device_path,
            backend_encryption_secret=backend_encryption_secret,
            backend_persistent_state=backend_persistent_state,
            backend_type=backend_type,
            backend_version=backend_version,
            model=model,
        )

        return typing.cast(None, jsii.invoke(self, "putTpm", [value]))

    @jsii.member(jsii_name="putVideo")
    def put_video(self, *, type: typing.Optional[builtins.str] = None) -> None:
        """
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#type Domain#type}.
        """
        value = DomainVideo(type=type)

        return typing.cast(None, jsii.invoke(self, "putVideo", [value]))

    @jsii.member(jsii_name="putXml")
    def put_xml(self, *, xslt: typing.Optional[builtins.str] = None) -> None:
        """
        :param xslt: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#xslt Domain#xslt}.
        """
        value = DomainXml(xslt=xslt)

        return typing.cast(None, jsii.invoke(self, "putXml", [value]))

    @jsii.member(jsii_name="resetArch")
    def reset_arch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArch", []))

    @jsii.member(jsii_name="resetAutostart")
    def reset_autostart(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutostart", []))

    @jsii.member(jsii_name="resetBootDevice")
    def reset_boot_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDevice", []))

    @jsii.member(jsii_name="resetCloudinit")
    def reset_cloudinit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudinit", []))

    @jsii.member(jsii_name="resetCmdline")
    def reset_cmdline(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCmdline", []))

    @jsii.member(jsii_name="resetConsole")
    def reset_console(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsole", []))

    @jsii.member(jsii_name="resetCoreosIgnition")
    def reset_coreos_ignition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreosIgnition", []))

    @jsii.member(jsii_name="resetCpu")
    def reset_cpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpu", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisk")
    def reset_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisk", []))

    @jsii.member(jsii_name="resetEmulator")
    def reset_emulator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmulator", []))

    @jsii.member(jsii_name="resetFilesystem")
    def reset_filesystem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilesystem", []))

    @jsii.member(jsii_name="resetFirmware")
    def reset_firmware(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirmware", []))

    @jsii.member(jsii_name="resetFwCfgName")
    def reset_fw_cfg_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFwCfgName", []))

    @jsii.member(jsii_name="resetGraphics")
    def reset_graphics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGraphics", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitrd")
    def reset_initrd(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitrd", []))

    @jsii.member(jsii_name="resetKernel")
    def reset_kernel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKernel", []))

    @jsii.member(jsii_name="resetMachine")
    def reset_machine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachine", []))

    @jsii.member(jsii_name="resetMemory")
    def reset_memory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemory", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetNetworkInterface")
    def reset_network_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkInterface", []))

    @jsii.member(jsii_name="resetNvram")
    def reset_nvram(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNvram", []))

    @jsii.member(jsii_name="resetQemuAgent")
    def reset_qemu_agent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQemuAgent", []))

    @jsii.member(jsii_name="resetRunning")
    def reset_running(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunning", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTpm")
    def reset_tpm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTpm", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetVcpu")
    def reset_vcpu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVcpu", []))

    @jsii.member(jsii_name="resetVideo")
    def reset_video(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideo", []))

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
    @jsii.member(jsii_name="bootDevice")
    def boot_device(self) -> "DomainBootDeviceList":
        return typing.cast("DomainBootDeviceList", jsii.get(self, "bootDevice"))

    @builtins.property
    @jsii.member(jsii_name="console")
    def console(self) -> "DomainConsoleList":
        return typing.cast("DomainConsoleList", jsii.get(self, "console"))

    @builtins.property
    @jsii.member(jsii_name="cpu")
    def cpu(self) -> "DomainCpuOutputReference":
        return typing.cast("DomainCpuOutputReference", jsii.get(self, "cpu"))

    @builtins.property
    @jsii.member(jsii_name="disk")
    def disk(self) -> "DomainDiskList":
        return typing.cast("DomainDiskList", jsii.get(self, "disk"))

    @builtins.property
    @jsii.member(jsii_name="filesystem")
    def filesystem(self) -> "DomainFilesystemList":
        return typing.cast("DomainFilesystemList", jsii.get(self, "filesystem"))

    @builtins.property
    @jsii.member(jsii_name="graphics")
    def graphics(self) -> "DomainGraphicsOutputReference":
        return typing.cast("DomainGraphicsOutputReference", jsii.get(self, "graphics"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> "DomainNetworkInterfaceList":
        return typing.cast("DomainNetworkInterfaceList", jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="nvram")
    def nvram(self) -> "DomainNvramOutputReference":
        return typing.cast("DomainNvramOutputReference", jsii.get(self, "nvram"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DomainTimeoutsOutputReference":
        return typing.cast("DomainTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="tpm")
    def tpm(self) -> "DomainTpmOutputReference":
        return typing.cast("DomainTpmOutputReference", jsii.get(self, "tpm"))

    @builtins.property
    @jsii.member(jsii_name="video")
    def video(self) -> "DomainVideoOutputReference":
        return typing.cast("DomainVideoOutputReference", jsii.get(self, "video"))

    @builtins.property
    @jsii.member(jsii_name="xml")
    def xml(self) -> "DomainXmlOutputReference":
        return typing.cast("DomainXmlOutputReference", jsii.get(self, "xml"))

    @builtins.property
    @jsii.member(jsii_name="archInput")
    def arch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "archInput"))

    @builtins.property
    @jsii.member(jsii_name="autostartInput")
    def autostart_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autostartInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDeviceInput")
    def boot_device_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainBootDevice"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainBootDevice"]]], jsii.get(self, "bootDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudinitInput")
    def cloudinit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudinitInput"))

    @builtins.property
    @jsii.member(jsii_name="cmdlineInput")
    def cmdline_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[typing.Mapping[builtins.str, builtins.str]]]]:
        return typing.cast(
            typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[typing.Mapping[builtins.str, builtins.str]]]], jsii.get(self, "cmdlineInput")
        )

    @builtins.property
    @jsii.member(jsii_name="consoleInput")
    def console_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainConsole"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainConsole"]]], jsii.get(self, "consoleInput"))

    @builtins.property
    @jsii.member(jsii_name="coreosIgnitionInput")
    def coreos_ignition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coreosIgnitionInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuInput")
    def cpu_input(self) -> typing.Optional["DomainCpu"]:
        return typing.cast(typing.Optional["DomainCpu"], jsii.get(self, "cpuInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="diskInput")
    def disk_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainDisk"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainDisk"]]], jsii.get(self, "diskInput"))

    @builtins.property
    @jsii.member(jsii_name="emulatorInput")
    def emulator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emulatorInput"))

    @builtins.property
    @jsii.member(jsii_name="filesystemInput")
    def filesystem_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainFilesystem"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainFilesystem"]]], jsii.get(self, "filesystemInput"))

    @builtins.property
    @jsii.member(jsii_name="firmwareInput")
    def firmware_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firmwareInput"))

    @builtins.property
    @jsii.member(jsii_name="fwCfgNameInput")
    def fw_cfg_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fwCfgNameInput"))

    @builtins.property
    @jsii.member(jsii_name="graphicsInput")
    def graphics_input(self) -> typing.Optional["DomainGraphics"]:
        return typing.cast(typing.Optional["DomainGraphics"], jsii.get(self, "graphicsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initrdInput")
    def initrd_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "initrdInput"))

    @builtins.property
    @jsii.member(jsii_name="kernelInput")
    def kernel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kernelInput"))

    @builtins.property
    @jsii.member(jsii_name="machineInput")
    def machine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceInput")
    def network_interface_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainNetworkInterface"]]]:
        return typing.cast(
            typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainNetworkInterface"]]], jsii.get(self, "networkInterfaceInput")
        )

    @builtins.property
    @jsii.member(jsii_name="nvramInput")
    def nvram_input(self) -> typing.Optional["DomainNvram"]:
        return typing.cast(typing.Optional["DomainNvram"], jsii.get(self, "nvramInput"))

    @builtins.property
    @jsii.member(jsii_name="qemuAgentInput")
    def qemu_agent_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "qemuAgentInput"))

    @builtins.property
    @jsii.member(jsii_name="runningInput")
    def running_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "runningInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "DomainTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "DomainTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="tpmInput")
    def tpm_input(self) -> typing.Optional["DomainTpm"]:
        return typing.cast(typing.Optional["DomainTpm"], jsii.get(self, "tpmInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="vcpuInput")
    def vcpu_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vcpuInput"))

    @builtins.property
    @jsii.member(jsii_name="videoInput")
    def video_input(self) -> typing.Optional["DomainVideo"]:
        return typing.cast(typing.Optional["DomainVideo"], jsii.get(self, "videoInput"))

    @builtins.property
    @jsii.member(jsii_name="xmlInput")
    def xml_input(self) -> typing.Optional["DomainXml"]:
        return typing.cast(typing.Optional["DomainXml"], jsii.get(self, "xmlInput"))

    @builtins.property
    @jsii.member(jsii_name="arch")
    def arch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arch"))

    @arch.setter
    def arch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a720164e9e10731dc47105f6c435ad111f261b4759095c5ffbffd3a838fdc96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arch", value)  # pyright: ignore[reportArgumentType]

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
            type_hints = typing.get_type_hints(_typecheckingstub__2ac7b4f211596cd73824f42a9ececd56997da696c7dd9f59b34b17af84054235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autostart", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cloudinit")
    def cloudinit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudinit"))

    @cloudinit.setter
    def cloudinit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7408b99b8cffd9ebcf9f5325fdc4ad6f0c42e9d0e40fba43bfcd3a8bc5e30c5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudinit", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cmdline")
    def cmdline(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "cmdline"))

    @cmdline.setter
    def cmdline(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c40aa4b535935ab323370a5926f65e3964823a388e0f008170d70e8d7247bc40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cmdline", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="coreosIgnition")
    def coreos_ignition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "coreosIgnition"))

    @coreos_ignition.setter
    def coreos_ignition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5d9f1ea52569ef408123331c22ac96299263d268cee934b97b587ba4338d284)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreosIgnition", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d135d0953ad0314009200069377a33116cc8f1c5e70e72c873747d6102670fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="emulator")
    def emulator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emulator"))

    @emulator.setter
    def emulator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b7ecc1e7fa5bea8af302507fdce30eb164dd3d5482ae72bf5a5e5545667c956)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emulator", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="firmware")
    def firmware(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firmware"))

    @firmware.setter
    def firmware(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__058ad35768b28d6745fc41c014a93a7338568a35550d601f3a60f38b001f014b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firmware", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fwCfgName")
    def fw_cfg_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fwCfgName"))

    @fw_cfg_name.setter
    def fw_cfg_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fc263b3b9de5c8b61189aa5574687547fff18fde3e758de2cbc56165ca170f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fwCfgName", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5897970913bed040adb4a2cbf98092a0712c803b81be91e8d621ee37ada3b77c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="initrd")
    def initrd(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initrd"))

    @initrd.setter
    def initrd(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__716cdea228dbd9b0a78b8f5a4966714fa61d9f78fcb3c0dccca6a2cbcac7ae51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initrd", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kernel")
    def kernel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kernel"))

    @kernel.setter
    def kernel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87cbcb56e9329f1d84fe0e0d84b14c4583ab069ce791037296d4a2defb076932)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kernel", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="machine")
    def machine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machine"))

    @machine.setter
    def machine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__345c0f122bff0cabd7972ac32125eff1d2389af58362513e042d9396f9cff014)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machine", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__115cdf3e8c4aca725cabf335be093158abfba8f13d6801c08f9c0ed0cfb93773)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__898915eed96cf0ef11a4b9a14a37531660e23f8e421720f4a94c8cd3b166e22e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8899a70160a8366e43f32fee66a45fe54679d5ec7f845b71d67e449543f8999)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="qemuAgent")
    def qemu_agent(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "qemuAgent"))

    @qemu_agent.setter
    def qemu_agent(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaa087b38638ac08ece9731a7689109ddd3329088011a30f97665d6e12fcc0af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qemuAgent", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="running")
    def running(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "running"))

    @running.setter
    def running(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebc4bb4ce2a15843391e0f3ffed8621b55eb1d70a99ea6479ee650046ede9907)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "running", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e1c56b30bf522501d7e49a738aba9cfa62ad1f9d531a2a8d5a37815f7e67038)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vcpu")
    def vcpu(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vcpu"))

    @vcpu.setter
    def vcpu(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7f583c44b29d4f851d1d1c34446efe1f2bc23c4768684116bdf60368376d438)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vcpu", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.domain.DomainBootDevice",
    jsii_struct_bases=[],
    name_mapping={"dev": "dev"},
)
class DomainBootDevice:
    def __init__(
        self,
        *,
        dev: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param dev: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#dev Domain#dev}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a40fa6125abf99453da6d5912f18a243a73b0e6bdbdbe0589af43890c9237a3)
            check_type(argname="argument dev", value=dev, expected_type=type_hints["dev"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dev is not None:
            self._values["dev"] = dev

    @builtins.property
    def dev(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#dev Domain#dev}."""
        result = self._values.get("dev")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainBootDevice(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DomainBootDeviceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainBootDeviceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6e0dfd0a7670c5b91ff78b88111b214e581ba1c9b74e74cae3a2e9958e300af)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DomainBootDeviceOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c0e610a46e72d33c53ef03483c00bd0d4b3e8da6e41794ba41bcfa3333a8a89)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DomainBootDeviceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27711cf08ffe01ecf2849d6642be80eef4878c86649a60a1b88a8c8601e9f095)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9e7fd30666e001211d5427b83d1ec6d4b60ea7ec3723c50cf2f3e3c0a7ad3a9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d2bc3c909dc4400abdf3f53905641a42775473bd56130aefb86f02c512682cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainBootDevice]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainBootDevice]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainBootDevice]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c358de4e713622f0b3ace66efa0a350939467a607aab61804164c0d2d3c18ee1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class DomainBootDeviceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainBootDeviceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2d32d61b7484b7a15128d0972a9d563fed457f86186d7ea51ba21953673de3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDev")
    def reset_dev(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDev", []))

    @builtins.property
    @jsii.member(jsii_name="devInput")
    def dev_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "devInput"))

    @builtins.property
    @jsii.member(jsii_name="dev")
    def dev(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dev"))

    @dev.setter
    def dev(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d237e03cce70e6983634e99cd373877a41383f16de7f0a44ae1402efe9296ad7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dev", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainBootDevice]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainBootDevice]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainBootDevice]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__433295b0bad9b4ff1a6d7552b392dc27380b2b36774f637ff912e0bb6e023db5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.domain.DomainConfig",
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
        "arch": "arch",
        "autostart": "autostart",
        "boot_device": "bootDevice",
        "cloudinit": "cloudinit",
        "cmdline": "cmdline",
        "console": "console",
        "coreos_ignition": "coreosIgnition",
        "cpu": "cpu",
        "description": "description",
        "disk": "disk",
        "emulator": "emulator",
        "filesystem": "filesystem",
        "firmware": "firmware",
        "fw_cfg_name": "fwCfgName",
        "graphics": "graphics",
        "id": "id",
        "initrd": "initrd",
        "kernel": "kernel",
        "machine": "machine",
        "memory": "memory",
        "metadata": "metadata",
        "network_interface": "networkInterface",
        "nvram": "nvram",
        "qemu_agent": "qemuAgent",
        "running": "running",
        "timeouts": "timeouts",
        "tpm": "tpm",
        "type": "type",
        "vcpu": "vcpu",
        "video": "video",
        "xml": "xml",
    },
)
class DomainConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        arch: typing.Optional[builtins.str] = None,
        autostart: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        boot_device: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainBootDevice, typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        cloudinit: typing.Optional[builtins.str] = None,
        cmdline: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Mapping[builtins.str, builtins.str]]]] = None,
        console: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainConsole", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        coreos_ignition: typing.Optional[builtins.str] = None,
        cpu: typing.Optional[typing.Union["DomainCpu", typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        disk: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainDisk", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        emulator: typing.Optional[builtins.str] = None,
        filesystem: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainFilesystem", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        firmware: typing.Optional[builtins.str] = None,
        fw_cfg_name: typing.Optional[builtins.str] = None,
        graphics: typing.Optional[typing.Union["DomainGraphics", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        initrd: typing.Optional[builtins.str] = None,
        kernel: typing.Optional[builtins.str] = None,
        machine: typing.Optional[builtins.str] = None,
        memory: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[builtins.str] = None,
        network_interface: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DomainNetworkInterface", typing.Dict[builtins.str, typing.Any]]]]
        ] = None,
        nvram: typing.Optional[typing.Union["DomainNvram", typing.Dict[builtins.str, typing.Any]]] = None,
        qemu_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        running: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["DomainTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        tpm: typing.Optional[typing.Union["DomainTpm", typing.Dict[builtins.str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        vcpu: typing.Optional[jsii.Number] = None,
        video: typing.Optional[typing.Union["DomainVideo", typing.Dict[builtins.str, typing.Any]]] = None,
        xml: typing.Optional[typing.Union["DomainXml", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#name Domain#name}.
        :param arch: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#arch Domain#arch}.
        :param autostart: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#autostart Domain#autostart}.
        :param boot_device: boot_device block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#boot_device Domain#boot_device}
        :param cloudinit: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#cloudinit Domain#cloudinit}.
        :param cmdline: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#cmdline Domain#cmdline}.
        :param console: console block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#console Domain#console}
        :param coreos_ignition: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#coreos_ignition Domain#coreos_ignition}.
        :param cpu: cpu block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#cpu Domain#cpu}
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#description Domain#description}.
        :param disk: disk block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#disk Domain#disk}
        :param emulator: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#emulator Domain#emulator}.
        :param filesystem: filesystem block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#filesystem Domain#filesystem}
        :param firmware: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#firmware Domain#firmware}.
        :param fw_cfg_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#fw_cfg_name Domain#fw_cfg_name}.
        :param graphics: graphics block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#graphics Domain#graphics}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#id Domain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initrd: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#initrd Domain#initrd}.
        :param kernel: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#kernel Domain#kernel}.
        :param machine: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#machine Domain#machine}.
        :param memory: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#memory Domain#memory}.
        :param metadata: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#metadata Domain#metadata}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#network_interface Domain#network_interface}
        :param nvram: nvram block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#nvram Domain#nvram}
        :param qemu_agent: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#qemu_agent Domain#qemu_agent}.
        :param running: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#running Domain#running}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#timeouts Domain#timeouts}
        :param tpm: tpm block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#tpm Domain#tpm}
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#type Domain#type}.
        :param vcpu: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#vcpu Domain#vcpu}.
        :param video: video block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#video Domain#video}
        :param xml: xml block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#xml Domain#xml}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cpu, dict):
            cpu = DomainCpu(**cpu)
        if isinstance(graphics, dict):
            graphics = DomainGraphics(**graphics)
        if isinstance(nvram, dict):
            nvram = DomainNvram(**nvram)
        if isinstance(timeouts, dict):
            timeouts = DomainTimeouts(**timeouts)
        if isinstance(tpm, dict):
            tpm = DomainTpm(**tpm)
        if isinstance(video, dict):
            video = DomainVideo(**video)
        if isinstance(xml, dict):
            xml = DomainXml(**xml)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae7067743acdda5e59683d1113f500a3766ee9aa2eeb14dcbec4975e742a63c4)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument arch", value=arch, expected_type=type_hints["arch"])
            check_type(argname="argument autostart", value=autostart, expected_type=type_hints["autostart"])
            check_type(argname="argument boot_device", value=boot_device, expected_type=type_hints["boot_device"])
            check_type(argname="argument cloudinit", value=cloudinit, expected_type=type_hints["cloudinit"])
            check_type(argname="argument cmdline", value=cmdline, expected_type=type_hints["cmdline"])
            check_type(argname="argument console", value=console, expected_type=type_hints["console"])
            check_type(argname="argument coreos_ignition", value=coreos_ignition, expected_type=type_hints["coreos_ignition"])
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disk", value=disk, expected_type=type_hints["disk"])
            check_type(argname="argument emulator", value=emulator, expected_type=type_hints["emulator"])
            check_type(argname="argument filesystem", value=filesystem, expected_type=type_hints["filesystem"])
            check_type(argname="argument firmware", value=firmware, expected_type=type_hints["firmware"])
            check_type(argname="argument fw_cfg_name", value=fw_cfg_name, expected_type=type_hints["fw_cfg_name"])
            check_type(argname="argument graphics", value=graphics, expected_type=type_hints["graphics"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initrd", value=initrd, expected_type=type_hints["initrd"])
            check_type(argname="argument kernel", value=kernel, expected_type=type_hints["kernel"])
            check_type(argname="argument machine", value=machine, expected_type=type_hints["machine"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument nvram", value=nvram, expected_type=type_hints["nvram"])
            check_type(argname="argument qemu_agent", value=qemu_agent, expected_type=type_hints["qemu_agent"])
            check_type(argname="argument running", value=running, expected_type=type_hints["running"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument tpm", value=tpm, expected_type=type_hints["tpm"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument vcpu", value=vcpu, expected_type=type_hints["vcpu"])
            check_type(argname="argument video", value=video, expected_type=type_hints["video"])
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
        if arch is not None:
            self._values["arch"] = arch
        if autostart is not None:
            self._values["autostart"] = autostart
        if boot_device is not None:
            self._values["boot_device"] = boot_device
        if cloudinit is not None:
            self._values["cloudinit"] = cloudinit
        if cmdline is not None:
            self._values["cmdline"] = cmdline
        if console is not None:
            self._values["console"] = console
        if coreos_ignition is not None:
            self._values["coreos_ignition"] = coreos_ignition
        if cpu is not None:
            self._values["cpu"] = cpu
        if description is not None:
            self._values["description"] = description
        if disk is not None:
            self._values["disk"] = disk
        if emulator is not None:
            self._values["emulator"] = emulator
        if filesystem is not None:
            self._values["filesystem"] = filesystem
        if firmware is not None:
            self._values["firmware"] = firmware
        if fw_cfg_name is not None:
            self._values["fw_cfg_name"] = fw_cfg_name
        if graphics is not None:
            self._values["graphics"] = graphics
        if id is not None:
            self._values["id"] = id
        if initrd is not None:
            self._values["initrd"] = initrd
        if kernel is not None:
            self._values["kernel"] = kernel
        if machine is not None:
            self._values["machine"] = machine
        if memory is not None:
            self._values["memory"] = memory
        if metadata is not None:
            self._values["metadata"] = metadata
        if network_interface is not None:
            self._values["network_interface"] = network_interface
        if nvram is not None:
            self._values["nvram"] = nvram
        if qemu_agent is not None:
            self._values["qemu_agent"] = qemu_agent
        if running is not None:
            self._values["running"] = running
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if tpm is not None:
            self._values["tpm"] = tpm
        if type is not None:
            self._values["type"] = type
        if vcpu is not None:
            self._values["vcpu"] = vcpu
        if video is not None:
            self._values["video"] = video
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#name Domain#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def arch(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#arch Domain#arch}."""
        result = self._values.get("arch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def autostart(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#autostart Domain#autostart}."""
        result = self._values.get("autostart")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def boot_device(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainBootDevice]]]:
        """boot_device block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#boot_device Domain#boot_device}
        """
        result = self._values.get("boot_device")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainBootDevice]]], result)

    @builtins.property
    def cloudinit(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#cloudinit Domain#cloudinit}."""
        result = self._values.get("cloudinit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cmdline(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[typing.Mapping[builtins.str, builtins.str]]]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#cmdline Domain#cmdline}."""
        result = self._values.get("cmdline")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[typing.Mapping[builtins.str, builtins.str]]]], result)

    @builtins.property
    def console(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainConsole"]]]:
        """console block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#console Domain#console}
        """
        result = self._values.get("console")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainConsole"]]], result)

    @builtins.property
    def coreos_ignition(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#coreos_ignition Domain#coreos_ignition}."""
        result = self._values.get("coreos_ignition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu(self) -> typing.Optional["DomainCpu"]:
        """cpu block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#cpu Domain#cpu}
        """
        result = self._values.get("cpu")
        return typing.cast(typing.Optional["DomainCpu"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#description Domain#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainDisk"]]]:
        """disk block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#disk Domain#disk}
        """
        result = self._values.get("disk")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainDisk"]]], result)

    @builtins.property
    def emulator(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#emulator Domain#emulator}."""
        result = self._values.get("emulator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filesystem(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainFilesystem"]]]:
        """filesystem block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#filesystem Domain#filesystem}
        """
        result = self._values.get("filesystem")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainFilesystem"]]], result)

    @builtins.property
    def firmware(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#firmware Domain#firmware}."""
        result = self._values.get("firmware")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fw_cfg_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#fw_cfg_name Domain#fw_cfg_name}."""
        result = self._values.get("fw_cfg_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def graphics(self) -> typing.Optional["DomainGraphics"]:
        """graphics block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#graphics Domain#graphics}
        """
        result = self._values.get("graphics")
        return typing.cast(typing.Optional["DomainGraphics"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#id Domain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initrd(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#initrd Domain#initrd}."""
        result = self._values.get("initrd")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kernel(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#kernel Domain#kernel}."""
        result = self._values.get("kernel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def machine(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#machine Domain#machine}."""
        result = self._values.get("machine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#memory Domain#memory}."""
        result = self._values.get("memory")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metadata(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#metadata Domain#metadata}."""
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainNetworkInterface"]]]:
        """network_interface block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#network_interface Domain#network_interface}
        """
        result = self._values.get("network_interface")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DomainNetworkInterface"]]], result)

    @builtins.property
    def nvram(self) -> typing.Optional["DomainNvram"]:
        """nvram block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#nvram Domain#nvram}
        """
        result = self._values.get("nvram")
        return typing.cast(typing.Optional["DomainNvram"], result)

    @builtins.property
    def qemu_agent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#qemu_agent Domain#qemu_agent}."""
        result = self._values.get("qemu_agent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def running(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#running Domain#running}."""
        result = self._values.get("running")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DomainTimeouts"]:
        """timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#timeouts Domain#timeouts}
        """
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DomainTimeouts"], result)

    @builtins.property
    def tpm(self) -> typing.Optional["DomainTpm"]:
        """tpm block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#tpm Domain#tpm}
        """
        result = self._values.get("tpm")
        return typing.cast(typing.Optional["DomainTpm"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#type Domain#type}."""
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vcpu(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#vcpu Domain#vcpu}."""
        result = self._values.get("vcpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def video(self) -> typing.Optional["DomainVideo"]:
        """video block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#video Domain#video}
        """
        result = self._values.get("video")
        return typing.cast(typing.Optional["DomainVideo"], result)

    @builtins.property
    def xml(self) -> typing.Optional["DomainXml"]:
        """xml block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#xml Domain#xml}
        """
        result = self._values.get("xml")
        return typing.cast(typing.Optional["DomainXml"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainConfig(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


@jsii.data_type(
    jsii_type="libvirt.domain.DomainConsole",
    jsii_struct_bases=[],
    name_mapping={
        "target_port": "targetPort",
        "type": "type",
        "source_host": "sourceHost",
        "source_path": "sourcePath",
        "source_service": "sourceService",
        "target_type": "targetType",
    },
)
class DomainConsole:
    def __init__(
        self,
        *,
        target_port: builtins.str,
        type: builtins.str,
        source_host: typing.Optional[builtins.str] = None,
        source_path: typing.Optional[builtins.str] = None,
        source_service: typing.Optional[builtins.str] = None,
        target_type: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param target_port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#target_port Domain#target_port}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#type Domain#type}.
        :param source_host: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#source_host Domain#source_host}.
        :param source_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#source_path Domain#source_path}.
        :param source_service: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#source_service Domain#source_service}.
        :param target_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#target_type Domain#target_type}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a1795b4c54d41b1dc98a48d23802135257a61afccea02837f4a58339e1f218b)
            check_type(argname="argument target_port", value=target_port, expected_type=type_hints["target_port"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument source_host", value=source_host, expected_type=type_hints["source_host"])
            check_type(argname="argument source_path", value=source_path, expected_type=type_hints["source_path"])
            check_type(argname="argument source_service", value=source_service, expected_type=type_hints["source_service"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_port": target_port,
            "type": type,
        }
        if source_host is not None:
            self._values["source_host"] = source_host
        if source_path is not None:
            self._values["source_path"] = source_path
        if source_service is not None:
            self._values["source_service"] = source_service
        if target_type is not None:
            self._values["target_type"] = target_type

    @builtins.property
    def target_port(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#target_port Domain#target_port}."""
        result = self._values.get("target_port")
        assert result is not None, "Required property 'target_port' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#type Domain#type}."""
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_host(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#source_host Domain#source_host}."""
        result = self._values.get("source_host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_path(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#source_path Domain#source_path}."""
        result = self._values.get("source_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_service(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#source_service Domain#source_service}."""
        result = self._values.get("source_service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#target_type Domain#target_type}."""
        result = self._values.get("target_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainConsole(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DomainConsoleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainConsoleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__48551f42e6acd60301b27b16165e969378452d63c571143dd4531198821f9eed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DomainConsoleOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8b9abe723384725f445eeeefecb30ec720f5306a9a74f92f3c2be9022a78467)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DomainConsoleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75d7e23f91f80e0b09188b932f1765fd0ab20f37b844825e768d6b6138c2b21d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__da69cd4d6c1a5081df82430b2a6d25bf4f94e36dfd24867c458f20b9e6b90f6e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d755081f1ba47cf029ffd00d3c01d15a44c611478aa1b5981538bd28567f7e6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainConsole]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainConsole]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainConsole]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78037a96821755c96287a8f30f94a5e0672fca9186ac687ece4a1d76e1668841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class DomainConsoleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainConsoleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c24f4570548e1d065dd619c40fd2e5be945aa3a2f766cc88b45805a27903cb0a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSourceHost")
    def reset_source_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceHost", []))

    @jsii.member(jsii_name="resetSourcePath")
    def reset_source_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourcePath", []))

    @jsii.member(jsii_name="resetSourceService")
    def reset_source_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceService", []))

    @jsii.member(jsii_name="resetTargetType")
    def reset_target_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetType", []))

    @builtins.property
    @jsii.member(jsii_name="sourceHostInput")
    def source_host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceHostInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcePathInput")
    def source_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourcePathInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceServiceInput")
    def source_service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPortInput")
    def target_port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetPortInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTypeInput")
    def target_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceHost")
    def source_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceHost"))

    @source_host.setter
    def source_host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c39b96707227cfffae16a410cf46b1d0d07b15f2e54bd051a4ccc8d3df4c7750)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceHost", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourcePath")
    def source_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourcePath"))

    @source_path.setter
    def source_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__366a997a90ef83a32e4b4d7c1a08d52d743088a4d5944ac9cc69bdcea02e7271)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourcePath", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceService")
    def source_service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceService"))

    @source_service.setter
    def source_service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__367c9c2731c514b06d51c96f1965e9e1137605f9cb5b5b16879a7f99c61009dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceService", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetPort")
    def target_port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPort"))

    @target_port.setter
    def target_port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1b3cd746b765c1b4fcd489059a8803b233603f9dbe34ff549cd7bb192d4ad89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPort", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b96f4c2d34365b8ece351584b33920a472a3171da29bf3214448995e925d9e4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d10e23c27da09131c01e4422c2a8ea40dc12fc66294c34ea08f49a5529329d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainConsole]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainConsole]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainConsole]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c34235f3273a11931871c1aa0984933ac59b944920050d41595f68777310a94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.domain.DomainCpu",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode"},
)
class DomainCpu:
    def __init__(self, *, mode: typing.Optional[builtins.str] = None) -> None:
        """
        :param mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#mode Domain#mode}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e4a0e7dceef07956b36f0791dca27e23c6d36de24034b421f653ae35e3dc111)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#mode Domain#mode}."""
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainCpu(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DomainCpuOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainCpuOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4392f36095f8c2033898406eb388b73b2e59340bce4a0dceda006c116bfeb7cc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__660e1f183345e917282c0062e5ad62bdcecd5dd1acf9518515fb6995dc998656)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DomainCpu]:
        return typing.cast(typing.Optional[DomainCpu], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DomainCpu]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6462972d4c39cbe81cc2cbdf014ce4c9e27d88f564e5fe517924e13187dcef0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.domain.DomainDisk",
    jsii_struct_bases=[],
    name_mapping={
        "block_device": "blockDevice",
        "file": "file",
        "scsi": "scsi",
        "url": "url",
        "volume_id": "volumeId",
        "wwn": "wwn",
    },
)
class DomainDisk:
    def __init__(
        self,
        *,
        block_device: typing.Optional[builtins.str] = None,
        file: typing.Optional[builtins.str] = None,
        scsi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        url: typing.Optional[builtins.str] = None,
        volume_id: typing.Optional[builtins.str] = None,
        wwn: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param block_device: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#block_device Domain#block_device}.
        :param file: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#file Domain#file}.
        :param scsi: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#scsi Domain#scsi}.
        :param url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#url Domain#url}.
        :param volume_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#volume_id Domain#volume_id}.
        :param wwn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#wwn Domain#wwn}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4e784fe06b91cb7b5dad6050e8ecca68f012b889a0ecba4963cc1f1b103e936)
            check_type(argname="argument block_device", value=block_device, expected_type=type_hints["block_device"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument scsi", value=scsi, expected_type=type_hints["scsi"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument wwn", value=wwn, expected_type=type_hints["wwn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if block_device is not None:
            self._values["block_device"] = block_device
        if file is not None:
            self._values["file"] = file
        if scsi is not None:
            self._values["scsi"] = scsi
        if url is not None:
            self._values["url"] = url
        if volume_id is not None:
            self._values["volume_id"] = volume_id
        if wwn is not None:
            self._values["wwn"] = wwn

    @builtins.property
    def block_device(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#block_device Domain#block_device}."""
        result = self._values.get("block_device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#file Domain#file}."""
        result = self._values.get("file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scsi(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#scsi Domain#scsi}."""
        result = self._values.get("scsi")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#url Domain#url}."""
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#volume_id Domain#volume_id}."""
        result = self._values.get("volume_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wwn(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#wwn Domain#wwn}."""
        result = self._values.get("wwn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainDisk(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DomainDiskList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainDiskList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3df3892ce89bd814ab7712dcd929107c10449e4d7bcb8583d1ac3c44c0110e9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DomainDiskOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e955114a12834dd5b6c0883ab5e5215dd8bdb41504a574596ecb005b5cc47a99)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DomainDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__251035cae2d5727ea3a7a7e29a0d002ad24517c4d2cc1cc5d0b003ad43439f9f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__efd44d2c54097083797b2e526a195138bfd8a364dc3db6669eb90419999cfd65)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9076a2d220c97727839af9decba6b22be063fb197e479cf76733362c0e1871c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainDisk]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc3d7ce33f47ec94e553b077a64f893af9e7cdd495746f7112057fdc6f06ac17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class DomainDiskOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainDiskOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__80e5db5d2ef56c7d8e2dc136dd1994f81d34a6e9bd704b0e3acd25d996d43dbc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBlockDevice")
    def reset_block_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockDevice", []))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetScsi")
    def reset_scsi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScsi", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @jsii.member(jsii_name="resetVolumeId")
    def reset_volume_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeId", []))

    @jsii.member(jsii_name="resetWwn")
    def reset_wwn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWwn", []))

    @builtins.property
    @jsii.member(jsii_name="blockDeviceInput")
    def block_device_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blockDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="scsiInput")
    def scsi_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "scsiInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeIdInput")
    def volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="wwnInput")
    def wwn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "wwnInput"))

    @builtins.property
    @jsii.member(jsii_name="blockDevice")
    def block_device(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blockDevice"))

    @block_device.setter
    def block_device(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a33a9cd64763bb54ae3e0fb8843b7267174df1e2a84cc95e0438c2541f1dc0f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockDevice", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "file"))

    @file.setter
    def file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__521b885b3d37c2f575b1b39c97f77bdf356c99919313d7cef2044257938190f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "file", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scsi")
    def scsi(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "scsi"))

    @scsi.setter
    def scsi(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fb33ae601d695bc2b90e203b85d8da24430f927b649c6ba6036bd35f2535663)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scsi", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35513ae0684c0b819be55c4bb939146455e9698a9980df2352e43efcee420dd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b165e682b62938fdf2f7a2a7536162136485bfcc1fd10373868e1e196bde8f67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wwn")
    def wwn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "wwn"))

    @wwn.setter
    def wwn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cad529267d52139a8b6a76d8eef0626571bf8ebd997c11a7e3ea6155ef714b8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wwn", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainDisk]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainDisk]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainDisk]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__166f0c6e1040de7df2273f702058a38062f5df392f2ed4efac412d6f6ba27ce2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.domain.DomainFilesystem",
    jsii_struct_bases=[],
    name_mapping={
        "source": "source",
        "target": "target",
        "accessmode": "accessmode",
        "readonly": "readonly",
    },
)
class DomainFilesystem:
    def __init__(
        self,
        *,
        source: builtins.str,
        target: builtins.str,
        accessmode: typing.Optional[builtins.str] = None,
        readonly: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        """
        :param source: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#source Domain#source}.
        :param target: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#target Domain#target}.
        :param accessmode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#accessmode Domain#accessmode}.
        :param readonly: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#readonly Domain#readonly}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f24774ac0ebdaf04814b202ebc2c618d1df36202ec80a6a7a07793c5005c8a1)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument accessmode", value=accessmode, expected_type=type_hints["accessmode"])
            check_type(argname="argument readonly", value=readonly, expected_type=type_hints["readonly"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source": source,
            "target": target,
        }
        if accessmode is not None:
            self._values["accessmode"] = accessmode
        if readonly is not None:
            self._values["readonly"] = readonly

    @builtins.property
    def source(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#source Domain#source}."""
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#target Domain#target}."""
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accessmode(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#accessmode Domain#accessmode}."""
        result = self._values.get("accessmode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readonly(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#readonly Domain#readonly}."""
        result = self._values.get("readonly")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainFilesystem(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DomainFilesystemList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainFilesystemList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__75d8fc48026cd6dd2026e4f1654cb5e7ff450a5d4ed14206bcd12f15f821664f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DomainFilesystemOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc6fa75b380b921e39520cc51481a6f73fc4fcfa2013128da883a3340bea2bd9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DomainFilesystemOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17331764201939cdd5433acea5dbdc6e0e642cc820320fab276844b24edb4830)
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
            type_hints = typing.get_type_hints(_typecheckingstub__56df4a362d11d475475b21688af74e9917bdf63f6ed0458eec8273fc02cbb332)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f7e108c5ec13264f06aca827ab00162b3122d099ac5a483310051c01929a0f09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainFilesystem]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainFilesystem]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainFilesystem]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd423f84ac31c8416f8f5f8e35abd51054006b1883494141a33ae7ef4789440e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class DomainFilesystemOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainFilesystemOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5878b05698997a0467349cf1a0749497cd856a23604eb33619eff2db47d87828)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccessmode")
    def reset_accessmode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessmode", []))

    @jsii.member(jsii_name="resetReadonly")
    def reset_readonly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadonly", []))

    @builtins.property
    @jsii.member(jsii_name="accessmodeInput")
    def accessmode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessmodeInput"))

    @builtins.property
    @jsii.member(jsii_name="readonlyInput")
    def readonly_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readonlyInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="accessmode")
    def accessmode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessmode"))

    @accessmode.setter
    def accessmode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff033c4f3362bd1a63c7ff82b2c3d87d9ffd0950a2ec6d6afab48e224361a991)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessmode", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="readonly")
    def readonly(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readonly"))

    @readonly.setter
    def readonly(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__681665f1518f551ad4fce032b7d84937e6e5022648098e2960baff724bf246dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readonly", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23f6e250b7a12ef4e2dad7b63c1f61225b028b18ad29dca3ac0a8fd53644842f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a6dd2c6b7f933a0150129c75e3e43d8da96fb1e4d9bee62231ba419fbdd978d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainFilesystem]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainFilesystem]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainFilesystem]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4de6df821ace1b895c0a8a423624d2ababd98699f076b0179ddeead41f90e9b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.domain.DomainGraphics",
    jsii_struct_bases=[],
    name_mapping={
        "autoport": "autoport",
        "listen_address": "listenAddress",
        "listen_type": "listenType",
        "type": "type",
        "websocket": "websocket",
    },
)
class DomainGraphics:
    def __init__(
        self,
        *,
        autoport: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        listen_address: typing.Optional[builtins.str] = None,
        listen_type: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        websocket: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param autoport: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#autoport Domain#autoport}.
        :param listen_address: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#listen_address Domain#listen_address}.
        :param listen_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#listen_type Domain#listen_type}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#type Domain#type}.
        :param websocket: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#websocket Domain#websocket}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d5392c7f0813408749e4b6b0a8e64a69f07d4803a8b488b65597096956fe17d)
            check_type(argname="argument autoport", value=autoport, expected_type=type_hints["autoport"])
            check_type(argname="argument listen_address", value=listen_address, expected_type=type_hints["listen_address"])
            check_type(argname="argument listen_type", value=listen_type, expected_type=type_hints["listen_type"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument websocket", value=websocket, expected_type=type_hints["websocket"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if autoport is not None:
            self._values["autoport"] = autoport
        if listen_address is not None:
            self._values["listen_address"] = listen_address
        if listen_type is not None:
            self._values["listen_type"] = listen_type
        if type is not None:
            self._values["type"] = type
        if websocket is not None:
            self._values["websocket"] = websocket

    @builtins.property
    def autoport(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#autoport Domain#autoport}."""
        result = self._values.get("autoport")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def listen_address(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#listen_address Domain#listen_address}."""
        result = self._values.get("listen_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def listen_type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#listen_type Domain#listen_type}."""
        result = self._values.get("listen_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#type Domain#type}."""
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def websocket(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#websocket Domain#websocket}."""
        result = self._values.get("websocket")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainGraphics(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DomainGraphicsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainGraphicsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5121ce649f603f6a42f0f596afdd8b08a10b34a6f21e6e8e7f98ddd256b00c8d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAutoport")
    def reset_autoport(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoport", []))

    @jsii.member(jsii_name="resetListenAddress")
    def reset_listen_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetListenAddress", []))

    @jsii.member(jsii_name="resetListenType")
    def reset_listen_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetListenType", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetWebsocket")
    def reset_websocket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebsocket", []))

    @builtins.property
    @jsii.member(jsii_name="autoportInput")
    def autoport_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoportInput"))

    @builtins.property
    @jsii.member(jsii_name="listenAddressInput")
    def listen_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "listenAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="listenTypeInput")
    def listen_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "listenTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="websocketInput")
    def websocket_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "websocketInput"))

    @builtins.property
    @jsii.member(jsii_name="autoport")
    def autoport(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoport"))

    @autoport.setter
    def autoport(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f522aedaf067da86654019ccd618a4386c0c6334070b9f6e42e32d83bfb27bad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoport", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="listenAddress")
    def listen_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "listenAddress"))

    @listen_address.setter
    def listen_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8af68c1e948f663042b334d3be0333b3d2c40553ee5823bf6d1421a3d5e7732)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listenAddress", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="listenType")
    def listen_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "listenType"))

    @listen_type.setter
    def listen_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__771aef29c26059c3a7cdb604ef24e094948e3e31c48c11be05a5e95da2ef6648)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listenType", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d85512f170363c1198b56ddf90743f4cfca3e870941980f66540ed7136729462)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="websocket")
    def websocket(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "websocket"))

    @websocket.setter
    def websocket(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c8693dc4ef71228aba9aea0de42f0de1b63413685242bc3c44b3b7b1acfad53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "websocket", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DomainGraphics]:
        return typing.cast(typing.Optional[DomainGraphics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DomainGraphics]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b39d060fb38e80c4e486bfcaa297476a06e98f1994d4790d58e5eea81e71506a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.domain.DomainNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={
        "addresses": "addresses",
        "bridge": "bridge",
        "hostname": "hostname",
        "mac": "mac",
        "macvtap": "macvtap",
        "network_id": "networkId",
        "network_name": "networkName",
        "passthrough": "passthrough",
        "vepa": "vepa",
        "wait_for_lease": "waitForLease",
    },
)
class DomainNetworkInterface:
    def __init__(
        self,
        *,
        addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        bridge: typing.Optional[builtins.str] = None,
        hostname: typing.Optional[builtins.str] = None,
        mac: typing.Optional[builtins.str] = None,
        macvtap: typing.Optional[builtins.str] = None,
        network_id: typing.Optional[builtins.str] = None,
        network_name: typing.Optional[builtins.str] = None,
        passthrough: typing.Optional[builtins.str] = None,
        vepa: typing.Optional[builtins.str] = None,
        wait_for_lease: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        """
        :param addresses: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#addresses Domain#addresses}.
        :param bridge: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#bridge Domain#bridge}.
        :param hostname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#hostname Domain#hostname}.
        :param mac: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#mac Domain#mac}.
        :param macvtap: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#macvtap Domain#macvtap}.
        :param network_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#network_id Domain#network_id}.
        :param network_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#network_name Domain#network_name}.
        :param passthrough: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#passthrough Domain#passthrough}.
        :param vepa: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#vepa Domain#vepa}.
        :param wait_for_lease: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#wait_for_lease Domain#wait_for_lease}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b57cf7acb7a90973c1900b7a65f7b4ca029256d90dbf0b8ecf241c0891fc56a)
            check_type(argname="argument addresses", value=addresses, expected_type=type_hints["addresses"])
            check_type(argname="argument bridge", value=bridge, expected_type=type_hints["bridge"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument mac", value=mac, expected_type=type_hints["mac"])
            check_type(argname="argument macvtap", value=macvtap, expected_type=type_hints["macvtap"])
            check_type(argname="argument network_id", value=network_id, expected_type=type_hints["network_id"])
            check_type(argname="argument network_name", value=network_name, expected_type=type_hints["network_name"])
            check_type(argname="argument passthrough", value=passthrough, expected_type=type_hints["passthrough"])
            check_type(argname="argument vepa", value=vepa, expected_type=type_hints["vepa"])
            check_type(argname="argument wait_for_lease", value=wait_for_lease, expected_type=type_hints["wait_for_lease"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if addresses is not None:
            self._values["addresses"] = addresses
        if bridge is not None:
            self._values["bridge"] = bridge
        if hostname is not None:
            self._values["hostname"] = hostname
        if mac is not None:
            self._values["mac"] = mac
        if macvtap is not None:
            self._values["macvtap"] = macvtap
        if network_id is not None:
            self._values["network_id"] = network_id
        if network_name is not None:
            self._values["network_name"] = network_name
        if passthrough is not None:
            self._values["passthrough"] = passthrough
        if vepa is not None:
            self._values["vepa"] = vepa
        if wait_for_lease is not None:
            self._values["wait_for_lease"] = wait_for_lease

    @builtins.property
    def addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#addresses Domain#addresses}."""
        result = self._values.get("addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bridge(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#bridge Domain#bridge}."""
        result = self._values.get("bridge")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#hostname Domain#hostname}."""
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mac(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#mac Domain#mac}."""
        result = self._values.get("mac")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def macvtap(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#macvtap Domain#macvtap}."""
        result = self._values.get("macvtap")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#network_id Domain#network_id}."""
        result = self._values.get("network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#network_name Domain#network_name}."""
        result = self._values.get("network_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def passthrough(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#passthrough Domain#passthrough}."""
        result = self._values.get("passthrough")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vepa(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#vepa Domain#vepa}."""
        result = self._values.get("vepa")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_for_lease(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#wait_for_lease Domain#wait_for_lease}."""
        result = self._values.get("wait_for_lease")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainNetworkInterface(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DomainNetworkInterfaceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f369a300656ab1a975735ebf8e62fdb97aee818c65701eae450c83935719ed80)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DomainNetworkInterfaceOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5e842ff7a47a36c3485e0e0853b9b23024b348cb3f084ac838984f7d0896b19)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DomainNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79fa20fe886bb4cea4ebf7bc3abe20a044ae9cdb9a3deb226bc1e708fae3d0af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a57308e3dc17d976afc1d9d061cc5ea95cca285dbc17caaa01ca5e61bbd5fd6f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a810cb2dca56aebadbdd4800c1654859d40c3417f41e1e8d1c95e594cc4146d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f79ffce99e0b42f1583ec60ec4345aef3fba34adc5a7f1db14786eb1c9de86b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


class DomainNetworkInterfaceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1dffedc473ab0eff55e6afc4bc7fb9fca46f67932554f2baa94e63c33d81c4c0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAddresses")
    def reset_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddresses", []))

    @jsii.member(jsii_name="resetBridge")
    def reset_bridge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBridge", []))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetMac")
    def reset_mac(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMac", []))

    @jsii.member(jsii_name="resetMacvtap")
    def reset_macvtap(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMacvtap", []))

    @jsii.member(jsii_name="resetNetworkId")
    def reset_network_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkId", []))

    @jsii.member(jsii_name="resetNetworkName")
    def reset_network_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkName", []))

    @jsii.member(jsii_name="resetPassthrough")
    def reset_passthrough(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassthrough", []))

    @jsii.member(jsii_name="resetVepa")
    def reset_vepa(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVepa", []))

    @jsii.member(jsii_name="resetWaitForLease")
    def reset_wait_for_lease(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForLease", []))

    @builtins.property
    @jsii.member(jsii_name="addressesInput")
    def addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "addressesInput"))

    @builtins.property
    @jsii.member(jsii_name="bridgeInput")
    def bridge_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bridgeInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="macInput")
    def mac_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "macInput"))

    @builtins.property
    @jsii.member(jsii_name="macvtapInput")
    def macvtap_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "macvtapInput"))

    @builtins.property
    @jsii.member(jsii_name="networkIdInput")
    def network_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="networkNameInput")
    def network_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkNameInput"))

    @builtins.property
    @jsii.member(jsii_name="passthroughInput")
    def passthrough_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passthroughInput"))

    @builtins.property
    @jsii.member(jsii_name="vepaInput")
    def vepa_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vepaInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForLeaseInput")
    def wait_for_lease_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitForLeaseInput"))

    @builtins.property
    @jsii.member(jsii_name="addresses")
    def addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "addresses"))

    @addresses.setter
    def addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e2294639bbd1b615ad6586257640b7c48acf626a2338791402ab9d7e58f86e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addresses", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="bridge")
    def bridge(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bridge"))

    @bridge.setter
    def bridge(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eefb094f8c9982f81cec55a3621ff064552e74613c1f8803e776d90ca1bb1aea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bridge", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b2a538a7c553721b2789539da8b56e4b359c4f94a10a42d93c4da27ef29e063)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mac")
    def mac(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mac"))

    @mac.setter
    def mac(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e69d9e19f9e9891d999b2c2db28ce06c1dfecfa3beec5a0596b2b3e960abd9f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mac", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="macvtap")
    def macvtap(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macvtap"))

    @macvtap.setter
    def macvtap(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ce3ccdd26844864bc5dce612f3054db5f3a33550d7cc5beec6bebea449dbe53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "macvtap", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkId")
    def network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkId"))

    @network_id.setter
    def network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__833dffb83cb1dee96c96b384c5373c4daeaeec7d088c6b51bcd8f9db71a38c3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkId", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkName")
    def network_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkName"))

    @network_name.setter
    def network_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43049989b6583694bb2c0e4d8ec6aac10f64800c8ac50f9a9fff9b487be906ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkName", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="passthrough")
    def passthrough(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passthrough"))

    @passthrough.setter
    def passthrough(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6429482c09bfa1a8479d06e5f3f98e7105e3eca65fe2f59433729bcaf5a1235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passthrough", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vepa")
    def vepa(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vepa"))

    @vepa.setter
    def vepa(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36b1b87e886970a2fb7009b711701be8d149d3593716d4d86c49789aafc27235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vepa", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="waitForLease")
    def wait_for_lease(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitForLease"))

    @wait_for_lease.setter
    def wait_for_lease(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab5954348dc57b7ad436e857e44fbe6bc8ec51bf93547684044eb16593a4256a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForLease", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainNetworkInterface]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainNetworkInterface]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainNetworkInterface]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17605999a26f1c3e73316076849bd832a79819073eea44979faa2f93e0c1123d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.domain.DomainNvram",
    jsii_struct_bases=[],
    name_mapping={"file": "file", "template": "template"},
)
class DomainNvram:
    def __init__(
        self,
        *,
        file: typing.Optional[builtins.str] = None,
        template: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param file: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#file Domain#file}.
        :param template: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#template Domain#template}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bf51cbcbe6b4730fc469d50d9b5fa53da1bab117af7301824e545406f5fa46f)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if file is not None:
            self._values["file"] = file
        if template is not None:
            self._values["template"] = template

    @builtins.property
    def file(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#file Domain#file}."""
        result = self._values.get("file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#template Domain#template}."""
        result = self._values.get("template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainNvram(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DomainNvramOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainNvramOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c49fb5673d83b5687f82b4b8b292e91a3dadd3c6965ec08bda8a4baf304ccc7b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetTemplate")
    def reset_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="templateInput")
    def template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateInput"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "file"))

    @file.setter
    def file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3deacabd1b46ede9cf418bc158e742025a2cc19d2ceaa61f263e9c58921d1cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "file", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "template"))

    @template.setter
    def template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d25c43fc22d68687270f58c5ceba6a3f14fe733e4fcc83eb787b51481f8dd3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "template", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DomainNvram]:
        return typing.cast(typing.Optional[DomainNvram], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DomainNvram]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__940f3f366a9a398e7b39765b147a7e059c70310028b3fc012425e9083a92f4f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.domain.DomainTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class DomainTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        """
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#create Domain#create}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a61ce323290ba843e9592c0a6815dda87262655fc4b8c3bed7828c1c3b16c94c)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#create Domain#create}."""
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainTimeouts(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DomainTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ef085109e212125e44757347aa413c817498b49fc7c58e7b3c7129e455e88ba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec31cb1b737f7744ee7f52ff5734c80d592700fbf8ec6542b055439a8e80a0c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7459c88530b6af7b9e2d9640e6849d9f7fdf54096c213b6fd72049b45be0542)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.domain.DomainTpm",
    jsii_struct_bases=[],
    name_mapping={
        "backend_device_path": "backendDevicePath",
        "backend_encryption_secret": "backendEncryptionSecret",
        "backend_persistent_state": "backendPersistentState",
        "backend_type": "backendType",
        "backend_version": "backendVersion",
        "model": "model",
    },
)
class DomainTpm:
    def __init__(
        self,
        *,
        backend_device_path: typing.Optional[builtins.str] = None,
        backend_encryption_secret: typing.Optional[builtins.str] = None,
        backend_persistent_state: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        backend_type: typing.Optional[builtins.str] = None,
        backend_version: typing.Optional[builtins.str] = None,
        model: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param backend_device_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_device_path Domain#backend_device_path}.
        :param backend_encryption_secret: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_encryption_secret Domain#backend_encryption_secret}.
        :param backend_persistent_state: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_persistent_state Domain#backend_persistent_state}.
        :param backend_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_type Domain#backend_type}.
        :param backend_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_version Domain#backend_version}.
        :param model: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#model Domain#model}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__344b45b07fc1b3990b9aca1a5bc87cce888a1f866bd855329ddba0931adaac21)
            check_type(argname="argument backend_device_path", value=backend_device_path, expected_type=type_hints["backend_device_path"])
            check_type(argname="argument backend_encryption_secret", value=backend_encryption_secret, expected_type=type_hints["backend_encryption_secret"])
            check_type(argname="argument backend_persistent_state", value=backend_persistent_state, expected_type=type_hints["backend_persistent_state"])
            check_type(argname="argument backend_type", value=backend_type, expected_type=type_hints["backend_type"])
            check_type(argname="argument backend_version", value=backend_version, expected_type=type_hints["backend_version"])
            check_type(argname="argument model", value=model, expected_type=type_hints["model"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backend_device_path is not None:
            self._values["backend_device_path"] = backend_device_path
        if backend_encryption_secret is not None:
            self._values["backend_encryption_secret"] = backend_encryption_secret
        if backend_persistent_state is not None:
            self._values["backend_persistent_state"] = backend_persistent_state
        if backend_type is not None:
            self._values["backend_type"] = backend_type
        if backend_version is not None:
            self._values["backend_version"] = backend_version
        if model is not None:
            self._values["model"] = model

    @builtins.property
    def backend_device_path(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_device_path Domain#backend_device_path}."""
        result = self._values.get("backend_device_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backend_encryption_secret(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_encryption_secret Domain#backend_encryption_secret}."""
        result = self._values.get("backend_encryption_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backend_persistent_state(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_persistent_state Domain#backend_persistent_state}."""
        result = self._values.get("backend_persistent_state")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def backend_type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_type Domain#backend_type}."""
        result = self._values.get("backend_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backend_version(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#backend_version Domain#backend_version}."""
        result = self._values.get("backend_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#model Domain#model}."""
        result = self._values.get("model")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainTpm(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DomainTpmOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainTpmOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d5ad6976690aa75d705132be55b0c256da252a348df7cd4228650fb4958b21f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBackendDevicePath")
    def reset_backend_device_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendDevicePath", []))

    @jsii.member(jsii_name="resetBackendEncryptionSecret")
    def reset_backend_encryption_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendEncryptionSecret", []))

    @jsii.member(jsii_name="resetBackendPersistentState")
    def reset_backend_persistent_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendPersistentState", []))

    @jsii.member(jsii_name="resetBackendType")
    def reset_backend_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendType", []))

    @jsii.member(jsii_name="resetBackendVersion")
    def reset_backend_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendVersion", []))

    @jsii.member(jsii_name="resetModel")
    def reset_model(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModel", []))

    @builtins.property
    @jsii.member(jsii_name="backendDevicePathInput")
    def backend_device_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendDevicePathInput"))

    @builtins.property
    @jsii.member(jsii_name="backendEncryptionSecretInput")
    def backend_encryption_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendEncryptionSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="backendPersistentStateInput")
    def backend_persistent_state_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "backendPersistentStateInput"))

    @builtins.property
    @jsii.member(jsii_name="backendTypeInput")
    def backend_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="backendVersionInput")
    def backend_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="modelInput")
    def model_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelInput"))

    @builtins.property
    @jsii.member(jsii_name="backendDevicePath")
    def backend_device_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendDevicePath"))

    @backend_device_path.setter
    def backend_device_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf1d07dce46483435561e66a80c96042669158c1fc9d7702bae6faa0d6f4b1ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendDevicePath", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="backendEncryptionSecret")
    def backend_encryption_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendEncryptionSecret"))

    @backend_encryption_secret.setter
    def backend_encryption_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7088b68cc82e891e6145ed99e11a90b8f364eb8719a13ccadbc4cc519f529eb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendEncryptionSecret", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="backendPersistentState")
    def backend_persistent_state(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "backendPersistentState"))

    @backend_persistent_state.setter
    def backend_persistent_state(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76720c03d7417f20b42b32aaf96c9470062eb4d4e5f728ba68665533cd8fe20f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendPersistentState", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="backendType")
    def backend_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendType"))

    @backend_type.setter
    def backend_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__439b1fc60a2a7b90cf6c4d58e23715412c3e62f5f7a0b122524ac67310954ca2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendType", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="backendVersion")
    def backend_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendVersion"))

    @backend_version.setter
    def backend_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdcf4c339a95eb37f7c1af81bd744d112803d83988bc9ebb4f83aaf4c582deb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendVersion", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="model")
    def model(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "model"))

    @model.setter
    def model(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__524acb0d9b62f9dfd9cbae81434fc679f4287efe54f2191b73170d33959563cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "model", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DomainTpm]:
        return typing.cast(typing.Optional[DomainTpm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DomainTpm]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4850b7b29e284b7f4dc8d2ce607988196faf507101d309dccae33d2bdc4f1b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.domain.DomainVideo",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class DomainVideo:
    def __init__(self, *, type: typing.Optional[builtins.str] = None) -> None:
        """
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#type Domain#type}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7171f1403b128ae1b075be8eb7f361b9358714c650a48b4ff3b7c05709fe79ec)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#type Domain#type}."""
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainVideo(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DomainVideoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainVideoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cbc343989a7736b9f7c97fd4c74adeb0cca6254c791855299750e2163271e8ab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59793e5c052b17f3a9b239401872ce4d2a4b4d1a34137caa0d621dad32ed9c4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DomainVideo]:
        return typing.cast(typing.Optional[DomainVideo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DomainVideo]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35234c5d5fb013cc5bdba65c24a299dcb8b9628baf54af1f2f06393201e755f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.domain.DomainXml",
    jsii_struct_bases=[],
    name_mapping={"xslt": "xslt"},
)
class DomainXml:
    def __init__(self, *, xslt: typing.Optional[builtins.str] = None) -> None:
        """
        :param xslt: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#xslt Domain#xslt}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efcfa42120140ba5d532606c6cb2a6e7320db375607f744b1c128a989bb71424)
            check_type(argname="argument xslt", value=xslt, expected_type=type_hints["xslt"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if xslt is not None:
            self._values["xslt"] = xslt

    @builtins.property
    def xslt(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs/resources/domain#xslt Domain#xslt}."""
        result = self._values.get("xslt")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainXml(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


class DomainXmlOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.domain.DomainXmlOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9f725828c2839a02a40cabe2e0338b759f9c4dc0d9103abcef8b85acc530845)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eec4aa2a61da7b66cbf03e8e9caf4a49ebb1cbb09f85a961db20bc0798391d97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xslt", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DomainXml]:
        return typing.cast(typing.Optional[DomainXml], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[DomainXml]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11f15844567193022da0cf12d5d5e986f4e43b773eba9c10fd22338b58f555c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)  # pyright: ignore[reportArgumentType]


__all__ = [
    "Domain",
    "DomainBootDevice",
    "DomainBootDeviceList",
    "DomainBootDeviceOutputReference",
    "DomainConfig",
    "DomainConsole",
    "DomainConsoleList",
    "DomainConsoleOutputReference",
    "DomainCpu",
    "DomainCpuOutputReference",
    "DomainDisk",
    "DomainDiskList",
    "DomainDiskOutputReference",
    "DomainFilesystem",
    "DomainFilesystemList",
    "DomainFilesystemOutputReference",
    "DomainGraphics",
    "DomainGraphicsOutputReference",
    "DomainNetworkInterface",
    "DomainNetworkInterfaceList",
    "DomainNetworkInterfaceOutputReference",
    "DomainNvram",
    "DomainNvramOutputReference",
    "DomainTimeouts",
    "DomainTimeoutsOutputReference",
    "DomainTpm",
    "DomainTpmOutputReference",
    "DomainVideo",
    "DomainVideoOutputReference",
    "DomainXml",
    "DomainXmlOutputReference",
]

publication.publish()


def _typecheckingstub__f08ce5592300df3006f0dcfcf5ac2fd27b6f0c9fc6ec8053dc56d3f28a2a8e27(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    arch: typing.Optional[builtins.str] = None,
    autostart: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    boot_device: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainBootDevice, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
    cloudinit: typing.Optional[builtins.str] = None,
    cmdline: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Mapping[builtins.str, builtins.str]]]] = None,
    console: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainConsole, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
    coreos_ignition: typing.Optional[builtins.str] = None,
    cpu: typing.Optional[typing.Union[DomainCpu, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainDisk, typing.Dict[builtins.str, typing.Any]]]]] = None,
    emulator: typing.Optional[builtins.str] = None,
    filesystem: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainFilesystem, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
    firmware: typing.Optional[builtins.str] = None,
    fw_cfg_name: typing.Optional[builtins.str] = None,
    graphics: typing.Optional[typing.Union[DomainGraphics, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    initrd: typing.Optional[builtins.str] = None,
    kernel: typing.Optional[builtins.str] = None,
    machine: typing.Optional[builtins.str] = None,
    memory: typing.Optional[jsii.Number] = None,
    metadata: typing.Optional[builtins.str] = None,
    network_interface: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainNetworkInterface, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
    nvram: typing.Optional[typing.Union[DomainNvram, typing.Dict[builtins.str, typing.Any]]] = None,
    qemu_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    running: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[DomainTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    tpm: typing.Optional[typing.Union[DomainTpm, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
    vcpu: typing.Optional[jsii.Number] = None,
    video: typing.Optional[typing.Union[DomainVideo, typing.Dict[builtins.str, typing.Any]]] = None,
    xml: typing.Optional[typing.Union[DomainXml, typing.Dict[builtins.str, typing.Any]]] = None,
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


def _typecheckingstub__f07ca475ed20be22d520ab95c8d4b38da5e9eccf638c7b822809cf175b0ca649(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ce75af6d68e6a26edf8e0240dc67d9b99ab3ac7eff47bc99d416dd1ac2498429(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainBootDevice, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__af3f3564a2def969d9f74933d186e37d37ba6221d562696cc7a2d9538dc386d4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainConsole, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2e312859d46d5599c4e456366d708f960ff2fb1780e13e56f5921197aadaaf03(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainDisk, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__66a6f9cf9542ccb66d5fca1b18ebf2291ae8d4cde4b7678d9ada05a0afcd292a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainFilesystem, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b4ec0708232225d90dd6eac1b113af66556ccee2b1057f41a7b789a8fd413ea0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainNetworkInterface, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0a720164e9e10731dc47105f6c435ad111f261b4759095c5ffbffd3a838fdc96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2ac7b4f211596cd73824f42a9ececd56997da696c7dd9f59b34b17af84054235(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7408b99b8cffd9ebcf9f5325fdc4ad6f0c42e9d0e40fba43bfcd3a8bc5e30c5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c40aa4b535935ab323370a5926f65e3964823a388e0f008170d70e8d7247bc40(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d5d9f1ea52569ef408123331c22ac96299263d268cee934b97b587ba4338d284(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0d135d0953ad0314009200069377a33116cc8f1c5e70e72c873747d6102670fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3b7ecc1e7fa5bea8af302507fdce30eb164dd3d5482ae72bf5a5e5545667c956(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__058ad35768b28d6745fc41c014a93a7338568a35550d601f3a60f38b001f014b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4fc263b3b9de5c8b61189aa5574687547fff18fde3e758de2cbc56165ca170f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5897970913bed040adb4a2cbf98092a0712c803b81be91e8d621ee37ada3b77c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__716cdea228dbd9b0a78b8f5a4966714fa61d9f78fcb3c0dccca6a2cbcac7ae51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__87cbcb56e9329f1d84fe0e0d84b14c4583ab069ce791037296d4a2defb076932(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__345c0f122bff0cabd7972ac32125eff1d2389af58362513e042d9396f9cff014(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__115cdf3e8c4aca725cabf335be093158abfba8f13d6801c08f9c0ed0cfb93773(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__898915eed96cf0ef11a4b9a14a37531660e23f8e421720f4a94c8cd3b166e22e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e8899a70160a8366e43f32fee66a45fe54679d5ec7f845b71d67e449543f8999(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__aaa087b38638ac08ece9731a7689109ddd3329088011a30f97665d6e12fcc0af(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ebc4bb4ce2a15843391e0f3ffed8621b55eb1d70a99ea6479ee650046ede9907(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4e1c56b30bf522501d7e49a738aba9cfa62ad1f9d531a2a8d5a37815f7e67038(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a7f583c44b29d4f851d1d1c34446efe1f2bc23c4768684116bdf60368376d438(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4a40fa6125abf99453da6d5912f18a243a73b0e6bdbdbe0589af43890c9237a3(
    *,
    dev: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e6e0dfd0a7670c5b91ff78b88111b214e581ba1c9b74e74cae3a2e9958e300af(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8c0e610a46e72d33c53ef03483c00bd0d4b3e8da6e41794ba41bcfa3333a8a89(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__27711cf08ffe01ecf2849d6642be80eef4878c86649a60a1b88a8c8601e9f095(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a9e7fd30666e001211d5427b83d1ec6d4b60ea7ec3723c50cf2f3e3c0a7ad3a9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6d2bc3c909dc4400abdf3f53905641a42775473bd56130aefb86f02c512682cc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c358de4e713622f0b3ace66efa0a350939467a607aab61804164c0d2d3c18ee1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainBootDevice]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b2d32d61b7484b7a15128d0972a9d563fed457f86186d7ea51ba21953673de3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d237e03cce70e6983634e99cd373877a41383f16de7f0a44ae1402efe9296ad7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__433295b0bad9b4ff1a6d7552b392dc27380b2b36774f637ff912e0bb6e023db5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainBootDevice]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ae7067743acdda5e59683d1113f500a3766ee9aa2eeb14dcbec4975e742a63c4(
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
    arch: typing.Optional[builtins.str] = None,
    autostart: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    boot_device: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainBootDevice, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
    cloudinit: typing.Optional[builtins.str] = None,
    cmdline: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Mapping[builtins.str, builtins.str]]]] = None,
    console: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainConsole, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
    coreos_ignition: typing.Optional[builtins.str] = None,
    cpu: typing.Optional[typing.Union[DomainCpu, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    disk: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainDisk, typing.Dict[builtins.str, typing.Any]]]]] = None,
    emulator: typing.Optional[builtins.str] = None,
    filesystem: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainFilesystem, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
    firmware: typing.Optional[builtins.str] = None,
    fw_cfg_name: typing.Optional[builtins.str] = None,
    graphics: typing.Optional[typing.Union[DomainGraphics, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    initrd: typing.Optional[builtins.str] = None,
    kernel: typing.Optional[builtins.str] = None,
    machine: typing.Optional[builtins.str] = None,
    memory: typing.Optional[jsii.Number] = None,
    metadata: typing.Optional[builtins.str] = None,
    network_interface: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DomainNetworkInterface, typing.Dict[builtins.str, typing.Any]]]]
    ] = None,
    nvram: typing.Optional[typing.Union[DomainNvram, typing.Dict[builtins.str, typing.Any]]] = None,
    qemu_agent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    running: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    timeouts: typing.Optional[typing.Union[DomainTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    tpm: typing.Optional[typing.Union[DomainTpm, typing.Dict[builtins.str, typing.Any]]] = None,
    type: typing.Optional[builtins.str] = None,
    vcpu: typing.Optional[jsii.Number] = None,
    video: typing.Optional[typing.Union[DomainVideo, typing.Dict[builtins.str, typing.Any]]] = None,
    xml: typing.Optional[typing.Union[DomainXml, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0a1795b4c54d41b1dc98a48d23802135257a61afccea02837f4a58339e1f218b(
    *,
    target_port: builtins.str,
    type: builtins.str,
    source_host: typing.Optional[builtins.str] = None,
    source_path: typing.Optional[builtins.str] = None,
    source_service: typing.Optional[builtins.str] = None,
    target_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__48551f42e6acd60301b27b16165e969378452d63c571143dd4531198821f9eed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c8b9abe723384725f445eeeefecb30ec720f5306a9a74f92f3c2be9022a78467(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__75d7e23f91f80e0b09188b932f1765fd0ab20f37b844825e768d6b6138c2b21d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__da69cd4d6c1a5081df82430b2a6d25bf4f94e36dfd24867c458f20b9e6b90f6e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d755081f1ba47cf029ffd00d3c01d15a44c611478aa1b5981538bd28567f7e6f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__78037a96821755c96287a8f30f94a5e0672fca9186ac687ece4a1d76e1668841(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainConsole]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c24f4570548e1d065dd619c40fd2e5be945aa3a2f766cc88b45805a27903cb0a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c39b96707227cfffae16a410cf46b1d0d07b15f2e54bd051a4ccc8d3df4c7750(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__366a997a90ef83a32e4b4d7c1a08d52d743088a4d5944ac9cc69bdcea02e7271(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__367c9c2731c514b06d51c96f1965e9e1137605f9cb5b5b16879a7f99c61009dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d1b3cd746b765c1b4fcd489059a8803b233603f9dbe34ff549cd7bb192d4ad89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b96f4c2d34365b8ece351584b33920a472a3171da29bf3214448995e925d9e4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4d10e23c27da09131c01e4422c2a8ea40dc12fc66294c34ea08f49a5529329d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3c34235f3273a11931871c1aa0984933ac59b944920050d41595f68777310a94(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainConsole]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1e4a0e7dceef07956b36f0791dca27e23c6d36de24034b421f653ae35e3dc111(
    *,
    mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4392f36095f8c2033898406eb388b73b2e59340bce4a0dceda006c116bfeb7cc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__660e1f183345e917282c0062e5ad62bdcecd5dd1acf9518515fb6995dc998656(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6462972d4c39cbe81cc2cbdf014ce4c9e27d88f564e5fe517924e13187dcef0c(
    value: typing.Optional[DomainCpu],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a4e784fe06b91cb7b5dad6050e8ecca68f012b889a0ecba4963cc1f1b103e936(
    *,
    block_device: typing.Optional[builtins.str] = None,
    file: typing.Optional[builtins.str] = None,
    scsi: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    url: typing.Optional[builtins.str] = None,
    volume_id: typing.Optional[builtins.str] = None,
    wwn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f3df3892ce89bd814ab7712dcd929107c10449e4d7bcb8583d1ac3c44c0110e9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e955114a12834dd5b6c0883ab5e5215dd8bdb41504a574596ecb005b5cc47a99(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__251035cae2d5727ea3a7a7e29a0d002ad24517c4d2cc1cc5d0b003ad43439f9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__efd44d2c54097083797b2e526a195138bfd8a364dc3db6669eb90419999cfd65(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9076a2d220c97727839af9decba6b22be063fb197e479cf76733362c0e1871c1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cc3d7ce33f47ec94e553b077a64f893af9e7cdd495746f7112057fdc6f06ac17(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainDisk]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__80e5db5d2ef56c7d8e2dc136dd1994f81d34a6e9bd704b0e3acd25d996d43dbc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a33a9cd64763bb54ae3e0fb8843b7267174df1e2a84cc95e0438c2541f1dc0f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__521b885b3d37c2f575b1b39c97f77bdf356c99919313d7cef2044257938190f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8fb33ae601d695bc2b90e203b85d8da24430f927b649c6ba6036bd35f2535663(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__35513ae0684c0b819be55c4bb939146455e9698a9980df2352e43efcee420dd9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b165e682b62938fdf2f7a2a7536162136485bfcc1fd10373868e1e196bde8f67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cad529267d52139a8b6a76d8eef0626571bf8ebd997c11a7e3ea6155ef714b8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__166f0c6e1040de7df2273f702058a38062f5df392f2ed4efac412d6f6ba27ce2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainDisk]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4f24774ac0ebdaf04814b202ebc2c618d1df36202ec80a6a7a07793c5005c8a1(
    *,
    source: builtins.str,
    target: builtins.str,
    accessmode: typing.Optional[builtins.str] = None,
    readonly: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__75d8fc48026cd6dd2026e4f1654cb5e7ff450a5d4ed14206bcd12f15f821664f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cc6fa75b380b921e39520cc51481a6f73fc4fcfa2013128da883a3340bea2bd9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__17331764201939cdd5433acea5dbdc6e0e642cc820320fab276844b24edb4830(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__56df4a362d11d475475b21688af74e9917bdf63f6ed0458eec8273fc02cbb332(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f7e108c5ec13264f06aca827ab00162b3122d099ac5a483310051c01929a0f09(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cd423f84ac31c8416f8f5f8e35abd51054006b1883494141a33ae7ef4789440e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainFilesystem]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5878b05698997a0467349cf1a0749497cd856a23604eb33619eff2db47d87828(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ff033c4f3362bd1a63c7ff82b2c3d87d9ffd0950a2ec6d6afab48e224361a991(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__681665f1518f551ad4fce032b7d84937e6e5022648098e2960baff724bf246dd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__23f6e250b7a12ef4e2dad7b63c1f61225b028b18ad29dca3ac0a8fd53644842f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1a6dd2c6b7f933a0150129c75e3e43d8da96fb1e4d9bee62231ba419fbdd978d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4de6df821ace1b895c0a8a423624d2ababd98699f076b0179ddeead41f90e9b9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainFilesystem]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6d5392c7f0813408749e4b6b0a8e64a69f07d4803a8b488b65597096956fe17d(
    *,
    autoport: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    listen_address: typing.Optional[builtins.str] = None,
    listen_type: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    websocket: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5121ce649f603f6a42f0f596afdd8b08a10b34a6f21e6e8e7f98ddd256b00c8d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f522aedaf067da86654019ccd618a4386c0c6334070b9f6e42e32d83bfb27bad(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b8af68c1e948f663042b334d3be0333b3d2c40553ee5823bf6d1421a3d5e7732(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__771aef29c26059c3a7cdb604ef24e094948e3e31c48c11be05a5e95da2ef6648(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d85512f170363c1198b56ddf90743f4cfca3e870941980f66540ed7136729462(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6c8693dc4ef71228aba9aea0de42f0de1b63413685242bc3c44b3b7b1acfad53(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b39d060fb38e80c4e486bfcaa297476a06e98f1994d4790d58e5eea81e71506a(
    value: typing.Optional[DomainGraphics],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1b57cf7acb7a90973c1900b7a65f7b4ca029256d90dbf0b8ecf241c0891fc56a(
    *,
    addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
    bridge: typing.Optional[builtins.str] = None,
    hostname: typing.Optional[builtins.str] = None,
    mac: typing.Optional[builtins.str] = None,
    macvtap: typing.Optional[builtins.str] = None,
    network_id: typing.Optional[builtins.str] = None,
    network_name: typing.Optional[builtins.str] = None,
    passthrough: typing.Optional[builtins.str] = None,
    vepa: typing.Optional[builtins.str] = None,
    wait_for_lease: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f369a300656ab1a975735ebf8e62fdb97aee818c65701eae450c83935719ed80(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b5e842ff7a47a36c3485e0e0853b9b23024b348cb3f084ac838984f7d0896b19(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__79fa20fe886bb4cea4ebf7bc3abe20a044ae9cdb9a3deb226bc1e708fae3d0af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a57308e3dc17d976afc1d9d061cc5ea95cca285dbc17caaa01ca5e61bbd5fd6f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a810cb2dca56aebadbdd4800c1654859d40c3417f41e1e8d1c95e594cc4146d1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f79ffce99e0b42f1583ec60ec4345aef3fba34adc5a7f1db14786eb1c9de86b8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DomainNetworkInterface]]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1dffedc473ab0eff55e6afc4bc7fb9fca46f67932554f2baa94e63c33d81c4c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7e2294639bbd1b615ad6586257640b7c48acf626a2338791402ab9d7e58f86e4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__eefb094f8c9982f81cec55a3621ff064552e74613c1f8803e776d90ca1bb1aea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0b2a538a7c553721b2789539da8b56e4b359c4f94a10a42d93c4da27ef29e063(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e69d9e19f9e9891d999b2c2db28ce06c1dfecfa3beec5a0596b2b3e960abd9f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5ce3ccdd26844864bc5dce612f3054db5f3a33550d7cc5beec6bebea449dbe53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__833dffb83cb1dee96c96b384c5373c4daeaeec7d088c6b51bcd8f9db71a38c3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__43049989b6583694bb2c0e4d8ec6aac10f64800c8ac50f9a9fff9b487be906ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c6429482c09bfa1a8479d06e5f3f98e7105e3eca65fe2f59433729bcaf5a1235(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__36b1b87e886970a2fb7009b711701be8d149d3593716d4d86c49789aafc27235(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ab5954348dc57b7ad436e857e44fbe6bc8ec51bf93547684044eb16593a4256a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__17605999a26f1c3e73316076849bd832a79819073eea44979faa2f93e0c1123d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainNetworkInterface]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7bf51cbcbe6b4730fc469d50d9b5fa53da1bab117af7301824e545406f5fa46f(
    *,
    file: typing.Optional[builtins.str] = None,
    template: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c49fb5673d83b5687f82b4b8b292e91a3dadd3c6965ec08bda8a4baf304ccc7b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e3deacabd1b46ede9cf418bc158e742025a2cc19d2ceaa61f263e9c58921d1cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6d25c43fc22d68687270f58c5ceba6a3f14fe733e4fcc83eb787b51481f8dd3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__940f3f366a9a398e7b39765b147a7e059c70310028b3fc012425e9083a92f4f3(
    value: typing.Optional[DomainNvram],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a61ce323290ba843e9592c0a6815dda87262655fc4b8c3bed7828c1c3b16c94c(
    *,
    create: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1ef085109e212125e44757347aa413c817498b49fc7c58e7b3c7129e455e88ba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ec31cb1b737f7744ee7f52ff5734c80d592700fbf8ec6542b055439a8e80a0c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d7459c88530b6af7b9e2d9640e6849d9f7fdf54096c213b6fd72049b45be0542(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DomainTimeouts]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__344b45b07fc1b3990b9aca1a5bc87cce888a1f866bd855329ddba0931adaac21(
    *,
    backend_device_path: typing.Optional[builtins.str] = None,
    backend_encryption_secret: typing.Optional[builtins.str] = None,
    backend_persistent_state: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    backend_type: typing.Optional[builtins.str] = None,
    backend_version: typing.Optional[builtins.str] = None,
    model: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6d5ad6976690aa75d705132be55b0c256da252a348df7cd4228650fb4958b21f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bf1d07dce46483435561e66a80c96042669158c1fc9d7702bae6faa0d6f4b1ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7088b68cc82e891e6145ed99e11a90b8f364eb8719a13ccadbc4cc519f529eb2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__76720c03d7417f20b42b32aaf96c9470062eb4d4e5f728ba68665533cd8fe20f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__439b1fc60a2a7b90cf6c4d58e23715412c3e62f5f7a0b122524ac67310954ca2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cdcf4c339a95eb37f7c1af81bd744d112803d83988bc9ebb4f83aaf4c582deb4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__524acb0d9b62f9dfd9cbae81434fc679f4287efe54f2191b73170d33959563cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b4850b7b29e284b7f4dc8d2ce607988196faf507101d309dccae33d2bdc4f1b0(
    value: typing.Optional[DomainTpm],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7171f1403b128ae1b075be8eb7f361b9358714c650a48b4ff3b7c05709fe79ec(
    *,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cbc343989a7736b9f7c97fd4c74adeb0cca6254c791855299750e2163271e8ab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__59793e5c052b17f3a9b239401872ce4d2a4b4d1a34137caa0d621dad32ed9c4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__35234c5d5fb013cc5bdba65c24a299dcb8b9628baf54af1f2f06393201e755f1(
    value: typing.Optional[DomainVideo],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__efcfa42120140ba5d532606c6cb2a6e7320db375607f744b1c128a989bb71424(
    *,
    xslt: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a9f725828c2839a02a40cabe2e0338b759f9c4dc0d9103abcef8b85acc530845(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__eec4aa2a61da7b66cbf03e8e9caf4a49ebb1cbb09f85a961db20bc0798391d97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__11f15844567193022da0cf12d5d5e986f4e43b773eba9c10fd22338b58f555c9(
    value: typing.Optional[DomainXml],
) -> None:
    """Type checking stubs"""
    pass
