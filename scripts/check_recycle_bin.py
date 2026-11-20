import os
import subprocess
import json

# Check Recycle Bin using PowerShell
ps_cmd = """
$shell = New-Object -ComObject Shell.Application
$recycleBin = $shell.Namespace(0xA) # 0xA = 10 is Recycle Bin
foreach ($item in $recycleBin.Items()) {
    if ($item.Name -like "*.md*" -or $item.Name -like "*BAB*") {
        [PSCustomObject]@{
            Name = $item.Name
            Path = $item.Path
            Size = $item.Size
            ModifyDate = $item.ModifyDate
        } | ConvertTo-Json -Compress
    }
}
"""

res = subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], capture_output=True, text=True)
print("=== Recycle Bin Items ===")
print(res.stdout)
if res.stderr:
    print("Error:", res.stderr)
