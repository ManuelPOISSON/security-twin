import logging
import os
import socket

import dns.resolver
import dns.reversename

logger = logging.getLogger(__name__)

def resolve_ip(hostname, dns_server=None):
    try:
        if dns_server:
            resolver = dns.resolver.Resolver()
            resolver.nameservers = [str(dns_server)]
            answers = resolver.resolve(hostname, "A")
            return answers[0].to_text()
        else:
            return socket.gethostbyname(hostname) 
    except (socket.gaierror, dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
        return None

def reverse_dns_query(ip_address, nameserver) -> list[str] | None:
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [nameserver]
    reverse_name = dns.reversename.from_address(ip_address)

    try:
        answer = resolver.resolve(reverse_name, 'PTR')
        return [ str(host) for host in answer ]
    except (socket.gaierror, dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout) as e:
        logger.warning(f"Failed to perform a reverse dns query for {ip_address} to the nameserver {nameserver} ")
        logger.warning(f"Exception : {e}")
        return None

def query_srv_record(domain: str, nameserver: str, timeout: int = 3):
    """
    Query SRV records for a domain using a specific DNS nameserver.

    Args:
        domain (str): The domain to query, e.g. '_kerberos._tcp.ad2016.local'
        nameserver (str): The DNS server IP to query
        timeout (int): Timeout in seconds (default: 3)

    Returns:
        list of dict: List of SRV records with priority, weight, port, and target
    """
    query = dns.message.make_query(domain, dns.rdatatype.SRV)
    
    try:
        response = dns.query.udp(query, nameserver, timeout=timeout)
    except Exception as e:
        print(f"[!] DNS query failed: {e}")
        return None

    srv_records = []
    for answer in response.answer:
        for item in answer:
            srv_records.append(str(item.target).rstrip('.'))

    return srv_records




def init_krb_context(controller: str, realm: str, kdc: str, output_directory: str):
    """
    Initializes a temporary Kerberos configuration for use with GSSAPI.

    This is necessary because GSSAPI relies on the Kerberos client configuration
    (krb5.conf) to locate the KDC and realm information. In environments where
    the system-wide configuration is missing or cannot be used, this function
    ensures GSSAPI can obtain credentials by providing the required context.
    """
    krb_conf = f"""
[libdefaults]
    default_realm = {realm.upper()}
[realms]
    {realm.upper()} = {{
        kdc = {controller}
        admin_server = {controller}
        default_domain = {realm.upper()}
    }}

    {realm} = {{
        kdc = {controller}
        admin_server = {controller}
        default_domain = {realm}
    }}
"""
    with open(f"{output_directory}/krb_temp.conf", "w") as f:
        logger.debug(f"Write Kerberos config file : {krb_conf}")
        f.write(krb_conf)
        os.environ["KRB5_CONFIG"] = f.name
        return True
    return False
