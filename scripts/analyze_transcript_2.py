import re
from pathlib import Path

txt_path = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU\TRANSKRIP TEKS (TXT)\BIMBINGAN KEDUA (BU AYU)_WITH_TIMESTAMPS.txt")
lines = txt_path.read_text(encoding="utf-8").splitlines()

print(f"Total lines in timestamps transcript: {len(lines)}")

# Let's see samples across various time slices
# 00:00 - 10:00, 10:00 - 20:00, 20:00 - 30:00, 30:00 - 40:00, 40:00 - 50:00, 50:00 - 60:00, 60:00 - 70:00, 70:00 - 80:00, 80:00 - end

time_buckets = {}
for line in lines:
    m = re.match(r"\[(\d{2}):(\d{2})", line)
    if not m:
        m = re.match(r"\[(\d{2}):(\d{2}):(\d{2})", line)
        if m:
            h, mi, s = int(m.group(1)), int(m.group(2)), int(m.group(3))
            bucket = (h * 60 + mi) // 10 * 10
        else:
            bucket = 0
    else:
        mi = int(m.group(1))
        bucket = mi // 10 * 10
    time_buckets.setdefault(bucket, []).append(line)

print("\nDistribution across 10-minute intervals:")
for b in sorted(time_buckets.keys()):
    print(f"Minute {b:02d} - {b+10:02d}: {len(time_buckets[b])} segments")
