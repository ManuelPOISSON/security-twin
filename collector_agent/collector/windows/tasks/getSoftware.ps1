
function Get-WindowsInstalledCapability() {
    return Get-WindowsCapability -Online | Select-Object * | Where-Object { $_.State -eq "Installed" }
}
function Get-InstalledPackage {
    return Get-Package | Select-Object Name, Version
}

function Get-InstalledPackageX {
    return Get-AppxPackage | Select-Object Name, Version
}
function Get-Software {
    param ()
    $allSoftwareInfo = @{
        time_sec             = $null 
        windows_capabilities = $null 
        installed_packages   = $null 
        appx_packages        = $null
    }
    $time = Measure-Command {
        try {
            $allSoftwareInfo["windows_capabilities"] = Get-WindowsInstalledCapability
        }
        catch {
            $errMsg = $_.Exception
            Write-Error "$errMsg"
            Write-Error "During call to Get-WindowsInstalledCapability"
            $allSoftwareInfo["windows_capabilities"] = $null
        }

        try {
            
            $allSoftwareInfo["installed_packages"] = Get-InstalledPackage
        }
        catch {
            $errMsg = $_.Exception
            Write-Error "$errMsg"
            Write-Error "During call to Get-InstalledPackage"
            $allSoftwareInfo["installed_packages"] = $null
        }

        try {
            $allSoftwareInfo["appx_packages"] = Get-InstalledPackageX
        }
        catch {
            $errMsg = $_.Exception
            Write-Error "$errMsg"
            Write-Error "During call to Get-InstalledPackageX"
            $allSoftwareInfo["appx_packages"] = $null
        }
    }
    $allSoftwareInfo["time_sec"] = $time.Seconds
    return $allSoftwareInfo | ConvertTo-Json -Depth 10 -Compress
}

Write-Output (Get-Software)