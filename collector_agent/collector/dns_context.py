import logging
import socket
from typing import Dict

main_logger = logging.getLogger(__name__)


class DNSContext:
    """
    This class implements a Monkey Patching to hook the method socket.getaddrinfo.
    ```
    with DNSContext(hosts) as dns_context:
        dns_context.hosts["krb.domain.com"] = 192.128.122.20
    ```
    or
    ```
        dns_context = DnsContext(hosts)
        dns_context.init()
        dns_context.hosts["krb.domain.com"] = 192.128.122.20
        dns_context.exit()

    ```
    """

    def __init__(self, hosts: Dict[str, str] | None = None, logger: logging.Logger | None = None):
        """
        override_dns : a dictionary {hostname: fake_ip} to override DNS resolution.
        hook_function : a custom function to replace getaddrinfo entirely.
                        If not provided, a default hook is used.
        """
        self.hosts = hosts or {}
        self.original_getaddrinfo = socket.getaddrinfo
        self.hook_function = self.hook_getaddrinfo
        if logger is not None:
            self.logger = logger
        else:
            self.logger = main_logger

    def hook_getaddrinfo(self, host, port, family=0, type=0, proto=0, flags=0):
        self.logger.debug(f"[DNSContext] Hooked getaddrinfo('{host}', {port})")

        if host in self.hosts:
            fake_ip = self.hosts[host]
            self.logger.debug(f"[DNSContext] Returning IP for {host}: {fake_ip}")
            return [(socket.AF_INET, socket.SOCK_STREAM, proto, "", (fake_ip, port))]

        # Fallback to the original getaddrinfo
        return self.original_getaddrinfo(host, port, family, type, proto, flags)

    def init(self):
        self.__enter__()

    def exit(self):
        self.__exit__(None, None, None)

    def __enter__(self):
        socket.getaddrinfo = self.hook_function
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        socket.getaddrinfo = self.original_getaddrinfo
