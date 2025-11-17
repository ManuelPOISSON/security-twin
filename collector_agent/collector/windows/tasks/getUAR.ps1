function get-UAR() {
    $output = @{
        time_sec = $null
        result   = $null
    }
    $time = Measure-Command {
        try {
            $out_filename = "C:\Windows\Temp\secedit_result.txt"

            $seceditOutput = & secedit /export /areas USER_RIGHTS /cfg $out_filename 2>&1
            if (!(Test-Path $out_filename)) {
                throw $seceditOutput
            }
            $content = Get-Content $out_filename -Raw
            $bytes = [System.Text.Encoding]::UTF8.GetBytes($content)
            $result_json = [Convert]::ToBase64String($bytes)
            Remove-Item -Path $out_filename
        }
        catch {
            $errMsg = $_.Exception.Message
            Write-Error "An error occurred while executing secedit export: $errMsg"
            $result_json = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($errMsg))
        }
    }
    $output["time_sec"] = $time.TotalSeconds
    $output["xml_b64encoded"] = $result_json
    return $output
}

Write-Output (get-UAR | ConvertTo-Json -Depth 5 -Compress)
