import re
import logging
from collections import defaultdict
from itertools import product

import networkx as nx

from attack_graph.graph import Graph
from attack_graph.node import Node


class Conditions:
    def __init__(self, cond: list[str]):
        self.conditions = cond

    def __str__(self):
        return str(self.conditions)


class PathWithConditions:
    def __init__(
        self,
        path: list[Node],
        conditions: list[Conditions],
        edge_labels: list[str] = None,
    ):
        self.path: list[Node] = path
        self.conditions = conditions
        self.src: Node = self.path[0]
        self.dst: Node = self.path[-1]
        if edge_labels is None:
            self.edge_labels = []
        self.edge_labels: list[str] = edge_labels

    def get_involved_computers(self) -> set[str]:
        return set(node.machine for node in self.path)

    def dump_conditions(self):
        for cond_edge in self.conditions:
            cond_edge.conditions and print(
                "\n".join(f"- {c}" for c in cond_edge.conditions)
            )

    def __str__(self):
        ret = f"path length {len(self.path)}, dst: {self.path[-1]}\n"
        for idx, sub_node in enumerate(self.path):
            ret += f"\t{str(sub_node)} {self.edge_labels[idx]}\n"
        return ret


class EdgeWithConditions:
    def __init__(
        self, src_node_str, edge_label, cond_edge: Conditions, cond_node: Conditions
    ):
        self.src_node_str = src_node_str
        self.edge_label = edge_label
        self.cond_edge = cond_edge
        self.cond_node = cond_node

    def __str__(self):
        return (
            f"{self.src_node_str} {self.edge_label} {self.cond_edge} {self.cond_node}"
        )


def compare_graph_nodes(
    g_initial: Graph, g_modified: Graph
) -> tuple[list[tuple[Node, Node]], list[Node], list[Node]]:
    """

    :param g_initial:
    :param g_modified:
    :return: tuple of [updated_nodes, deleted_nodes, created_nodes]
    """
    updated: list[tuple[Node, Node]] = []
    deleted: list[Node] = []
    created: list[Node] = []

    def parse_ddif(indexes: list[str]):
        idx = []
        for root_index in indexes:
            int_idx = int(root_index.split("[")[1][:-1])
            idx.append(int_idx)
        return idx

    # initial_nodes_sorted = sorted(n for n in g_initial.graph.nodes)
    # new_nodes_sorted = sorted(n for n in g_modified.graph.nodes)
    # l_init = [n.user.gid + ";" + n.computer.gid for n in initial_nodes_sorted]
    # l_new = [n.user.gid + ";" + n.computer.gid for n in new_nodes_sorted]
    #
    # ddiff = DeepDiff(l_init, l_new)
    #
    # if "iterable_item_removed" in ddiff.keys():
    #     nodes_str_deleted = ddiff["iterable_item_removed"]
    #     deleted = [
    #         initial_nodes_sorted[i] for i in parse_ddif(nodes_str_deleted.keys())
    #     ]
    #
    # if "iterable_item_added" in ddiff.keys():
    #     nodes_str_created = ddiff["iterable_item_added"]
    #     created = [new_nodes_sorted[i] for i in parse_ddif(nodes_str_created.keys())]
    #
    # if "values_changed" in ddiff.keys():
    #     nodes_str_updated = ddiff["values_changed"]
    #     nodes_after_update = (
    #         new_nodes_sorted[i] for i in parse_ddif(nodes_str_updated.keys())
    #     )
    #
    #     ddiff = DeepDiff(l_new, l_init)
    #     nodes_before_update = (
    #         initial_nodes_sorted[i] for i in parse_ddif(ddiff["values_changed"].keys())
    #     )
    #     updated = [(n[0], n[1]) for n in zip(nodes_before_update, nodes_after_update)]
    #
    # for nodes_list, text in zip(
    #     (updated, deleted, created), ("updated", "deleted", "created")
    # ):
    #     logging.debug(
    #         f"nodes {text} : {len(nodes_list)} {'; '.join(map(str, nodes_list))}"
    #     )

    return updated, deleted, created


def index_node_tuple_in_nodes_list(
    node_searched: tuple[Node, Node], nodes_list: list[tuple[Node, Node]]
):
    for src_in_node_list, dst_in_node_list in nodes_list:
        if (
            src_in_node_list == node_searched[0]
            and dst_in_node_list == node_searched[1]
        ):
            return src_in_node_list, dst_in_node_list

    return None


def compare_graph_edges(initial_graph: Graph, new_graph: Graph):
    """
    An edge e is tuple[srcNode: Node, dstNode: Node]

    :param initial_graph:
    :param new_graph:
    :return: e_updated, e_del, e_added where update=list[(e_before, e_after),...] and e_del/e_add are list[e,...]
    """
    updated0, deleted_from_init, deleted_from_new = [], [], []
    # def only_in_one_edges_list(
    #     graph_a: Graph, graph_b: Graph
    # ) -> tuple[
    #     list[tuple[tuple[Node, Node], tuple[Node, Node]]], list[tuple[Node, Node]]
    # ]:
    #     """
    #     :param graph_a:
    #     :param graph_b:
    #     :return: [updated, deleted] where updated= list[[src_node_in_graph_a, dst_node_in_graph_a],[src_node_in_graph_b, dst_node_in_graph_b]]
    #     and deleted=list[[src_node_in_graph_a, dst_node_in_graph_a]]
    #     """
    #     edges_a: list[tuple[Node, Node]] = sorted(list(graph_a.graph.edges))
    #     edges_b: list[tuple[Node, Node]] = sorted(list(graph_b.graph.edges))
    #
    #     deleted: list[tuple[Node, Node]] = []
    #     updated: list[tuple[tuple[Node, Node], tuple[Node, Node]]] = []
    #     for nodes_a in edges_a:
    #         nodes_found = index_node_tuple_in_nodes_list(nodes_a, edges_b)
    #         if nodes_found:
    #             init_rel = graph_a.relations[nodes_a]
    #             new_rel = graph_b.relations[nodes_found]
    #             if str(init_rel) != str(new_rel):
    #                 updated.append((nodes_a, nodes_found))
    #         else:
    #             deleted.append(nodes_a)
    #     return updated, deleted
    #
    # print("=" * 20)
    # # print(
    # #     f"init nodes :{len(initial_graph.graph.nodes)}, new : {len(new_graph.graph.nodes)}, diff {len(initial_graph.graph.nodes) - len(new_graph.graph.nodes)}"
    # # )
    # print(
    #     f"init edges: {len(initial_graph.relations)}, new : {len(new_graph.relations)}, diff {len(initial_graph.relations) - len(new_graph.relations)}"
    # )
    # print("=" * 20)
    # updated0, deleted_from_init = only_in_one_edges_list(initial_graph, new_graph)
    # updated1, deleted_from_new = only_in_one_edges_list(new_graph, initial_graph)
    # for text, relations_list in zip(
    #     ("updated ", "deleted ", "created "),
    #     (updated0, deleted_from_init, deleted_from_new),
    # ):
    #     logging.debug(f"edges {text}{len(relations_list)} {relations_list}")
    return updated0, deleted_from_init, deleted_from_new


def get_path_edges_attr(
    path: list[Node], graph: nx.MultiDiGraph
) -> list[list[EdgeWithConditions]]:
    """

    :param path:
    :param graph:
    :return: list of paths
     path is represented as a list of tuples [(node.__str__, label, conditions_edge, conditions_node), (...), ...].
    Final tuple is (node, '', [], conditions_node)
    """
    returned_paths = []
    path_multi_edges = []
    for u, v in zip(path[0:], path[1:]):
        u: Node
        v: Node
        # print(u)
        # print(v)
        # print(graph)
        # print(type(graph))
        # print(graph[u][v])
        # print("=")
        if len(u.reasons) < 1:
            raise ValueError(f"path {path}\nno condition for node {u=}")
        edge_label_and_cond: tuple[str, ...] = tuple(
            [edge_val["label"] for edge_val in graph[u][v].values()]
        )

        path_multi_edges.append((u, edge_label_and_cond))

    path_multi_edges.append((path[-1], tuple([""]), path[-1].reasons))
    all_edges_conditions = []
    for path_edges in path_multi_edges:
        all_edges_conditions.append(path_edges[1])

    for edge_condition in product(*all_edges_conditions):
        path_no_parallel_edges = []
        for node_idx, edge in enumerate(edge_condition):
            node_obj: Node = path_multi_edges[node_idx][0]
            assert isinstance(node_obj, Node)
            edge_label: str = edge.split("[")[0]
            if edge_label:
                edge_condition = eval("[" + edge.split("[")[1])
            else:
                edge_condition = []
            if not isinstance(edge_condition, list):
                raise ValueError(
                    f"eval should return a list with parameter {edge_condition}"
                )

            # print("pathExpanded > ", path_multi_edges[node_idx][0], edge_label, edge_condition, path_multi_edges[node_idx][2])
            path_no_parallel_edges.append(
                EdgeWithConditions(
                    str(node_obj).replace("\n", "."),
                    edge_label,
                    Conditions(edge_condition),
                    Conditions(node_obj.reasons),
                )
            )

        path_no_parallel_edges: list[EdgeWithConditions]
        returned_paths.append(path_no_parallel_edges)
    return returned_paths


def get_path_conditions(
    paths_list: list[list[Node]],
    nx_graph: nx.MultiDiGraph,
) -> list[PathWithConditions]:
    """
    from a list of paths, get the conditions for each path
    :param paths_list:
    :param nx_graph:
    :return:
    """
    all_paths_conditions = []
    paths_with_conditions: list[PathWithConditions] = []
    for node_list in paths_list:
        detailed_paths = get_path_edges_attr(node_list, nx_graph)
        for detailed_path in detailed_paths:
            all_paths_conditions.append(
                [path_detail.cond_edge for path_detail in detailed_path]
                + [path_detail.cond_node for path_detail in detailed_path]
            )
            paths_with_conditions.append(
                PathWithConditions(
                    node_list,
                    all_paths_conditions[-1],
                    [path_detail.edge_label for path_detail in detailed_path],
                )
            )

    return paths_with_conditions


def filter_paths_by_dst(
    paths_list: list[list[Node]],
    dst_machine: str,
    dst_user: str,
) -> list[list[Node]]:
    """
    from a list of paths, filter by dst_machine and dst_user
    :param paths_list:
    :param dst_machine:
    :param dst_user:
    :return:
    """
    filtered_paths = []
    for node_list in paths_list:
        sub_node = node_list[-1]
        if dst_machine and dst_machine not in sub_node.machine:
            continue
        if dst_user and dst_user not in sub_node.user:
            continue
        filtered_paths.append(node_list)
    return filtered_paths


def find_path(
    archi_graph: Graph,
    src_machine: str,
    src_user: str,
    dst_machine: str = "",
    dst_user: str = "",
) -> list[PathWithConditions]:
    """
    single_source_shortest_path
    :param archi_graph:
    :param src_machine: src machine
    :param src_user: src user
    :param dst_machine: dst machine
    :param dst_user: dst user
    :return:
    """
    at_least_one_src_node = False
    all_paths_with_conditions = []
    for node in archi_graph.graph.nodes:
        node: Node
        if (
            src_user.lower() in node.user.lower()
            and src_machine.lower() in node.machine.lower()
        ):
            at_least_one_src_node = True
            logging.debug(f"src node {node=}")
            paths = nx.single_source_shortest_path(archi_graph.graph, node)
            # print(f"node0 {list(paths.keys())}")
            # print(f"node0 {list(paths.values())}")
            nodes_of_paths = filter_paths_by_dst(
                list(paths.values()), dst_machine, dst_user
            )
            all_paths_with_conditions += get_path_conditions(
                nodes_of_paths, archi_graph.graph
            )

    for ii, path_w_cond in enumerate(all_paths_with_conditions):
        print(f"[{ii}] {str(path_w_cond)}")

    if not at_least_one_src_node:
        print(f"no src node found with {src_machine=} {src_user=}")
    elif not all_paths_with_conditions:
        print(
            f"some paths started from {src_machine=} {src_user=} but none match filter on {dst_machine=} {dst_user=}"
        )
    else:
        print(f"all {len(all_paths_with_conditions)} path(s) displayed")
    return all_paths_with_conditions


def find_path_src_dst(archi_graph: Graph, src_u, src_m, dst_u, dst_m):
    nxgraph = archi_graph.graph
    src = archi_graph.get_node(src_u, src_m)
    dst = archi_graph.get_node(dst_u, dst_m)
    logging.debug(f"search all paths from {str(src)} to {str(dst)}")
    paths = nx.all_simple_paths(nxgraph, src, dst)

    if not paths:
        logging.info("no path here")
        return
    for node_list in paths:
        log_path(node_list, nxgraph)
    logging.debug("all paths logged")


def single_source_shortest_path(archi_graph: Graph, src_machine: str, src_user: str):
    paths = nx.single_source_shortest_path(
        archi_graph.graph,
        archi_graph.get_node_by_machine_user(src_machine, src_user, strict=False),
    )
    if not paths:
        logging.info("no path here")
        return
    for idx, node_list in enumerate(paths.values()):
        node_list: list[Node]
        print(f"path {idx}")
        dump_path_table(node_list, archi_graph.graph)
    logging.debug("all paths logged")


def get_all_critical_paths(
    graph: Graph,
    only_shortest=False,
    max_retrieve: int = -1,
    include_all_nodes_as_initials=False,
):
    critical_paths: list[list[Node]] = []
    initial_iterator = graph.initial_nodes
    if include_all_nodes_as_initials:
        initial_iterator = graph.graph.nodes
    for done, initial_node in enumerate(initial_iterator):
        if graph.graph.degree(initial_node) == 0:
            continue
        if (done * 100 // len(graph.initial_nodes)) % 10 == 0:
            logging.info(
                f"{(done * 100 // len(graph.initial_nodes))}% search critical path from {initial_node}"
            )
        for dst_node in graph.critical_nodes:
            if initial_node == dst_node:
                logging.warning(f"Found initial node that is critical ({initial_node})")
                continue
            if graph.graph.degree(dst_node) == 0:
                continue
            else:
                criticals = []
                # TODO test that function works as expected
                if only_shortest:
                    try:
                        criticals = list(
                            nx.all_shortest_paths(graph.graph, initial_node, dst_node)
                        )
                    except nx.exception.NetworkXNoPath:
                        # no path found from src to dst
                        pass
                else:
                    criticals = list(
                        nx.all_simple_paths(graph.graph, initial_node, dst_node)
                    )
                critical_paths.extend(criticals)
                for p in criticals:
                    log_path(p, graph.graph)

        if max_retrieve != -1 and len(critical_paths) > max_retrieve:
            break

    logging.info(f"{len(critical_paths)} critical paths found")

    return critical_paths


def get_critical_path_remedations_str(
    critical_path_nodes: list[Node], archi_graph: Graph
) -> list[str]:
    pass
    # remediations_str = []
    # for src_node, dst_node in zip(critical_path_nodes[0:], critical_path_nodes[1:]):
    #     relation_obj: Relation = archi_graph.relations[(src_node, dst_node)]
    #     remediations_str.append(
    #         f"{str(src_node)=} {str(dst_node)=} rel {relation_obj.get_remediation()}"
    #     )
    # print("\n-".join(remediations_str))
    # return remediations_str


def log_path(nodes_list, nxgraph):
    logging.error(f"src to dst: path length {len(nodes_list)}")
    # print(nodes_list)
    cond_list = get_path_edges_attr(nodes_list, nxgraph)
    if len(cond_list) != 1:
        raise NotImplementedError("not implemented yet")
    logging.error(f"{' '.join(list(map(str, cond_list[0])))}")


def dump_path_table(nodes_list: list[Node], nxgraph):
    """
    from path as nodes_list, print cvs separated with semicolon ;
    src > dst; edge_label; conditions_edge
    src > dst; edge_label; conditions_edge
    ...
    src > dst; edge_label; conditions_edge
    :param nodes_list:
    :param nxgraph:
    :return:
    """

    def merge_gpo_undef(conditions: list[str]) -> list[str]:
        gpo_dict = defaultdict(list)
        other_lines = []

        for line in conditions:
            match = re.match(r"(machine \w+), GPO (\w+) is undefined", line)
            if match:
                machine = match.group(1)
                gpo = match.group(2)
                gpo_dict[machine].append(gpo)
            else:
                other_lines.append(line)
        result = []
        for machine, gpos in gpo_dict.items():
            if len(gpos) >= 1:
                result.append(f"{machine}, GPO undefined: {', '.join(gpos)}")
        result.extend(other_lines)
        return result

    print(f"src to dst: path length {len(nodes_list)}")
    # print(nodes_list)
    cond_list = get_path_edges_attr(nodes_list, nxgraph)
    if len(cond_list) != 1:
        raise NotImplementedError("not implemented yet")
    for edge_cond0, edge_cond1 in zip(cond_list[0], cond_list[0][1:]):
        edge_cond0: EdgeWithConditions
        edge_cond1: EdgeWithConditions
        all_cond = (
            edge_cond0.cond_edge.conditions
            + edge_cond0.cond_node.conditions
            + edge_cond1.cond_node.conditions
        )

        all_cond = list(set(all_cond))

        all_cond = merge_gpo_undef(all_cond)
        all_cond.sort()
        print(
            f"{edge_cond0.src_node_str} > {edge_cond1.src_node_str}; "  # noqa E702
            f"{edge_cond0.edge_label}; "  # noqa E702
            f"{all_cond}"  # noqa E702
        )
        input("ok?")


def dump_conditions(conditions: list[Conditions]):
    # TODO move somewhere else
    for cond_edge in conditions:
        cond_edge.conditions and print(
            "\n".join(f"- {c}" for c in cond_edge.conditions)
        )


def find_longest_shortest_path(archi_graph: Graph, len_min: int = 2):
    logging.debug("get longest path")
    nx_g = archi_graph.graph
    for src_node in nx_g.nodes:
        if archi_graph.graph.degree(src_node) == 0:
            continue
        for dst_node in nx_g.nodes:
            if str(src_node) == str(dst_node):
                continue
            if archi_graph.graph.degree(dst_node) == 0:
                continue
            all_short = None
            try:
                all_short = nx.all_shortest_paths(nx_g, src_node, dst_node)
                # all_short = nx.all_simple_paths(nx_g, src_node, dst_node)
            except nx.exception.NetworkXNoPath:
                print("except reached")
            if all_short is None:
                continue
            try:
                get_path_conditions(list(all_short), nx_g)
                # for shortpath in all_short:
                #     print(f"short path of {len(shortpath)} from {shortpath[0]} to {shortpath[-1]}")
                #     if len(shortpath) < len_min:
                #         continue
                #     get_path_conditions([shortpath], nx_g)
                #     #     logging.info(f"--short with len>{len_min} --"*5)
                #     #     log_path(paths[0], nx_g)

            except nx.exception.NetworkXNoPath:
                pass


def get_strongly_connected_components(archi_graph: Graph):
    nxgraph = archi_graph.graph
    for nodes in sorted(nx.strongly_connected_components(nxgraph), key=len):
        print(len(nodes), "_" * 10)
        for node in nodes:
            print(str(node).replace("\n", ","))


def find_most_valuable_node(archi_graph: Graph):
    logging.debug("let's go")
    nxgraph = archi_graph.graph
    all_paths = []
    for node in nxgraph.nodes:
        paths = nx.single_source_shortest_path(nxgraph, node)
        logging.debug(f"{len(paths)} {str(node)}")
        all_paths.append(paths)
    all_paths.sort(key=len, reverse=True)
    len_by_src_node: defaultdict = defaultdict(int)
    for a in all_paths:
        len_by_src_node[len(a)] += 1
    sum_nodes = 0
    for v in len_by_src_node.values():
        sum_nodes += v
    print("nodes found", sum_nodes)


def find_paths_by_edge_labels(
    archi_graph: Graph,
    edge_labels_sequence: list[str],
) -> list[PathWithConditions]:
    """
    Find all paths in the graph where the sequence of edge labels matches the input list.
    
    :param archi_graph: The attack graph to search
    :param edge_labels_sequence: List of edge labels in order (e.g., ["RDP", "runas", "wmic", "ServiceExeModify"])
    :return: List of PathWithConditions objects matching the label sequence
    """
    if not edge_labels_sequence:
        return []
    
    nxgraph = archi_graph.graph
    matching_paths: list[list[Node]] = []
    
    def extract_label(edge_label_str: str) -> str:
        """Extract the base label from edge data (removes conditions in brackets)"""
        # Edge labels are stored as "LABEL[['condition1', 'condition2']]"
        # Extract just the label part
        if "[" in edge_label_str:
            return edge_label_str.split("[")[0]
        return edge_label_str
    
    def dfs_match_labels(
        current_node: Node,
        remaining_labels: list[str],
        current_path: list[Node],
        visited_edges: set[tuple[Node, Node, int]],
    ):
        """
        Depth-first search to find paths matching the label sequence.
        :param current_node: Current node in the traversal
        :param remaining_labels: Remaining edge labels to match
        :param current_path: Current path being built
        :param visited_edges: Set of visited edges (u, v, key) to avoid cycles
        """
        # If we've matched all labels, we found a valid path
        if not remaining_labels:
            matching_paths.append(current_path[:])
            return
        
        # Get the next label we need to match
        next_label = remaining_labels[0]
        next_remaining_labels = remaining_labels[1:]
        
        # Check all outgoing edges from current node
        for neighbor in nxgraph.successors(current_node):
            # Check all edges between current_node and neighbor (MultiDiGraph can have multiple)
            edge_data_dict = nxgraph.get_edge_data(current_node, neighbor)
            if edge_data_dict is None:
                continue
            
            for edge_key, edge_data in edge_data_dict.items():
                edge_label = extract_label(edge_data["label"])
                
                # Check if this edge matches the next label we're looking for
                if edge_label == next_label:
                    edge_tuple = (current_node, neighbor, edge_key)
                    # Avoid revisiting the same edge (but allow revisiting nodes)
                    if edge_tuple in visited_edges:
                        continue
                    
                    # Add edge to visited set and continue search
                    visited_edges.add(edge_tuple)
                    current_path.append(neighbor)
                    
                    # Recursively search from the neighbor with remaining labels
                    dfs_match_labels(neighbor, next_remaining_labels, current_path, visited_edges)
                    
                    # Backtrack
                    current_path.pop()
                    visited_edges.remove(edge_tuple)
    
    # Start DFS from all nodes in the graph
    for start_node in nxgraph.nodes:
        visited_edges = set()
        current_path = [start_node]
        dfs_match_labels(start_node, edge_labels_sequence, current_path, visited_edges)
    
    # Convert matching paths to PathWithConditions objects
    paths_with_conditions = get_path_conditions(matching_paths, nxgraph)
    
    return paths_with_conditions


def graph_stats(archi_graph: Graph):
    """
    Print some statistics about the graph.
    :param archi_graph:
    :return:
    """
    nxgraph = archi_graph.graph
    print(
        f"Graph '{archi_graph.name}' has {nxgraph.number_of_nodes()} nodes and {nxgraph.number_of_edges()} edges"
    )
    # count edges by label
    edge_labels = defaultdict(int)
    for u, v, data in nxgraph.edges(data=True):
        edge_labels[data["label"].split("['")[0]] += 1
    print("Edge labels count:")
    for label, count in edge_labels.items():
        print(f"  {label}: {count}")
