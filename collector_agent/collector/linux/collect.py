import json
import logging
import shutil
import tarfile
import traceback
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

import paramiko
import requests
from cyclonedx.model.bom import Bom
from paramiko import PKey
from paramiko.client import WarningPolicy
from paramiko.ssh_exception import SSHException
from tqdm import tqdm

from collector.model.exporter import JsonExporter
from collector.model.linux import LinuxData
from collector.model.local_windows import Software
from collector.utils import LinuxContext

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

TRYVY_EXEC_CMD = "./trivy rootfs --offline-scan --format cyclonedx -o sbom.json /  --skip-dirs /tmp/ "
URL_TRIVY = "https://github.com/aquasecurity/trivy/releases/download/v0.67.2/trivy_0.67.2_Linux-64bit.tar.gz"


def prepare_trivy() -> Path | None:
    path = shutil.which("trivy")
    if path:
        return Path(path)

    path_to_trivy = Path.cwd() / "extra" / "trivy"
    if path_to_trivy.exists():
        return path_to_trivy

    dir_trivy = path_to_trivy.parent
    dir_trivy.mkdir(parents=True, exist_ok=True)

    logger.info("Cannot find the trivy path")
    logger.info(f"Attempting to download trivy on this url: {URL_TRIVY}")

    try:
        response = requests.get(URL_TRIVY, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get("content-length", 0))
        chunk_size = 8192

        with (
            open(dir_trivy / "trivy.tar.gz", "wb") as f,
            tqdm(total=total_size, unit="B", unit_scale=True, desc="Trivy download") as bar,
        ):
            for chunk in response.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                bar.update(len(chunk))
        logger.info("Download completed")

        logger.info("Extraction...")
        with tarfile.open(dir_trivy / "trivy.tar.gz", "r:gz") as tar:
            for member in tar.getmembers():
                if member.name.endswith("/trivy") or member.name == "trivy":
                    member.name = "trivy"
                    tar.extract(member, path=dir_trivy)
                    break
        logger.info("Extraction completed")
    except Exception as e:
        logger.error("Cannot download Trivy")
        traceback.print_exc()
        return None

    return path_to_trivy


def linux_collect(context: LinuxContext) -> int:
    trivy_path = prepare_trivy()
    if not trivy_path:
        logger.critical("Cannot find Trivy... exit")
        return -1

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(WarningPolicy())

    try:
        if context.key_path:
            logger.info("Trying to connect to ")
            passphrase = None
            if context.passphrase:
                passphrase = context.passphrase.encode()
            ssh_key = PKey.from_path(context.key_path, passphrase=passphrase)
            client.connect(context.hostname, context.port, username=context.username, pkey=ssh_key)
        else:
            client.connect(
                context.hostname,
                context.port,
                context.username,
                context.password,
                allow_agent=False,
                look_for_keys=False,
            )

        stdin, stdout, stderr = client.exec_command("mktemp -d")

        tmp_path = stdout.read().decode().strip()
        sftp = client.open_sftp()

        sftp.put(trivy_path, tmp_path + "/trivy")

        _, stdout, _ = client.exec_command(f"cd {tmp_path} && chmod +x trivy && {TRYVY_EXEC_CMD} ")

        logger.warning(f"Trivy return code:{stdout.channel.recv_exit_status()}")
        sftp.get(f"{tmp_path}/sbom.json", "out.json")

        client.exec_command(f"rm {tmp_path}")

        client.close()

        with open("out.json", "r") as f:
            bom = Bom.from_json(data=json.loads(f.read()))

        machine_name = bom.metadata.component.name

        softwares: list[Software] = []
        for component in bom.components:
            softwares.append(Software(name=component.name, version=component.version))
        data = LinuxData(machine_name=machine_name, softwares=softwares)
        Path(context.output_directory).mkdir(parents=True, exist_ok=True)
        exporter = JsonExporter(f"{context.output_directory}/linux/{machine_name}")
        exporter.export(data, "all.json")

    except (SSHException, OSError) as e:
        logger.error(e)
        traceback.print_exc()
        return -1
    return 0
