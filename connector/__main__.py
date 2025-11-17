import argparse
import logging
import traceback
from dataclasses import dataclass
from pathlib import Path

from sqlalchemy.orm import Session

from model.db import reset_db
from model.fill_db import DBPopulate
from connector.base_parser import ParserAdData, ParserComputerData, ParserLinux
from connector.model import AdData, LocalComputerData, ModelDTO, LinuxData
from connector.mapper import (
    ADDomainMapper,
    ADUserMapper,
    ADMachineMapper,
    ADGroupMapper,
    IMapper,
    MachineMapper,
    GroupMapper,
    UserMapper,
    GPOResultMapper,
    FileMapper,
    FileRightsMapper,
    RootCimv2Mapper,
    ServicesMapper,
    SoftwaresMapper,
)
from connector.unitofwork import UnitOfWork


logger = logging.getLogger(__name__)


@dataclass
class Config:
    directory: str
    host: str
    database: str
    username: str
    password: str
    port: int


def parse_ldap(base_dir: Path) -> dict[str, dict]:
    # The ad directory follows the current hierarchy:
    # ad \ domain1 \ computer.json, gpo.json ...
    #    \ domain2 \ computer.json, gpo.json
    domain_dirs = [dir for dir in base_dir.iterdir() if dir.is_dir()]
    data_domains = {}
    for domain_dir in domain_dirs:
        domain_name = domain_dir.name
        parser = ParserAdData(domain_dir)
        ad_data = parser.get_data()

        if ad_data:
            sid_map = parser.get_sid_mapping()
            data_domains[domain_name] = {}
            data_domains[domain_name]["sid_map"] = sid_map
            data_domains[domain_name]["data"] = ad_data

        else:
            logger.error(f"Cannot import AD data for domain {domain_name}")
            continue
    return data_domains


def parse_computers(
    base_dir: Path, domain_sid_map: dict[str, object]
) -> list[LocalComputerData]:
    computer_dirs = [dir for dir in base_dir.iterdir() if dir.is_dir()]
    computers_data = {}
    for computer_dir in computer_dirs:
        computer_name = computer_dir.name
        parser = ParserComputerData(computer_dir, domain_sid_map, "json")
        computer_data = parser.get_data()
        if computer_data:
            computers_data[computer_name] = computer_data
        else:
            logger.error(f"Cannot import computer data for {computer_name}")
            traceback.print_exc()
            continue
    return computers_data


def parse_linux(base_dir: Path) -> list[LinuxData] | None:
    if not base_dir.exists():
        return None
    linux_machines = [dir for dir in base_dir.iterdir() if dir.is_dir()]
    results: list[LinuxData] = []
    for linux_machine in linux_machines:
        parser = ParserLinux(linux_machine)
        linux_data = parser.get_data()
        if linux_data:
            results.append(linux_data)
    return results


def populate_domain(db_populate: DBPopulate, model_dto: ModelDTO):
    mappers: list[IMapper] = [
        ADDomainMapper,
        MachineMapper,
        ADMachineMapper,
        ADUserMapper,
        ADGroupMapper,
        UserMapper,
        GroupMapper,
        RootCimv2Mapper,
        SoftwaresMapper,
        GPOResultMapper,
        ServicesMapper,
        FileMapper,
        FileRightsMapper,
    ]

    for mapper in mappers:
        with UnitOfWork(Session(db_populate.engine, autoflush=False)) as uow:
            orm_objects = mapper.to_orm(model_dto)
            uow.session.add_all(orm_objects)
            uow.session.commit()


def main(conf: Config) -> int:
    base_dir = Path(conf.directory)
    if not base_dir.exists():
        logger.critical(f"Cannot find directory: {conf.directory} ")
        return -1

    engine_path = (
        f"mysql+pymysql://{conf.username}:{conf.password}@{conf.host}:{conf.port}/"
    )

    # Workaround
    import model.db

    model.db.engine_base_path = engine_path

    db_populate = DBPopulate(engine_path, conf.database)
    reset_db(conf.database)

    ldap_dir = base_dir / "ad"
    if not ldap_dir.exists():
        logger.critical("Cannot find the directory containing LDAP data")
        return -1

    domains_data = parse_ldap(ldap_dir)

    local_computers = base_dir / "computers"
    if not local_computers.exists():
        logger.critical("Cannot find the directory containing Local Computer data")

    linux_dir = base_dir / "linux"

    for domain_name, domain_data in domains_data.items():
        local_computers_data = parse_computers(local_computers, domain_data["sid_map"])
        linux_data = parse_linux(linux_dir)
        model_dto = ModelDTO(
            ad_data=domain_data["data"],
            windows_local_data=local_computers_data,
            linux_local_data=linux_data,
        )
        populate_domain(db_populate, model_dto)

    return 0


def parse_cli() -> Config | None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory")
    parser.add_argument("-i", "--host", required=True)
    parser.add_argument("-db", "--database", required=True)
    parser.add_argument("-u", "--username", required=True)
    parser.add_argument("-p", "--password", required=True)
    parser.add_argument("--port", default=3306)

    args = vars(parser.parse_args())
    try:
        return Config(**args)
    except ValueError as e:
        logger.error(f"Error while unpacking arguments : {e}")
        return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    config = parse_cli()
    if config is None:
        exit(-1)
    exit(main(config))
