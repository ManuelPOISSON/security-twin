function Get-ServiceSP {
    param (
        [Parameter(Mandatory = $true)]
        [string]$StartName
    )

    $normalized = $StartName.Trim().ToLower()

    $mapping = @{
        "localsystem"    = "NT AUTHORITY\SYSTEM"
        "localservice"   = "NT AUTHORITY\LocalService"
        "networkservice" = "NT AUTHORITY\NetworkService"
    }

    $account = $mapping[$normalized]
    if (-not $account) { $account = $StartName }

    try {
        $sid = (New-Object System.Security.Principal.NTAccount($account)).Translate([System.Security.Principal.SecurityIdentifier]).Value
    }
    catch {
        $sid = $null
    }

    [PSCustomObject]@{
        name = $StartName
        sid  = $sid
    }
}



function Get-ServiceExeACL {
    $output = @{
        time_sec = $null
        result   = $null
    }

    $time = Measure-Command {
        $services = Get-WmiObject -Class Win32_Service | Select-Object Name, PathName, State, StartName
        $results = $services | ForEach-Object {
            $service = $_
            $exePath = $service.PathName -replace '"', '' 
            $startName = $service.StartName
            if ([string]::IsNullOrWhiteSpace($startName)) {
                $run_by = $null
            }
            else {
                $run_by = Get-ServiceSP $startName
            }

            if (Test-Path $exePath) {
                
                $escapedPath = $exePath -replace '\\', '\\'
                $fileSec = Get-WmiObject -Class Win32_LogicalFileSecuritySetting -Filter "Path='$escapedPath'" -ErrorAction SilentlyContinue
                if (-not $fileSec) { 
                    Write-Error "Cannot get the Win32_LogicalFileSecuritySetting with Path=$escapedPath "
                }

                
                $sd = $fileSec.GetSecurityDescriptor()

                function Make-Trustee($trustee) {
                    if ($null -eq $trustee) { return $null }
                    $domain = $trustee.Domain
                    $name = $trustee.Name
                    $sid = $trustee.SIDString
                    return [PSCustomObject]@{
                        domain = $domain
                        name   = $name
                        sid    = $sid
                    }
                }
     
                
                function Get-PermissionsFromMask($mask) {
                    $rights = @()
                    if ($mask -band 1) { $rights += "READ_DATA" }
                    if ($mask -band 2) { $rights += "WRITE_DATA" }
                    if ($mask -band 4) { $rights += "APPEND_DATA" }
                    if ($mask -band 8) { $rights += "READ_EA" }
                    if ($mask -band 16) { $rights += "WRITE_EA" }
                    if ($mask -band 32) { $rights += "EXECUTE" }
                    if ($mask -band 64) { $rights += "DELETE_CHILD" }
                    if ($mask -band 128) { $rights += "READ_ATTRIBUTES" }
                    if ($mask -band 256) { $rights += "WRITE_ATTRIBUTES" }
                    if ($mask -band 65536) { $rights += "DELETE" }
                    if ($mask -band 131072) { $rights += "READ_CONTROL" }
                    if ($mask -band 262144) { $rights += "WRITE_DAC" }
                    if ($mask -band 524288) { $rights += "WRITE_OWNER" }
                    return , $rights
                }

                [PSCustomObject]@{
                    name                = $service.Name
                    path                = $exePath
                    status              = $service.State
                    run_by              = $run_by

                    security_descriptor = [PSCustomObject]@{
                        owner = Make-Trustee $sd.Descriptor.Owner
                        group = Make-Trustee $sd.Descriptor.Group
                        dacl  = @($sd.Descriptor.DACL | ForEach-Object {
                                [PSCustomObject]@{
                                    access_mask = $_.AccessMask
                                    trustee     = Make-Trustee $_.Trustee
                                    inherited   = [bool]($_.AceFlags -band 0x10)
                                    permissions = , @(Get-PermissionsFromMask $_.AccessMask)
                                }
                            })
                    }
                }
            }
            else {
                [PSCustomObject]@{
                    name                = $service.Name
                    path                = $exePath
                    status              = $service.State
                    run_by              = $run_by
                    security_descriptor = $null
                }
            }

        }
    }

    $output["time_sec"] = $time.TotalSeconds
    $output["result"] = $results
    return $output | ConvertTo-Json -Compress -Depth 100
}

Write-Output (Get-ServiceExeACL)