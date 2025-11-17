import importlib
import logging
import os
from pathlib import Path

import digitaltwin.templates as templates

from cdktf import Fn, TerraformOutput
from constructs import Construct

from digitaltwin.cdktf_api.providers.libvirt.domain import (
    Domain,
    DomainConsole,
    DomainDisk,
    DomainNetworkInterface,
)
from digitaltwin.cdktf_api.providers.libvirt.volume import Volume
from digitaltwin.cdktf_api.providers.libvirt.pool import Pool
from digitaltwin.cdktf_api.providers.libvirt.cloudinit_disk import CloudinitDisk
from digitaltwin.model.host_dto import HostDTO
from digitaltwin.os_store import os_store


def get_ssh_public_key() -> str:
    """
    Get SSH public key from default digitaltwin key, environment variable, or user's SSH keys.
    Returns the public key content or empty string if not found.
    """
    # First, try the default digitaltwin SSH key (highest priority)
    default_key_path = Path(__file__).parent.parent / "utils" / "id_rsa_linux.pub"
    if default_key_path.exists():
        try:
            with open(default_key_path, "r") as f:
                return f.read().strip()
        except Exception as e:
            logging.warning(f"Could not read default SSH key from {default_key_path}: {e}")
    
    # Second, try environment variable
    ssh_key = os.getenv("SSH_PUBLIC_KEY", "")
    if ssh_key:
        return ssh_key.strip()
    
    # Third, try to read from user's default SSH key locations
    home = Path.home()
    ssh_key_paths = [
        home / ".ssh" / "id_ed25519.pub",
        home / ".ssh" / "id_rsa.pub",
        home / ".ssh" / "id_ecdsa.pub",
    ]
    
    for key_path in ssh_key_paths:
        if key_path.exists():
            try:
                with open(key_path, "r") as f:
                    return f.read().strip()
            except Exception as e:
                logging.warning(f"Could not read SSH key from {key_path}: {e}")
                continue
    
    logging.warning("No SSH public key found. SSH key authentication will not be configured.")
    return ""


class LinuxHostLibvirt(Construct):
    def __init__(self, scope: Construct, host: HostDTO, pool: Pool):
        super().__init__(scope, host.id)
        tpl_path = importlib.resources.files(templates) / "linux"
        ssh_key = get_ssh_public_key()

        self.disks: list[DomainDisk] = []
        self.console = [
            DomainConsole(target_port="0", type="pty", target_type="serial")
        ]

        self.network_interfaces: list[DomainNetworkInterface] = []

        for interface in host.interfaces:
            self.network_interfaces.append(
                DomainNetworkInterface(
                    network_name=interface.net_name,
                    mac=interface.mac_address,
                    wait_for_lease=True if interface.dhcp else False,
                )
            )

        # Should volume initiation be included in host creation or in the infrastructure?
        self.volumes = []

        try:
            os_type_dict = os_store.get(host.os_type)
            if os_type_dict is None:
                raise KeyError(f"OS type '{host.os_type}' not found in os_store")
            os_dict = os_type_dict.get(host.os)
            if os_dict is None:
                raise KeyError(f"OS '{host.os}' not found for OS type '{host.os_type}' in os_store")
            version_dict = os_dict.get(host.version)
            if version_dict is None:
                raise KeyError(f"Version '{host.version}' not found for OS '{host.os}' (type '{host.os_type}') in os_store. Available versions: {list(os_dict.keys())}")
            url_base_image = version_dict.get("path")
            if url_base_image is None:
                raise KeyError(f"Path not found for version '{host.version}' of OS '{host.os}'")
        except (KeyError, AttributeError) as e:
            print(f"Error: Cannot retrieve the base image path from os_store: {e}")
            raise

        # For now, we just support one volume for simplicity
        self.volumes.append(
            Volume(
                self,
                id_=f"volume_host-{host.id}",
                name=f"volume_host-{host.id}",
                pool=pool.name,
                source=url_base_image,
                depends_on=[pool],
            )
        )

        for vol in self.volumes:
            self.disks.append(DomainDisk(volume_id=vol.id))

        template_file = tpl_path / "cloud-init" / "user-data.tftpl"
        cloud_init_data = Fn.templatefile(
            str(template_file),
            vars={
                "hostname": host.name,
                "ssh_key": ssh_key,
            },
        )

        network_file = tpl_path / "cloud-init" / "network-data.tftpl"

        network_data = Fn.templatefile(
            str(network_file),
            vars={
                "interfaces": [interface.__dict__ for interface in host.interfaces],
            },
        )

        self.cloud_init_disk = CloudinitDisk(
            self,
            id_=f"cloud_init_disk_{host.id}",
            name=f"cloud_init_disk_{host.id}",
            user_data=cloud_init_data,
            network_config=network_data,
            pool=pool.name,
            depends_on=[pool],
        )

        self.domain = Domain(
            self,
            id_=f"domain-{host.id}",
            name=host.name,
            vcpu=int(host.vcpu),
            memory=int(host.vmem),
            network_interface=self.network_interfaces,
            cloudinit=self.cloud_init_disk.id,
            console=self.console,
            disk=self.disks,
            depends_on=[pool],
        )
