#!/usr/bin/env python3
import logging
import os
import json
import sys

from typing import Optional, Type, Any
import argparse

from sqlalchemy import create_engine, select, Engine
from sqlalchemy.orm import Session

from .db import reset_db, print_non_empty_tables, engine_base_path

from .model import (
    MachineWindows,
    ADMachine,
    ADDomain,
    ADUser,
    User,
    RootCimv2,
    RootCimv2Rights,
    Group,
    GroupMemberUser,
    GroupMemberADUser,
    GroupMemberADGroup,
    RunasCreds,
    RunasImpersonated,
    ADGroup,
    ADGroupMemberADUser,
    ADGroupMemberADGroup,
    SecurityPrincipal,
    File,
    FileRight,
    Service,
    GPOResult,
    TypeSp,
    Software,
    Machine,
)
from .db_connect import connection_cred
from parse_data.parser_services import ParserServices


def print_args(func):
    def wrapper(*args, **kwargs):
        args_and_types = ""
        print(f"Calling function {func.__name__}")
        for arg in args:
            args_and_types += f"{arg}:{type(arg)} "  # noqa E231
        print(f"Arguments: {args_and_types}, Keyword Arguments: {kwargs}")
        return func(*args, **kwargs)

    return wrapper


def is_userorgroup(
    engine: Engine,
    known_match: dict = None,
    sp_name: str = None,
    sp_id: int = None,
    machinename: Optional[str] = None,
) -> tuple[TypeSp | None, SecurityPrincipal | None]:
    """
    sp_name or sp_id must be defined

    :param engine:
    :param sp_name: name of a user or a group
    :param sp_id: id of a user or a group
    :param machinename: name of a machine (for local user/group)
    :return: (type, obj) if one object is found, (None, None) otherwise.
     Type is one of TypeSp.user, TypeSp.group, TypeSp.ADuser, TypeSp.ADgroup.
     If machinename is not None, first search in AD, then in local users/groups.
    """
    if sp_id is None and sp_name is None:
        raise ValueError("You must provide either sp_id or sp_name")
    if sp_name and not isinstance(sp_name, str):
        raise TypeError(f"{sp_name=} must be a string")
    elif sp_id:
        sp_id = int(sp_id)
    match_key = f"{sp_id}-{sp_name}-{machinename}"
    if known_match is not None:
        if match_key in known_match:
            match = known_match[match_key]
            if match is None:
                return None, None
            return match.type, match

    with Session(engine) as session:
        # filter on objects with attribute id == sp_id
        if sp_id is not None:
            stmt = select(SecurityPrincipal).filter(SecurityPrincipal.id == sp_id)
            new_obj = session.scalars(stmt).all()

        # filter on objects with attribute name == sp_name
        elif sp_name is not None:
            new_obj = []
            for cls in (User, ADUser, Group, ADGroup):
                q = session.query(cls).filter(cls.name == sp_name)
                new_obj.extend(q.all())

        if machinename is not None:
            new_obj_machine = []
            for object in new_obj:
                if object.type == TypeSp.ADuser or object.type == TypeSp.ADgroup:
                    new_obj_machine.append(object)
                elif object.id_machine == machinename:
                    new_obj_machine.append(object)

            new_obj = new_obj_machine
        # TODO take into account domain name
        if len(new_obj) == 0:
            print(f"\033[91m{sp_name=} {sp_id=} {machinename=} not found\033[0m")
            to_return = None, None
        elif len(new_obj) > 1:
            print(
                f"\033[91m{sp_name=} {sp_id=} {machinename=} found multiple times\033[0m"
            )
            to_return = None, None
        else:
            ##### unexplainable but important to make the code work as expected ####
            # Due to some obscure reason, calling new_obj[0].name actually instantiates the object properties

            # print("wierd vars", vars(new_obj[0]))
            new_obj[0].name
            # print("wierd vars", vars(new_obj[0]))
            to_return = new_obj[0].type, new_obj[0]

        ##### unexplainable but important to make the code work as expected ####
        if known_match is not None:
            known_match[match_key] = to_return[1]
        return to_return


class DBPopulate:
    def __init__(
        self,
        engine_base_path: str,
        db_name: str,
    ):
        self.engine = create_engine(f"{engine_base_path}{db_name}")
        self.known_match = {}

    def add_root_cimv2(self, machine: str, userorgroup: str, rights: list[str]) -> None:
        """
        example call add_root_cimv2("UniPalais", "Marchombres", ["Enable", "RemoteAccess"])

        :param machine:
        :param userorgroup: name of an (AD)user or an (AD)group
        :param rights:
        :return:
        """
        with Session(self.engine) as session:
            sp_type, user_or_group = is_userorgroup(
                self.engine,
                known_match=self.known_match,
                sp_name=userorgroup,
                machinename=machine,
            )
            if user_or_group is None:
                raise ValueError(
                    f"{userorgroup} is neither a valid name for user nor a group (AD or local)"
                )

            root_cimv2_entry = RootCimv2(
                id_machine=machine,
                id_sp=user_or_group.id,
                rights=list([RootCimv2Rights(right=right) for right in rights]),
            )
            session.add(root_cimv2_entry)
            session.commit()

    def add_runas_creds(
        self, win_machine_name: str, can_runas: str, users_impersonated: list[str]
    ):
        """
        example add_runas_creds("opForet", "pilipip.petit", ["sayanel.lyvant"])

        :param win_machine_name:
        :param can_runas:
        :param users_impersonated:
        :return:
        """
        with Session(self.engine) as session:
            # get id of user with name can_runas
            sp_type, obj = is_userorgroup(
                self.engine,
                known_match=self.known_match,
                sp_name=can_runas,
                machinename=win_machine_name,
            )
            if sp_type not in [TypeSp.user, TypeSp.ADuser]:
                raise ValueError(f"{can_runas=} is neither a valid user nor an AD user")
            elif sp_type == TypeSp.user:
                # local user
                runas_creds = RunasCreds(
                    id_machine=win_machine_name, can_runas_local=obj.id
                )
            elif sp_type == TypeSp.ADuser:
                # AD
                runas_creds = RunasCreds(
                    id_machine=win_machine_name, can_runas_AD=obj.id
                )
            session.add(runas_creds)
            session.commit()
            for user_impersonated in users_impersonated:
                sp_type, user_object = is_userorgroup(
                    self.engine, known_match=self.known_match, sp_name=user_impersonated
                )
                if sp_type not in [TypeSp.user, TypeSp.ADuser]:
                    raise ValueError(
                        f"{user_impersonated=} is neither a valid user nor an AD user"
                    )
                elif sp_type == TypeSp.user:
                    session.add(
                        RunasImpersonated(
                            runas_id=runas_creds.id, user_loc=user_object.id
                        )
                    )
                elif sp_type == TypeSp.ADuser:
                    session.add(
                        RunasImpersonated(
                            runas_id=runas_creds.id, user_AD=user_object.id
                        )
                    )
            session.commit()

    def add_machines(self, machines: list[Machine]):
        """
        Add a list of Machine (or MachineWindows or MachineLinux) to the database
        :param win_machines: list of MachineWindows objects
        :return:
        """
        with Session(self.engine) as session:
            session.add_all(machines)
            session.commit()

    def add_localgroup(
        self, win_machine_name: str, lg_name: str, lg_members: list[str]
    ):
        """
        example call add_localgroup("windowsEnterpriseVm2", "Remote Desktop Users", ['Marchombres'])

        :param win_machine_name:
        :param lg_name:
        :param lg_members: names' list of (AD)users or (AD)groups
        :return:
        """
        # TODO change win_machine var name
        with Session(self.engine) as session:
            # create group
            group_obj = Group(id_machine=win_machine_name, name=lg_name)
            session.add(group_obj)
            session.commit()
            # add group members
            for member_name in lg_members:
                sp_type, user_or_group = is_userorgroup(
                    self.engine,
                    known_match=self.known_match,
                    sp_name=member_name,
                    machinename=win_machine_name,
                )
                if user_or_group is None:
                    raise ValueError(
                        f"{win_machine_name=} {lg_name=} {member_name=} is neither a valid user nor a group"
                    )

                elif sp_type == TypeSp.user:
                    print(f"add user {win_machine_name} {lg_name} {user_or_group}")
                    if user_or_group.id_machine != group_obj.id_machine:
                        raise ValueError(
                            f"tried to add local user from {user_or_group.id_machine} to local group of {group_obj.id_machine}"
                        )
                    session.add(
                        GroupMemberUser(member=user_or_group.id, member_of=group_obj.id)
                    )
                elif sp_type == TypeSp.group:
                    raise ValueError(
                        f"You cannot add a group to a group (on {user_or_group.id_machine}, "
                        f"tried to add '{user_or_group.name}' to group '{lg_name}')"
                    )
                elif sp_type == TypeSp.ADuser:
                    session.add(
                        GroupMemberADUser(
                            member=user_or_group.id, member_of=group_obj.id
                        )
                    )
                elif sp_type == TypeSp.ADgroup:
                    session.add(
                        GroupMemberADGroup(
                            member=user_or_group.id, member_of=group_obj.id
                        )
                    )
                else:
                    raise ValueError(f"Unknown type {sp_type} {user_or_group}")
            session.commit()

    def add_localgroups_current_machine(
        self, machine_name: str, localgroups: dict[str, list[str]]
    ):
        for lg_name, lg_members in localgroups.items():
            self.add_localgroup(machine_name, lg_name, lg_members)

    def add_localusers(self, machine: str, localusers: dict[str, str]):
        with Session(self.engine) as session:
            for username, password in localusers.items():
                print(f"add user {username} with {password=} to {machine}")
                session.add(User(name=username, password=password, id_machine=machine))
            session.commit()

    def add_ad_adusers_admachines(self, AD, ad_users, ad_machines):
        with Session(self.engine) as session:
            session.add(AD)
            session.commit()
            session.add_all(ad_users)
            session.add_all(ad_machines)
            session.commit()

    def add_adusers(self, ad_users: list[ADUser]):
        with Session(self.engine) as session:
            session.add_all(ad_users)
            session.commit()

    def add_all_adgroups(self, domain: str, all_adgroups: dict[str, list[str]]):
        """
        add ad_groups to the database and populate them with members
        :param domain:
        :param all_adgroups: dict [group_name: [members0, member1]]
        :return:
        """
        with Session(self.engine) as session:
            # create all ad_groups
            session.add_all(
                [
                    ADGroup(id_domain=domain, name=group_name)
                    for group_name in all_adgroups.keys()
                ]
            )
            session.commit()
            logging.debug(
                f"Added {len(all_adgroups)} AD groups to domain {domain}\n"
                f"Populating with members..."
            )
            # populate ad_groups
            for group_name, group_members in all_adgroups.items():
                if len(group_members) < 1:
                    continue
                # get id of ad group containing group_members
                ad_group: Type[ADGroup] = (
                    session.query(ADGroup)
                    .filter_by(name=group_name, id_domain=domain)
                    .first()
                )
                if ad_group is None:
                    raise ValueError(
                        f"No AD group named {group_name} in domain {domain}"
                    )
                for member_name in group_members:
                    sp_type, obj = is_userorgroup(
                        self.engine, known_match=self.known_match, sp_name=member_name
                    )
                    if sp_type == TypeSp.ADuser:
                        session.add(
                            ADGroupMemberADUser(member=obj.id, member_of=ad_group.id)
                        )
                    elif sp_type == TypeSp.ADgroup:
                        session.add(
                            ADGroupMemberADGroup(member=obj.id, member_of=ad_group.id)
                        )
                    else:
                        logging.warning(
                            f"{member_name} is neither a valid name for AD user nor AD group"
                        )
                        # TODO maybe error instead of warning
                session.commit()
            logging.debug("Populated all AD groups members")

    def add_files(self, machine: str, files: dict[str, dict[str, str]]):
        """
            example of parameter files
            {"C:\\Program Files\\Mozilla\\firefox.exe":
                {"Administrateur": "FullControl",
                "Utilisateurs du journal de performances": "ReadPermissions,Delete",
                "pilipip.petit": "FullControl"}
            }

        :param machine: name of a machine (the machine must already exist in the database)
        :param files: dict {file_path: {sp_name: rights}}, sp_name is a (AD)user or group, file_path with double backslashes
        :return: None
        """
        with Session(self.engine) as session:
            for file_path, file_rights in files.items():
                file = File(path=file_path, id_machine=machine)
                session.add(file)
                session.commit()
                for sp_name, rights in file_rights.items():
                    sp_type, user_or_group = is_userorgroup(
                        self.engine,
                        known_match=self.known_match,
                        sp_name=sp_name,
                        machinename=machine,
                    )
                    if user_or_group is None:
                        raise ValueError(
                            f"'{sp_name}' is neither a valid name for user nor a group (AD or local)"
                        )
                    session.add(
                        FileRight(
                            id_file=file.id, id_sp=user_or_group.id, rights=rights
                        )
                    )
                session.commit()

    def add_service(self, machine: str, services: list[dict[str, str]]):
        """
            example of parameter services (list of services)
            [
                {'executable_path': 'C:\\Program Files\\Mozilla\\firefox.exe',
                'name': 'Mozilla',
                'run_by': 'SYSTEMpalais',
                'status': 'running',
                'version': '1.0.0'}
            ]

        :param machine: name of a machine (the machine must already exist in the database)
        :param services: list[dict] see example and model.Service
        :return:
        """
        services_to_insert: list[Service] = []
        for service in services:
            for expected_key in (
                "name",
                "version",
                "run_by",
                "port",
                "executable_path",
                "status",
            ):
                if expected_key not in service.keys():
                    service[expected_key] = None
            service_to_create = Service(
                name=service["name"],
                version=service["version"],
                id_machine=machine,
                run_by=service["run_by"],
                port=service["port"],
                executable_path=service["executable_path"],
                status=service["status"],
            )
            if (
                service["run_by"] == "SYSTEM"
                or service["run_by"] == ParserServices.DEFAULT_RUN_BY
            ):
                with Session(self.engine) as session:
                    run_by_id = (
                        session.query(User)
                        .filter_by(name=service["run_by"], id_machine=machine)
                        .all()[0]
                        .id
                    )
                    service_to_create.run_by = run_by_id if run_by_id else None

            services_to_insert.append(service_to_create)
        with Session(self.engine) as session:
            session.add_all(services_to_insert)
            session.commit()

    def add_gporesult(self, win_machine_name: str, gporesult: dict[str, list[str]]):
        """
        example call add_gporesult("UniPalais", {"SeRemoteInteractiveLogonRight": ["gHR", "sayanel.lyvant"]})
        :param win_machine_name:
        :param gporesult: dict {policy: [sp_name]}
        :return:

        policy is the output of the command gpresult /r
        policies of interest are
        "SeInteractiveLogonRight",
        "SeDenyInteractiveLogonRight",
        "SeRemoteInteractiveLogonRight",
        "SeDenyRemoteInteractiveLogonRight"
        """
        all_results = []
        for policy, granted_sp in gporesult.items():
            for sp_name in granted_sp:
                sp_type, sp_obj = is_userorgroup(
                    self.engine,
                    known_match=self.known_match,
                    sp_name=sp_name,
                    machinename=win_machine_name,
                )
                if sp_obj is None:
                    raise ValueError(f"{sp_name=} not found")
                else:
                    # TODO replace policy by use class GPOPolicy(enum.Enum):
                    all_results.append(
                        GPOResult(
                            id_machine=win_machine_name, policy=policy, id_sp=sp_obj.id
                        )
                    )
        with Session(self.engine) as session:
            session.add_all(all_results)
            session.commit()

    def add_all_softwares(self, machine: str, softwares: list[dict[str, str]]):
        """
        required keys of software dict: "name"
        Optional: "version", "run_by", "port"
        :param machine:
        :param softwares:
        :return:
        """
        for soft_char in softwares:
            self.add_software(soft_char, machine)

    def add_software(self, soft_charac: dict[str, str], machine: str):
        """
        example call add_software({"name": "Apache ActiveMQ", "version": "5.16.0"})
        :param soft_charac: dict {software_name: {version: version}}
        :return:
        """

        logging.debug(f"machine {machine}, add with char {soft_charac}")
        soft_name = soft_charac["name"]
        with Session(self.engine) as session:
            if "version" in soft_charac.keys():
                version = soft_charac["version"]
            else:
                version = ""
            if "run_by" in soft_charac.keys():
                _, sp_run_by = is_userorgroup(
                    self.engine,
                    known_match=self.known_match,
                    sp_name=soft_charac["run_by"],
                    machinename=machine,
                )
                sp_run_by_id = sp_run_by.id
            # a software is not necessarily run by always the same user (e.g. winrar). Might be the difference Soft/Service
            # else:
            #     _, sp_run_by = is_userorgroup(
            #         self.engine, sp_name="SYSTEM", machinename=machine
            #     )
            else:
                sp_run_by_id = None
            if "port" in soft_charac.keys():
                port = int(soft_charac["port"])
            else:
                port = None
            software = Software(
                name=soft_name,
                version=version,
                name_machine=machine,
                run_by=sp_run_by_id,
                port=port,
            )
            session.add(software)
            session.commit()

    def add_rdp(self, win_machine_name: str):
        """
        set has_RDP attribute to machine if its port 3389 is open
        :param win_machine_name:
        :return:
        """
        with Session(self.engine) as session:
            # modify attribute has_RDP of MachineWindows
            machine = session.query(Machine).filter_by(name=win_machine_name).first()
            machine.has_RDP = True
            session.commit()

    def add_psremote(self, win_machine_name: str):
        """
        set has_RDP attribute to machine if its port 5985 or 5986 is open
        :param win_machine_name:
        :return:
        """
        with Session(self.engine) as session:
            # modify attribute has_PSRemote of MachineWindows
            machine = session.query(Machine).filter_by(name=win_machine_name).first()
            machine.has_psRemote = True
            session.commit()

    def replace_sid_by_name(self):
        """
        in tables ADUser/ADGroup, if the name is a SID, replace it by the name of the u_num
        :return:
        """

        for sp_type in ((ADUser, "u"), (ADGroup, "g")):
            num = 0
            obj_type, prefix = sp_type
            with Session(self.engine) as session:
                objects = session.query(obj_type).all()
                for obj in objects:
                    if obj.name.startswith("S-1-5-21"):
                        new_name = f"{prefix}{num}_replaced"
                        # replace SID by name
                        logging.debug(f'"{obj.name}":"{new_name}",')  # noqa E231
                        obj.name = new_name
                        num += 1
                        session.commit()
                logging.debug(f"Replaced {num} SIDs by names in {obj.type} table")


def translate_is(
    is_desc: dict[str, Any], extra_translation: dict = None
) -> dict[str, Any]:
    """

    :param is_desc: original description of IS
    :return: id_dest with french strings translated in english
    """
    groups_dict = {
        "Administrateurs": "Administrators",
        "Utilisateurs": "Users",
        "Invités": "Guests",
        "Utilisateurs avec pouvoirs": "Power Users",
        "Opérateurs de sauvegarde": "Backup Operators",
        "Utilisateurs du Bureau à distance": "Remote Desktop Users",
        "Opérateurs de configuration réseau": "Network Configuration Operators",
        "IIS_IUSRS": "IIS_IUSRS",
        "Utilisateurs authentifiés": "Authenticated Users",
        "Tout le monde": "Everyone",
        "Connexion anonyme": "Anonymous Logon",
        "Opérateurs systèmes": "System Operators",
        "Opérateurs d'impression": "Print Operators",
        "Administrateurs Hyper-V": "Hyper-V Administrators",
        "Utilisateurs de Gestion à distance": "Remote Management Users",
        "Utilisateurs du journal de performances": "Performance Log Users",
        "Utilisateurs du modèle COM Distribué": "Distributed COM Users",
    }
    if extra_translation:
        groups_dict.update(extra_translation)
    sorted_trans = {
        k: v for k, v in sorted(groups_dict.items(), key=lambda item: -len(item[0]))
    }
    is_desc_str = json.dumps(is_desc, sort_keys=True, ensure_ascii=False)

    for french, english in sorted_trans.items():
        is_desc_str = is_desc_str.replace(french, english)

    return json.loads(is_desc_str)


def create_machines(is_desc: dict[str, Any]) -> list[MachineWindows]:
    """
    Only create machine Windows for now. TODO, create machines Linux
    :param is_desc:
    :return:
    """
    win_machines = []
    # create all Windows machines in database
    for name in list(is_desc["win_machines"].keys()):
        print(f"create machine and windows machine {name}")
        if "OS_version" not in is_desc["win_machines"][name]:
            machine_windows = MachineWindows(name=name)
        else:
            machine_windows = MachineWindows(
                name=name, os_version=is_desc["win_machines"][name]["OS_version"]
            )
        win_machines.append(machine_windows)
    return win_machines


def fill_win_machines(
    db_populate: DBPopulate, win_machines_name_attributes: dict[str, dict[str, str]]
) -> None:
    for win_machine_name, attributes in win_machines_name_attributes:
        print(win_machine_name, attributes)
        if "localusers" in attributes:
            db_populate.add_localusers(win_machine_name, attributes["localusers"])
        if "localgroups" in attributes:
            for lg in attributes["localgroups"]:
                print(f"add localgroup {lg} to {win_machine_name}")
                db_populate.add_localgroup(
                    win_machine_name, lg, attributes["localgroups"][lg]
                )
        if "rootcimv2" in attributes:
            for ug_rootcim, rights in attributes["rootcimv2"].items():
                db_populate.add_root_cimv2(win_machine_name, ug_rootcim, rights)
        if "saved_creds" in attributes:
            for can_runas, users_impersonated in attributes["saved_creds"].items():
                db_populate.add_runas_creds(
                    win_machine_name, can_runas, users_impersonated
                )
        if "files" in attributes:
            db_populate.add_files(win_machine_name, attributes["files"])
        if "services" in attributes:
            db_populate.add_service(win_machine_name, attributes["services"])
        if "gporesult" in attributes:
            db_populate.add_gporesult(win_machine_name, attributes["gporesult"])
        if "rdp" in attributes and attributes["rdp"]:
            print(f"add rdp to {win_machine_name}")
            db_populate.add_rdp(win_machine_name)
        if "psremote" in attributes and attributes["psremote"]:
            print(f"add psremote to {win_machine_name}")
            db_populate.add_psremote(win_machine_name)
        if "software" in attributes and attributes["software"]:
            db_populate.add_all_softwares(win_machine_name, attributes["software"])


def fill(
    is_desc: dict, db_name: str = connection_cred["db_name"], translate: bool = True
) -> None:
    """

    :param is_desc: description of the information system (its win_machines, domain, users, ...)
    :param db_name: name of the db to fill
    :param translate: Optional translate french words in english. Default True
    :return:
    """
    if translate:
        is_desc = translate_is(is_desc)

    win_machines = create_machines(is_desc)

    ad_domain = ADDomain(name=list(is_desc["domain"].keys())[0])
    ADname = ad_domain.name
    # add machines to AD
    ad_machines = []
    for machine in is_desc["domain"][ADname]["machines"]:
        print(f"add {machine=} to AD")
        ad_machines.append(
            ADMachine(
                name=machine,
                id_domain=ADname,
                is_dc=(machine in is_desc["domain"][ADname]["dcs"]),
            )
        )
    # add users to AD
    ad_users = []
    for username, password in is_desc["domain"][ADname]["users"]:
        print(f"add user {username} to AD")
        ad_users.append(ADUser(name=username, id_domain=ADname, password=password))

    db_populate = DBPopulate(engine_base_path, db_name)

    db_populate.add_machines(win_machines)

    db_populate.add_ad_adusers_admachines(ad_domain, ad_users, ad_machines)

    if "groups" in is_desc["domain"][ADname].keys():
        db_populate.add_all_adgroups(ADname, is_desc["domain"][ADname]["groups"])

    fill_win_machines(db_populate, is_desc["win_machines"].items())


def get_IS_data(file_path: str) -> dict[str:Any]:
    """

    :param file_path:
    :return: the dict containing the information system description
    """
    import importlib

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")
    # if not os.getcwd().endswith("model"):
    #     raise ImportError("Please run this script from the model directory")

    # Convert absolute path to module path
    # Remove .py extension and convert to module path
    module_path = file_path.split(".py")[0]
    # If it's an absolute path, extract the relative part from the project root
    if os.path.isabs(module_path):
        # Find the project root (assuming we're in security-twin directory)
        # Get the absolute path and find where 'data' starts
        parts = module_path.split(os.sep)
        try:
            # Find the index of 'data' in the path
            data_idx = parts.index('data')
            # Reconstruct from 'data' onwards
            module_path = '.'.join(parts[data_idx:])
        except ValueError:
            # If 'data' not found, try to extract relative to current working directory
            cwd = os.getcwd()
            if module_path.startswith(cwd):
                module_path = module_path[len(cwd)+1:].replace(os.sep, ".")
            else:
                # Fallback: just use the filename
                module_path = os.path.basename(module_path)
    else:
        module_path = module_path.replace("/", ".").replace("\\", ".")
    
    module_SI = importlib.import_module(module_path)
    if not module_SI.lab:
        raise ImportError(f"Could not import property 'lab' from module in {file_path}")
    return module_SI.lab


def main(args: argparse.Namespace) -> None:
    if args.command == "s":
        if args.table_name_filter:
            print_non_empty_tables(table_name_filter=args.table_name_filter)
        else:
            print_non_empty_tables()
    elif args.command == "reset":
        reset_db(args.dbname)
        if not args.information_system:
            return

        lab = get_IS_data(args.information_system)
        fill(lab, args.dbname)
        # print in green
        logging.info(
            f"\033[92mDatabase '{args.dbname}' successfully filled with data from {args.information_system}\033[0m"
        )


if __name__ == "__main__":
    # set logging to info
    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description="Database management script")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Subparser for the 's' command
    parser_s = subparsers.add_parser(
        "s",
        help="Show non-empty tables with a name containing "
        "the argument following this 's'. Example: fill_db s user",
    )
    parser_s.add_argument(
        "table_name_filter",
        nargs="?",
        help="Optional. display only tables containing this string (case insensitive)",
    )

    # Subparser for the 'reset' command
    parser_reset = subparsers.add_parser(
        "reset",
        help="Reset (and fill) the database. Example: ./fill_db.py reset (data/lab_test.py)",
    )
    parser_reset.add_argument(
        "information_system",
        type=str,
        nargs="?",
        default="",
        help="Optional. Path to the information system description file."
        "If omitted, the database will be reset without any data.",
    )
    parser_reset.add_argument(
        "-dbname",
        type=str,
        default=connection_cred["db_name"],
        help="Optional. Name of the database to use. Default is 'model'.",
    )
    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)
    args = parser.parse_args()
    main(args)
