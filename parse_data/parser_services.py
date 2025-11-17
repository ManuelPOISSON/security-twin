import logging
from pathlib import Path

from model import ServiceStatus
from parse_data.parser_ldap import ParserLDAP
from parse_data.translations import FR_TO_EN
from parse_data.utils import clean_sp_name


class ParserServices(ParserLDAP):

    DEFAULT_RUN_BY = "NT AUTHORITY\\SYSTEM"
    DEFAULT_STATUS = ServiceStatus.running
    DEFAULT_VERSION = "-1"
    IGNORED_ACLS = {
        "AUTORITÉ DE PACKAGE D’APPLICATION\\TOUS LES PACKAGES D’APPLICATION",
        "AUTORITÉ DE PACKAGE D’APPLICATION\\TOUS LES PACKAGES D’APPLICATION RESTREINTS",
        "Tout le monde",
    }

    def __init__(self, path_machine_dir: Path, domain: str = None) -> None:
        super().__init__(path_machine_dir, "services")
        if domain:
            self.domain = domain
        else:
            self.domain = ""

    def extract_acl(self, acl) -> dict[str, str]:
        """Extracts ACL information from the given ACL object."""
        if not acl:
            return {}
        acl_str = str(acl)
        for key_expected in ["FileSystemRights", "IdentityReference"]:
            if key_expected not in acl_str:
                logging.warning(
                    f"ACL does not contain 'FileSystemRights': {acl_str}. Returning empty dict."
                )
                return {}
        extracted = {}
        for ace in acl:
            if ace["IdentityReference"] in self.IGNORED_ACLS:
                logging.debug(f"Ignoring ACL for {ace['IdentityReference']}")
                continue
            key = clean_sp_name(ace["IdentityReference"], self.domain, translate=True)
            extracted[key] = ace["FileSystemRights"]
        return extracted

    def parse(self) -> tuple[list[dict[str, [str]]], dict[str, dict[str, str]]]:
        """Returns a tuple (list of service with their attributes, dict of file paths and rights per service).

        attribute run_by is set by default to NT AUTHORITY\\SYSTEM
        """
        services = []
        file_paths_and_rights_per_sp = {}
        for service in self.json_data:
            logging.debug(f"Parsing service: {service}")
            file_path = service[
                "Path"
            ].lower()  # in windows, paths are case-insensitive
            # TODO take into account case when machine OS is Linux and file paths are case-sensitive
            services.append(
                {
                    "name": service["ServiceName"],
                    "executable_path": file_path,
                    "run_by": service.get("RunAs", ParserServices.DEFAULT_RUN_BY),
                    "status": service.get("Status", ParserServices.DEFAULT_STATUS),
                    "version": service.get("Version", ParserServices.DEFAULT_VERSION),
                }
            )
            file_paths_and_rights_per_sp[file_path] = self.extract_acl(
                service.get("ACL", {})
            )
        """
            name=service["name"],
            version=service["version"],
            id_machine=machine,
            run_by=service["run_by"],
            port=service["port"],
            executable_path=service["executable_path"],
            status=service["status"],
        """
        return services, file_paths_and_rights_per_sp


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    path_machine = Path(
        "/home/manuel/Documents/mantis_amossys/dataamossys/collect_companyA_250716/cleaned/CN=PC-DR74,OU=PC,OU=Amossys,DC=dr,DC=amossys,DC=fr"
    )
    parser = ParserServices(path_machine)
    services, files = parser.parse()
    logging.info(f"Parsed services: {services}")
    logging.info(f"Parsed files: {files}")
    for k, v in files.items():
        logging.info(f"File: {k}, Rights: {v}")
        if "Everyone" in str(v):
            logging.warning(f"File {k} has 'Everyone' in its ACL: {v}")
            input("stop")
