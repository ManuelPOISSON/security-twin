import importlib

import digitaltwin.templates as templates

from cdktf import Fn
from constructs import Construct

from digitaltwin.os_store import os_store
from digitaltwin.model.host_dto import HostDTO
from digitaltwin.cdktf_api.providers.libvirt.domain import (
    Domain,
    DomainDisk,
    DomainNetworkInterface,
    DomainConsole,
    DomainBootDevice,
    DomainXml,
)
from digitaltwin.cdktf_api.providers.libvirt.pool import Pool
from digitaltwin.cdktf_api.providers.libvirt.volume import Volume
from digitaltwin.components_libvirt.utils import size_to_bytes, ISO


class WindowsHostLibvirt(Construct):
    def __init__(
        self,
        infra,
        host: HostDTO,
        base_volumes: list[Volume],
        optimized: bool = True,
    ):
        super().__init__(infra, host.id)
        self.volumes: list[Volume] = []
        self.network_interfaces: list[DomainNetworkInterface] = []
        self.disks: list[DomainDisk] = []
        self.console: list[DomainConsole]
        self.boot_device: list[DomainBootDevice]
        self.iso_path: list[str] = []
        self.custom_iso: Volume = None
        self.optimized = optimized
        self.console = [DomainConsole(target_port="0", type="pty", target_type="serial")]
        self.boot_device = [DomainBootDevice(dev=["hd", "cdrom"])]

        tpl_path = importlib.resources.files(templates) / "windows"

        xml: DomainXml = None
        if optimized:
            xml = DomainXml(xslt=Fn.file(str(tpl_path / "optimization.xslt")))

        unattend_file = tpl_path / host.os / "autounattend.xml"
        script_path = tpl_path / "enable_winrm.ps1"
        iso_path = f"/tmp/dvd-{infra.id}-{host.id}.iso"
        iso = ISO(iso_path)
        iso.add_file(unattend_file, "autounattend.xml")
        iso.add_file(script_path, "WinRm.ps1")
        iso.write()
        self.iso_path.append(iso_path)

        for interface in host.interfaces:
            self.network_interfaces.append(
                DomainNetworkInterface(
                    network_name=interface.net_name,
                    mac=interface.mac_address,
                    wait_for_lease=True if interface.dhcp == "True" else False,
                )
            )

        # For now, we just support one volume for simplicity
        self.volumes.append(
            Volume(
                self,
                id_=f"main-volume-{host.id}",
                name=f"main-volume-{host.id}",
                pool=infra.pool.name,
                size=size_to_bytes(host.disk_size),
            )
        )

        iso_path = Volume(self, id_=f"{host.id}-unattend", name=f"{host.id}-unattend.iso", source=f"{iso_path}", format="raw", pool=infra.pool.name)
        # Disk creation
        for vol in self.volumes:
            self.disks.append(DomainDisk(volume_id=vol.id))

        for vol in base_volumes:
            self.disks.append(DomainDisk(file=f"{infra.pool_path}/{vol.name}"))

        self.disks.append(DomainDisk(file=f"{infra.pool_path}/{host.id}-unattend.iso"))

        self.domain = Domain(
            self,
            id_=f"domain-{host.id}",
            machine="q35",
            vcpu=int(host.vcpu),
            name=host.name,
            memory=int(host.vmem),
            network_interface=self.network_interfaces,
            console=self.console,
            boot_device=self.boot_device,
            disk=self.disks,
            depends_on=base_volumes + [iso_path],
            xml=xml,
        )
