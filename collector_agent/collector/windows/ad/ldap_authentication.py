import datetime
import logging
import sys
import traceback
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal

from impacket.krb5 import constants
from impacket.krb5.asn1 import TGS_REP
from impacket.krb5.crypto import Enctype, Key
from impacket.krb5.gssapi import GSS_C_REPLAY_FLAG, GSS_C_SEQUENCE_FLAG
from impacket.krb5.kerberosv5 import (
    AP_REQ,
    Authenticator,
    CheckSumField,
    KerberosError,
    KerberosTime,
    SPNEGO_NegTokenInit,
    Ticket,
    TypesMech,
    encoder,
    getKerberosTGS,
    getKerberosTGT,
    noValue,
    seq_set,
)
from impacket.krb5.types import Principal
from ldap3 import ALL, ENCRYPT, KERBEROS, NTLM, SASL, SIMPLE, Connection, Server
from ldap3.operation.bind import bind_operation
from pyasn1.codec.der import decoder

if sys.platform == "linux":
    import gssapi

logger = logging.getLogger(__name__)


@dataclass
class TGT:
    tgt_blob: bytes
    cipher: Enctype
    key: Key
    session_key: Key


@dataclass
class TGS:
    tgs_blob: bytes
    cipher: Enctype
    key: Key
    session_key: Key


class LDAPAuthStrategy(ABC):
    @abstractmethod
    def get_ldap_connection(self):
        pass


class LDAPKerberosAuthenticationSPNEGO:
    """
    This class implements the LDAP Kerberos Authentication using the GSS_SPNEGO mechanism.
    See https://datatracker.ietf.org/doc/html/rfc4178.
    It leverages the Impacket library to obtain a valid Ticket Granting Service (TGS) ticket
    and constructs a valid AP_REQ
    Finally it builds a NegTokenInit message and sends it as an LDAP bind request via the
    ldap3 library.

    The primary reason for using Impacket is that the python-gssapi used in ldap3
    relies on the system’s Kerberos tools (kinit, klist, etc.).
    While this can be very handy, it doesn't meet the requirement of the collector (this tools).

    One major limitation is that ldap3 currently supports LDAP signing (also known as LDAP integrity)
    only for the MD5-Digest mechanism and GSSAPI which used system configuration.
    As a result, this class does not support Kerberos signing, since doing so would require a
    complete rewrite of the LDAP stack.
    """

    def __init__(self, dc_hostname: str, domain: str, kdc_ip: str, username: str, password: str):
        self.domain = domain
        self.kdc_ip = kdc_ip
        self.hostname = dc_hostname
        self.username = Principal(username, type=constants.PrincipalNameType.NT_PRINCIPAL.value)
        self.password = password

    def get_tgt(self) -> TGT | None:
        logger.info(f"Getting TGT for user {self.username}")
        try:
            tgt = TGT(
                *getKerberosTGT(self.username, self.password, self.domain, lmhash="", nthash="", kdcHost=self.kdc_ip)
            )
        except KerberosError:
            logger.warning("Failed to get a valid TGT")
            logger.warning(traceback.format_exc())
            return None
        else:
            return tgt

    def get_tgs(self, tgt: TGT, hostname: str) -> TGS | None:
        logger.info(f"Getting a TGS for user {self.username}")

        servername = Principal("ldap/%s" % hostname, type=constants.PrincipalNameType.NT_SRV_INST.value)
        try:
            tgs = TGS(*getKerberosTGS(servername, self.domain, self.kdc_ip, tgt.tgt_blob, tgt.cipher, tgt.session_key))
        except KerberosError:
            logger.warning("Failed to get a valid TGS")
            logger.warning(traceback.format_exc())
            return None
        else:
            return tgs

    """
        Returns a AP_REQ blob 
    """

    def get_ap_req(self, tgs: TGS) -> AP_REQ:
        # For more explanation see https://datatracker.ietf.org/doc/html/rfc4120#section-5.5.1
        # and https://datatracker.ietf.org/doc/html/rfc4121#section-4.1.1
        ap_req = AP_REQ()

        # Kerberos version
        ap_req["pvno"] = 5

        # AP REQ Magic Number
        ap_req["msg-type"] = 14

        # No option
        opts = []
        ap_req["ap-options"] = constants.encodeFlags(opts)

        # Extraction of the ticket from the tgs
        tgs_decoded, _ = decoder.decode(tgs.tgs_blob, asn1Spec=TGS_REP())
        ticket = Ticket().from_asn1(tgs_decoded["ticket"])
        # Add ticket to the AP_REQ
        seq_set(ap_req, "ticket", ticket.to_asn1)

        authenticator = Authenticator()
        authenticator["authenticator-vno"] = 5
        authenticator["crealm"] = self.domain
        seq_set(authenticator, "cname", self.username.components_to_asn1)

        now = datetime.datetime.now(datetime.UTC)
        authenticator["cusec"] = now.microsecond
        authenticator["ctime"] = KerberosTime.to_asn1(now)

        # Add checksum to authenticator
        authenticator["cksum"] = noValue
        authenticator["cksum"]["cksumtype"] = 0x8003
        chk_field = CheckSumField()
        chk_field["Lgth"] = 16
        chk_field["Flags"] = GSS_C_SEQUENCE_FLAG | GSS_C_REPLAY_FLAG

        authenticator["cksum"]["checksum"] = chk_field.getData()
        authenticator["seq-number"] = 0

        # Encrypted authenticator with the KDC key
        encoded_auth = encoder.encode(authenticator)

        # https://www.rfc-editor.org/rfc/rfc4757.html
        # These encryption types use key derivation.  With each message, the
        # message type (T) is used as a component of the keying material.
        # AP-REQ Authenticator (includes application authenticator
        # subkey), encrypted with the application session key (T=11)
        encrypted_auth = tgs.cipher.encrypt(tgs.session_key, 11, encoded_auth, None)

        ap_req["authenticator"] = noValue
        ap_req["authenticator"]["etype"] = tgs.cipher.enctype
        ap_req["authenticator"]["cipher"] = encrypted_auth

        return ap_req

    def get_ldap_connection(self) -> Connection | None:
        server = Server(f"ldap://{self.hostname}", get_info=ALL)
        conn = Connection(server, auto_referrals=False, auto_bind=False, authentication=SASL, sasl_mechanism=KERBEROS)
        conn.open(read_server_info=False)

        # Get a TGT from the KDC
        tgt = self.get_tgt()
        if tgt is None:
            logger.error("Unable to instanciate LDAP Connection ")
            return None

        tgs = self.get_tgs(tgt, self.hostname)
        if tgs is None:
            logger.error("Unable to instanciate LDAP Connection")
            return None

        # Create an AP REQ
        ap_req = self.get_ap_req(tgs)

        # Build an NegTokenInit
        # See https://www.rfc-editor.org/rfc/rfc4178.html#section-4.2.1
        neg_token_init = SPNEGO_NegTokenInit()
        neg_token_init["MechTypes"] = [TypesMech["MS KRB5 - Microsoft Kerberos 5"]]

        # We may use of the optimistic mechanism token.
        neg_token_init["MechToken"] = encoder.encode(ap_req)
        request = bind_operation(conn.version, SASL, "", None, conn.sasl_mechanism, neg_token_init.getData())

        response = conn.post_send_single_response(conn.send("bindRequest", request, None))[0]
        conn.result = response
        if response["result"] == 0:
            logger.error("Successfull authentification to the ldap server using Kerberos")
            conn.bound = True
            conn.refresh_server_info()
            return conn
        logger.error("Cannot authenticate to the ldap server")
        logger.error(f"Binding Failed : {conn.result}")
        return None


class LDAPKerberosAuthenticationGSSAPI(LDAPAuthStrategy):
    def __init__(self, hostname, domain: str, username: str, password: str):
        self.hostname = hostname
        self.domain = domain
        self.username = username
        self.password = password
        # Should realm is always the domain name in uppercase ?
        self.realm = domain.upper()

    def get_ldap_connection(self) -> Connection | None:
        server = Server(f"ldap://{self.hostname}", get_info=ALL)
        user = None
        creds = None
        if sys.platform == "linux":
            user = gssapi.Name(base=self.username + "@" + self.realm, name_type=gssapi.NameType.krb5_nt_principal_name)
            creds = gssapi.raw.acquire_cred_with_password(user, self.password.encode()).creds
        conn = Connection(
            server,
            auto_referrals=False,
            auto_bind=False,
            authentication=SASL,
            sasl_mechanism=KERBEROS,
            session_security=None,
            sasl_credentials=(None, None, creds),
        )
        if conn.bind():
            logger.info("Successfull authentification to the ldap server using Kerberos")
            return conn
        if conn.result.get("description") == "strongerAuthRequired":
            logger.info("LDAP server may require signing to authenticate")
            logger.info("Trying Kerberos authentication with signature")
            if sys.platform == "linux":
                user = gssapi.Name(
                    base=self.username + "@" + self.realm, name_type=gssapi.NameType.krb5_nt_principal_name
                )
                creds = gssapi.raw.acquire_cred_with_password(user, self.password.encode()).creds
            conn = Connection(
                server,
                auto_referrals=False,
                auto_bind=False,
                authentication=SASL,
                sasl_mechanism=KERBEROS,
                session_security=ENCRYPT,
                sasl_credentials=(None, None, creds),
            )
            if conn.bind():
                logger.info("Successfull authentification to the ldap server using kerberos signing")
                return conn

        logger.error("Cannot authenticate to the ldap server")
        logger.error(f"Binding Failed : {conn.result}")
        return None


class LDAPDigestMD5Authentication(LDAPAuthStrategy):
    def __init__(self, hostname: str, domain: str, username: str, password: str):
        self.hostname = hostname
        self.domain = domain
        self.username = username
        self.password = password

    def get_ldap_connection(self):
        server = Server(self.hostname, get_info=ALL)
        conn = Connection(
            server,
            user=self.username,
            password=self.password,
            authentication="SASL",
            lazy=False,
            sasl_mechanism="DIGEST-MD5",
            sasl_credentials=(None, self.username, self.password, None, None),
        )
        if conn.bind():
            logger.info("Successfull authentification to the ldap server using DIGEST-MD5")
            return conn
        if conn.result.get("description") == "strongerAuthRequired":
            logger.info("LDAP server may require signing to authenticate")
            logger.info("Trying MD5-DIGEST authentication with signature")
            conn = Connection(
                server,
                user=self.username,
                password=self.password,
                authentication="SASL",
                lazy=False,
                sasl_mechanism="DIGEST-MD5",
                sasl_credentials=(None, self.username, self.password, None, "sign"),
            )
        if conn.bind():
            logger.info("Successfull authentification to the ldap server using Digest-MD5 signing")
            return conn
        logger.error("Cannot authenticate to the ldap server")
        logger.error(f"Binding Failed : {conn.result}")
        return None


class LDAPSimpleBindAuthentication(LDAPAuthStrategy):
    def __init__(self, hostname: str, domain: str, username: str, password: str):
        self.domain = domain
        self.hostname = hostname
        self.username = username
        self.password = password

    def get_ldap_connection(self):
        server = Server(self.hostname, get_info=ALL)
        conn = Connection(server, user=self.username, password=self.password, authentication=SIMPLE)
        if conn.bind():
            logger.info("Successfull authentification to the ldap server using Kerberos")
            return conn
        logger.error("Cannot authenticate to the ldap server")
        logger.error(f"Binding Failed : {conn.result}")
        return None


class LDAPNTLMAuthentication(LDAPAuthStrategy):
    def __init__(self, hostname: str, domain: str, username: str, password: str):
        self.hostname = hostname
        self.domain = domain
        self.username = username
        self.password = password

    def get_ldap_connection(self) -> Connection | None:
        try:
            server = Server(self.hostname, get_info=ALL)
            user = f"{self.domain}\\{self.username}"

            conn = Connection(
                server,
                user=user,
                password=self.password,
                authentication=NTLM,
                auto_bind=False,
            )

            if conn.bind():
                logger.info("Successful authentication to the LDAP server using NTLM")
                return conn

            if conn.result.get("description") == "strongerAuthRequired":
                logger.info("LDAP server may require signing to authenticate")
                conn = Connection(
                    server,
                    user=user,
                    password=self.password,
                    authentication=NTLM,
                    auto_bind=False,
                    session_security="ENCRYPT",
                )
                if conn.bind():
                    logger.info("Successfull authentification to the ldap server using NTLM signing")
                    return conn
            logger.error("Cannot authenticate to the LDAP server using NTLM")
            logger.error(f"Binding failed: {conn.result}")
            return None

        except Exception as e:
            logger.error("Exception occurred during NTLM authentication")
            logger.error(str(e))
            return None


class LDAPAuthFactory:
    @classmethod
    def create(
        cls,
        auth_type: Literal["simple", "ntlm", "kerberos", "spnego"],
        dc_hostname: str,
        domain: str,
        username: str,
        password: str,
        kdc_ip: str | None = None,
    ) -> LDAPAuthStrategy | None:
        auth_type = auth_type.lower()
        ldap_auth = None
        if auth_type == "simple":
            ldap_auth = LDAPSimpleBindAuthentication(dc_hostname, domain, username, password)
        elif auth_type == "ntlm":
            ldap_auth = LDAPNTLMAuthentication(dc_hostname, domain, username, password)
        elif auth_type == "kerberos":
            ldap_auth = LDAPKerberosAuthenticationGSSAPI(dc_hostname, domain, username, password)
        elif auth_type == "spnego":
            ldap_auth = LDAPKerberosAuthenticationSPNEGO(dc_hostname, domain, kdc_ip, username, password)
        elif auth_type == "digest-md5":
            ldap_auth = LDAPDigestMD5Authentication(dc_hostname, domain, username, password)
        if ldap_auth is None:
            logger.error(f"Failed to instanciate an LDAP object with the authentication method {auth_type}")

        return ldap_auth
