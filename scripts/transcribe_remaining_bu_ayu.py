import os
import sys
import time
import datetime
import whisper

FFMPEG_DIR = r"C:\Users\ARIEL\AppData\Roaming\Python\Python313\site-packages\imageio_ffmpeg\binaries"
if os.path.exists(FFMPEG_DIR) and FFMPEG_DIR not in os.environ.get("PATH", ""):
    os.environ["PATH"] = FFMPEG_DIR + ";" + os.environ.get("PATH", "")

AUDIO_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU\BIMBINGAN KE-1 (Bu Ayu).m4a"
OUTPUT_DIR = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU"
OUTPUT_WITH_TS = os.path.join(OUTPUT_DIR, "BIMBINGAN KE-1 (Bu Ayu)_WITH_TIMESTAMPS.txt")
OUTPUT_PLAIN = os.path.join(OUTPUT_DIR, "BIMBINGAN KE-1 (Bu Ayu).txt")
OUTPUT_MD = os.path.join(OUTPUT_DIR, "BIMBINGAN_KE_1_BU_AYU.md")

START_OFFSET_SEC = 2833.0  # 47 menit 13 detik (titik sebelum loop terjadi)

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hours > 0:
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"

def main():
    print("=" * 60)
    print("TRANSKRIPSI LANJUTAN: MENIT 47:13 SAMPAI SELESAI (72:48)")
    print(f"File Audio: {AUDIO_PATH}")
    print(f"Waktu Mulai: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # 1. Baca data bersih dari bagian 1 (00:00 - 47:13, yaitu sebelum baris 1128)
    part1_ts_lines = []
    part1_plain_lines = []
    with open(OUTPUT_WITH_TS, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if idx < 1127: # Baris 0 sampai 1126
                part1_ts_lines.append(line)
    
    with open(OUTPUT_PLAIN, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if idx < 1127:
                part1_plain_lines.append(line)

    print(f"Bagian 1 (00:00 - 47:13) diamankan: {len(part1_ts_lines)} baris valid.")

    print("\nMemuat audio dari menit 47:13 sampai selesai...")
    audio = whisper.load_audio(AUDIO_PATH)
    sr = 16000
    start_sample = int(START_OFFSET_SEC * sr)
    remaining_audio = audio[start_sample:]
    remaining_duration = len(remaining_audio) / sr
    print(f"Durasi sisa yang akan ditranskrip: {remaining_duration:.1f} detik ({remaining_duration/60:.2f} menit)")

    print("\nMemuat model Whisper 'large-v3-turbo'...")
    model = whisper.load_model("large-v3-turbo")

    prompt = (
        "Bimbingan tugas akhir Bu Ayu dan Ariel. Membahas rumusan masalah, tujuan, 5 poin tujuan, "
        "metode PxP, Extreme Programming, Scrum, Agile, perancangan, implementasi, testing, evaluasi, "
        "keterlibatan mitra Artha, Radit, stakeholder, literasi digital."
    )

    print("\nMemulai transkripsi bagian 2 dengan condition_on_previous_text=False (bebas looping)...")
    start_time = time.time()
    result = model.transcribe(
        remaining_audio,
        language="id",
        initial_prompt=prompt,
        condition_on_previous_text=False,
        verbose=True,
        fp16=False,
        temperature=0.0
    )

    segments_part2 = result.get("segments", [])
    print(f"\nSelesai decoding {len(segments_part2)} segmen baru dalam {(time.time() - start_time)/60:.2f} menit.")

    part2_ts_lines = []
    part2_plain_lines = []
    for seg in segments_part2:
        actual_start = START_OFFSET_SEC + seg["start"]
        actual_end = START_OFFSET_SEC + seg["end"]
        text = seg["text"].strip()
        
        # Filter jika ada segmen kosong atau noise murni
        if not text:
            continue
            
        start_str = format_timestamp(actual_start)
        end_str = format_timestamp(actual_end)
        
        part2_ts_lines.append(f"[{start_str} - {end_str}] {text}\n")
        part2_plain_lines.append(f"{text}\n")

    # 3. Gabungkan Bagian 1 dan Bagian 2
    full_ts_lines = part1_ts_lines + part2_ts_lines
    full_plain_lines = part1_plain_lines + part2_plain_lines

    print(f"\nMenyimpan seluruh transkrip lengkap (Total: {len(full_ts_lines)} baris percakapan)...")

    with open(OUTPUT_WITH_TS, "w", encoding="utf-8") as f:
        f.writelines(full_ts_lines)

    with open(OUTPUT_PLAIN, "w", encoding="utf-8") as f:
        f.writelines(full_plain_lines)

    # 4. Buat Markdown Lengkap
    md_lines = [
        "# 🎙️ Transkrip Lengkap Bimbingan Ke-1 (Bu Ayu)",
        "",
        "- **File Sumber**: `BIMBINGAN KE-1 (Bu Ayu).m4a`",
        "- **Dosen Pembimbing 2**: Ibu Sri Rahayu Natasia, S.Kom., M.Si., M.Sc. (Bu Ayu)",
        "- **Mahasiswa**: Ariel",
        f"- **Durasi Total**: 72 Menit 48 Detik (Lengkap 100%)",
        f"- **Tanggal Ekstraksi**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "- **Model AI**: OpenAI Whisper `large-v3-turbo` (High-Resolution Extraction)",
        f"- **Total Segmen**: {len(full_ts_lines)}",
        "",
        "---",
        "",
        "## 📝 Percakapan Lengkap Berdasarkan Waktu (*Timestamp*)",
        ""
    ]
    for line in full_ts_lines:
        line_clean = line.strip()
        if line_clean:
            # Format: **[MM:SS - MM:SS]** Teks
            parts = line_clean.split("] ", 1)
            if len(parts) == 2:
                md_lines.append(f"**{parts[0]}]** {parts[1]}\n")
            else:
                md_lines.append(f"{line_clean}\n")

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print("=" * 60)
    print("100% SUKSES! File transkrip lengkap tersimpan di:")
    print(f"1. {OUTPUT_WITH_TS}")
    print(f"2. {OUTPUT_PLAIN}")
    print(f"3. {OUTPUT_MD}")
    print("=" * 60)

if __name__ == "__main__":
    main()
