from pathlib import Path

f1 = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BAB 3 - RANCANGAN PROTOTIPE (REVISI TEMPLATE TERBARU) copy.md")
f2 = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BAB 3 - RANCANGAN PROTOTIPE (DRAFT 1) copy.md")

print("File 1 (REVISI TEMPLATE TERBARU copy):", f1.stat().st_size, "bytes,", len(f1.read_text(encoding='utf-8').splitlines()), "lines")
print("File 2 (DRAFT 1 copy):", f2.stat().st_size, "bytes,", len(f2.read_text(encoding='utf-8').splitlines()), "lines")
