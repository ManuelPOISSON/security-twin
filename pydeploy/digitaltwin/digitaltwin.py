import shutil
from pathlib import Path

from cdktf import App, LocalBackend
import os
import stat

from digitaltwin.model.host_dto import HostDTO
from digitaltwin.model.network_dto import NetworkDTO
from digitaltwin.components_libvirt.infrastructure import InfrastructureLibvirt
from digitaltwin.runner import Runner
from digitaltwin.utils.config import Config


class VirtualDigitalTwin:
    def __init__(self, uri: str, input_data: dict, outdir: str = "output", config: Config = None, pool_path: str = None):
        self.model = input_data
        self.app = App(outdir=outdir)
        if config is None:
            config = Config()
        self.config = config

        self.runner = Runner(outdir, self.config)

        hosts: list[HostDTO] = []
        for host in input_data["hosts"]:
            # Unpack dict host and create HostDTO more readibilty
            # I'm not sure that this class should assume this responsibility
            try:
                hosts.append(HostDTO(**host))
            except:
                print("Error with the input model, exit")
                raise Exception()

        networks: list[NetworkDTO] = []
        for net in input_data["networks"]:
            try:
                networks.append(NetworkDTO(**net))
            except Exception as e:
                raise e
        if pool_path is not None:
            self.set_pool_path(pool_path)
        self.infra = InfrastructureLibvirt(self.app, os.getenv("INFRA_ID", "default-infra"), uri, hosts, networks, pool_path=pool_path)
        self.backend = LocalBackend(self.infra, path="./backend/terraform.tfstate", workspace_dir=outdir)

    def set_pool_path(self, pool_path: str):
        """
        Recursively set the execute bit for 'others' on the pool path and its parents.
        """
        if not Path(pool_path).is_dir():
            os.makedirs(pool_path, exist_ok=True)

        pfile = Path(pool_path)
        while pfile.name != "":
            current_mode = os.stat(pfile).st_mode
            # Check if the execute bit for others is set
            if not current_mode & stat.S_IXOTH:
                print(f"adding execute bit for others on {pfile}")
                new_mode = current_mode | stat.S_IXOTH
                os.chmod(pfile, new_mode)

            pfile = pfile.parent

    def deploy(self):
        self.app.synth()
        self.runner.run_deploy()

    def destroy(self, rm_outdir: bool = True):
        self.runner.run_destroy()
        if rm_outdir and os.path.isdir(f"{self.runner.outdir}"):
            print(f"Removing directory {self.runner.outdir}")
            shutil.rmtree(f"{self.runner.outdir}")

    def update(self, model):
        return NotImplemented
        self.model = model
        self.infra.update(self.model)
        self.deploy()
