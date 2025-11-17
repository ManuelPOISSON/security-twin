import json
import os
import sys

from dotenv import load_dotenv

load_dotenv(override=True)


class HostFactory:

    hosts_count = 0

    @classmethod
    def create_host(cls, suffix: str, os_data: str, disk_size: str = "40GB"):
        prefix = os.getenv("PREFIX_VM_NAME", "")
        subnet = os.getenv("SUBNET", "100")

        os_data_split = os_data.split(",")
        ALLOWED_OS = ("windows,windows10,21H2", "windows,server19,17763.737", "linux,debian,20250811-2201")
        if len(os_data_split) != 3:
            print(f"Error: os_data '{os_data}' is not in the correct format 'os_type,os,version' (example: 'windows,windows10,21H2')")
            sys.exit(1)
        if os_data not in ALLOWED_OS:
            print(f"Error: os_data '{os_data}' is not in the allowed OS list: {ALLOWED_OS}")
            sys.exit(1)
        os_type, os_name, version = os_data_split
        cls.hosts_count += 1

        # Configure network settings based on OS type
        if os_type == "linux":
            # Linux/Debian configuration
            interface_name = "ens3"
            dhcp = "True"
            ipv4_address = f"192.168.{subnet}.{100 + cls.hosts_count - 1}/24"
            gateway = f"192.168.{subnet}.254"
        else:
            # Windows configuration
            interface_name = "Ethernet Instance 0"
            dhcp = "False"
            ipv4_address = f"192.168.{subnet}.254/24"
            gateway = "192.168.1.254"

        return {
            "id": f"S-{cls.hosts_count - 1}",
            "name": f"{prefix}{suffix}",
            "vmem": "4096",
            "disk_size": disk_size,
            "vcpu": "2",
            "os_type": os_type,
            "os": os_name,
            "version": version,
            "interfaces": [
                {
                    "net_name": os.getenv("NETWORK_NAME", "intnet0"),
                    "interface_name": interface_name,
                    "mac_address": f"c0:47:0e:6a:b0:a{cls.hosts_count - 1}",
                    "dhcp": dhcp,
                    "ipv4_address": ipv4_address,
                    "ipv4_netmask": "255.255.255.0",
                    "gateway": gateway,
                }
            ],
        }


network_name = os.getenv("NETWORK_NAME", "intnet0")
networks = [
    {
        "id": "N-0",
        "name": network_name,
        "mode": "nat",
        "addresses": ["192.168." + os.getenv("SUBNET", "100") + ".0/24"],
        "dhcp": True,
    },
]


def gen_hosts_model(input_hosts_file: str, output_hosts_model: str):
    if not os.path.isfile(input_hosts_file):
        print(f"Error: Input hosts file '{input_hosts_file}' does not exist.")
        sys.exit(1)
    with open(input_hosts_file, "r") as f:
        input_hosts = f.readlines()
    host_factory = HostFactory()
    model_hosts = []
    for host_line in input_hosts:
        suffix, os_data, disk_size = host_line.strip().split(";")
        print(f"Creating host: suffix={suffix}, os_data={os_data}, disk_size={disk_size}")
        model_hosts.append(host_factory.create_host(suffix, os_data, disk_size))

    json.dump(
        {
            "hosts": model_hosts,
            "networks": networks,
        },
        open(output_hosts_model, "w"),
        indent=2,
    )
