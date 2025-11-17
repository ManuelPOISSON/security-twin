from cdktf import TerraformStack

from digitaltwin.cdktf_api.providers.libvirt.network import Network
from digitaltwin.cdktf_api.providers.libvirt.pool import Pool
from digitaltwin.cdktf_api.providers.libvirt.provider import LibvirtProvider
from digitaltwin.cdktf_api.providers.libvirt.volume import Volume
from digitaltwin.components_libvirt.linux_host import LinuxHostLibvirt
from digitaltwin.components_libvirt.windows_host import WindowsHostLibvirt
from digitaltwin.components_libvirt.network import NetworkLibvirt
from digitaltwin.model.host_dto import HostDTO
from digitaltwin.model.network_dto import NetworkDTO
from digitaltwin.os_store import os_store


class InfrastructureLibvirt(TerraformStack):
    def __init__(self, scope, id: str, uri: str, hosts: list[HostDTO], networks: list[NetworkDTO], pool_path: str = None):
        super().__init__(scope, id)
        self.id = id
        self.provider = LibvirtProvider(self, "provider", uri=uri)
        self.networks = []
        self.hosts = []
        self.base_volume: dict = dict()
        if pool_path is None:
            self.pool_path = f"/opt/libvirt/pool_{id}"
        else:
            self.pool_path = pool_path
        for net in networks:
            self.networks.append(NetworkLibvirt(self, net))

        self.pool = Pool(
            self,
            id_=f"pool_{id}",
            name=f"pool_{id}",
            type="dir",
            target={"path": self.pool_path},
            depends_on=self.networks,
        )

        for host in hosts:
            if host.os_type == "linux":
                self.hosts.append(LinuxHostLibvirt(self, host, self.pool))
            elif host.os_type == "windows":
                path_base_image = os_store.get(host.os_type, {}).get(host.os, {}).get(host.version, {}).get("path")
                base_volumes = []
                if path_base_image not in self.base_volume:
                    self.base_volume[path_base_image] = Volume(
                        self,
                        id_=f"{host.os}-{host.version}.iso",
                        name=f"{host.os}-{host.version}.iso",
                        source=path_base_image,
                        format="raw",
                        pool=self.pool.name,
                        depends_on=[self.pool],
                    )

                base_volumes.append(self.base_volume[path_base_image])

                if os_store["virtio"]["path"] not in self.base_volume:
                    self.base_volume[os_store["virtio"]["path"]] = Volume(
                        self,
                        id_=f"virtio-driver.iso",
                        name=f"virtio-driver.iso",
                        source=os_store["virtio"]["path"],
                        format="iso",
                        pool=self.pool.name,
                        depends_on=[self.pool],
                    )
                base_volumes.append(self.base_volume[os_store["virtio"]["path"]])

                self.hosts.append(WindowsHostLibvirt(self, host, base_volumes))

    def update():
        pass
