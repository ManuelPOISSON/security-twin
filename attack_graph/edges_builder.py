import fnmatch
import logging
from abc import ABC, abstractmethod

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session
from sqlalchemy.engine.row import Row

from model.db import engine_base_path
from model.db_connect import connection_cred

from attack_graph.edge import Edge
from attack_graph.node import Node

from model import ADMachine, MachineWindows, Machine, ADUser, Software
from model.select_in_db import (
    select_group_all_user_members_recursively,
    select_gpo_result,
    apply_gpo_policy,
    select_saved_creds,
    select_service_exe_users,
    expand_sp_id_iterable,
    select_name_by_id,
    select_rootcimv2,
    select_machines_by_name,
    select_all_in_table,
)


class EdgeBuilder(ABC):
    def __init__(self, engine: Engine, machine_name: str = "") -> None:
        if not hasattr(self, "label"):
            raise ValueError(f"{self} label not defined")
        self.engine = engine
        self.machine_name = machine_name

    @abstractmethod
    def build_edges(self) -> list[Edge]:
        raise NotImplementedError("This method is abstract")


class BuilderRDP(EdgeBuilder):
    label = "RDP"

    def __init__(self, engine: Engine, machine_name: str = "") -> None:
        super().__init__(engine, machine_name)

    def _machine_has_RDP(self, machine_name: str) -> bool:
        machines = select_machines_by_name(self.engine, machine_name)
        if len(machines) != 1:
            raise ValueError(f"Expected exactly 1 machine with name {machine_name}")
        return machines[0].has_RDP

    def build_edges_one_machine(
        self, one_machine_name: str, machine_has_RDP_ensured: bool = False
    ) -> list[Edge]:
        edges: list[Edge] = []
        # TODO differentiate french and english names
        groups_of_interest = (
            "Administrators",
            "Remote Desktop Users",
            # "Administrateurs",
            # "Utilisateurs du Bureau à distance",
        )
        if not machine_has_RDP_ensured and not self._machine_has_RDP(one_machine_name):
            return edges

        administrators = select_group_all_user_members_recursively(
            self.engine, groups_of_interest[0], one_machine_name
        )
        allowed_users: list[tuple[str, tuple[int, str], list[str]]] = [
            (
                one_machine_name,
                (member_id, member_name),
                [
                    f"machine {one_machine_name} localgroup {groups_of_interest[0]} member: <{member_id}>"
                ],
            )
            for (member_id, member_name) in administrators
        ]

        with Session(self.engine) as session:
            ad_machine: list[Row] = (
                session.query(ADMachine)
                .filter(ADMachine.name == one_machine_name)
                .all()
            )
            # if machine (is in AD and not a DC) or (is not in AD)
            if (ad_machine and not ad_machine[0].is_dc) or not ad_machine:
                remote_desktop_users = select_group_all_user_members_recursively(
                    self.engine, groups_of_interest[1], one_machine_name
                )
                allowed_users += [
                    (
                        one_machine_name,
                        (member_id, member_name),
                        [
                            f"machine {one_machine_name} is not DC",
                            f"machine {one_machine_name} localgroup {groups_of_interest[1]} member: <{member_id}>",
                        ],
                    )
                    for (member_id, member_name) in remote_desktop_users
                ]
        logging.debug(f"rdp allowed_users {allowed_users}")
        if not allowed_users:
            return edges

        all_gpo_current_machine = select_gpo_result(self.engine, one_machine_name)
        for pol in (
            "SeRemoteInteractiveLogonRight",
            "SeDenyRemoteInteractiveLogonRight",
        ):
            allowed_users = apply_gpo_policy(
                self.engine, pol, all_gpo_current_machine, allowed_users
            )
        logging.debug(f"RDP after GPO applied: {allowed_users=}")

        for mach_name, (user_id, user_name), reasons in allowed_users:
            user_full_name = select_name_by_id(self.engine, user_id)
            reasons.append(f"machine {one_machine_name} has RDP enabled")
            reasons_full = [r.replace(f"<{user_id}>", user_full_name) for r in reasons]
            edges.append(
                Edge(
                    Node("*", user_full_name),
                    Node(one_machine_name, user_full_name, reasons_full),
                    self.label,
                    reasons_full,
                )
            )
        # TODO take into account attribute UserWorkstations
        return edges

    def build_edges(self) -> list[Edge]:
        if self.machine_name:
            return self.build_edges_one_machine(self.machine_name)
        else:
            with Session(self.engine) as session:
                machine_objs = session.query(Machine.name, Machine.has_RDP).all()
            edges = []
            for machine_obj in machine_objs:
                if machine_obj.has_RDP:
                    edges.extend(
                        self.build_edges_one_machine(
                            machine_obj.name, machine_has_RDP_ensured=True
                        )
                    )
            return edges


class BuilderRunas(EdgeBuilder):
    label = "runas"

    def __init__(self, engine: Engine, machine_name: str = "") -> None:
        super().__init__(engine, machine_name)

    def build_edges(self) -> list[Edge]:
        edges = []
        for (
            machine_src_dst,
            impersonator,
            tor_id,
            impersonated,
            ted_id,
        ) in select_saved_creds(self.engine, self.machine_name):
            tor_full = select_name_by_id(self.engine, tor_id)
            ted_full = select_name_by_id(self.engine, ted_id)
            edges.append(
                Edge(
                    Node(machine_src_dst, tor_full),
                    Node(machine_src_dst, ted_full),
                    self.label,
                    [
                        f"machine {machine_src_dst}: {tor_full} has saved the creds of {ted_full} (runas /savecred)",
                    ],
                    cmd=f"runas /savecred /user:{impersonated} cmd.exe",  # noqa E231
                )
            )
        return edges


class BuilderServiceExeModify(EdgeBuilder):
    label = "ServiceExeModify"

    def __init__(self, engine: Engine, machine_name: str = "") -> None:
        super().__init__(engine, machine_name)

    def _add_edge(
        self,
        edges,
        usr_src,
        usr_dst,
        machine_name,
        path,
        usr_src_rights,
        service_name,
        service_version,
    ):
        edges.append(
            Edge(
                Node(machine_name, usr_src),
                Node(machine_name, usr_dst),
                self.label,
                [
                    f"machine {machine_name}: service {service_name}{service_version} executed by {usr_dst} executes file at {path}",
                    f"machine {machine_name}: {usr_src} has rights {usr_src_rights} on file at {path}",
                ],
                cmd=f"copy cmd.exe {path}",
            )
        )
        return edges

    def build_edges(self) -> list[Edge]:
        # TODO check what happens if
        #  the user <aoro> rights (F) on file at same path on different machines and arg machine_name=''
        edges: list[Edge] = []

        serivce_exe_modify = select_service_exe_users(self.engine, self.machine_name)

        iterable = expand_sp_id_iterable(
            self.engine,
            [
                (id_sp, machine_id, (path, rights, run_by, service_name, version))
                for machine_id, path, rights, id_sp, run_by, service_name, version in serivce_exe_modify
            ],
        )
        for (
            id_user,
            machine_id,
            (path, rights, run_by, service_name, version),
        ) in iterable:
            edges = self._add_edge(
                edges,
                select_name_by_id(self.engine, id_user),
                select_name_by_id(self.engine, run_by),
                machine_id,
                path,
                rights,
                service_name,
                version,
            )
        return edges


class BuilderWmic(EdgeBuilder):
    label = "wmic"

    def __init__(self, engine: Engine, machine_name: str = "") -> None:
        super().__init__(engine, machine_name)

    def build_edges(self) -> list[Edge]:
        users_rootcimv2_rights = {}
        machines = []
        edges = []
        groups_of_interest = (
            "Administrators",
            "Performance Log Users",
            "Distributed COM Users",
            "Administrateurs",
            "Utilisateurs du journal de performances",
            "Utilisateurs du modèle COM Distribué",
        )
        rootcimv2_rights = select_rootcimv2(self.engine, self.machine_name)

        for machine_name, sp_id, name, rights in rootcimv2_rights:
            # right RemoteAccess is required for wmic
            if "RemoteAccess" not in rights:
                continue
            if machine_name not in machines:
                machines.append(machine_name)
            for sp_user_id, mach_name, _ in expand_sp_id_iterable(
                self.engine, [(sp_id, machine_name, ())]
            ):
                users_rootcimv2_rights[(sp_user_id, machine_name)] = (
                    sp_user_id,
                    select_name_by_id(self.engine, sp_user_id),
                    rights,
                )
        for machine_name in machines:
            for group_implied in groups_of_interest:
                for sp_id, name in select_group_all_user_members_recursively(
                    self.engine, group_implied, machine_name
                ):
                    if (sp_id, machine_name) in users_rootcimv2_rights.keys():
                        user_full_name = select_name_by_id(self.engine, sp_id)
                        reasons_full = [
                            f"machine {machine_name} localgroup {group_implied} member: {user_full_name}",
                            f"machine {machine_name}: rootcimv2rights {users_rootcimv2_rights[(sp_id, machine_name)][1:]}",
                        ]
                        edge = Edge(
                            Node("*", user_full_name),
                            Node(machine_name, user_full_name),
                            "wmic",
                            reasons_full,
                            cmd=f"wmic /node:{machine_name} process call create 'cmd.exe /c calc.exe'",  # noqa E231
                        )
                        if str(edge) not in [str(ee) for ee in edges]:
                            edges.append(edge)
                        else:
                            logging.error(f"{edges}")
                            raise RuntimeError(f"edge duplicate {edge=}")
        return edges


class BuilderPSRemote(EdgeBuilder):
    label = "PSRemote"

    def __init__(self, engine: Engine, machine_name: str = "") -> None:
        super().__init__(engine, machine_name)

    def build_edges(self) -> list[Edge]:
        return_edges: list[Edge] = []
        if self.machine_name:
            machine_objs = [select_machines_by_name(self.engine, self.machine_name)[0]]
        else:
            with Session(self.engine) as session:
                machine_objs = session.query(MachineWindows).all()
        groups_of_interest = (
            "Administrators",
            "Remote Management Users",
            "Administrateurs",
            "Utilisateurs de Gestion à distance",
        )
        for machine_obj in machine_objs:
            has_ps_remote = machine_obj.has_psRemote
            if not has_ps_remote:
                continue

            for group_implied in groups_of_interest:
                for sp_id, name in select_group_all_user_members_recursively(
                    self.engine, group_implied, machine_obj.name
                ):
                    user_full = select_name_by_id(self.engine, sp_id)
                    return_edges.append(
                        Edge(
                            Node("*", user_full),
                            Node(machine_obj.name, user_full),
                            self.label,
                            [
                                f"{machine_obj.name} has_psRemote",
                                f"machine {machine_obj.name} localgroup {group_implied} member: {user_full}",
                            ],
                            cmd=f"Invoke-Command -ScriptBlock {{cmd.exe /c whoami}} {machine_obj.name}",  # noqa E231
                        )
                    )
        return return_edges


class BuilderCVE_sam_the_admin_2021_42278(EdgeBuilder):
    """
    from Node(admachine_not_dc.name, ADUser), to Node(dc.name, "SYSTEM"),
    """

    label = "CVE_2021_42278_sam_the_admin"
    vulnerable_OS = (
        "Windows Server 2008",
        "Windows Server 2012",
        "Windows Server 2004",
        "Windows Server 2019 10.0.17763.1999",
        "Windows Server 2019 10.0.17763.1999",
        "Windows Server 2019 10.0.17763.2061",
        "Windows Server 2019 10.0.17763.2114",
        "Windows Server 2019 10.0.17763.2183",
        "Windows Server 2019 10.0.17763.2237",
        "Windows Server 2022 10.0.20348.230",
        "Windows Server 2022 10.0.20348.261",
        "Windows Server 2022 10.0.20348.288",
        "Windows Server 2022 10.0.20348.320",
    )

    def __init__(self, engine: Engine, machine_name: str = "") -> None:
        super().__init__(engine, machine_name)

    def build_edges(self) -> list[Edge]:
        ret = []
        ad_users = select_all_in_table(self.engine, ADUser)
        admachines = [
            admachine for admachine in select_all_in_table(self.engine, ADMachine)
        ]
        domain_controllers = [admachine for admachine in admachines if admachine.is_dc]
        admachines_not_dc = list(set(admachines) - set(domain_controllers))
        if not domain_controllers:
            return ret
        for dc in domain_controllers:
            # get os version of Machine
            dc_version = select_machines_by_name(self.engine, dc.name)[0].os_version
            logging.debug(f"{dc.name} is a DC with version {dc_version}")
            if dc_version in self.vulnerable_OS:
                for admachine_not_dc in admachines_not_dc:
                    for ad_user in ad_users:
                        user_full_name = select_name_by_id(self.engine, ad_user.id)
                        ret.append(
                            Edge(
                                Node(admachine_not_dc.name, user_full_name),
                                Node(dc.name, "SYSTEM"),
                                self.label,
                                [
                                    f"User {user_full_name} in AD domain {ad_user.id_domain}",
                                    f"{dc.name} is a DC in AD domain {ad_user.id_domain} with version {dc_version}, CVE sam_the_admin",
                                ],
                            )
                        )
        return ret


class BuilderCVE_ZeroLogon_2020_1472(EdgeBuilder):
    """
    From Node(*, *), to Node(dc.name, ADUser),
    https://nvd.nist.gov/vuln/detail/CVE-2020-1472
    """

    label = "CVE_2020_1472_zerologon"
    vulnerable_OS = (
        "Windows Server 2004*",
        "Windows Server 2008*",
        "Windows Server 2012*",
        "Windows Server 2016*",
        "Windows Server 2019*",
        "Windows Server 20h2*",
    )

    def __init__(self, engine: Engine, machine_name: str = "") -> None:
        super().__init__(engine, machine_name)

    def get_vulnerable_machines_in_model(
        self, machines: list[Machine]
    ) -> list[tuple[Machine, str]]:
        ret = []
        for machine in machines:
            os_version = select_machines_by_name(self.engine, machine.name)[
                0
            ].os_version
            logging.debug(f"{machine.name} {os_version=}")
            for vuln_version in self.vulnerable_OS:
                logging.debug(
                    f"{os_version=} {vuln_version=} {fnmatch.fnmatch(os_version, vuln_version)}"
                )
                if fnmatch.fnmatch(os_version, vuln_version):
                    ret.append((machine, os_version))
                    logging.debug(f"need to add edge related to {machine}")
                    break
        return ret

    def build_edges(self) -> list[Edge]:
        ret = []
        ad_users = select_all_in_table(self.engine, ADUser)
        admachines = [
            admachine for admachine in select_all_in_table(self.engine, ADMachine)
        ]
        domain_controllers = [admachine for admachine in admachines if admachine.is_dc]
        if not domain_controllers:
            logging.info("no domain controllers")
            return ret
        logging.info(f"domain_controllers: {domain_controllers}")
        for dc, dc_vulnerable_version in self.get_vulnerable_machines_in_model(
            domain_controllers
        ):
            logging.debug(f"{dc.name} is a DC with version vulnerable {dc_vulnerable_version}")
            for ad_user in ad_users:
                user_full_name = select_name_by_id(self.engine, ad_user.id)
                ret.append(
                    Edge(
                        Node("*", "*"),
                        Node(dc.name, user_full_name),
                        self.label,
                        [
                            f"{dc.name} is a DC in AD domain {ad_user.id_domain} with version {dc_vulnerable_version}, CVE zerologon",
                            f"User {user_full_name} in AD domain {ad_user.id_domain}",
                        ],
                        cmd="https://github.com/dirkjanm/CVE-2020-1472",
                    )
                )
        return ret


class BuilderCVE_software(EdgeBuilder):
    def __init__(self, engine, machine):
        if not hasattr(self, "vulnerable_softwares"):
            raise ValueError(f"{self} vulnerable_softwares not defined")
        if not isinstance(self.vulnerable_softwares, list):
            raise ValueError(f"{self} vulnerable_softwares not a list")
        super().__init__(engine, machine)

    def get_vulnerable_softwares_in_model(
        self, name_case_insensitive: bool = True
    ) -> list[Software]:
        ret = []
        softwares = select_all_in_table(self.engine, Software)
        softwares_list = []
        for software in softwares:
            sname = self.vulnerable_softwares[0].split(",")[0]
            if (name_case_insensitive and sname.lower() in software.name.lower()) or (
                not name_case_insensitive and sname in software.name
            ):
                softwares_list.append(software)

        logging.debug(f"{softwares_list=}")
        if not softwares_list:
            return []
        vulnerable_versions = [
            vulnerable.split(" ")[-1] for vulnerable in self.vulnerable_softwares
        ]
        logging.debug(f"{vulnerable_versions=}")
        for software_obj in softwares_list:
            for vuln_version in vulnerable_versions:
                if fnmatch.fnmatch(software_obj.version, vuln_version):
                    logging.debug(f"need to add edge related to {software_obj}")
                    ret.append(software_obj)
                    break
        return ret


class BuilderCVE_ActiveMQ_2023_46604(BuilderCVE_software):
    """
    https://nvd.nist.gov/vuln/detail/CVE-2023-46604
    ("*", "*") -> (software_activemq.name_machine, user_dst),
    """

    label = "CVE_2023_46604_ActiveMQ"
    vulnerable_softwares = ["Apache ActiveMQ, 4.*"]
    vulnerable_softwares.extend(
        [f"Apache ActiveMQ, 5.{version}.*" for version in range(5, 16)]
    )
    vulnerable_softwares.extend(
        [f"Apache ActiveMQ, 5.{version}.*" for version in range(3)]
    )

    vulnerable_softwares.extend(
        [
            "Apache ActiveMQ, 5.3.*",
            "Apache ActiveMQ, 5.16.0",
            "Apache ActiveMQ, 5.16.1",
            "Apache ActiveMQ, 5.16.2",
            "Apache ActiveMQ, 5.16.6",
            "Apache ActiveMQ, 5.17.0",
            "Apache ActiveMQ, 5.17.4",
            "Apache ActiveMQ, 5.18.0",
        ]
    )

    def __init__(self, engine: Engine, machine_name: str = "") -> None:
        super().__init__(engine, machine_name)

    def build_edges(self) -> list[Edge]:
        ret = []

        for software_activemq in self.get_vulnerable_softwares_in_model():
            user_dst = select_name_by_id(self.engine, software_activemq.run_by)
            ret.append(
                Edge(
                    Node("*", "*"),
                    Node(software_activemq.name_machine, user_dst),
                    self.label,
                    [
                        f"machine {software_activemq.name_machine} is running {software_activemq.name} with version {software_activemq.version} as user {user_dst}, CVE_2023_46604",
                    ],
                    cmd="msfconsole > use exploit/multi/misc/apache_activemq_rce_cve_2023_46604",
                )
            )
        return ret


class BuilderCVE_winrar_2023_38831(BuilderCVE_software):
    """
    https://nvd.nist.gov/vuln/detail/cve-2023-38831
    https://www.cvedetails.com/cve/CVE-2023-38831/
    """

    label = "CVE_2023_38831_winrar"

    vulnerable_softwares = ["winrar, 4.*"]
    vulnerable_softwares.extend(
        [
            "winrar, 3.*",
            "winrar, 4.*",
            "winrar, 5.*",
            "winrar, 6.20*",
            "winrar, 6.21*",
            "winrar, 6.22*",
        ]
    )

    def __init__(self, engine: Engine, machine_name: str = "") -> None:
        super().__init__(engine, machine_name)

    def build_edges(self) -> list[Edge]:
        ret = []
        shared_dir = "C:\\Users\\Public\\Documents"
        for software_winrar in self.get_vulnerable_softwares_in_model():
            ret.append(
                Edge(
                    Node(software_winrar.name_machine, "*"),
                    Node(software_winrar.name_machine, "*"),
                    self.label,
                    [
                        f"machine {software_winrar.name_machine} has installed {software_winrar.name} with version {software_winrar.version}, CVE_2023_38831",
                        f"usr_src can write any .rar file in {shared_dir} and user_dst can read it",
                    ],
                    cmd="msfconsole > use exploit/multi/misc/apache_activemq_rce_cve_2023_46604",
                )
            )
        return ret

class BuilderCVE_log4j_2021_44228(BuilderCVE_software):
    """
    https://nvd.nist.gov/vuln/detail/CVE-2021-44228
    """

    label = "CVE_2021_44228_log4j"

    vulnerable_softwares = ["Log4j, 1.*"]

    vulnerable_softwares.extend(
        [
            "log4j-core", "2.0.*",
            "log4j-core", "2.1*",
            "log4j-core", "2.2*",
            "log4j-core", "2.3.0",
            "log4j-core", "2.4*",
            "log4j-core", "2.5*",
            "log4j-core", "2.6*",
            "log4j-core", "2.7*",
            "log4j-core", "2.8*",
            "log4j-core", "2.9*",
            "log4j-core", "2.10*",
            "log4j-core", "2.11*",
            "log4j-core", "2.12.0*",
            "log4j-core", "2.12.1*",
            "log4j-core", "2.13.*",
            "log4j-core", "2.14.*",
        ]
    )

    def __init__(self, engine: Engine, machine_name: str = "") -> None:
        super().__init__(engine, machine_name)

    def build_edges(self) -> list[Edge]:
        ret = []
        for software_log4j in self.get_vulnerable_softwares_in_model():
            ret.append(
                Edge(
                    Node("*", "*"),
                    Node(software_log4j.name_machine, f"root@{software_log4j.name_machine}"),
                    self.label,
                    [
                        f"machine {software_log4j.name_machine} is running {software_log4j.name} with version {software_log4j.version}, CVE_2021_44228",
                    ],
                    cmd="msfconsole",
                )
            )
        return ret


def main():
    common_engine = create_engine(f"{engine_base_path}{connection_cred['db_name']}")
    all_edges = []
    edge_builders = [
        BuilderRDP,
        BuilderRunas,
        BuilderServiceExeModify,
        BuilderWmic,
        BuilderPSRemote,
        BuilderCVE_ActiveMQ_2023_46604,
    ]
    for edge_builder in edge_builders:
        print(edge_builder)
        edge_builder_instance = edge_builder(common_engine)
        all_edges.extend(edge_builder_instance.build_edges())
    print(" -" + "\n -".join(map(str, all_edges)))


if __name__ == "__main__":
    main()
