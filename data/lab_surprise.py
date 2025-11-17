import json

default_pwd = "234P@ss"
ad_users = [
    ("Administrateur", default_pwd),  # 0
    ("u3", default_pwd),  # 1
    ("u4", default_pwd),  # 2
    ("u5", default_pwd),  # 3
    ("u0", default_pwd),  # 4
    ("u6", default_pwd),  # 5
    ("u2", default_pwd),  # 6
    ("u7", default_pwd),  # 7
    ("u1", default_pwd),  # 8
    ("user", "sameN4meAsLocalUser"),  # 9
    ("u8", "Maillard35!"),  # 10
    ("u04", "H€ll0W0rld"),  # 11
    ("u14", "H€ll0W0rld"),  # 12
    ("u24", "H€ll0W0rld"),  # 13
    ("u34", "H€ll0W0rld"),  # 14
    ("u44", "H€ll0W0rld"),  # 15
    ("ugSci", "Us€rMarchombre00"),  # 16
    ("userGhr", "Us€rGhr00"),  # 17
]

path_mozilla_exe = "C:\\Program Files\\Mozilla\\firefox.exe"

windows_machines = {
    "c0": {  # VM1 SYSTEM-PC
        "rootcimv2": {
            "gHr": ["Enable"],
        },
        "localusers": {
            "c0local": default_pwd,
        },
        "localgroups": {
            "Utilisateurs du journal de performances": ["u1"],
        },
        "rdp": False,
    },
    "c1": {  # VM2
        "localusers": {
            "c1user2": default_pwd,
            "c1user": default_pwd,
        },
        "localgroups": {
            "Utilisateurs du Bureau à distance": ["gSci", "u0"],
            "Administrateurs": ["u1"],
        },
        "saved_creds": {
            "u0": ["u1"],
        },
        "files": {
            "C:\\Users\\master\\Documents\\secret.txt": {
                ad_users[0][0]: "FullControl",
            },
        },
        "rdp": True,
    },
    "c3": {
        "localgroups": {
            "Utilisateurs du journal de performances": [ad_users[0][0]],
            "Remote Management Users": ["u0"],
        },
        "psremote": True,
        "software": [{"name": "winrar", "version": "6.22"}],
    },
    "c2": {
        "gporesult": {
            "SeDenyRemoteInteractiveLogonRight": ["u0"],
        },
        "localgroups": {
            "Utilisateurs du modèle COM Distribué": ["u1"],
            "Utilisateurs du Bureau à distance": ["u0"],
        },
        "localusers": {
            "SYSTEM": "",
        },
        "rootcimv2": {
            "u1": ["Enable", "MethodExecute", "RemoteAccess"],
        },
        "files": {path_mozilla_exe: {"u1": "FullControl"}},
        "services": [
            {
                "name": "Mozilla",
                "version": "1.0.0",
                "run_by": "SYSTEM",
                "executable_path": path_mozilla_exe,
                "status": "running",
            },
        ],
        "rdp": True,
    },
    "c4": {
        "gporesult": {
            "SeDenyInteractiveLogonRight": ["u2"],
        },
    },
    "c5": {
        "gporesult": {
            "SeDenyRemoteInteractiveLogonRight": ["gAllUsers"],
        },
        "localgroups": {
            "Utilisateurs du Bureau à distance": ["gAllUsers"],
        },
        "rdp": True,
    },
    "DC0": {
        "OS_version": "Windows Server 2019 10.0.17763.2237",
        "localusers": {
            "SYSTEM": "",
        },
        "gporesult": {
            "SeInteractiveLogonRight": ["Domain admins"],
        },
    },
}

domain = {
    "lab.local": {
        "users": ad_users,
        "groups": {
            "gSci": ["u7", "u1", "ugSci"],
            "gHr": ["gSci", "userGhr"],
            "gHelloWorld": [ad_u[0] for ad_u in ad_users if "hello.world" in ad_u[0]],
            "gEmpty": [],
            "gAllUsers": [ad_u[0] for ad_u in ad_users],
            "Domain admins": ["Administrateur"],
        },
        "machines": list(windows_machines.keys()),
        "dcs": ["DC0"],
    }
}
dcs = [list(windows_machines.keys())[-1]]

lab = {"win_machines": windows_machines, "domain": domain}

if __name__ == "__main__":
    file_output = "lab_surprise.json"
    print(f"it's main, write to file {file_output}")
    with open(file_output, "w") as f:
        f.write(json.dumps(lab, indent=2, sort_keys=True))

"""
Expected
Graph shows:
- All users can log to wksDenyEwilan except u2
- No user can use RDP on wksRdpOnButDenyAllUsers


# Expected attack paths

mach = "palais"
user = "essindra"
attributes = find_path(graph, mach, user)

[3] path length 2, dst: (dcserver,Administrateur@surpriz.local)
    (UniPalais,u0@surpriz.local) CVE_2020_1472_zerologon
    (dcserver,Administrateur@surpriz.local)
[5] path length 3, dst: (wksAnything,u5@surpriz.local)
        (UniPalais,u0@surpriz.local) PSRemote
        (wksAnything,u0@surpriz.local) CVE_2023_38831_winrar
        (wksAnything,u5@surpriz.local)
[25] path length 5, dst: (wksEnterprise,SYSTEM)
    (UniPalais,u0@surpriz.local) RDP
    (opForet,u0@surpriz.local) runas
    (opForet,u1@surpriz.local) wmic
    (wksEnterprise,u1@surpriz.local) ServiceExeModify
    (wksEnterprise,SYSTEM)

OK (UniPalais,u0@surpriz.local) RDP (opForet,u0@surpriz.local)
KO (UniPalais,u0@surpriz.local) RDP (wksEnterprise,u0@surpriz.local) GPO SeDenyRemoteInteractiveLogon

OK (opForet,u1@surpriz.local) wmic (wksEnterprise,u1@surpriz.local)
KO (opForet,u1@surpriz.local) wmic (UniPalais,u1@surpriz.local) rootcimv2 gHr missing RemoteAccess
"""
