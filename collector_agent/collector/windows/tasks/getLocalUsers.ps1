function Get-SIDFromAccount {
    param (
        [Parameter(Mandatory = $true)]
        [string]$AccountName
    )

    try {
        $ntAccount = New-Object System.Security.Principal.NTAccount($AccountName)

        $sid = $ntAccount.Translate([System.Security.Principal.SecurityIdentifier])
        return $sid.Value
    }
    catch {
        Write-Warning "Get-SidFrom Account impossible to translate: '$AccountName' ."
        return $null
    }
}

function Get-SIDFromAccount {
    param (
        [Parameter(Mandatory = $true)]
        [string]$AccountName
    )

    try {
        $ntAccount = New-Object System.Security.Principal.NTAccount($AccountName)
        $sid = $ntAccount.Translate([System.Security.Principal.SecurityIdentifier])
        return $sid.Value
    }
    catch {
        Write-Warning "Unable to translate account '$AccountName' to SID."
        return $null
    }
}

function Get-LocalUsersADSI {
    param (
        # Optional parameter, defaults to the local computer name if not provided
        [string]$ComputerName = $env:COMPUTERNAME
    )

    try {
        $computer = [ADSI]"WinNT://$ComputerName"

        $result = @()

        foreach ($child in $computer.Children) {
            if ($child.SchemaClassName -eq 'User') {
                $name = $child.Name
                $sid = Get-SIDFromAccount -AccountName $name
                if ($sid) {
                    $result += [PSCustomObject]@{
                        name = $name
                        sid  = $sid
                    }
                }
            }
        }
        return $result
    }
    catch {
        Write-Error "Failed to enumerate users on "$ComputerName": $($_.Exception.Message)"
    }
}


function Get-LocalUsersNet {
    $output = net user
    $capture = $false
    $users = @()

    foreach ($line in $output) {
        if ($line -match '---+') {
            $capture = $true
            continue
        }
        if ($capture -and ($line -match 'The command completed successfully')) {
            break
        }

        if ($capture) {
            $entries = $line -split '\s+'
            foreach ($entry in $entries) {
                if ($entry -ne '') {
                    $users += $entry
                }
            }
        }
    }

    $result = @()
    foreach ($name in $users) {
        $sid = Get-SIDFromAccount -AccountName $name
        if ($sid) {
            $result += [PSCustomObject]@{
                name = $name
                sid  = $sid
            }
        }
    }

    return $result
}


function Get-LocalUsersPw {
    $userNames = Get-LocalUser | Select-Object -ExpandProperty Name
    

    $result = @()

    foreach ($name in $userNames) {
        $sid = Get-SIDFromAccount -AccountName $name
        if ($sid) {
            $result += [PSCustomObject]@{
                name = $name
                sid  = $sid
            }
        }
    }

    return $result
}

function Get-LocalUsersWMI {
    $accounts = Get-CimInstance Win32_Account |
    Where-Object { $_.LocalAccount -eq $true -and ($_.SIDType -eq 1 -or $_.SIDType -eq 5) }

    $result = @()

    foreach ($acct in $accounts) {
        $result += [PSCustomObject]@{
            name = $acct.Name
            sid  = $acct.SID
        }
    }

    return $result
}


function Get-LocalUsers {
    param ()
    $output = @{
        time_sec = $null
        result   = $null
    }
    
    $time = Measure-Command {
        try {
            $result = Get-LocalUsersWMI

        }
        catch {
            Write-Error "Failed to retrieve local users with WMI function: $($_.Exception.Message)"
            $result = $null
            
        }
    }
    if ($null -ne $result) {
        $output["time_sec"] = $time.TotalSeconds
        $output["result"] = $result
        return $output
    }


    $time = Measure-Command {
        try {
            $result = Get-LocalUsersPw

        }
        catch {
            Write-Error "Failed to retrieve local users with Powershell function: $($_.Exception.Message)"
            $result = $null
            
        }
    }
    if ($null -ne $result) {
        $output["time_sec"] = $time.TotalSeconds
        $output["result"] = $result
        return $output
    }

    $time = Measure-Command {
        try {
            $result = Get-LocalUsersADSI
        }
        catch {
            Write-Error "Failed to retrieve local users with ADSI: $($_.Exception.Message)"
            $result = $null
        }
    }
    if ($null -ne $result) {
        $output["time_sec"] = $time.TotalSeconds
        $output["result"] = $result
        return $output
    }

    $time = Measure-Command {
        try {
            $result = Get-LocalUsersNet
        }
        catch {
            Write-Error "Failed to retrieve local users with net command: $($_.Exception.Message)"
            $result = $null
        }
    }
    if ($null -ne $result) {
        $output["time_sec"] = $time.TotalSeconds
        $output["result"] = $result
        return $output
    }
    
    $output["time_sec"] = $null
    $output["result"] = "error"
    
    return $output 
}

Write-Output (Get-LocalUsers | ConvertTo-Json -Depth 100 -Compress )
