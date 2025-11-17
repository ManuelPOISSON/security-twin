#!/usr/bin/env python3

import argparse
import json
import logging
import os
import sys

from dotenv import load_dotenv
from digitaltwin.digitaltwin import VirtualDigitalTwin
from digitaltwin.host_factory import gen_hosts_model
from digitaltwin.utils.config import resolve_env_path

load_dotenv()


def parse_input_file(path_inputfile: str):
    def model_from_json(path_json):
        logging.debug(f"gen model from '{path_json}'")
        with open(path_json, "r") as fd:
            return json.load(fd)

    if not os.path.isfile(path_inputfile):
        raise FileNotFoundError(path_inputfile)
    try:
        model = model_from_json(path_inputfile)
    except json.decoder.JSONDecodeError as err:
        gen_hosts_model(path_inputfile, f"{path_inputfile}.json")
        model = model_from_json(f"{path_inputfile}.json")
    return model

def parse_cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="pydeploy", description="Lib to deploy an infrastructure")
    parser.add_argument(
        "action",
        choices=["create", "destroy"],
        help="Action to perform: create or destroy",
    )

    parser.add_argument("-i", "--input", required=True, help="JSON or hosts Input file")

    parser.add_argument("-d", "--directory", required=True, help="Directory where the terraform state will be stored")

    return parser.parse_args()


def main():
    args = parse_cli()

    model = parse_input_file(args.input)
    ssh_username = os.getenv("SSH_USERNAME")
    ssh_key = os.getenv("SSH_KEY")
    vdt_prefix = "qemu:///system"
    if ssh_username and ssh_key:
        vdt_prefix = "qemu+ssh://" + os.getenv("SSH_USERNAME") + "@172.16.2.53/system?keyfile=" + os.getenv("SSH_KEY")
    pool_path = resolve_env_path("POOL_PATH", f"/opt/libvirt/pool_{os.getenv('INFRA_ID', 'digital_twin_infra')}")
    vdt = VirtualDigitalTwin(
        vdt_prefix + os.getenv("VIRT_PARAM", ""),
        input_data=model,
        outdir=args.directory,
        pool_path=pool_path
    )
    if args.action == "create":
        vdt.deploy()
    elif args.action == "destroy":
        vdt.destroy()
    else:
        return -1

    return 0


if __name__ == "__main__":
    main()
