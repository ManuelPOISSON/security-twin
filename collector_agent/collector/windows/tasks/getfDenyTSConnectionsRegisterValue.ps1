function Get-RemoteDesktopStatus {
    param ()
    $output = @{
        time_sec = $null
        result   = $null
    }
    $time = Measure-Command {

  
        $registryPath = "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server"
        $propertyName = "fDenyTSConnections"

        try {
            $value = Get-ItemProperty -Path $registryPath -Name $propertyName -ErrorAction Stop |
            Select-Object -ExpandProperty $propertyName

            $result = @{
                key   = "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\fDenyTSConnections"
                value = $value.toString()
            }

            
        }
        catch {
            Write-Error "Failed to retrieve the registry value: $_"
            $result = @{"error" = $_ }
        }
    }
    $output["time_sec"] = $time.TotalSeconds
    $output["result"] = $result
    return $output | ConvertTo-Json -Compress 
}
Write-Output (Get-RemoteDesktopStatus)