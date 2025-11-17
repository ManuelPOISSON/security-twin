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



function Get-LocalGroupsADSI {
    $result = @()
    try {
        $computer = [ADSI]"WinNT://$env:COMPUTERNAME"
        $groups = @($computer.Children | Where-Object { $_.SchemaClassName -eq 'Group' })

        foreach ($group in $groups) {
            $groupName = $group.Name
            $groupSID = Get-SIDFromAccount -AccountName $groupName
            $groupInfo = @{
                name    = $groupName
                sid     = $groupSID
                members = @()
            }

            try {
                $members = @($group.psbase.Invoke("Members"))
                foreach ($member in $members) {
                    $memberName = ([ADSI]$member).InvokeGet("Name")
                    $memberSID = Get-SIDFromAccount -AccountName $memberName
                    $groupInfo.Members += @{
                        name = $memberName
                        sid  = $memberSID
                    }
                }
            }
            catch {
                Write-Warning "Unable to retrieve members of group '$groupName'."
                $groupInfo["error"] = "Unable to retrieve members (ADSI)"
            }

            $result += $groupInfo
        }
    }
    catch {
        Write-Error "Failed to retrieve groups using ADSI: $($_.Exception.Message)"
    }
    return $result
}

function Get-LocalGroupsNet {
    $result = @()
    $groupsOutput = net localgroup
    $lines = $groupsOutput -split "`r?`n"
    $inMembersSection = $false

    foreach ($line in $lines) {
        if ($line -match "^\*\s*(.+?)\s*$" -and $line -notmatch "^(.*command completed successfully.*|\-\-\-|\s*)$") {
            
            $groupName = $matches[1].Trim()
            $groupSID = Get-SIDFromAccount -AccountName $groupName
            $quotedGroupName = "`"$groupName`""
            $groupMembersOutput = net localgroup $quotedGroupName 2>&1

            if ($LASTEXITCODE -ne 0) {
                Write-Error "Error retrieving members of group: $quotedGroupName"
                $groupMembersOutput | ForEach-Object { Write-Error "  $_" }
            }

            $members = @()
            $inMembersSection = $false
            
            for ($i = 0; $i -lt $groupMembersOutput.Count - 2; $i++) {
                $groupMemberLine = $groupMembersOutput[$i]

                if ($groupMemberLine -match '^\--*') {
                    $inMembersSection = $true
                    continue
                }

                if ($inMembersSection) {
                    $groupMemberLine = $groupMemberLine.Trim()
                    if ($groupMemberLine -ne '') {
                        $memberSID = Get-SIDFromAccount -AccountName $groupMemberLine
                        $members += @{
                            Name = $groupMemberLine
                            SID  = $memberSID
                        }
                    }
                }
            }
    
            $result += @{
                Name    = $groupName
                SID     = $groupSID
                Members = $members
            }
        }
    }
    return $result
}

function Get-LocalGroupsPw {
    $groups = Get-LocalGroup
    $result = @()

    foreach ($group in $groups) {
        $groupSID = Get-SIDFromAccount -AccountName $group.Name
        $groupInfo = @{
            name    = $group.Name
            sid     = $groupSID
            members = @()
        }

        try {
            $members = Get-LocalGroupMember -Group $group.Name
            foreach ($member in $members) {
                $memberSID = Get-SIDFromAccount -AccountName $member.Name
                $groupInfo.Members += @{
                    name = $member.Name
                    sid  = $memberSID
                }
            }
        }
        catch {
            $groupInfo["error"] = "Unable to retrieve members"
            Write-Error "Failed to retrieve members of group '$($group.Name)': $($_.Exception.Message)"
        }

        $result += $groupInfo
    }

    return $result
}
<#
.SYNOPSIS
Retrieves local groups and their members using multiple fallback methods.

.DESCRIPTION
Attempts to gather local group membership information using three methods:
1. PowerShell cmdlets.
2. ADSI (Active Directory Service Interfaces).
3. Net command.

The function returns the result along with the time taken by the successful method.
If all methods fail, it returns "error".

.OUTPUTS
Hashtable containing:
- time_sec : Time taken in seconds.
- result   : Group data or "error" if all methods fail.
#>
function Get-LocalGroupsAndMembers {
    param ()
    $output = @{
        time_sec = $null
        result   = $null
    }
    $time = Measure-Command {
        try {
            $result = Get-LocalGroupsPw
        }
        catch {
            Write-Error "Failed to retrieve local groups with Powershell function: $($_.Exception.Message)"
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
            $result = Get-LocalGroupsADSI 
        }
        catch {
            Write-Error "Failed to retrieve local groups with ADSI: $($_.Exception.Message)"
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
            $result = Get-LocalGroupsNet
        }
        catch {
            Write-Error "Failed to retrieve local groups with net command: $($_.Exception.Message)"
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

function get-LocalGroupsMembersAll {
    # Try PowerShell method first
    try {
        $timePw = Measure-Command {
            $output = Get-LocalGroupsPw
        }
        Write-Verbose "Get-LocalGroupsPw succeeded in $($timePw.TotalSeconds)s"
        # Return a structured object including the result and execution time
        return [PSCustomObject]@{
            method   = "PowerShell"
            time_sec = $timePw.TotalSeconds
            result   = $output
        }
    }
    catch {
        Write-Warning "Get-LocalGroupsPw failed: $($_.Exception.Message)"
    }

    # Try ADSI method if PowerShell failed
    try {
        $timeADSI = Measure-Command {
            $output = Get-LocalGroupsADSI
        }
        Write-Verbose "Get-LocalGroupsADSI succeeded in $($timeADSI.TotalSeconds)s"
        return [PSCustomObject]@{
            method   = "ADSI"
            time_sec = $timeADSI.TotalSeconds
            result   = $output
        }
    }
    catch {
        Write-Warning "Get-LocalGroupsADSI failed: $($_.Exception.Message)"
    }

    # Try net method if ADSI failed
    try {
        $timeNet = Measure-Command {
            $output = Get-LocalGroupsNet
        }
        Write-Verbose "Get-LocalGroupsNet succeeded in $($timeNet.TotalSeconds)s"
        return [PSCustomObject]@{
            method   = "Net"
            time_sec = $timeNet.TotalSeconds
            result   = $output
        }
    }
    catch {
        Write-Warning "Get-LocalGroupsNet failed: $($_.Exception.Message)"
    }

    # If all methods fail
    Write-Error "All methods failed to retrieve local groups."
    return $null
}

Write-Output (get-LocalGroupsMembersAll | ConvertTo-Json -Depth 10 -Compress  )

