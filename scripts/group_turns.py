from pathlib import Path
import re

txt_path = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU\TRANSKRIP TEKS (TXT)\BIMBINGAN KEDUA (BU AYU)_WITH_TIMESTAMPS.txt")
lines = txt_path.read_text(encoding="utf-8").splitlines()

# Let's inspect the flow of dialogue by merging short lines into conversational turns
turns = []
cur_time = ""
cur_text = []

for line in lines:
    m = re.match(r"\[([0-9:]+) - [0-9:]+\]\s*(.*)", line)
    if m:
        ts = m.group(1)
        text = m.group(2).strip()
        if not cur_time:
            cur_time = ts
        cur_text.append(text)
        # Group every ~50-80 words or when there's a strong pause
        if len(" ".join(cur_text).split()) >= 40:
            turns.append((cur_time, " ".join(cur_text)))
            cur_time = ""
            cur_text = []

if cur_text:
    turns.append((cur_time, " ".join(cur_text)))

print(f"Total conversational blocks: {len(turns)}")

# Let's write out all turns to a scratch file so we can view specific sections
scratch_file = Path("scripts/bimbingan2_turns.txt")
with open(scratch_file, "w", encoding="utf-8") as f:
    for ts, text in turns:
        f.write(f"[{ts}] {text}\n\n")

print(f"Saved to {scratch_file}")
