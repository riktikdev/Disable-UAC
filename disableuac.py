import subprocess

# Run the command to disable UAC
subprocess.call("REG ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f", shell=True)

# Reboot the system to apply the changes
subprocess.call("shutdown /r /t 0", shell=True)
