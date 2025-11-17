import json

import winrm

class WinRMConnection:
    def __init__(self, host: str, user: str, password: str):
        self.session = winrm.Session(host, auth=(user, password))
        self.ps_script = ""
    
    def get_register_value(self, path: str,  register: str) -> str:
        result = self.session.run_ps(f"(Get-ItemProperty -Path '{path}' -Name '{register}').{register}")
        if result.status_code == 0:
            return result.std_out.decode('utf-8')
        else:
            return f"Error: {result.std_err.decode('utf-8')}"
    

    def file_exists(self, path: str) -> bool:
        result = self.session.run_ps(f"Test-Path '{path}'")
        if result.status_code == 0:
            return result.std_out.decode('utf-8').strip().lower() == 'true'
        else:
            return False
    
    def get_services(self) -> dict:
        result = self.session.run_ps('Get-WmiObject -Class Win32_Service | Select-Object Name, PathName | ConvertTo-Json')

        if result.status_code != 0:
            print(result.std_err.decode('utf-8'))
            return None
        
        return json.loads(result.std_out.decode())
    
    def get_acl_from_list_of_files(self, paths: list[str]):
        for path in paths:
            if self.file_exists(path):
                self.session.run_ps(f"Get-Acl {path}.Access")

    def execute_ps_script(self, path: str):
        with open(path, "r") as fd:
            result = self.session.run_ps(fd.read())
            if result.status_code != 0:
                result.std_err.decode('utf-8 ')
                return None
            return json.loads(result.std_out.decode())