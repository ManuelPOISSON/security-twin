#!/usr/bin/env python3

import logging
from collections import defaultdict
from typing import Any

from sqlalchemy.orm import Session, aliased
from sqlalchemy import Engine
from sqlalchemy.engine.row import Row
from sqlalchemy import create_engine
from sqlalchemy import text

from .fill_db import is_userorgroup

from .model import (
    Group,
    GroupMemberUser,
    User,
    GroupMemberADUser,
    ADUser,
    GroupMemberADGroup,
    ADGroup,
    MachineLinux,
    MachineWindows,
    RunasCreds,
    RunasImpersonated,
    ADGroupMemberADUser,
    ADGroupMemberADGroup,
    Machine,
    FileRight,
    File,
    RootCimv2,
    RootCimv2Rights,
    TypeSp,
    Service,
    ADMachine,
    SecurityPrincipal,
    Software,
)
from .db import engine_base_path
from .db_connect import connection_cred
from .select_in_db_sql_queries import (
    query_select_users_can_runas,
    query_select_gpo_result,
    query_select_adgroup_members_recursive,
)

# Enable logging
logging.basicConfig()
# logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)


def print_results(results: list[Row], headers: list[str] = None, quiet: bool = False):
    """
    print results with nice alignment
    """
    if headers:
        for header in headers:
            print(f"{header[:29]:30}", end="|")  # noqa E231
        print("\n", "-" * (len(headers) * 30 + len(headers)))
    if len(results) == 0 and not quiet:
        print("No results")
        return
    for result in results:
        if len(result) == 2:
            for elem in result:
                # print elem with a fixed width of 20 characters
                print(f"{str(elem)[:69]:70}", end="|")  # noqa E231
        else:
            for elem in result:
                # print elem with a fixed width of 20 characters
                print(f"{str(elem)[:39]:40}", end="|")  # noqa E231
        print("")


def select_name_by_id(
    engine: Engine, id: int, include_domain: bool = True, upn_format: bool = True
) -> str | None:
    """

    :param engine:
    :param id: of an object (AD)user or (AD)group
    :return: e.g. if include_domain, upn_format is True (default), return "sayanel.lyvant@lab.local"
    if include_domain is True and upn_format is False, return "LAB\\sayanel.lyvant"
    """
    query = text(
        """
        SELECT name, id_belong_to
        FROM (
            SELECT name, id, CONCAT('@', id_machine) AS id_belong_to  # noqa W291
            FROM user
            UNION
            SELECT name, id, CONCAT('@', id_domain) AS id_belong_to
            FROM ADuser
            UNION
            SELECT name, id, CONCAT('@', id_machine) AS id_belong_to # noqa W291
            FROM `group`
            UNION
            SELECT name, id, CONCAT('@', id_domain) AS id_belong_to
            FROM ADgroup
        ) AS combined
        WHERE id = :id
    """
    )
    with Session(engine) as session:
        results = session.execute(query, {"id": id}).fetchall()
        if len(results) != 1:
            raise ValueError(f"Expected 1 result, got {len(results)}, {id=} {results}")
        if include_domain:
            if upn_format:
                return results[0].name + results[0].id_belong_to
            else:
                return (
                    results[0].id_belong_to.split(".")[0].replace("@", "").upper()
                    + "\\"
                    + results[0].name
                )
        else:
            return results[0].name + results[0].id_belong_to


def select_local_all_groups(engine: Engine):
    with Session(engine) as session:
        # Perform the query
        query = (
            session.query(
                Group.id_machine,
                Group.name.label("group_name"),
                User.name.label("user_name"),
                ADUser.name.label("aduser_name"),
                ADGroup.name.label("adgroup_name"),
            )
            .outerjoin(GroupMemberUser, Group.id == GroupMemberUser.member_of)
            .outerjoin(User, GroupMemberUser.member == User.id)
            .outerjoin(GroupMemberADUser, Group.id == GroupMemberADUser.member_of)
            .outerjoin(ADUser, GroupMemberADUser.member == ADUser.id)
            .outerjoin(GroupMemberADGroup, Group.id == GroupMemberADGroup.member_of)
            .outerjoin(ADGroup, GroupMemberADGroup.member == ADGroup.id)
            .order_by(Group.id_machine)
        )

        # Execute the query
        results: list[Row] = query.all()
        print_results(results)


def select_all_in_table(engine: Engine, obj_type):
    with Session(engine) as session:
        return session.query(obj_type).all()


def select_all_adusers_names(engine: Engine) -> list[str]:
    with Session(engine) as session:
        query = session.query(ADUser.name)
        results: list[Row] = query.all()
        return [str(row[0]) for row in results]


def select_softwares_installed_on_machine(
    engine: Engine, machine_name: str
) -> list[Software]:
    with Session(engine) as session:
        query = session.query(Software).filter(Software.name_machine == machine_name)
        results: list[Row] = query.all()
    return results


def select_machines_by_name(
    engine: Engine, machine_name: str
) -> list[MachineWindows | MachineLinux] | None:
    """
    :param engine:
    :param machine_name:
    :return: [<model.MachineWindows object at 0x7f214d7ea4b0>] or None
    """
    with Session(engine) as session:
        results = (
            session.query(MachineWindows)
            .filter(MachineWindows.name == machine_name)
            .all()
        )
        results += (
            session.query(MachineLinux).filter(MachineLinux.name == machine_name).all()
        )
        if len(results) == 0:
            return None
        elif len(results) > 1:
            print(f"Warning! Found {len(results)} machines with name {machine_name}")
        return results


def select_adgroup_with_members(
    engine: Engine,
) -> list[tuple[ADGroup | ADUser, ADGroup]]:
    """

    :param engine:
    :return: List of tuples [memberOfADGroup, ADGroup]
    """
    with Session(engine) as session:
        # Query to get ADGroup and their ADUser members
        adgroup_user_members = (
            session.query(ADUser, ADGroup)
            .join(ADGroupMemberADUser, ADGroup.id == ADGroupMemberADUser.member_of)
            .join(ADUser, ADGroupMemberADUser.member == ADUser.id)
            .all()
        )

        # Query to get ADGroup and their ADGroup members
        adgroup_group_members_with_ids = (
            session.query(ADGroupMemberADGroup.member, ADGroup)
            .join(ADGroup, ADGroupMemberADGroup.member_of == ADGroup.id)
            .all()
        )
        adgroup_group_members = []
        for id, obj in adgroup_group_members_with_ids:
            obj: ADGroup
            adgroup_member: ADGroup | None = (
                session.query(ADGroup).filter(ADGroup.id == id).first()
            )
            if adgroup_member is None:
                raise ValueError(f"ADGroup with id {id} not found")
            adgroup_user_members.append((adgroup_member, obj))

        # Combine results
        accounts_groups = adgroup_user_members + adgroup_group_members

    return accounts_groups


def select_localgroup_with_members(
    engine: Engine, machine: Machine, group_name: str = "", order: bool = False
) -> list[tuple[User | ADUser | ADGroup, Group]]:
    """

    :param engine:
    :param machine:
    :return: list of tuples [memberOf, Group] where memberOf is a User, ADUser or ADGroup
    by default, this is done for all groups of the machine
    """
    with Session(engine) as session:
        # Query to get Group and their User members
        query = (
            session.query(User, Group)
            .join(GroupMemberUser, Group.id == GroupMemberUser.member_of)
            .join(User, GroupMemberUser.member == User.id)
            .filter(Group.id_machine == machine.name)
        )
        if group_name:
            query = query.filter(Group.name == group_name)
        group_user_members = query.all()

        # Query to get Group and their ADUser members
        query = (
            session.query(ADUser, Group)
            .join(GroupMemberADUser, Group.id == GroupMemberADUser.member_of)
            .join(ADUser, GroupMemberADUser.member == ADUser.id)
            .filter(Group.id_machine == machine.name)
        )
        if group_name:
            query = query.filter(Group.name == group_name)
        group_aduser_members = query.all()

        # Query to get Group and their ADGroup members
        query = (
            session.query(GroupMemberADGroup.member, Group)
            .join(Group, GroupMemberADGroup.member_of == Group.id)
            .filter(Group.id_machine == machine.name)
        )
        if group_name:
            query = query.filter(Group.name == group_name)
        group_adgroup_members_with_ids = query.all()

        group_adgroup_members = []
        for id, obj in group_adgroup_members_with_ids:
            obj: Group
            group_member: ADGroup | None = (
                session.query(ADGroup).filter(ADGroup.id == id).first()
            )
            if group_member is None:
                raise ValueError(f"ADGroup with id {id} not found")
            group_adgroup_members.append((group_member, obj))

        # Combine results
        accounts_groups = (
            group_user_members + group_aduser_members + group_adgroup_members
        )
        if order:
            # Sort by group name and member name
            accounts_groups.sort(
                key=lambda x: (x[1].name, x[0].name if isinstance(x[0], User) else "")
            )

    return accounts_groups


def _select_adgroup_all_members_recursively(
    engine: Engine, adgroup_id: str
) -> list[tuple[int, str]]:
    """
    Please use select_group_all_user_members_recursively.
    This function should be called only by select_group_all_user_members_recursively
    :param engine:
    :param adgroup_name:
    :return:
    """

    textual = query_select_adgroup_members_recursive.strip().replace(
        "<adgroup_id>", str(adgroup_id)
    )
    with Session(engine) as session:
        results: list[tuple[int, str]] = list(
            ((id, name) for id, name in session.execute(text(textual)).all())
        )
    return results


def select_group_all_user_members_recursively(
    engine: Engine, group: str, machine_name: str = ""
) -> list[tuple[int, str]]:
    """

    :param engine:
    :param group:
    :param machine_name: Optional, use it to query local group of a machine.
    If omitted, will only search for groups in domain
    :return: [(security_principal.id, (AD)user.name)]
    """
    results = []
    textual_group_request = f"""
    SELECT id, type from security_principal WHERE id=(SELECT id FROM `group` WHERE name = '{group}' AND id_machine = '{machine_name}'
        UNION
        SELECT id FROM ADgroup WHERE name = '{group}' LIMIT 1)
    """.strip()
    with Session(engine) as session:
        # TODO, replace by sqlAlchemy request
        group_entry: list[Row] = session.execute(text(textual_group_request)).first()
    if not group_entry:
        logging.debug(f"{group=} not found ({machine_name=})")
        return results

    group_id, group_type = group_entry
    if group_type == str(TypeSp.ADgroup).split(".")[1]:
        results = _select_adgroup_all_members_recursively(engine, group_id)
    elif group_type == str(TypeSp.group).split(".")[1]:
        machine = select_machines_by_name(engine, machine_name)
        direct_members = select_localgroup_with_members(engine, machine[0], group)
        for member, _ in direct_members:
            if not isinstance(member, ADGroup):
                results.append((member.id, member.name))
            else:
                results.extend(
                    _select_adgroup_all_members_recursively(engine, member.id)
                )
    else:
        ValueError(f"Unknown group type {group_type}")
    return results


def select_acl(engine: Engine, machine_name: str) -> list[tuple[str, str, str, str]]:
    """

    :param engine:
    :param machine:
    :return: list of tuples (sp_name, path, rights, machine_name)
    """
    ret = []
    with Session(engine) as session:
        query = (
            session.query(FileRight.id_sp, File.path, FileRight.rights, File.id_machine)
            .join(File, FileRight.id_file == File.id)
            .filter(File.id_machine == machine_name)
        )
        results: list[Row] = query.all()
        for res in results:
            ret.append((select_name_by_id(engine, res[0]), *res[1:]))
    return ret


def select_rootcimv2(
    engine: Engine, mach_name: str = ""
) -> list[tuple[str, int, str, str]]:
    """
    :param engine:
    :param machine: Optional. If omitted, all machines are selected
    :return: list of tuples (machine_id, sp_id, sp_name, rights)
    """
    ret: list[tuple[str, int, str, str]] = []
    with Session(engine) as session:
        sess_query = session.query(
            RootCimv2.id_machine, RootCimv2.id_sp, RootCimv2Rights.right
        ).join(RootCimv2Rights, RootCimv2.id == RootCimv2Rights.id_root_cimv2)
        if mach_name:
            sess_query = sess_query.filter(RootCimv2.id_machine == mach_name)
        results: list[Row] = sess_query.all()
        rights = defaultdict(list)
        for machine_id, sp_id, namepace_right in results:
            rights[(machine_id, sp_id, select_name_by_id(engine, sp_id))].append(
                str(namepace_right).replace("NameSpaceRights.", "")
            )
        for machine_and_sp_id_name, rights_current_sp in rights.items():
            ret.append(
                (
                    machine_and_sp_id_name[0],
                    machine_and_sp_id_name[1],
                    machine_and_sp_id_name[2],
                    ",".join(rights_current_sp),
                )
            )
    return ret


def select_saved_creds(
    engine: Engine, machine_name: str = ""
) -> list[tuple[str, str, int, str, int]]:
    """

    :param engine:
    :param machine_name: Optional. If omitted, will select on all machines
    :return: list of tuples (machine_name, name of user who can_runas, id of user can_runas, name of user impersonated, id of user impersonated)
    """
    textual_query = text(
        query_select_users_can_runas
        + ("" if not machine_name else f" WHERE rc.id_machine = '{machine_name}'")
    )
    # execute the query
    with Session(engine) as session:
        results: list[Row] = session.execute(textual_query).all()
        # print_results(results, ["Machine", "Impersonator", "Impersonated"])
    return results


def select_passowrd_for_user(
    engine: Engine, user_name: str = None, user_id: int = None
) -> str:
    if user_name is None and user_id is None:
        raise ValueError("Please provide user_name or user_id")
    if user_name is not None and user_id is not None:
        raise ValueError("Please provide only one of user_name or user_id")
    with Session(engine) as session:
        if user_name:
            user_id = is_userorgroup(engine, user_name=user_name)[1].id

        return (
            session.query(SecurityPrincipal.password)
            .filter(SecurityPrincipal.id == user_id)
            .first()
        )[0]


def select_gpo_result(
    engine, machine_name: str = ""
) -> list[tuple[str, str, str, int]]:
    """

    :param engine:
    :param machine_name:
    :return: [(id_machine, GPOresult.policy, sp.name, sp.id_sp), ...]
    """
    with Session(engine) as session:
        query_text = query_select_gpo_result
        if machine_name:
            query_text += f' WHERE GPOresult.id_machine = "{machine_name}"'
        results: list[tuple[str, str, str, int]] = session.execute(
            text(query_text)
        ).all()
    # print_results(results, ["Machine", "Policy", "", "sp id"])
    return results


def expand_sp_id_iterable(
    engine: Engine, iterable: list[tuple[int, str, Any]]
) -> list[tuple[int, str, Any]]:
    """

    :param iterable: list of tuples (sp_id, machine_name, attributes): sp_id is the id of a security principal (ad)group or (ad)user
    :return: expanded list of tuples (sp_id, machine_name, attributes) where sp_id is the id of a user, machine_name/attributes is the same as in the input

    example:
    user with id u1 is member of group with id g2

    input:  [(u0, "machine", (sthA)), (g2, "machine", (sthB))]

    output: [(u0, "machine", (sthA)), (u1, "machine", (sthB))]
    """
    expanded = []

    for current_iteration in iterable:
        sp_id, machine_name, attributes = current_iteration
        sp_type, sp_obj = is_userorgroup(engine, sp_id=sp_id, machinename=machine_name)

        if sp_type == TypeSp.user or sp_type == TypeSp.ADuser:
            expanded.append((sp_id, machine_name, attributes))
        elif sp_type == TypeSp.group or sp_type == TypeSp.ADgroup:
            members = select_group_all_user_members_recursively(
                engine, sp_obj.name, machine_name
            )
            for member_sp_id, username in members:
                # print(f"{sp_obj.name=} expanded to {username=} {member_sp_id}")
                expanded.append((member_sp_id, machine_name, attributes))
    return expanded


def apply_gpo_policy(
    engine,
    policy_name: str,
    all_gpo_current_machine: list[tuple[str, str, str, int]],
    allowed_users: list[tuple[str, tuple[int, str], list[str]]],
) -> list[tuple[str, tuple[int, str], list[str]]]:
    """

    :param policy_name: must be one of "SeRemoteInteractiveLogonRight", "SeDenyRemoteInteractiveLogonRight"
    :param all_gpo_current_machine: [(machine_name, policy_name, sp_name, sp_id), (...), ...]
    :param allowed_users: {(machine_name, (user_id, user_name), reason), (...), ...}
    :return: modified allowed_users by removing users that are not allowed by the GPO
    """
    # TODO warning if allowed_users contains machine_names not in all_gpo_current_machine and vice versa
    implemented_policies = [
        "SeRemoteInteractiveLogonRight",
        "SeDenyRemoteInteractiveLogonRight",
        "SeInteractiveLogonRight",
        "SeDenyInteractiveLogonRight",
    ]

    def get_new_allowed_users(original_allowed, case: str):
        new_allowed = []

        for m_name, (u_id, u_name), r in original_allowed:
            if case == "Interactive":
                cond_str = f"applies on {u_name}"
                must_append = (u_id, m_name) in policy_logon
            elif case == "DenyInteractive":
                cond_str = f"does not apply on {u_name}"
                must_append = (u_id, m_name) not in policy_logon
            elif case == "GPO_undefined":
                cond_str = "is undefined"
                must_append = True
            else:
                raise ValueError(f"argument {case=} is not in allowed values")

            if must_append:
                new_allowed.append(
                    (
                        m_name,
                        (u_id, u_name),
                        r + [f"machine {m_name}, GPO {policy_name} {cond_str}"],
                    )
                )
        return new_allowed

    if policy_name not in implemented_policies:
        raise ValueError(f"Unknown GPO_name: {policy_name}")
    policy_logon = list(
        (m, u)
        for m, u, _ in expand_sp_id_iterable(
            engine,
            [
                (sp_id, machine_n, ())
                for machine_n, policy, sp_name, sp_id in all_gpo_current_machine
                if policy == policy_name
            ],
        )
    )

    if policy_logon:
        # keep user only if the policy applies to them
        if policy_name in (implemented_policies[0], implemented_policies[2]):
            allowed_users = get_new_allowed_users(allowed_users, "Interactive")
        # remove user if the policy applies to them (Deny policies)
        elif policy_name in (implemented_policies[1], implemented_policies[3]):
            allowed_users = get_new_allowed_users(allowed_users, "DenyInteractive")
    else:
        allowed_users = get_new_allowed_users(allowed_users, "GPO_undefined")
    return allowed_users


def select_service_exe_users(
    engine, machine_name: str = ""
) -> list[tuple[Any, Any, Any, Any, Any, Any, Any]]:
    with Session(engine) as session:
        sess_query = (
            session.query(
                File.id_machine,
                File.path,
                FileRight.rights,
                FileRight.id_sp,
                Service.run_by,
                Service.name,
                Service.version,
            )
            .join(FileRight, File.id == FileRight.id_file)
            .join(
                Service,
                Service.executable_path == File.path,
            )
            .filter(Service.id_machine == File.id_machine)
            .filter(FileRight.rights.like("%FullControl%"))
        )  # TODO probably other permissions than Full access like "modify"
        if machine_name:
            sess_query = sess_query.filter(Service.id_machine == machine_name)
        ret = sess_query.all()
    return ret


if __name__ == "__main__":
    dbname = connection_cred["db_name"]
    engine = create_engine(f"{engine_base_path}{dbname}")  # noqa E231
    # select_local_all_groups(engine)
    print_results(
        select_group_all_user_members_recursively(
            engine, "S-1-5-21-4029057679-3449900800-3633163903-1613"
        )
    )
    groups_interesting = [
        "Performance Log Users",
        "Performance Monitor Users",
        "Remote Management Users",
        "Remote Desktop Users",
        "Administrators",
    ]

    for m in select_all_in_table(engine, Machine):
        print(f"======= Machine {m.name}")
        if "DR38" not in m.name:
            continue
        for group_name in groups_interesting:
            print(f"Group {group_name}", end=": ")
            print_results(
                select_localgroup_with_members(engine, m, group_name, order=True),
                quiet=True,
            )
        print("")

        # print_results(select_localgroup_with_members(engine, m, order=True))
        # print_results(select_rootcimv2(engine, m.name))
    # for i in range(1, 28):
    #     print(i, select_passowrd_for_user(engine, user_id=i))
