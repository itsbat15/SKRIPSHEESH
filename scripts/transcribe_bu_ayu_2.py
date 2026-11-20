"""
transcribe_bu_ayu_2.py
======================
Skrip transkripsi audio otomatis menggunakan faster-whisper (large-v3-turbo, int8, VAD filter)
untuk rekaman "BIMBINGAN KEDUA (BU AYU).m4a" (durasi 85.8 menit).
Hasil disimpan secara streaming (real-time flush) ke:
1. BIMBINGAN KEDUA (BU AYU)_WITH_TIMESTAMPS.txt
2. BIMBINGAN KEDUA (BU AYU).txt
pada folder: c:\\Users\\ARIEL\\OneDrive - MSFT\\Documents\\ARTHA\\BIMBINGAN\\BU AYU\\TRANSKRIP TEKS (TXT)\\
"""

import os
import sys
import time
import datetime
from faster_whisper import WhisperModel

# Pastikan path ffmpeg dikenali
FFMPEG_DIR = r"C:\Users\ARIEL\AppData\Roaming\Python\Python313\site-packages\imageio_ffmpeg\binaries"
if os.path.exists(FFMPEG_DIR) and FFMPEG_DIR not in os.environ.get("PATH", ""):
    os.environ["PATH"] = FFMPEG_DIR + ";" + os.environ.get("PATH", "")

AUDIO_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU\REKAMAN AUDIO (M4A)\BIMBINGAN KEDUA (BU AYU).m4a"
OUTPUT_DIR = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU\TRANSKRIP TEKS (TXT)"
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_WITH_TS = os.path.join(OUTPUT_DIR, "BIMBINGAN KEDUA (BU AYU)_WITH_TIMESTAMPS.txt")
OUTPUT_PLAIN = os.path.join(OUTPUT_DIR, "BIMBINGAN KEDUA (BU AYU).txt")

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hours > 0:
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"

def main():
    print("=" * 70)
    print("TRANSKRIPSI WHISPER AI - BIMBINGAN KEDUA BERSAMA BU AYU")
    print(f"File Audio  : {AUDIO_PATH}")
    print(f"Folder Hasil: {OUTPUT_DIR}")
    print(f"Waktu Mulai : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    if not os.path.exists(AUDIO_PATH):
        print(f"Error: File audio tidak ditemukan di: {AUDIO_PATH}")
        sys.exit(1)

    threads = os.cpu_count() or 12
    print(f"\n[1/3] Memuat model Whisper 'large-v3-turbo' (CPU threads: {threads}, int8)...")
    t0 = time.time()
    model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=threads)
    print(f"Model berhasil dimuat dalam {time.time() - t0:.2f} detik!")

    prompt_panduan = (
        "Transkrip percakapan bimbingan Tugas Akhir Sistem Informasi ITK antara dosen pembimbing Bu Ayu (Ibu Sri Rahayu Natasia) "
        "dan mahasiswa Ariel. Topik: Rancang bangun sistem informasi manajemen operasional Bimbel Artha Balikpapan multicabang. "
        "Istilah: PxP, Personal Extreme Programming, Waterfall, Scrum, RAD, prototype, iterasi, refactoring, user story, tentor, "
        "SPP, cabang, kasir, mutasi bank, rekonsiliasi, WhatsApp, notifikasi, evaluasi, bab 1, latar belakang, rumusan masalah, "
        "tujuan, batasan masalah, kerangka berpikir, flowchart, fishbone, pengujian, black box, UAT."
    )

    print("\n[2/3] Memulai proses transkripsi penuh dengan Silero VAD Filter...")
    ts_file = open(OUTPUT_WITH_TS, "w", encoding="utf-8", buffering=1)
    plain_file = open(OUTPUT_PLAIN, "w", encoding="utf-8", buffering=1)

    t_start = time.time()
    total_segments = 0

    try:
        segments, info = model.transcribe(
            AUDIO_PATH,
            language="id",
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=500),
            initial_prompt=prompt_panduan,
            temperature=0.0
        )

        print(f"Bahasa terdeteksi: {info.language} (probabilitas: {info.language_probability:.2f})")
        print(f"Total durasi audio: {info.duration:.2f} detik ({info.duration / 60:.2f} menit)")
        print("Sedang menulis segmen transkrip ke file secara real-time...\n")

        last_report_sec = 0.0

        for seg in segments:
            total_segments += 1
            start_str = format_timestamp(seg.start)
            end_str = format_timestamp(seg.end)
            text = seg.text.strip()

            ts_line = f"[{start_str} - {end_str}] {text}\n"
            plain_line = f"{text}\n"

            ts_file.write(ts_line)
            plain_file.write(plain_line)
            ts_file.flush()
            plain_file.flush()

            # Laporan progres setiap 60 detik audio
            if seg.end - last_report_sec >= 60.0 or total_segments % 25 == 0:
                last_report_sec = seg.end
                pct = (seg.end / info.duration) * 100 if info.duration > 0 else 0
                now_str = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"[{now_str}] Progres: {seg.end/60:.1f}/{info.duration/60:.1f} m ({pct:.1f}%) | Segmen #{total_segments:04d}: [{start_str} - {end_str}] {text[:60]}...")

    finally:
        ts_file.close()
        plain_file.close()

    elapsed = time.time() - t_start
    print("\n" + "=" * 70)
    print(f"[3/3] TRANSKRIPSI SELESAI dalam waktu {elapsed/60:.2f} menit ({elapsed:.1f} detik)!")
    print(f"Total Segmen: {total_segments}")
    print(f"File Hasil Disimpan di:")
    print(f"1. {OUTPUT_WITH_TS} ({os.path.getsize(OUTPUT_WITH_TS):,} bytes)")
    print(f"2. {OUTPUT_PLAIN} ({os.path.getsize(OUTPUT_PLAIN):,} bytes)")
    print("=" * 70)

if __name__ == "__main__":
    main()
