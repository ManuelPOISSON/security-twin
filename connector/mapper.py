import logging
from abc import abstractmethod

from connector.model import (
    ModelDTO,
    AdGroup,
    LocalUser,
    AdUser,
    LocalGroup,
    Trustee,
    LocalPrincipal,
)
from model import (
    ADGroup,
    ADDomain,
    ADUser,
    ADOU,
    ADMachine,
    File,
    FileRight,
    Machine,
    MachineLinux,
    MachineWindows,
    RootCimv2,
    RootCimv2Rights,
    Software,
    GPOResult,
    GPOPolicy,
    Service,
    ServiceStatus,
    TypeOS,
    User,
    Group,
)


from connector.repository import GenericRepository
from connector.unitofwork import _current_uow
import contextvars

logger = logging.getLogger(__name__)

DC_PRIMARY_GROUP_ID = "516"
DEFAULT_PASSWORD = "1234P@ss"


DEFAULT_RUN_BY = "NT AUTHORITY\\SYSTEM"
DEFAULT_STATUS = ServiceStatus.running
DEFAULT_VERSION = "-1"
IGNORED_ACLS = {
    "AUTORITÉ DE PACKAGE D’APPLICATION\\TOUS LES PACKAGES D’APPLICATION",
    "AUTORITÉ DE PACKAGE D’APPLICATION\\TOUS LES PACKAGES D’APPLICATION RESTREINTS",
    "Tout le monde",
}
FULL_CONTROL = 0x1F01FF

SE_INTERACTIVE_LOGON_RIGHT_DEFAULTS = ("Backup Operators", "Administrators", "Users")
SE_DENY_REMOTE_INTERACTIVE_DEFAULTS = ("Administrators", "Remote Desktop Users")

DEFAULT_LOCAL_GROUPS_DC = ["Administrators"]

_current_providers = contextvars.ContextVar("_current_providers", default={})


def provider(repo_cls):
    current = _current_providers.get()
    repo = current.get(repo_cls)
    if not repo:
        raise RuntimeError(f"No provider registered for {repo_cls}")
    return repo


def register_provider(*providers):
    def decorator(func):
        def wrapper(data, *args, **kwargs):
            uow = _current_uow.get()
            if uow is None:
                raise RuntimeError("No active UnitOfWork context")

            repos = {p: uow.get_repo(p) for p in providers}

            token = _current_providers.set(repos)
            try:
                return func(data, *args, **kwargs)
            finally:
                _current_providers.reset(token)

        return wrapper

    return decorator


def flatten_permissions(permissions):
    flat = []
    for perm in permissions:
        if isinstance(perm, str):
            flat.append(perm)
        elif isinstance(perm, (list, tuple, set)):
            flat.extend(flatten_permissions(perm))
        else:
            continue
    return flat


class IMapper:
    @staticmethod
    @abstractmethod
    def to_orm(data: ModelDTO): ...

    @staticmethod
    @register_provider(
        GenericRepository[User],
        GenericRepository[Group],
        GenericRepository[ADUser],
        GenericRepository[ADGroup],
    )
    def find_sp(name: str, comp_name: str = ""):
        user_repo: GenericRepository[User] = provider(GenericRepository[User])
        group_repo: GenericRepository[Group] = provider(GenericRepository[Group])
        ad_group_repo: GenericRepository[ADGroup] = provider(GenericRepository[ADGroup])
        ad_user_repo: GenericRepository[ADUser] = provider(GenericRepository[ADUser])
        sp = None
        if comp_name:
            if sp := user_repo.get(name=name, id_machine=comp_name):
                return sp
            elif sp := group_repo.get(name=name, id_machine=comp_name):
                return sp

        if sp := ad_user_repo.get(name=name):
            return sp
        elif sp := ad_group_repo.get(name=name):
            return sp

        logger.warning(f"Cannot find SP with name '{name}' with machine '{comp_name}'")
        return None


class ADDomainMapper(IMapper):
    @staticmethod
    def to_orm(data: ModelDTO) -> list[ADDomain]:
        domain_name = data.ad_data.domain_name
        return [ADDomain(name=domain_name)]


class ADGroupMapper(IMapper):
    @staticmethod
    @register_provider(GenericRepository[ADUser])
    def to_orm(data: ModelDTO) -> list[ADGroup]:
        orm_groups: list[ADGroup] = []
        dto_groups = data.ad_data.groups
        repo_user: GenericRepository[ADUser] = provider(GenericRepository[ADUser])
        for ad_group in dto_groups:
            orm_groups.append(
                ADGroup(name=ad_group.name, id_domain=data.ad_data.domain_name)
            )

        for dto_group, orm_group in zip(dto_groups, orm_groups):
            if not dto_group.member:
                continue

            members_users: list[ADUser] = []
            members_groups: list[ADGroup] = []
            for username in dto_group.member:
                model_user = repo_user.get(
                    name=username, id_domain=data.ad_data.domain_name
                )
                if model_user:
                    members_users.append(model_user)
                    continue

                member_group = next((p for p in orm_groups if p.name == username), None)
                if member_group:
                    members_groups.append(member_group)
                    continue

                logger.warning(f"Unknown correspondance for group {username}")
            orm_group.members_groups = members_groups
            orm_group.members_users = members_users

        return orm_groups


class ADUserMapper(IMapper):
    @staticmethod
    def to_orm(data: ModelDTO) -> list[ADUser]:
        results = []
        ad_users = data.ad_data.users
        for ad_user in ad_users:
            results.append(
                ADUser(name=ad_user.name, id_domain=data.ad_data.domain_name)
            )
        return results


class ADOuMapper(IMapper):
    @staticmethod
    def to_orm(data: ModelDTO) -> list[ADOU]:
        results = []
        ous = data.ad_data.ous
        for ou in ous:
            results.append(
                ADOU(name=ou.ou, path=ou.distinguishedName, id_domain=data.ad_data)
            )
        return results


class ADMachineMapper(IMapper):
    @staticmethod
    @register_provider(GenericRepository[Machine])
    def to_orm(data: ModelDTO) -> list[ADMachine]:
        results: list[ADMachine] = []
        ad_machines = data.ad_data.computers
        machine_repo: GenericRepository[Machine] = provider(GenericRepository[Machine])
        for ad_machine in ad_machines:
            if not machine_repo.exists(name=ad_machine.name):
                continue
            is_dc = ad_machine.primaryGroupID == DC_PRIMARY_GROUP_ID
            results.append(
                ADMachine(
                    name=ad_machine.name,
                    is_dc=is_dc,
                    id_domain=data.ad_data.domain_name,
                )
            )
        return results


class MachineMapper(IMapper):
    @staticmethod
    def to_orm(data: ModelDTO) -> list[Machine]:
        results = []

        for machine in data.ad_data.computers:
            comp_data = data.windows_local_data.get(machine.name)
            if not comp_data:
                continue
            name = machine.name
            os_type = machine.operatingSystem
            os_version = f"{machine.operatingSystem}  {machine.operatingSystemVersion}"
            has_rdp = False

            has_psRemote = True

            if comp_data.fdeny_ts_connections.value == "0":
                has_rdp = True

            if "windows" in os_type.lower():
                results.append(
                    MachineWindows(
                        name=name,
                        os_type=TypeOS.windows,
                        os_version=os_version,
                        has_RDP=has_rdp,
                        has_psRemote=has_psRemote,
                    )
                )
            elif "linux" in os_type.lower():
                results.append(
                    MachineLinux(name=name, os_type=TypeOS.linux, os_version=os_version)
                )
            else:
                logger.warning(
                    f"Found unknown operating system on {name}, os: {os_type}; version: {os_version}"
                )

        if data.linux_local_data:
            for machine in data.linux_local_data:
                results.append(
                    MachineLinux(name=machine.machine_name, os_type=TypeOS.linux)
                )
        return results


class UserMapper(IMapper):
    @staticmethod
    @register_provider(GenericRepository[ADMachine])
    def to_orm(data: ModelDTO) -> list[User]:
        results = []
        ad_machine_repo: GenericRepository[ADMachine] = provider(
            GenericRepository[ADMachine]
        )
        for comp_name, local_data in data.windows_local_data.items():
            # For Domain Controllers, the SAM database is replaced by NTDS.dit.
            # Therefore, every Security Principal (SP) in NTDS becomes a local SP on a DC.
            # Since it's not possible to create local SPs on a Domain Controller,
            # we skip this step.
            ad_machine: ADMachine = ad_machine_repo.get(name=comp_name)
            if not ad_machine:
                logger.error(
                    f"Trying to insert user on non-existing AD Machine '{comp_name}'"
                )
                continue
            if ad_machine.is_dc:
                results.append(User(id_machine=comp_name, name="Local System"))
                continue

            for loc_user in local_data.local_users:
                results.append(User(id_machine=comp_name, name=loc_user.name))
        return results


class GroupMapper(IMapper):
    @staticmethod
    @register_provider(
        GenericRepository[User],
        GenericRepository[ADGroup],
        GenericRepository[ADUser],
        GenericRepository[ADMachine],
    )
    def to_orm(
        data: ModelDTO,
    ) -> list[Group]:
        orm_all_groups: list[Group] = []

        repo_ad_user: GenericRepository[ADUser] = provider(GenericRepository[ADUser])
        repo_user: GenericRepository[User] = provider(GenericRepository[User])
        repo_ad_group: GenericRepository[Group] = provider(GenericRepository[ADGroup])
        ad_machine_repo: GenericRepository[ADMachine] = provider(
            GenericRepository[ADMachine]
        )

        for comp_name, local_data in data.windows_local_data.items():
            # For Domain Controllers, the SAM database is replaced by NTDS.dit.
            # Therefore, every Security Principal (SP) in NTDS becomes a local SP on a DC.
            # Since it's not possible to create local SPs on a Domain Controller,
            # we skip this step (except for built-in).
            ad_machine: ADMachine = ad_machine_repo.get(name=comp_name)
            if not ad_machine:
                logger.error(
                    f"Trying to insert group on non-existing AD Machine '{comp_name}'"
                )
                continue
            if ad_machine.is_dc:
                for name in DEFAULT_LOCAL_GROUPS_DC:
                    orm_all_groups.append(Group(id_machine=ad_machine.name, name=name))
                continue

            orm_comp_groups: list[Group] = []

            for loc_group in local_data.local_groups:
                orm_comp_groups.append(Group(id_machine=comp_name, name=loc_group.name))

            for loc_group, orm_group in zip(local_data.local_groups, orm_comp_groups):
                users: list[User] = []
                ad_users: list[ADUser] = []
                ad_groups: list[AdGroup] = []
                for member in loc_group.members:
                    if user := repo_user.get(name=member.name, id_machine=comp_name):
                        users.append(user)
                    elif ad_user := repo_ad_user.get(name=member.name):
                        ad_users.append(ad_user)
                    elif ad_group := repo_ad_group.get(name=member.name):
                        ad_groups.append(ad_group)
                    else:
                        logger.warning(
                            f"No matches found for member {member.name} of group {loc_group.name} on {comp_name} "
                        )

                orm_group.user_members.extend(users)
                orm_group.aduser_members.extend(ad_users)
                orm_group.adgroup_members.extend(ad_groups)
            orm_all_groups.extend(orm_comp_groups)
        return orm_all_groups


class RootCimv2Mapper(IMapper):
    @staticmethod
    @register_provider(
        GenericRepository[Machine],
    )
    def to_orm(data: ModelDTO):
        results: list[RootCimv2] = []
        repo_machine: GenericRepository[Machine] = provider(GenericRepository[Machine])
        for comp_name, comp_data in data.windows_local_data.items():
            for ace in comp_data.root_cimv2_sd.dacl:
                machine = repo_machine.get(name=comp_name)
                print(f"{ace.trustee.name}- {comp_name}")
                if not machine:
                    logger.warning(f"Machine named {comp_name} does not exist ")
                    continue
                sp = super(RootCimv2Mapper, RootCimv2Mapper).find_sp(
                    ace.trustee.name, comp_name=comp_name
                )

                if not sp:
                    logger.warning(
                        f"Trying to insert security descriptor of namespace rootcimv2 on computer '{comp_name}',"
                        f"but security principal '{ace.trustee.name}' does not exist !"
                    )
                    continue

                if isinstance(ace.permissions, list):
                    permissions = [
                        RootCimv2Rights(right=right) for right in ace.permissions
                    ]
                elif isinstance(ace.permissions, str):
                    permissions = [RootCimv2Rights(right=ace.permissions)]
                rootcimv2 = RootCimv2(
                    id_machine=machine.name, id_sp=sp.id, rights=permissions
                )

                results.append(rootcimv2)
        return results


class ServicesMapper(IMapper):
    @staticmethod
    @register_provider(GenericRepository[Machine], GenericRepository[User])
    def to_orm(data: ModelDTO) -> list[Service]:
        results = []
        machine_repo: GenericRepository[Machine] = provider(GenericRepository[Machine])
        user_repo: GenericRepository[User] = provider(GenericRepository[User])
        for comp_name, comp_data in data.windows_local_data.items():
            for service in comp_data.services:
                machine = machine_repo.get(name=comp_name)
                if not machine:
                    logger.warning(
                        f"Failed to instanciate service {service.name}, machine {comp_name} does not exist"
                    )
                    continue
                if service.run_by:
                    user = user_repo.get(name=service.run_by.name, id_machine=comp_name)
                    if not user:
                        """
                        logger.warning(
                            f"Service '{service.name}' has no associated Security Principal named '{service.run_by}'; "
                            f"assuming it runs under the System account."
                        )"""
                        run_by = user_repo.get(
                            name="Local System", id_machine=comp_name
                        )
                    else:
                        run_by = user
                else:
                    """logger.warning(
                        f"Service '{service.name}' has no associated Security Principal; "
                        f"assuming it runs under the System account."
                    )"""
                    run_by = user_repo.get(name="Local System", id_machine=comp_name)

                status = DEFAULT_STATUS
                if service.status:
                    try:
                        status = ServiceStatus(service.status.lower())
                    except ValueError as e:
                        logger.warning(e)

                service_orm = Service(
                    name=service.name,
                    id_machine=machine.name,
                    version=DEFAULT_VERSION,
                    run_by=run_by.id,
                    executable_path=service.path,
                    status=status,
                )
                results.append(service_orm)

        return results


class SoftwaresMapper(IMapper):
    @staticmethod
    def to_orm(data: ModelDTO) -> list[Software]:
        results = []
        for comp_name, comp_data in data.windows_local_data.items():
            for registry in comp_data.software_registries:
                for software in registry.softwares:
                    results.append(
                        Software(
                            name=software.name,
                            version=software.version,
                            name_machine=comp_name,
                        )
                    )

        if data.linux_local_data:
            for machine in data.linux_local_data:
                seen = set()
                for software in machine.softwares:
                    key = (software.name, software.version, machine.machine_name)
                    if key not in seen:
                        seen.add(key)
                        results.append(
                            Software(
                                name=software.name,
                                version=software.version,
                                name_machine=machine.machine_name,
                            )
                        )

        return results


class RDPMapper(IMapper):
    @staticmethod
    @register_provider(GenericRepository[Machine])
    def to_orm(data: ModelDTO) -> list[Machine]:
        results: list[Machine] = []
        repo_machine: GenericRepository[Machine] = provider(GenericRepository[Machine])
        for comp_name, comp_data in data.windows_local_data.items():
            machine = repo_machine.get(name=comp_name)
            if comp_data.fdeny_ts_connections.value == "0":
                machine.has_RDP = True
            results.append(machine)
        return results


class GPOResultMapper(IMapper):
    @staticmethod
    @register_provider(
        GenericRepository[MachineWindows],
    )
    def to_orm(data: ModelDTO) -> list[GPOResult]:
        results: list[GPOResult] = []
        repo_machine: GenericRepository[MachineWindows] = provider(
            GenericRepository[MachineWindows]
        )
        for comp_name, comp_data in data.windows_local_data.items():
            machine = repo_machine.get(name=comp_name)
            if machine is None:
                logger.warning(
                    f"Trying to insert GPOResult for non-existing machine {comp_name}"
                )
                continue

            for user_rights in comp_data.user_rights:
                name = user_rights.local_principal.name
                sp = super(GPOResultMapper, GPOResultMapper).find_sp(
                    name, comp_name=comp_name
                )
                if sp is None:
                    logger.warning(
                        f"Trying to insert GPOResult for non-existing security principal {name}"
                    )

                filter_perm = {e.value for e in GPOPolicy}
                permissions = list(set(user_rights.permissions) & filter_perm)

                # We ignore default SP
                if (
                    "SeInteractiveLogonRight" in permissions
                    and sp.name in SE_INTERACTIVE_LOGON_RIGHT_DEFAULTS
                ):
                    permissions.remove("SeInteractiveLogonRight")

                if (
                    "SeRemoteInteractiveLogonRight" in permissions
                    and sp.name in SE_DENY_REMOTE_INTERACTIVE_DEFAULTS
                ):
                    permissions.remove("SeRemoteInteractiveLogonRight")

                for perm in permissions:
                    results.append(
                        GPOResult(
                            id_machine=machine.name,
                            id_sp=sp.id,
                            policy=GPOPolicy(perm),
                        )
                    )

        return results


class FileMapper(IMapper):
    @staticmethod
    @register_provider(
        GenericRepository[Machine],
    )
    def to_orm(data: ModelDTO) -> list[File]:
        repos = {"machine": provider(GenericRepository[Machine])}

        results: list[File | FileRight] = []
        existing_files: set[tuple[str, str]] = set()
        for comp_name, comp_data in data.windows_local_data.items():
            machine = repos["machine"].get(name=comp_name)
            if not machine:
                logger.warning(
                    f"Trying to insert files for a non-existing machine '{comp_name}'"
                )
                continue

            services_with_acl = [s for s in comp_data.services if s.security_descriptor]

            for service in services_with_acl:
                if not service.path:
                    continue

                file_key = (service.path.lower(), comp_name)

                if file_key in existing_files:
                    # logger.debug(f"File '{service.path}' for machine '{comp_name}' already processed — skipping.")
                    continue
                file = File(path=service.path, id_machine=comp_name)
                results.append(file)
                existing_files.add(file_key)
        return results


class FileRightsMapper(IMapper):
    @staticmethod
    @register_provider(
        GenericRepository[Machine],
        GenericRepository[User],
        GenericRepository[Group],
        GenericRepository[ADUser],
        GenericRepository[ADGroup],
        GenericRepository[ADDomain],
        GenericRepository[File],
    )
    def to_orm(data: ModelDTO) -> list[FileRight]:
        repos = {
            "machine": provider(GenericRepository[Machine]),
            "user": provider(GenericRepository[User]),
            "group": provider(GenericRepository[Group]),
            "aduser": provider(GenericRepository[ADUser]),
            "adgroup": provider(GenericRepository[ADGroup]),
            "domain": provider(GenericRepository[ADDomain]),
            "file": provider(GenericRepository[File]),
        }

        results: list[FileRight] = []
        existing_rights: set[tuple[int, int]] = set()  # (id_file, id_sp)

        for comp_name, comp_data in data.windows_local_data.items():
            machine = repos["machine"].get(name=comp_name)
            if not machine:
                logger.warning(
                    f"Trying to insert file rights for a non-existing machine '{comp_name}'"
                )
                continue

            ad_domains = repos["domain"].get_all()

            for service in comp_data.services:
                if not service.path or not service.security_descriptor:
                    continue

                file = repos["file"].get(path=service.path, id_machine=comp_name)
                if not file:
                    logger.debug(
                        f"File '{service.path}' for machine '{comp_name}' not found in DB — skipping rights."
                    )
                    continue
                for ace in service.security_descriptor.dacl:
                    sp = None

                    if isinstance(ace.trustee, LocalGroup):
                        sp = repos["group"].get(
                            name=ace.trustee.name, id_machine=comp_name
                        )
                    elif isinstance(ace.trustee, LocalUser):
                        sp = repos["user"].get(
                            name=ace.trustee.name, id_machine=comp_name
                        )
                    elif isinstance(ace.trustee, AdUser):
                        sp = repos["aduser"].get(name=ace.trustee.name)
                    elif isinstance(ace.trustee, AdGroup):
                        sp = repos["adgroup"].get(name=ace.trustee.name)
                    elif isinstance(ace.trustee, Trustee):
                        if ace.trustee.domain is None:
                            continue
                        if ace.trustee.domain in (
                            "NT SERVICE",
                            "APPLICATION PACKAGE AUTHORITY",
                        ):
                            continue
                        sp = FileRightsMapper._find_security_principal(
                            ace, repos, ad_domains, service_name=service.name
                        )
                    elif isinstance(ace.trustee, LocalPrincipal):
                        sp = repos["group"].get(name=ace.trustee.name)
                        if sp is None:
                            sp = repos["user"].get(name=ace.trustee.name)
                        if sp is None:
                            sp = repos["aduser"].get(name=ace.trustee.name)
                        if sp is None:
                            sp = repos["adgroup"].get(anme=ace.trustee.name)

                    if sp is None:
                        logger.error(f"Cannot find appropriate SP for ACE: {ace}")
                        continue

                    if ace.access_mask == FULL_CONTROL:
                        permissions = "FullControl"
                    else:
                        permissions = ",".join(flatten_permissions(ace.permissions))

                    key = (file.id, sp.id)
                    if key in existing_rights:
                        # logger.debug(f"Skipping duplicate FileRight for file_id={file.id}, sp_id={sp.id}")
                        continue
                    existing_rights.add(key)
                    file_right = FileRight(
                        id_file=file.id,
                        id_sp=sp.id,
                        rights=permissions,
                    )
                    results.append(file_right)

        return results

    @staticmethod
    def _find_security_principal(ace, repos, ad_domains, service_name: str):
        """Recherche l'utilisateur ou le groupe associé à une ACE."""
        name = ace.trustee.name
        domain = ace.trustee.domain.lower()

        matched_domain = next(
            (d for d in ad_domains if d.name.split(".")[0].lower() == domain), None
        )

        if matched_domain:
            logger.debug(f"Found AD SP in ACL of {service_name}")
            user = repos["aduser"].get(name=name, id_domain=matched_domain.name)
            if user:
                return user
            group = repos["adgroup"].get(name=name, id_domain=matched_domain.name)
            if group:
                return group
        else:
            user = repos["user"].get(name=name, id_domain=domain)
            if user:
                return user
            group = repos["group"].get(name=name, id_domain=domain)
            if group:
                return group

        return None
