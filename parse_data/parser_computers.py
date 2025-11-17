import logging
from pathlib import Path

from model import MachineWindows, MachineLinux, Machine, ADMachine
from parse_data.parser_ldap import ParserLDAP


class ParserComputers(ParserLDAP):
    def __init__(self, path_sharphound_folder: Path) -> None:
        super().__init__(path_sharphound_folder, "computers")

    def get_machines(self) -> list[tuple[Machine, ADMachine]]:
        """Returns a list of Machine, ADMachine objects.

        By default, all ADMachines are set to is_dc=False.
        """
        machines = []
        for cn, val in self.json_data.items():
            name = val["name"]
            machine_os = val.get("operatingSystem", "")
            machine_to_add = None
            if "windows" in machine_os.lower():
                build = val.get("operatingSystemVersion", "")
                full_os = f"{machine_os} {build}".strip()
                logging.debug(f"found windows machine {name} {full_os}")
                machine_to_add = MachineWindows(name=name, os_version=full_os)

            elif "linux" in machine_os.lower():
                logging.warning(f"found linux machine {name} {machine_os}")
                machine_to_add = MachineLinux(name=name, os_version=machine_os)
            else:
                logging.warning(f"found machine with unknown os: {name} {machine_os=}")
                # machine_to_add = Machine(name=name, os_version=machine_os)
            if machine_to_add:
                machines.append(
                    (
                        machine_to_add,
                        ADMachine(
                            name=name,
                            id_domain=self.dir_name,
                            # 516 is the RID for Domain Controllers
                            is_dc=val.get("primaryGroupID") == "516",
                        ),
                    )
                )
        return machines


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = ParserComputers(
        Path("/home/manuel/Documents/mantis_amossys/dataamossys/cleaned/dr.amossys.fr")
    )
    ldap_machines = parser.get_machines()
    print(parser.dir_name)
