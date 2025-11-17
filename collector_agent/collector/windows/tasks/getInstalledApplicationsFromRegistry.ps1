function Get-InstalledApplications() {
    [cmdletbinding(DefaultParameterSetName = 'GlobalAndAllUsers')]
    Param (
        [Parameter(ParameterSetName = "Global")]
        [switch]$Global,
        [Parameter(ParameterSetName = "GlobalAndCurrentUser")]
        [switch]$GlobalAndCurrentUser,
        [Parameter(ParameterSetName = "GlobalAndAllUsers")]
        [switch]$GlobalAndAllUsers,
        [Parameter(ParameterSetName = "CurrentUser")]
        [switch]$CurrentUser,
        [Parameter(ParameterSetName = "AllUsers")]
        [switch]$AllUsers
    )
    if ($PSCmdlet.ParameterSetName -eq "GlobalAndAllUsers") {
        $GlobalAndAllUsers = $true
    }
    if ($GlobalAndAllUsers -or $AllUsers) {
        $RunningAsAdmin = (New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
        if ($RunningAsAdmin -eq $false) {
            Write-Error "The getInstalledApplications.ps1 is not run with Administrator privileges"
            $GlobalAndAllUsers = $false
            $AllUsers = $false
            $GlobalAndCurrentUser = $true
        }
    }
    $32BitPath = "SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*"
    $64BitPath = "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*"
    $Softwares = @()
    if ($Global -or $GlobalAndAllUsers -or $GlobalAndCurrentUser) {
        $Softwares += [PSCustomObject]@{registry = "HKLM:\${32BitPath}"; softwares = Get-ItemProperty ("HKLM:\${32BitPath}") }

        $Softwares += [PSCustomObject]@{registry = "HKLM:\${64BitPath}"; softwares = Get-ItemProperty "HKLM:\${64BitPath}" }
    }
    if ($CurrentUser -or $GlobalAndCurrentUser) {
        $Softwares += [PSCustomObject]@{
            registry  = "Registry::HKEY_CURRENT_USER\${32BitPath}"
            softwares = Get-ItemProperty -Path "Registry::HKEY_CURRENT_USER\${32BitPath}"
        }

        $Softwares += [PSCustomObject]@{
            registry  = "Registry::HKEY_CURRENT_USER\${64BitPath}"
            softwares = Get-ItemProperty -Path "Registry::HKEY_CURRENT_USER\${64BitPath}"
        }

    }
    if ($AllUsers -or $GlobalAndAllUsers) {
        $AllProfiles = Get-CimInstance Win32_UserProfile | Select-Object LocalPath, SID, Loaded, Special | Where-Object { $_.SID -like "S-1-5-21-*" }
        $MountedProfiles = $AllProfiles | Where-Object { $_.Loaded -eq $true }
        $UnmountedProfiles = $AllProfiles | Where-Object { $_.Loaded -eq $false }
        $MountedProfiles | % {
            $Softwares += [PSCustomObject]@{
                registry  = "Registry::HKEY_USERS\$($_.SID)\${32BitPath}"
                softwares = Get-ItemProperty -Path "Registry::HKEY_USERS\$($_.SID)\${32BitPath}"
            }

            $Softwares += [PSCustomObject]@{
                registry  = "Registry::HKEY_USERS\$($_.SID)\${64BitPath}"
                softwares = Get-ItemProperty -Path "Registry::HKEY_USERS\$($_.SID)\${64BitPath}"
            }

        }

        $UnmountedProfiles | % {

            $Hive = "$($_.LocalPath)\NTUSER.DAT"

            if (Test-Path $Hive) {
            
                REG LOAD HKU\temp $Hive

                $Softwares += [PSCustomObject]@{
                    registry  = "Registry::HKEY_USERS\temp\$($_.SID)\${32BitPath}"
                    softwares = Get-ItemProperty -Path "Registry::HKEY_USERS\temp\${32BitPath}" 
                }

                $Softwares += [PSCustomObject]@{
                    registry  = "Registry::HKEY_USERS\temp\$($_.SID)\${64BitPath}"
                    softwares = Get-ItemProperty -Path "Registry::HKEY_USERS\temp\${64BitPath}" 
                }

                [GC]::Collect()
                [GC]::WaitForPendingFinalizers()
            
                REG UNLOAD HKU\temp

            }
        }
    }

    return $Softwares 
}
$time = Measure-Command {
    $apps = Get-InstalledApplications
    $apps = foreach ($app in $apps) {
        $soft = $app.softwares

        if (-not $soft) { continue }
        $filteredSoftwares = @()
        foreach ($s in @($soft)) {
            if ($s.DisplayName -and $s.DisplayVersion) {
                $filteredSoftwares += [PSCustomObject]@{
                    name    = $s.DisplayName
                    version = $s.DisplayVersion
                }
            }
        }
        [PSCustomObject]@{
            registry  = $app.registry
            softwares = @($filteredSoftwares)
        }
        
    }
}
$appsResult = [PSCustomObject]@{
    result   = $apps
    time_sec = [math]::Round($time.TotalSeconds, 3)
}

$appsJson = $appsResult | ConvertTo-Json -Compress -Depth 5
Write-Output $appsJson