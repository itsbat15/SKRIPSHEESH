from pathlib import Path

turns = Path("scripts/bimbingan2_turns.txt").read_text(encoding="utf-8").split("\n\n")

print(f"Total turns: {len(turns)}")

# Let's read blocks in sections
def print_range(start_idx, end_idx, title):
    print(f"\n==================== {title} (Turns {start_idx} - {end_idx}) ====================")
    for i in range(start_idx, min(end_idx, len(turns))):
        if turns[i].strip():
            print(f"Turn {i}: {turns[i].strip()[:140]}...")

print_range(0, 30, "BAGIAN 1: PEMBUKA & METODOLOGI PXP VS WATERFALL/SCRUM/RAD (00:00 - 15:00)")
print_range(30, 60, "BAGIAN 2: AKTOR MITRA, PROYEK VS PROTOTIPE, BAB 2 DOMAIN (15:00 - 28:00)")
print_range(60, 95, "BAGIAN 3: KETERLIBATAN 4 AKTOR MITRA & ITERASI VALIDASI (28:00 - 42:00)")
print_range(95, 130, "BAGIAN 4: ALUR PROSES BISNIS, CONSTRAINT, & RUMUSAN MASALAH (42:00 - 55:00)")
print_range(130, 165, "BAGIAN 5: KOMBINASI INFORMASI, DASBOR, & TUJUAN PENELITIAN (55:00 - 01:10:00)")
print_range(165, 203, "BAGIAN 6: PENGUJIAN BLACK BOX, UAT, CITASI, & RENCANA TINDAK LANJUT (01:10:00 - SELESAI)")
