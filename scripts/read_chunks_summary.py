from pathlib import Path

# Let's inspect the main dialogue for each chunk
for i in range(1, 8):
    chunk_file = Path(f"scripts/bimbingan2_chunk_{i}.txt")
    lines = chunk_file.read_text(encoding="utf-8").splitlines()
    print(f"\n================ CHUNK {i} ({lines[0][:17]} s/d {lines[-1][:17]}) ================")
    # Print 10 representative lines throughout the chunk
    step = len(lines) // 8
    for j in range(0, len(lines), step):
        print(f"  {lines[j]}")
