import logging
from typing import Self

from sqlalchemy import Engine

from attack_graph.graph import Node
from model import User, ADUser, ADMachine
from model.select_in_db import (
    select_all_in_table,
    apply_gpo_policy,
    select_gpo_result,
)


class NodesBuilder:
    def __init__(self, engine: Engine, nodes_rdp: list[Node] = None):
        self.engine = engine
        self.nodes_rdp = nodes_rdp
        self.nodes: list[Node] = []

    def nodes_step1(
        self,
    ) -> tuple[list[tuple[str, tuple[int, str], list[str]]], tuple[str, ...]]:
        nodes = []
        # add local users
        nodes.extend(
            list(
                (
                    l_user.id_machine,
                    (l_user.id, f"{l_user.name}@{l_user.id_machine}"),
                    [f"{l_user.name} local user of {l_user.id_machine}"],
                )
                for l_user in select_all_in_table(self.engine, User)
            )
        )
        name_machines_with_l_users = set(mname for mname, _, _ in nodes)
        all_admachine_names = set(
            admachine.name for admachine in select_all_in_table(self.engine, ADMachine)
        )
        # add ad users
        nodes.extend(
            list(
                (
                    admachine_name,
                    (ad_user.id, ad_user.name + "@" + ad_user.id_domain),
                    [f"{ad_user.name} and {admachine_name} in same ad domain"],
                )
                for admachine_name in all_admachine_names
                for ad_user in select_all_in_table(self.engine, ADUser)
            )
        )
        all_machine_names = name_machines_with_l_users.union(all_admachine_names)
        return nodes, tuple(all_machine_names)

    def nodes_apply_gpo(
        self,
        nodes: list[tuple[str, tuple[int, str], list[str]]],
        all_machines_name: tuple[str, ...],
    ) -> Self:
        """
        modify self.nodes to only keep nodes that are allowed by GPO
        :param nodes:
        :param all_machines_name:
        :return: None
        """
        nodes_gpo_applied = []
        for machine_name in all_machines_name:
            logging.debug(f"nodes related to {machine_name}")
            gpo_result = select_gpo_result(self.engine, machine_name)
            nodes_current_machine = [node for node in nodes if node[0] == machine_name]
            nodes_current_machine = apply_gpo_policy(
                self.engine,
                "SeInteractiveLogonRight",
                gpo_result,
                nodes_current_machine,
            )
            nodes_current_machine = apply_gpo_policy(
                self.engine,
                "SeDenyInteractiveLogonRight",
                gpo_result,
                nodes_current_machine,
            )
            logging.debug(f"{nodes_current_machine=}")
            nodes_gpo_applied.extend(nodes_current_machine)
        logging.info(f"GPO applied. remaining {len(nodes_gpo_applied)} nodes")
        logging.debug("\n".join(str(node) for node in nodes_gpo_applied))
        self.nodes = [Node(m, u[1], reasons) for m, u, reasons in nodes_gpo_applied]
        return self

    def add_nodes_rpd(self) -> Self:
        self.nodes = list(set(self.nodes + self.nodes_rdp))
        return self

    def build_nodes(self) -> Self:
        n1, name_machines = self.nodes_step1()
        self.nodes_apply_gpo(n1, name_machines)
        if self.nodes_rdp is not None:
            self.add_nodes_rpd()
        else:
            logging.info("no RDP nodes were added")
        # TODO take into account attribute UserWorkstations
        return self
