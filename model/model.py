from __future__ import annotations

from typing import Optional, List

from sqlalchemy import (
    String,
    ForeignKey,
    CheckConstraint,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from typing_extensions import Annotated
import enum

intpkauto = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]

Base = declarative_base()


class TypeSp(enum.Enum):
    user = "user"
    group = "group"
    ADuser = "ADuser"
    ADgroup = "ADgroup"


class TypeOS(enum.Enum):
    windows = "windows"
    linux = "linux"


class NameSpaceRights(enum.Enum):
    Enable = "Enable"
    MethodExecute = "MethodExecute"
    FullWrite = "FullWrite"
    PartialWrite = "PartialWrite"
    ProviderWrite = "ProviderWrite"
    RemoteAccess = "RemoteAccess"
    ReadSecurity = "ReadSecurity"
    WriteSecurity = "WriteSecurity"


class GPOPolicy(enum.Enum):
    SeInteractiveLogonRight = "SeInteractiveLogonRight"
    SeDenyInteractiveLogonRight = "SeDenyInteractiveLogonRight"
    SeRemoteInteractiveLogonRight = "SeRemoteInteractiveLogonRight"
    SeDenyRemoteInteractiveLogonRight = "SeDenyRemoteInteractiveLogonRight"


class ServiceStatus(enum.Enum):
    running = "running"
    stopped = "stopped"
    # TODO add more status


class SecurityPrincipal(Base):
    __tablename__ = "security_principal"
    id: Mapped[intpkauto]
    type: Mapped[TypeSp]
    password: Mapped[str] = mapped_column(String(255), nullable=True)
    __mapper_args__ = {
        "polymorphic_on": "type",
        "polymorphic_identity": "security_principal",
    }


class User(SecurityPrincipal):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(
        ForeignKey("security_principal.id"), primary_key=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    id_machine: Mapped[str] = mapped_column(
        String(255), ForeignKey("machine.name"), nullable=False
    )
    __table_args__ = (
        UniqueConstraint("name", "id_machine", name="unique_user_name_id_machine"),
    )
    __mapper_args__ = {
        "polymorphic_identity": TypeSp.user,
    }

    def __str__(self):
        return f"User(name={self.name}, id_machine={self.id_machine}, id={self.id})"


"""
| **English Group Name**       | **French Group Name**        | **Description**                                                                 |
|-------------------------------|------------------------------|---------------------------------------------------------------------------------|
| Administrators                | Administrateurs             | Full control over the computer. Can perform any action.                        |
| Users                        | Utilisateurs                | Standard users with limited privileges.                                        |
| Guests                       | Invités                     | Temporary users with minimal permissions.                                      |
| Power Users                  | Utilisateurs avec pouvoirs  | Legacy group with more privileges than Users but less than Administrators.     |
| Backup Operators             | Opérateurs de sauvegarde    | Can back up and restore files, regardless of permissions.                      |
| Remote Desktop Users         | Utilisateurs du Bureau à distance | Allowed to log in via Remote Desktop.                                       |
| Network Configuration Operators | Opérateurs de configuration réseau | Can make changes to the network settings.                                |
| IIS_IUSRS                    | IIS_IUSRS                   | Used by IIS (Internet Information Services).                                   |
| Authenticated Users          | Utilisateurs authentifiés   | Includes all users who have authenticated to the system.                       |
| Everyone                     | Tout le monde               | Includes all users, authenticated or not.                                      |
| Anonymous Logon              | Connexion anonyme           | Users who log on anonymously.                                                 |
| System Operators             | Opérateurs systèmes         | Users who can manage certain system-level tasks.                               |
| Print Operators              | Opérateurs d'impression     | Can manage printers.                                                           |
| Hyper-V Administrators       | Administrateurs Hyper-V     | Can fully manage Hyper-V.                                                      |
| Remote Management Users      | Utilisateurs de Gestion à distance| WinRM PPSRemote                                                          |
| Performance Log Users        | Utilisateurs du journal de performances                          | WMIC                                                          |
| Distributed COM Users        | Utilisateurs du modèle COM Distribué                          | WMIC                                                          |
"""


class Group(SecurityPrincipal):
    """
    Only for local groups, for ADGroup see dedicated class
    """

    __tablename__ = "group"
    id: Mapped[int] = mapped_column(
        ForeignKey("security_principal.id"), primary_key=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    id_machine: Mapped[str] = mapped_column(String(255), ForeignKey("machine.name"))
    __table_args__ = (
        UniqueConstraint("name", "id_machine", name="unique_lgroup_name_per_machine"),
    )
    __mapper_args__ = {
        "polymorphic_identity": TypeSp.group,
    }

    user_members = relationship(
        "User", 
        secondary="group_member_user",
        primaryjoin="Group.id == GroupMemberUser.member_of",
        secondaryjoin="User.id == GroupMemberUser.member",
        backref="member_of_groups")
    
    aduser_members = relationship(
        "ADUser",
        secondary="group_member_ADuser",
        primaryjoin="Group.id == GroupMemberADUser.member_of",
        secondaryjoin="ADUser.id == GroupMemberADUser.member",
        backref="member_of_groups",
    )

    adgroup_members = relationship(
        "ADGroup",
        secondary="group_member_ADgroup",
        primaryjoin="Group.id == GroupMemberADGroup.member_of",
        secondaryjoin="ADGroup.id == GroupMemberADGroup.member",
        backref="member_of_groups"
    )

    def __str__(self):
        return f"Group(name={self.name}, id_machine={self.id_machine}, id={self.id})"


class GroupMemberUser(Base):
    __tablename__ = "group_member_user"
    member: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    member_of: Mapped[int] = mapped_column(ForeignKey("group.id"), primary_key=True)


class GroupMemberADUser(Base):
    __tablename__ = "group_member_ADuser"
    member: Mapped[int] = mapped_column(ForeignKey("ADuser.id"), primary_key=True)
    member_of: Mapped[int] = mapped_column(ForeignKey("group.id"), primary_key=True)


class GroupMemberADGroup(Base):
    __tablename__ = "group_member_ADgroup"
    member: Mapped[int] = mapped_column(ForeignKey("ADgroup.id"), primary_key=True)
    member_of: Mapped[int] = mapped_column(ForeignKey("group.id"), primary_key=True)


# TODO local group nesting (local group member of local group) is theoretically possible. This is not implemented yet.


class File(Base):
    __tablename__ = "file"
    id: Mapped[intpkauto]
    path: Mapped[str] = mapped_column(String(255))
    id_machine: Mapped[str] = mapped_column(String(255), ForeignKey("machine.name"))
    __table_args__ = (
        UniqueConstraint("path", "id_machine", name="unique_file_path_per_machine"),
    )


class FileRight(Base):
    __tablename__ = "file_right"
    id_file: Mapped[int] = mapped_column(ForeignKey("file.id"), primary_key=True)
    id_sp: Mapped[int] = mapped_column(
        ForeignKey("security_principal.id"), primary_key=True
    )
    rights: Mapped[str] = mapped_column(String(255))


class Service(Base):
    __tablename__ = "service"
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    version: Mapped[str] = mapped_column(String(255), primary_key=True, default="-1")
    id_machine: Mapped[str] = mapped_column(
        String(255), ForeignKey("machine.name"), primary_key=True
    )
    # TODO can an AD user run a service?
    run_by: Mapped[int] = mapped_column(ForeignKey("user.id"))
    port: Mapped[int] = mapped_column(nullable=True)
    executable_path: Mapped[str] = mapped_column(String(255))
    status: Mapped[ServiceStatus]
    __table_args__ = (
        CheckConstraint(
            "port IS NULL OR (port >= 0 AND port <= 65535)", name="check_port_range"
        ),
    )


class IpToMachine(Base):
    __tablename__ = "ip_to_machine"
    id_machine: Mapped[str] = mapped_column(
        String(255), ForeignKey("machine.name"), primary_key=True
    )
    ip_address: Mapped[str] = mapped_column(String(255), primary_key=True)


class Machine(Base):
    __tablename__ = "machine"
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    os_type: Mapped[TypeOS] = mapped_column(nullable=False)
    os_version: Mapped[str] = mapped_column(String(255), nullable=True)
    has_psRemote: Mapped[bool] = mapped_column(default=False)
    has_RDP: Mapped[bool] = mapped_column(default=False)
    __mapper_args__ = {
        "polymorphic_identity": "machine",
        "polymorphic_on": "os_type",
    }


class MachineWindows(Machine):
    __tablename__ = "machine_windows"
    name: Mapped[str] = mapped_column(
        String(255), ForeignKey("machine.name"), primary_key=True
    )
    __mapper_args__ = {
        "polymorphic_identity": TypeOS.windows,
    }


class MachineLinux(Machine):
    __tablename__ = "machine_linux"
    name: Mapped[str] = mapped_column(
        String(255), ForeignKey("machine.name"), primary_key=True
    )
    __mapper_args__ = {
        "polymorphic_identity": TypeOS.linux,
    }


class RootCimv2(Base):
    __tablename__ = "root_cimv2"
    id: Mapped[intpkauto]
    id_machine: Mapped[str] = mapped_column(
        String(255), ForeignKey("machine_windows.name"), nullable=False
    )
    id_sp: Mapped[int] = mapped_column(
        ForeignKey("security_principal.id"), nullable=False
    )

    rights: Mapped[List["RootCimv2Rights"]] = relationship(
        "RootCimv2Rights", back_populates="root_cimv2", cascade="all, delete-orphan"
    )
    __table_args__ = (
        UniqueConstraint(
            "id_machine", "id_sp", name="unique_rights_security_principal"
        ),
    )


class RootCimv2Rights(Base):
    __tablename__ = "root_cimv2_rights"
    id_root_cimv2: Mapped[int] = mapped_column(
        ForeignKey("root_cimv2.id"), primary_key=True
    )
    right: Mapped[NameSpaceRights] = mapped_column(primary_key=True)
    root_cimv2 = relationship("RootCimv2", back_populates="rights")


class RunasCreds(Base):
    __tablename__ = "runas_creds"
    id: Mapped[intpkauto]
    id_machine: Mapped[str] = mapped_column(
        String(255), ForeignKey("machine_windows.name")
    )
    can_runas_local: Mapped[Optional[int]] = mapped_column(ForeignKey("user.id"))
    can_runas_AD: Mapped[Optional[int]] = mapped_column(ForeignKey("ADuser.id"))
    __table_args__ = (
        CheckConstraint(
            "can_runas_local IS NOT NULL OR can_runas_AD IS NOT NULL",
            name="check_local-ad_user_not_null",
        ),
        UniqueConstraint("id_machine", "can_runas_local", name="unique_runas_local"),
        UniqueConstraint("id_machine", "can_runas_AD", name="unique_runas_ad"),
    )


class RunasImpersonated(Base):
    __tablename__ = "runas_impersonated"
    id: Mapped[intpkauto]
    runas_id: Mapped[int] = mapped_column(ForeignKey("runas_creds.id"))
    user_loc: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=True)
    user_AD: Mapped[int] = mapped_column(ForeignKey("ADuser.id"), nullable=True)
    # TODO user must be local user xor AD user, type Int, duplicate and constraint
    # TODO check if it is possible to have user same as can_runas
    __table_args__ = (
        CheckConstraint(
            "user_loc IS NOT NULL OR user_AD IS NOT NULL",
            name="check_local-ad_user_not_null_impersonated",
        ),
        UniqueConstraint(
            "runas_id", "user_loc", name="unique_runas_local_impersonated"
        ),
        UniqueConstraint("runas_id", "user_AD", name="unique_runas_ad_impersonated"),
    )


class GPOResult(Base):
    __tablename__ = "GPOresult"
    id_machine: Mapped[str] = mapped_column(
        String(255), ForeignKey("machine.name"), primary_key=True
    )
    policy: Mapped[GPOPolicy] = mapped_column(primary_key=True)
    id_sp: Mapped[int] = mapped_column(
        ForeignKey("security_principal.id"), primary_key=True
    )


class ADOU(Base):
    __tablename__ = "ADOU"
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    path: Mapped[str] = mapped_column(String(255))
    id_domaine: Mapped[str] = mapped_column(String(255), ForeignKey("ADDomain.name"))


class OUGroup(Base):
    __tablename__ = "OUgroup"
    ou: Mapped[str] = mapped_column(
        String(255), ForeignKey("ADOU.name"), primary_key=True
    )
    adgroup: Mapped[str] = mapped_column(
        String(255), ForeignKey("ADgroup.name"), primary_key=True
    )


class OUUser(Base):
    __tablename__ = "OUuser"
    ou: Mapped[str] = mapped_column(
        String(255), ForeignKey("ADOU.name"), primary_key=True
    )
    user: Mapped[str] = mapped_column(
        String(255), ForeignKey("user.name"), primary_key=True
    )


class OUOUs(Base):
    __tablename__ = "OUOUs"
    ou_contained: Mapped[str] = mapped_column(
        String(255), ForeignKey("ADOU.name"), primary_key=True
    )
    ou_container: Mapped[str] = mapped_column(
        String(255), ForeignKey("ADOU.name"), primary_key=True
    )


class OUMachines(Base):
    __tablename__ = "OUmachines"
    ou: Mapped[str] = mapped_column(
        String(255), ForeignKey("ADOU.name"), primary_key=True
    )
    ad_machine: Mapped[str] = mapped_column(
        String(255), ForeignKey("ADmachine.name"), primary_key=True
    )


class ADDomain(Base):
    __tablename__ = "ADDomain"
    name: Mapped[str] = mapped_column(String(255), primary_key=True)


class ADGroup(SecurityPrincipal):
    __tablename__ = "ADgroup"
    id: Mapped[int] = mapped_column(
        ForeignKey("security_principal.id"), primary_key=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    id_domain: Mapped[str] = mapped_column(String(255), ForeignKey("ADDomain.name"))
    __table_args__ = (
        UniqueConstraint("name", "id_domain", name="unique_ADgroup_name_per_domain"),
    )
    __mapper_args__ = {
        "polymorphic_identity": TypeSp.ADgroup,
    }

    members_users = relationship(
        "ADUser",
        secondary="ADgroup_member_ADuser",
        primaryjoin="ADGroup.id == ADGroupMemberADUser.member_of",
        secondaryjoin="ADUser.id == ADGroupMemberADUser.member",
        backref="member_of_adgroups",
    )

    members_groups = relationship(
        "ADGroup",
        secondary="ADgroup_member_ADgroup",
        primaryjoin="ADGroup.id == ADGroupMemberADGroup.member_of",
        secondaryjoin="ADGroup.id == ADGroupMemberADGroup.member",
        backref="member_of_adgroups",
    )


    def __str__(self):
        return f"ADGroup(name={self.name}, id_domain={self.id_domain}, id={self.id})"


class ADGroupMemberADUser(Base):
    __tablename__ = "ADgroup_member_ADuser"
    member: Mapped[int] = mapped_column(ForeignKey("ADuser.id"), primary_key=True)
    member_of: Mapped[int] = mapped_column(ForeignKey("ADgroup.id"), primary_key=True)


class ADGroupMemberADGroup(Base):
    __tablename__ = "ADgroup_member_ADgroup"
    member: Mapped[int] = mapped_column(ForeignKey("ADgroup.id"), primary_key=True)
    member_of: Mapped[int] = mapped_column(ForeignKey("ADgroup.id"), primary_key=True)
    # constraint member != member_of
    __table_args__ = (
        CheckConstraint("member != member_of", name="check_member_not_member_of"),
    )


class ADUser(SecurityPrincipal):
    __tablename__ = "ADuser"
    id: Mapped[int] = mapped_column(
        ForeignKey("security_principal.id"), primary_key=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    id_domain: Mapped[str] = mapped_column(String(255), ForeignKey("ADDomain.name"))
    __table_args__ = (
        UniqueConstraint("name", "id_domain", name="unique_ADuser_name_per_domain"),
    )
    __mapper_args__ = {
        "polymorphic_identity": TypeSp.ADuser,
    }



    def __str__(self):
        return f"ADUser(name={self.name}, id_domain={self.id_domain}, id={self.id})"


class ADMachine(Base):
    __tablename__ = "ADmachine"
    name: Mapped[str] = mapped_column(
        String(255), ForeignKey("machine.name"), primary_key=True
    )
    id_domain: Mapped[str] = mapped_column(
        String(255), ForeignKey("ADDomain.name"), primary_key=True
    )
    is_dc: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return f"ADMachine(name={self.name}, id_domain={self.id_domain}, is_dc={self.is_dc})"


class Docker(Base):
    __tablename__ = "docker"
    machine_host: Mapped[str] = mapped_column(
        String(255), ForeignKey("machine.name"), primary_key=True
    )


class VirtualMachine(Base):
    __tablename__ = "virtual_machine"
    machine_host: Mapped[str] = mapped_column(
        String(255), ForeignKey("machine.name"), primary_key=True
    )


class SoftwareUser(Base):
    __tablename__ = "software_user"
    user: Mapped[str] = mapped_column(String(255), primary_key=True)
    software: Mapped[str] = mapped_column(
        String(255), ForeignKey("software.name"), primary_key=True
    )


class Software(Base):
    __tablename__ = "software"
    name: Mapped[str] = mapped_column(String(255), primary_key=True)
    version: Mapped[str] = mapped_column(String(255), primary_key=True, default="-1")
    name_machine: Mapped[str] = mapped_column(
        String(255), ForeignKey("machine.name"), primary_key=True
    )
    run_by: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=True)
    port: Mapped[int] = mapped_column(nullable=True)

    def __repr__(self):
        return f"Software(name={self.name}, version={self.version}, name_machine={self.name_machine}, run_by={self.run_by}, port={self.port})"
