import argparse
import logging
import sys
import traceback
from dataclasses import dataclass
from pathlib import Path

# Add project root to Python path to ensure correct imports
# This file is in parser_v2/, so we need to go up one level
script_dir = Path(__file__).parent
project_root = script_dir.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from sqlalchemy.orm import Session

from model.db import reset_db
from model.fill_db import DBPopulate
from parser_v2.base_parser import ParserAdData, ParserComputerData
from parser_v2.model import AdData, LocalComputerData, ModelDTO
from parser_v2.mapper import (
    ADDomainMapper,
    ADUserMapper,
    ADMachineMapper,
    ADGroupMapper,
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
from parser_v2.unitofwork import UnitOfWork


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
            traceback.print_exception()
            continue
    return computers_data


def populate_domain(
    db_populate: DBPopulate,
    domain_data: AdData,
    local_computers_data: dict[str, LocalComputerData],
):
 
    model_dto = ModelDTO(ad_data=domain_data, local_data=local_computers_data)

    with UnitOfWork(Session(db_populate.engine, autoflush=False)) as uow:
        ad_domain = ADDomainMapper.to_orm(model_dto)
        users = ADUserMapper.to_orm(model_dto)
        machines = MachineMapper.to_orm(model_dto)
        uow.session.add(ad_domain)
        uow.session.add_all(users)
        uow.session.add_all(machines)
        uow.session.commit()

        ad_machine = ADMachineMapper.to_orm(model_dto)
        uow.session.add_all(ad_machine)
        uow.session.commit()

        ad_groups = ADGroupMapper.to_orm(model_dto)
        uow.session.add_all(ad_groups)
        uow.session.commit()

        users = UserMapper.to_orm(model_dto)
        uow.session.add_all(users)
        uow.session.commit()

        group = GroupMapper.to_orm(model_dto)
        uow.session.add_all(group)
        uow.session.commit()

        cimv2 = RootCimv2Mapper.to_orm(model_dto)
        uow.session.add_all(cimv2)
        uow.session.commit()

        soft = SoftwaresMapper.to_orm(model_dto)
        uow.session.add_all(soft)
        uow.session.commit()

        gpo_policy = GPOResultMapper.to_orm(model_dto)
        uow.session.add_all(gpo_policy)
        uow.session.commit()

        services = ServicesMapper.to_orm(model_dto)
        uow.session.add_all(services)

        files = FileMapper.to_orm(model_dto)

        uow.session.add_all(files)
        uow.session.commit()

        files_rights = FileRightsMapper.to_orm(model_dto)
        uow.session.add_all(files_rights)
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
    from model import db as model_db

    model_db.engine_base_path = engine_path

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

    for domain_name, domain_data in domains_data.items():
        local_computers_data = parse_computers(local_computers, domain_data["sid_map"])
        populate_domain(db_populate, domain_data["data"], local_computers_data)

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
