from pathlib import Path

txt_path = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU\TRANSKRIP TEKS (TXT)\BIMBINGAN KEDUA (BU AYU)_WITH_TIMESTAMPS.txt")
lines = txt_path.read_text(encoding="utf-8").splitlines()

# Write out full text broken down by 15-minute chunks for thorough inspection
out_chunks = []
current_chunk = []
chunk_idx = 1

for line in lines:
    current_chunk.append(line)
    if len(current_chunk) >= 500:
        chunk_file = Path(f"scripts/bimbingan2_chunk_{chunk_idx}.txt")
        chunk_file.write_text("\n".join(current_chunk), encoding="utf-8")
        print(f"Wrote chunk {chunk_idx}: {len(current_chunk)} lines")
        chunk_idx += 1
        current_chunk = []

if current_chunk:
    chunk_file = Path(f"scripts/bimbingan2_chunk_{chunk_idx}.txt")
    chunk_file.write_text("\n".join(current_chunk), encoding="utf-8")
    print(f"Wrote chunk {chunk_idx}: {len(current_chunk)} lines")
