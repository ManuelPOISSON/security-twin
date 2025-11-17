function Get-Trustee($accountName) {
    try {
        $ntAccount = New-Object System.Security.Principal.NTAccount($accountName)
        $sid = $ntAccount.Translate([System.Security.Principal.SecurityIdentifier]).Value
    }
    catch {
        $sid = ""
    }
    $split = $accountName -split "\\", 2
    if ($split.Count -eq 2) {
        [PSCustomObject]@{
            domain = $split[0]
            name   = $split[1]
            sid    = $sid
        }
    }
    else {
        [PSCustomObject]@{
            domain = ""
            name   = $accountName
            sid    = $sid
        }
    }
}

function Get-ServiceExeACL {
    $output = @{
        time_sec = $null
        result   = $null
    }

    $time = Measure-Command {
        $services = Get-WmiObject -Class Win32_Service | Select-Object Name, PathName 
        $results = $services | ForEach-Object {
            $service = $_
            $exePath = $service.PathName -replace '"', '' 

            if (Test-Path $exePath) { 
                $acl = Get-Acl $exePath

                [PSCustomObject]@{
                    name                = $service.Name
                    path                = $exePath
                    security_descriptor = [PSCustomObject]@{
                        owner = Get-Trustee $acl.Owner
                        group = Get-Trustee $acl.Group
                        dacl  = $acl.Access | ForEach-Object {
                            $access = $_
                            try {
                                $sid = ($access.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier])).Value
                            }
                            catch {
                                $idr = $access.IdentityReference.Value
                                $sid = $null
                                $serviceName = $service.Name
                                try {
                                    $name = $idr -split "\\"
                                    $NTAccount = New-Object -TypeName System.Security.Principal.NTAccount($name[1])
                                    $sid = $NTAccount.Translate([System.Security.Principal.SecurityIdentifier]).ToString()
                                } 
                                catch {
                                    Write-Error "$idr could not be Translated for service $serviceName"
                                }                      
                            }
                            [PSCustomObject]@{
                                domain            = ($access.IdentityReference.Value -split "\\")[0]
                                name              = ($access.IdentityReference.Value -split "\\")[1]
                                sid               = $sid
                                AccessControlType = $access.AccessControlType.ToString()
                                FileSystemRights  = ($access.FileSystemRights).ToString().Replace(", ", ",")
                            }
                        }
                    }
                }
            }
        }
    }

    $output["time_sec"] = $time.TotalSeconds
    $output["result"] = $results 
    return $output | ConvertTo-Json -Compress -Depth 100
}
Write-Error ( Get-ServiceExeACL)
Write-Output (Get-ServiceExeACL)