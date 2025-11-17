r"""
# `provider`

Refer to the Terraform Registry for docs: [`libvirt`](https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs).
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


class LibvirtProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="libvirt.provider.LibvirtProvider",
):
    """Represents a {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs libvirt}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        uri: builtins.str,
        alias: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs libvirt} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param uri: libvirt connection URI for operations. See https://libvirt.org/uri.html. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs#uri LibvirtProvider#uri}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs#alias LibvirtProvider#alias}
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aaa1d470b0dd5b725aca97d0a8eb2117840825d4609cbda47ef9ed6907f1878)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = LibvirtProviderConfig(uri=uri, alias=alias)

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        """Generates CDKTF code for importing a LibvirtProvider resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the LibvirtProvider to import.
        :param import_from_id: The id of the existing LibvirtProvider that should be imported. Refer to the {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the LibvirtProvider to import is found.
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__579446603dce0d9cdb9410cacf52ddf32276931ca28434735286ba729cf8bc50)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

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
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1eb25a499a2a1714d7f6e91f5f364988cfe093f9ae2a1c3103bfb0d83971fc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)  # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da5cbc1fc0dcde7314a045cad8dcb2483b7267ffa78608eb7ad8497d8e546661)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)  # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="libvirt.provider.LibvirtProviderConfig",
    jsii_struct_bases=[],
    name_mapping={"uri": "uri", "alias": "alias"},
)
class LibvirtProviderConfig:
    def __init__(
        self,
        *,
        uri: builtins.str,
        alias: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param uri: libvirt connection URI for operations. See https://libvirt.org/uri.html. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs#uri LibvirtProvider#uri}
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs#alias LibvirtProvider#alias}
        """
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e507654f6463fa479fc730eadc6d1e47f87cacb8ce5bb69896828be17d2e0023)
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "uri": uri,
        }
        if alias is not None:
            self._values["alias"] = alias

    @builtins.property
    def uri(self) -> builtins.str:
        """libvirt connection URI for operations. See https://libvirt.org/uri.html.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs#uri LibvirtProvider#uri}
        """
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        """Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/dmacvicar/libvirt/0.8.1/docs#alias LibvirtProvider#alias}
        """
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LibvirtProviderConfig(%s)" % ", ".join(k + "=" + repr(v) for k, v in self._values.items())


__all__ = [
    "LibvirtProvider",
    "LibvirtProviderConfig",
]

publication.publish()


def _typecheckingstub__2aaa1d470b0dd5b725aca97d0a8eb2117840825d4609cbda47ef9ed6907f1878(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    uri: builtins.str,
    alias: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__579446603dce0d9cdb9410cacf52ddf32276931ca28434735286ba729cf8bc50(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c1eb25a499a2a1714d7f6e91f5f364988cfe093f9ae2a1c3103bfb0d83971fc8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__da5cbc1fc0dcde7314a045cad8dcb2483b7267ffa78608eb7ad8497d8e546661(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e507654f6463fa479fc730eadc6d1e47f87cacb8ce5bb69896828be17d2e0023(
    *,
    uri: builtins.str,
    alias: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
