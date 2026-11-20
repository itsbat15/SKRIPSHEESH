import json
from pathlib import Path
import fitz

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")
AUD = ROOT / "JURNAL" / "AUDIT_SITASI_BAB1_2026-10-25"
data = json.loads((AUD / "MATRIKS_KLAIM_DAN_HALAMAN.json").read_text(encoding="utf-8"))

print(f"Total rows in JSON: {len(data['rows'])}")
print(f"Total sources in JSON: {len(data['sources'])}")

sources_by_id = {s["id"]: s for s in data["sources"]}

for s_id, s in sorted(sources_by_id.items()):
    p = Path(s["file"])
    exists = p.exists()
    print(f"[{s_id}] Exists: {exists} | Pages: {s['pdf_pages']} | {p.name}")
