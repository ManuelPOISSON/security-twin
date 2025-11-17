#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2021 AMOSSYS. All rights reserved.
#
# This file is part of Cyber Range AMOSSYS.
#
# Cyber Range AMOSSYS can not be copied and/or distributed without the express
# permission of AMOSSYS.
#
import os
from collections import OrderedDict
from typing import List

import pytest
from _pytest.python import Metafunc
from _pytest.python import Parser
from jinja2 import Template

import cr_api_client.core_api as core_api
from provisioning.actions.set_time.action import SetTime
from provisioning.Chronology import Chronology
from provisioning.ChronologyFactory import ChronologyFactory
from provisioning.ChronologyRunner import ChronologyRunner
from provisioning.data_model.Organization import Organization
from provisioning.OrganizationFactory import OrganizationFactory

AVAILABLE_BASEBOXES = core_api.fetch_baseboxes()


# Giving possibility to run tests focus on a basebox_id
def pytest_addoption(parser: Parser) -> None:
    parser.addoption(
        "--baseboxes",
        action="store",
        help="baseboxes: run tests only on baseboxes id provided (comma-separated)",
    )


# Defining baseboxes on which run tests
def pytest_generate_tests(metafunc: Metafunc) -> None:
    baseboxes = get_basebox_ids(
        os.path.join(os.path.dirname(metafunc.module.__file__), "basebox_list.txt")
    )
    metafunc.parametrize("basebox_id", baseboxes)


# Helpers functions


def get_basebox_ids(file: str) -> List:
    try:
        with open(file) as basebox_file:
            line = basebox_file.readline()
            ids = line.replace(" ", "").replace("\n", "").replace("\t", "").split(",")
            return ids
    except Exception:
        return []


def format_topology(file: str, basebox_id: str) -> str:
    content = ""
    with open(file) as topology_file:
        content = topology_file.read(-1)
    topology_template = Template(content)
    return topology_template.render(basebox_id=basebox_id)


#########################################################################
# Assuming provisioning tests have to define basebox_id fixture         #
# By default, topology is provided in test dir in topology.yaml         #
# It can be overiden by declaring topology fixture in test context      #
#########################################################################

# Environment setup fixtures


# Reseting CR state before each tests
@pytest.fixture(autouse=True)
def reset_cr() -> None:
    print("[+] Reset cyber range")
    core_api.reset()


@pytest.fixture(autouse=True)
def auto_skipper(basebox_id: str, request: pytest.FixtureRequest) -> None:
    baseboxes = request.config.getoption("--baseboxes")

    if not baseboxes:
        return
    if basebox_id not in baseboxes.split(","):
        pytest.skip()


# Ensure baseboxes are present ran before all tests
@pytest.fixture(autouse=True)
def ensure_basebox_exists(basebox_id: str, request: pytest.FixtureRequest) -> None:
    if basebox_id == "":
        pytest.skip(f"{request.node.name}: No basebox provided")
    basebox = next(
        (item for item in AVAILABLE_BASEBOXES if item["id"] == int(basebox_id)), None
    )
    if basebox is None:
        pytest.skip(f"{request.node.name}: Basebox {basebox_id} unknown")

    print(f" Running {request.node.name} against basebox {basebox['name']}")


@pytest.fixture
def topology(basebox_id: str, request: pytest.FixtureRequest) -> str:
    return format_topology(
        os.path.join(os.path.dirname(request.node.fspath), "topology.yaml"),
        basebox_id,
    )


@pytest.fixture
def simulation_id(topology: str, tmpdir: pytest.TempdirFactory) -> int:
    print("[+] Create and run simulation")
    file = tmpdir.join("topology.yaml")
    file.write(topology)
    id_simulation = core_api.create_simulation_from_topology(file.realpath())
    core_api.start_simulation(id_simulation, use_install_time=True)
    return id_simulation


# yield fixtures permits to release resources after the execution of test
# the code after the yield is run after the test
# this fixture is scoped to session:
# it permit to clean the CR state at the end of all tests
@pytest.fixture(scope="session", autouse=True)
def cleaning() -> None:
    yield None
    core_api.reset()


# Provisioning fixture


@pytest.fixture
def provisioning_config(request: pytest.FixtureRequest) -> str:
    content = ""
    with open(
        os.path.join(os.path.dirname(request.node.fspath), "provisioning.yaml")
    ) as provisioning_file:
        content = provisioning_file.read(-1)
    return content


@pytest.fixture
def provisioning_path(tmpdir: pytest.TempdirFactory) -> str:
    return tmpdir.realpath() + "/provisioning"


@pytest.fixture
def organization(simulation_id: int) -> Organization:
    of = OrganizationFactory(simulation_id)
    return of.generate()


@pytest.fixture
def chronology(organization: Organization, provisioning_config: str) -> Chronology:
    cf = ChronologyFactory(organization, provisioning_config)
    return cf.generate()


@pytest.fixture
def required_chronology(chronology: Chronology, required_actions: List) -> Chronology:
    """
    Keeping only required_actions in the provisioning generated chronology
    If required_chronology fixture needed test should declare
    required_actions fixture
    """
    new_steps = OrderedDict()
    for datetime in chronology.chronology_steps:
        actions_to_play = []
        for action in chronology.chronology_steps[datetime]:
            if action.__class__ in required_actions:
                actions_to_play += [action]
        if len(actions_to_play) > 0 and not (
            len(actions_to_play) == 1 and actions_to_play[0].__class__ == SetTime
        ):
            new_steps[datetime] = actions_to_play
    chronology.chronology_steps = new_steps
    return chronology


@pytest.fixture
def runner(simulation_id: int, provisioning_path: str) -> ChronologyRunner:
    return ChronologyRunner(simulation_id, provisioning_path)
