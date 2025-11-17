set WshShell = WScript.CreateObject("Wscript.Shell")
' works ok when manually executed with cscript /nologo first_runas.vbs
' does not work when executed from ansible playbook
WScript.Sleep 50
WshShell.run "cmd.exe /c whoami > whovbs.txt"
WScript.Sleep 50

WshShell.run "cmd.exe /c runas /savecred /user:lab.local\u1 " + Chr(34) + "cmd.exe" + Chr(34)
WScript.Sleep 250
WshShell.SendKeys "234P@ss"
WshShell.SendKeys "{ENTER}"

WScript.Sleep 50
WshShell.run "cmd.exe /c whoami > whovbs_2.txt"
WScript.Sleep 50

set WshShell = nothing