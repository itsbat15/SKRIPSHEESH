import re
from pathlib import Path

txt_path = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU\TRANSKRIP TEKS (TXT)\BIMBINGAN KEDUA (BU AYU)_WITH_TIMESTAMPS.txt")
lines = txt_path.read_text(encoding="utf-8").splitlines()

def parse_time(ts_str):
    parts = ts_str.split(":")
    if len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    elif len(parts) == 2:
        return int(parts[0]) * 60 + int(parts[1])
    return 0

parsed_segments = []
for line in lines:
    m = re.match(r"\[([0-9:]+) - ([0-9:]+)\]\s*(.*)", line)
    if m:
        t_start = parse_time(m.group(1))
        t_end = parse_time(m.group(2))
        text = m.group(3).strip()
        parsed_segments.append((t_start, t_end, m.group(1), m.group(2), text))

print(f"Total parsed segments: {len(parsed_segments)}")
first_t = parsed_segments[0][0]
last_t = parsed_segments[-1][1]
print(f"Time range: {first_t}s ({first_t/60:.1f}m) to {last_t}s ({last_t/60:.1f}m)")

# Breakdown by 10-minute intervals
intervals = range(0, last_t + 600, 600)
for start_sec in intervals:
    end_sec = start_sec + 600
    segs = [s for s in parsed_segments if start_sec <= s[0] < end_sec]
    if segs:
        print(f"\n--- Interval {start_sec//60:02d}:00 - {end_sec//60:02d}:00 ({len(segs)} segments) ---")
        # Combine text to see summary
        combined_text = " ".join(s[4] for s in segs)
        # Print first 250 characters and last 150 characters
        print("  Snippet: " + combined_text[:300] + " ... " + combined_text[-150:])
