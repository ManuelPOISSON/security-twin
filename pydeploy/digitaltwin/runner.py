import json
import os
import subprocess

from digitaltwin.utils.config import Config


class Runner:
    def __init__(self, outdir: str, config: Config):
        self.env = os.environ.copy()
        if config.debug:
            self.env["CDKTF_LOG_LEVEL"] = "debug"
        self.outdir = outdir
        self.cdktf_config = {
            "language": "python",
            "app": "echo '{}'",
            "sendCrashReports": "false",
            "terraformProviders": ["dmacvicar/libvirt@~> 0.8"],
            "codeMakerOutput": "providers",
            "context": {},
            "backend": {"local": {"path": "backend/terraform.tfstate"}},
        }
        with open(outdir + "/cdktf.json", "w") as fd:
            json.dump(self.cdktf_config, fd)

    def run_deploy(self):
        subprocess.run(
            ["cdktf", "deploy", "-o", ".", "--auto-approve"],
            cwd=self.outdir,
            env=self.env,
        )

    def run_destroy(self):
        subprocess.run(
            ["cdktf", "destroy", "-o", ".", "--auto-approve"],
            cwd=self.outdir,
            env=self.env,
        )
