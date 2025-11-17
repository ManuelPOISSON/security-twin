from parse_data.translations import FR_TO_EN


def clean_sp_name(sp_name: str, domain_name: str = "", translate: bool = True) -> str:
    """Cleans up the service principal name by removing unwanted prefixes."""

    sp_name = sp_name.replace("BUILTIN\\", "").replace(
        r"AUTORITE NT\Système", r"NT AUTHORITY\SYSTEM"
    )
    if domain_name:
        sp_name = sp_name.replace(f"{domain_name}\\", "")
    if translate:
        if sp_name.startswith("AUTORITE NT"):
            sp_name = "NT AUTHORITY" + sp_name.lstrip("AUTORITE NT")
        sp_name = FR_TO_EN.get(sp_name, sp_name)

    return sp_name
