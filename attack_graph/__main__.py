import logging
from pathlib import Path
import argparse

import networkx as nx
from sqlalchemy import create_engine

from attack_graph.edges_builder import (
    BuilderRDP,
    BuilderRunas,
    BuilderServiceExeModify,
    BuilderWmic,
    BuilderPSRemote,
    BuilderCVE_sam_the_admin_2021_42278,
    BuilderCVE_ActiveMQ_2023_46604,
    BuilderCVE_winrar_2023_38831,
    BuilderCVE_ZeroLogon_2020_1472,
    BuilderCVE_log4j_2021_44228,
)
from attack_graph.graph import Graph
from attack_graph.graph_data_extraction import (
    find_path,
    single_source_shortest_path,
    dump_conditions,
    find_longest_shortest_path,
    graph_stats,
)
from attack_graph.nodes_builder import NodesBuilder
from model.db import engine_base_path
from model.db_connect import connection_cred
from provisioning.prepare_deploy import gen_hosts_file


def parse_args():
    parser = argparse.ArgumentParser(
        description="Attack Graph CLI: python -m attack_graph MODE [ANALYSIS] [SRC_DST_NODES] [OPTIONS]"
    )
    parser.add_argument("mode", choices=["b", "l"], help="Mode: b (build) or l (load)")
    parser.add_argument(
        "analysis",
        choices=["csv", "human", "gui"],
        nargs="?",
        help="Analysis type (optional)",
        default=None,
    )
    parser.add_argument(
        "src_dst_nodes",
        nargs="*",
        help="Optional: srcM srcU [dstM dstU] (only if analysis is provided)",
    )
    parser.add_argument(
        "--hosts-file",
        type=str,
        help="Path to hosts file (only for human analysis)",
        default=None,
    )
    parser.add_argument(
        "--graph-path",
        type=str,
        help="Path to graph file: for load mode (l), path to existing file; for build mode (b), path where to save (e.g., 'data/graph/other_g') (required when mode is 'l')",
        default=None,
    )
    parser.add_argument('-lp', '--last-path',
                        action='store_true')
    args = parser.parse_args()

    if args.analysis is None and args.src_dst_nodes:
        parser.error("src_dst_nodes can only be provided if analysis is specified")

    if args.analysis != "human" and args.hosts_file is not None:
        parser.error("--hosts-file is only allowed when analysis is 'human'")

    if args.mode == "l" and args.graph_path is None:
        parser.error("--graph-path is required when mode is 'l' (load)")

    return args


def parse_src_dst_nodes(src_dst_nodes: list[str]) -> tuple[str, str, str, str]:
    if len(src_dst_nodes) not in [2, 4]:
        raise ValueError("You must provide 2 or 4 values for srcM srcU [dstM dstU]")
    src_mach = src_dst_nodes[0]
    src_user = src_dst_nodes[1]
    dst_mach = ""
    dst_user = ""
    if len(src_dst_nodes) == 4:
        dst_mach = src_dst_nodes[2]
        dst_user = src_dst_nodes[3]
    return src_mach, src_user, dst_mach, dst_user


def print_graph(gr: Graph):
    print(gr.graph)
    nx_edges_list = sorted(list(gr.graph.edges()), key=lambda x: str(x[0]) + str(x[1]))
    for nxedge in nx_edges_list:
        print("nxedge: ", str(nxedge))


def get_graph(args: argparse.Namespace) -> Graph:
    if args.mode == "l":
        graph_path = Path(args.graph_path)
        
        # If the path is a directory, look for a file inside it
        if graph_path.is_dir():
            raise FileNotFoundError(
                f"{graph_path} is a directory, not a file."
            )
        elif not graph_path.is_file():
            raise FileNotFoundError(
                f"{graph_path} is not a file."
            )        
        graph = Graph.load_object(str(graph_path))
    elif args.mode == "b":
        graph = full_build_graph(graph_path=args.graph_path)
    else:
        raise ValueError("You must chose a mode l (load) or b (build)")
    return graph


def full_build_graph(
    dbname: str = connection_cred["db_name"],
    graph_path: str = "",
) -> Graph:
    """
    :param dbname: name of the database to request (default: connection_cred["db_name"])
    :param graph_path: path to save the graph (e.g., "data/graph/other_g") (default: "", the graph is not saved)
    :return:
    """

    if graph_path:
        path_obj = Path(graph_path)
        save_dir = path_obj.parent
        graph_name = path_obj.name  # filename without extension
    else:
        save_dir = None
        graph_name = "default_name"

    logging.info(f"Building graph based on database {dbname}")
    engine = create_engine(f"{engine_base_path}{dbname}")
    all_edges = []
    edge_builders = [
        BuilderRDP,
        BuilderRunas,
        BuilderServiceExeModify,
        BuilderWmic,
        BuilderPSRemote,
        BuilderCVE_sam_the_admin_2021_42278,
        BuilderCVE_ActiveMQ_2023_46604,
        BuilderCVE_winrar_2023_38831,
        BuilderCVE_ZeroLogon_2020_1472,
        BuilderCVE_log4j_2021_44228,
    ]
    for edge_builder in edge_builders:
        logging.debug(f"{edge_builder}")
        edge_builder_instance = edge_builder(engine)
        all_edges.extend(edge_builder_instance.build_edges())
    logging.debug(f"Edges built: {all_edges}")
    nodes_rdp = [edge_rdp.dst for edge_rdp in all_edges if edge_rdp.label == "RDP"]
    nodes_builder = NodesBuilder(engine)
    nodes_builder.nodes_rdp = nodes_rdp
    nodes_builder.build_nodes()

    graph = Graph(
        nx.MultiDiGraph(), nodes_builder.nodes, all_edges, name=graph_name
    ).build_graph()

    if graph_path:
        # Create directory if it doesn't exist
        save_dir.mkdir(parents=True, exist_ok=True)
        # Save the file as data/graph/other_g (pickle file)
        save_path = save_dir / graph_name
        graph.save_object(str(save_path))
        logging.info(f"Graph saved in {save_path}")

    return graph


def analysis_human(graph: Graph, args: argparse.Namespace):
    src_mach, src_user, dst_mach, dst_user = parse_src_dst_nodes(args.src_dst_nodes)

    paths_with_cond = find_path(
        graph, src_mach, src_user, dst_machine=dst_mach, dst_user=dst_user
    )
    if not paths_with_cond:
        return
    if len(paths_with_cond) == 1:
        path_to_dump = 0
    elif args.last_path:
        path_to_dump = len(paths_with_cond) - 1
    else:
        try:
            path_to_dump = int(input(f"choose which path to reproduce (0 - {len(paths_with_cond) - 1}): "))
        except ValueError:
            try:
                path_to_dump = int(input(f"Invalid input. Please enter a number between 0 and {len(paths_with_cond) - 1}: "))
            except ValueError:
                raise Exception(f"Failed to enter a valid number between 0 and {len(paths_with_cond) - 1} after two attempts.")
    # path_to_dump = 5
    paths_with_cond[path_to_dump].dump_conditions()
    logging.info(
        f"computers in path: {paths_with_cond[path_to_dump].get_involved_computers()}"
    )
    if args.hosts_file:
        gen_hosts_file(
            Path(args.hosts_file),
            create_engine(f"{engine_base_path}{connection_cred['db_name']}"),
            paths_with_cond[path_to_dump].get_involved_computers(),
            ad=True,
        )


def analysis_gui(graph: Graph, nodes_to_remove: set[str] = None):
    if not nodes_to_remove:
        nodes_to_remove = set()
    graph.show_graph(
        save_pyvis=False,
        gephi_remove_isolated_node=True,
        nodes_to_remove=nodes_to_remove,
    )


def analysis_csv(graph: Graph, args: argparse.Namespace):
    src_mach, src_user, _, _ = parse_src_dst_nodes(args.src_dst_nodes)
    single_source_shortest_path(
        graph, src_mach, src_user
    )  # dump csv of paths with conditions


def main():
    args = parse_args()

    graph = get_graph(args)
    ## pp = find_paths_by_edge_labels(graph, ["RDP", "runas", "wmic", "ServiceExeModify"])
    ## logging.error(f"found {len(pp)} paths")
    ## for p in pp:
    ##     print("---",p)
 

    graph_stats(graph)
    if args.analysis == "csv":
        analysis_csv(graph, args)
    elif args.analysis == "human":
        analysis_human(graph, args)
    elif args.analysis == "gui":
        analysis_gui(graph)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main()

"""
working example: python -m attack_graph b human c0 u0 c2 SYSTEM
"""
