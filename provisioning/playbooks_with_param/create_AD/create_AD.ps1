
Param ([parameter(Mandatory = $true, Position = 0)][string] $domain,
    [parameter(Mandatory = $true, Position = 1)][string] $adminPasswd,
    [parameter(Mandatory = $true, Position = 2)][string] $netwId)

# create_AD.ps1 'domain.int' 'pwdPWD124#' '10.0.20.0/24'


$netbiosDomain = ($domain -split '\.')[0].ToUpperInvariant()
$safeModeAdminstratorPassword = ConvertTo-SecureString $adminPasswd -AsPlainText -Force
Install-WindowsFeature AD-Domain-Services, RSAT-AD-AdminCenter, RSAT-ADDS-Tools
Import-Module ADDSDeployment
Install-ADDSForest -CreateDnsDelegation:$false -DatabasePath "C:\Windows\NTDS" -DomainMode "WinThreshold" -DomainName $domain -DomainNetbiosName $netbiosDomain -ForestMode "WinThreshold" -InstallDns:$true -LogPath "C:\Windows\NTDS" -NoRebootOnCompletion:$false -SysvolPath "C:\Windows\SYSVOL" -SafeModeAdministratorPassword $safeModeAdminstratorPassword -Force
while ($true) {
    try {
		Get-ADDomain | Out-Null
		break
    } catch {
		Start-Sleep -Seconds 10
    }
}
# Ajout de la zone DNS inverse
Add-DNSServerPrimaryZone -NetworkId $netwId -ReplicationScope "Domain"
# Enregistrement de l'adresse IP courante dans la zone inverse
Register-DnsClient