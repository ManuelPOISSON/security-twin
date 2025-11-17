import logging
import pickle
from functools import cache
from pathlib import Path
import networkx as nx
from tqdm import tqdm

from attack_graph.edge import Edge
from attack_graph.node import Node
from attack_graph.edges_builder import (
    BuilderRDP,
    BuilderPSRemote,
    BuilderWmic,
    BuilderRunas,
    BuilderServiceExeModify,
    BuilderCVE_sam_the_admin_2021_42278,
    BuilderCVE_ActiveMQ_2023_46604,
    BuilderCVE_winrar_2023_38831,
    BuilderCVE_ZeroLogon_2020_1472,
    BuilderCVE_log4j_2021_44228,
)


class Graph:
    labels_colors = {
        BuilderRDP.label: "green",
        BuilderPSRemote.label: "red",
        BuilderWmic.label: "orange",
        BuilderServiceExeModify.label: "blue",
        BuilderRunas.label: "#990033",  # dark red/purple
        BuilderCVE_sam_the_admin_2021_42278.label: "#991111",
        BuilderCVE_ActiveMQ_2023_46604.label: "#992222",
        BuilderCVE_winrar_2023_38831.label: "#118877",
        BuilderCVE_ZeroLogon_2020_1472.label: "#888811",
        BuilderCVE_log4j_2021_44228.label: "#442288",
    }

    def __init__(
        self,
        graph: nx.MultiDiGraph,
        nodes: list[Node],
        edges: list[Edge],
        name: str = "graph_default",
    ):
        self.graph: nx.Graph = graph
        self.all_nodes: list[Node] = nodes
        self.all_edges: list[Edge] = edges
        self.name = name
        self.nodes_dict: dict[str, Node] = {}

    def resolve_wildcard_node(self, node: Node) -> list[Node]:
        ret = [node]
        if node.user == "*" and node.machine == "*":
            ret = self.all_nodes
        elif node.machine == "*":
            ret = [nod for nod in self.all_nodes if nod.user == node.user]
        elif node.user == "*":
            ret = [nod for nod in self.all_nodes if nod.machine == node.machine]
        # print(f"resolve wild Node {node} {node.user=} {node.machine=} to {ret}")
        return ret

    def resolve_wildcard_edge(self, edge: Edge) -> list[Edge]:
        """
        :param edge:
        :return: remove edges with same src and dst, expand wildcard nodes e.g. (m1, *) gives (m1, u0), (m1, u1), (m1, u2)
        """
        ret = [
            Edge(sours, dests, edge.label, edge.reasons, edge.command)
            for sours in self.resolve_wildcard_node(edge.src)
            for dests in self.resolve_wildcard_node(edge.dst)
            if (sours.machine != dests.machine) or (sours.user != dests.user)
        ]
        return ret

    def get_node_by_machine_user(
        self, machine: str, user: str, strict: bool = True
    ) -> Node | None:
        """

        :param machine:
        :param user:
        :param strict: if True, machine and user must match exactly, otherwise case insensitive match
        :return: a Node in self.all_nodes if machine and user match, None otherwise
        """
        if strict:
            ret = self.nodes_dict.get(f"{machine}{user}")
            if ret is not None:
                return ret
            logging.info(f"Not found {machine=}, {user=}")
            return None
        # not strict
        for node in self.all_nodes:
            if (
                machine.lower() in node.machine.lower()
                and user.lower() in node.user.lower()
            ):
                return node
        logging.info(f"Not found {machine=}, {user=}")
        return None

    @staticmethod
    @cache
    def extend_conditions(node1: Node, node2: Node) -> Node:
        """

        :param node1:
        :param node2:
        :return: node1 modified with its reasons extended with node2.reasons
        """
        for node_check in (node1, node2):
            if not isinstance(node_check.reasons, list):
                raise TypeError(
                    f"node_check.reasons must be a list (possible empty) {node_check=}"
                )
        node1.reasons = list(set(node2.reasons).union(set(node1.reasons)))
        return node1

    def build_graph(self) -> "Graph":
        self.graph.add_nodes_from(self.all_nodes)
        self.nodes_dict = {
            f"{node.machine}{node.user}": node for node in self.all_nodes
        }
        for edge in tqdm(self.all_edges):
            for sub_edge in self.resolve_wildcard_edge(edge):
                # Should not happen because resolve_wildcard_edge remove src == dst
                do_not_add_edge = False
                if (
                    sub_edge.src.machine == sub_edge.dst.machine
                    and sub_edge.src.user == sub_edge.dst.user
                ):
                    raise ValueError(
                        f"src == dst\n"
                        f"{sub_edge.src.__repr__()}\n"
                        f"{sub_edge.dst.__repr__()}\n"
                        f"{sub_edge.__repr__()}\n initial edge {edge}"
                    )

                node_src_no_reasons = self.get_node_by_machine_user(
                    sub_edge.src.machine, sub_edge.src.user
                )
                node_dst_no_reasons = self.get_node_by_machine_user(
                    sub_edge.dst.machine, sub_edge.dst.user
                )
                for node_with_no_reasons, src_dst in zip(
                    (node_src_no_reasons, node_dst_no_reasons), ("src", "dst")
                ):
                    if not node_with_no_reasons:
                        # This can be normal that src or dst is not in self.all_nodes
                        # e.g. In case of an edge CVESam_the_admin that took all (AD Users x all AD Machines) as src
                        # and some of these tuple (AD User, AD Machine) are not in self.all_nodes because of GPO (among other reasons)
                        logging.debug(
                            f"node {node_with_no_reasons} {src_dst} of the edge not in self.all_nodes. "
                            f"raised when processing {sub_edge=}"
                        )
                        do_not_add_edge = True

                if do_not_add_edge:
                    continue

                # TODO this might be optimized if needed
                node_src = Graph.extend_conditions(
                    node_src_no_reasons,
                    sub_edge.src,
                )
                node_dst = Graph.extend_conditions(
                    node_dst_no_reasons,
                    sub_edge.dst,
                )
                edge_in_nxg = self.graph.get_edge_data(node_src, node_dst)
                if edge_in_nxg:
                    labels = [
                        eval(edge_data["label"][edge_data["label"].index("[") :])
                        for edge_data in edge_in_nxg.values()
                    ]
                    if sub_edge.reasons in labels:
                        continue
                self.graph.add_edge(
                    node_src,
                    node_dst,
                    label=sub_edge.label + str(sub_edge.reasons),
                    color=Graph.labels_colors[sub_edge.label],
                )
        assert self.all_nodes == list(self.graph.nodes)
        return self

    def __repr__(self) -> str:
        ret = []
        nodes_displayed = set()
        count_isolated = 0
        for u, v, data in self.graph.edges(data=True):
            nodes_displayed.add(u)
            nodes_displayed.add(v)
            ret.append(f"({u}, {v}, {data['label']})")
        for n in self.graph.nodes:
            if n not in nodes_displayed:
                ret.append(f"isolated {n}")
                count_isolated += 1
        ret.append(f"nb isolated nodes: {count_isolated}")
        ret.sort()
        return "\n".join(ret)

    def filter_graph(self, set_attributes_to_remove: set[str]) -> None:
        """
        removes all nodes in self.graph if a set's element is part of node.machine.name or node.user.name
        :param set_attributes_to_remove:
        :return: None
        """
        nodes_to_remove = []
        for current_attribute in set_attributes_to_remove:
            for node in self.graph.nodes:
                if (
                    current_attribute.upper() in node.machine
                    or current_attribute.upper() in node.user
                ):
                    nodes_to_remove.append(node)

        self.graph.remove_nodes_from(nodes_to_remove)

    @staticmethod
    def convert_graph(nx_graph: nx.Graph) -> tuple[nx.DiGraph, list[Node]]:
        simple_graph = nx.DiGraph()
        count_nodes_with_deg0 = 0
        nodes_with_deg0 = []
        for node, degree in tqdm(nx_graph.degree(nx_graph.nodes)):
            node_str = str(node)
            if degree == 0:
                count_nodes_with_deg0 += 1
                nodes_with_deg0.append(node)
                continue
            if (
                "aoro" in node_str.lower()
                or "admin" in node_str.lower()
                or "system" in node_str.lower()
            ):
                simple_graph.add_node(
                    node_str, title=node_str, font="150px arial black", color="red"
                )
            else:
                simple_graph.add_node(
                    node_str, title=node_str, font="150px arial black"
                )
        print(f"nb nodes with degree 0: {count_nodes_with_deg0}")

        if len(nx.get_edge_attributes(nx_graph, "label")) != len(
            nx.get_edge_attributes(nx_graph, "color")
        ):
            raise ValueError(
                "len(attributes(nx_graph, 'label')) != len(attributes(nx_graph, 'color'))"
            )
        for edge in tqdm(
            zip(
                nx.get_edge_attributes(nx_graph, "label").items(),
                nx.get_edge_attributes(nx_graph, "color").items(),
            )
        ):
            srcdstint_labelreason, sth_color = edge
            # examples of srcdstint_labelreason
            # (('(dcserver,ewilan.gilsayan@ad2016.local)', '(UniPalais,ewilan.gilsayan@ad2016.local)', 0), 'RDP["ewilan.gilsayan@ad2016.local member of \'Administrators\'"]')
            # examples of sth_color
            # (('(dcserver,ewilan.gilsayan@ad2016.local)', '(UniPalais,ewilan.gilsayan@ad2016.local)', 0), 'green')

            src1, dst1, _ = srcdstint_labelreason[0]
            label = srcdstint_labelreason[1].split("[")[0]
            color = sth_color[1]
            simple_graph.add_edge(
                str(src1), str(dst1), color=color, label=label, title=label, value=7
            )
        return simple_graph, nodes_with_deg0

    def show_graph(
        self,
        nodes_to_remove: set[str] | None = None,
        gephi_remove_isolated_node: bool = False,
        save_pyvis: bool = True,
    ):
        """

        :param nodes_to_remove:
        :param save_file_name: saved in a html file
        :param gephi_remove_isolated_node:
        :return:
        """
        # plt.subplot(221)
        # nx.draw_kamada_kawai(self.graph, with_labels=True)
        # plt.subplot(222)
        # nx.draw_spring(self.graph, with_labels=True)
        # plt.subplot(223)
        # nx.draw_random(self.graph, with_labels=True)
        # plt.subplot(224)
        # nx.draw_spectral(self.graph, with_labels=True)

        if nodes_to_remove is None:
            nodes_to_remove = set()
        self.filter_graph(nodes_to_remove)
        if save_pyvis:
            from pyvis.network import Network

            simple_nx, nodes_deg0 = self.convert_graph(self.graph)

            pyvis_filename = f"{self.name}.html"
            graph_pyvis = Network(height=950, width=1800, notebook=True, directed=True)
            graph_pyvis.toggle_hide_edges_on_drag(True)
            graph_pyvis.barnes_hut()
            graph_pyvis.neighborhood_highlight = True

            # g.from_nx(simple_nx, default_node_size=30, node_size_transf=(lambda x: 2 * x))
            graph_pyvis.from_nx(
                simple_nx, default_node_size=30, node_size_transf=(lambda x: 2 * x)
            )
            graph_pyvis.show(pyvis_filename)
            logging.info(f"pyvis graph saved in {pyvis_filename}")

        if gephi_remove_isolated_node:
            simple_nx, nodes_deg0 = self.convert_graph(self.graph)
            logging.info(f"remove {len(nodes_deg0)} isolated nodes")
            self.graph.remove_nodes_from(nodes_deg0)

        # remove reasons of edges' labels
        for u, v, data in self.graph.edges(data=True):
            data["label"] = data["label"].split("[")[0]

        nx.write_gexf(self.graph, f"{self.name.split('.')[0]}.gexf")
        logging.info(f"gephi graph saved in {self.name.split('.')[0]}.gexf")

    def save_object(self, filename: str):
        if "/" in filename:
            Path(filename).parent.mkdir(parents=True, exist_ok=True)
        with open(filename, "wb") as outp:
            pickle.dump(self, outp, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_object(filename: str) -> "Graph":
        with open(filename, "rb") as inp:
            ret = pickle.load(inp)
        logging.info(f"Graph loaded from file {filename}")
        return ret
