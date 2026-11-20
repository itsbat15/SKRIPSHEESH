import subprocess
from pathlib import Path

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")
BIN_DIR = ROOT / "bin"
BIN_DIR.mkdir(parents=True, exist_ok=True)

dest_str = str(BIN_DIR)

ps_script = f"""
$shell = New-Object -ComObject Shell.Application
$recycleBin = $shell.Namespace(0xA)
$destFolder = $shell.Namespace('{dest_str}')

if ($destFolder -eq $null) {{
    Write-Output "Dest folder is null!"
}} else {{
    foreach ($item in $recycleBin.Items()) {{
        if ($item.Name -like "*BAB 1*" -or $item.Name -like "*BAB 3*" -or $item.Name -like "*KOREKSI*") {{
            Write-Output "Restoring: $($item.Name)"
            $destFolder.CopyHere($item)
        }}
    }}
}}
"""

res = subprocess.run(["powershell", "-NoProfile", "-Command", ps_script], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("Error:", res.stderr)
