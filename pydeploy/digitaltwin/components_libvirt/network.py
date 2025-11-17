from constructs import Construct

from digitaltwin.cdktf_api.providers.libvirt.network import Network
from digitaltwin.model.network_dto import NetworkDTO
from digitaltwin.utils.exceptions import RequirementException


class NetworkLibvirt(Construct):
    def __init__(self, scope, network: NetworkDTO):
        super().__init__(scope, network.id)
        if network.dhcp == "nat" and network.addresses is None:
            raise RequirementException

        dhcp = {"enabled": network.dhcp}
        Network(
            self,
            id_=network.id,
            name=network.name,
            mode=network.mode,
            dhcp=dhcp,
            autostart=True,
            addresses=network.addresses,
        )
