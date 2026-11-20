"""
transcribe_pak_arif_7.py
========================
Skrip transkripsi otomatis audio rekaman bimbingan ke-7 Pak Arif:
'BIMBINGAN KE-7.m4a' (durasi 46.95 menit).
Menggunakan faster-whisper large-v3-turbo (int8, multi-threaded CPU).
Anti-halusinasi: condition_on_previous_text=False, repetition_penalty=1.2, no_repeat_ngram_size=3, beam_size=1.
Hasil disimpan secara streaming (real-time flush) ke:
1. BIMBINGAN KE 7 (PAK ARIF)_WITH_TIMESTAMPS.txt
2. BIMBINGAN KE 7 (PAK ARIF).txt
pada folder: c:\\Users\\ARIEL\\OneDrive - MSFT\\Documents\\ARTHA\\BIMBINGAN\\PAK ARIF\\TRANSKRIP TEKS (TXT)\\
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

AUDIO_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\PAK ARIF\REKAMAN AUDIO (M4A)\BIMBINGAN KE-7.m4a"
OUTPUT_DIR = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\PAK ARIF\TRANSKRIP TEKS (TXT)"
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_WITH_TS = os.path.join(OUTPUT_DIR, "BIMBINGAN KE 7 (PAK ARIF)_WITH_TIMESTAMPS.txt")
OUTPUT_PLAIN = os.path.join(OUTPUT_DIR, "BIMBINGAN KE 7 (PAK ARIF).txt")

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hours > 0:
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"

def main():
    print("=" * 70, flush=True)
    print("TRANSKRIPSI WHISPER AI - BIMBINGAN KE-7 BERSAMA PAK ARIF", flush=True)
    print(f"File Audio  : {AUDIO_PATH}", flush=True)
    print(f"Folder Hasil: {OUTPUT_DIR}", flush=True)
    print(f"Waktu Mulai : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", flush=True)
    print("=" * 70, flush=True)

    if not os.path.exists(AUDIO_PATH):
        print(f"Error: File audio tidak ditemukan di: {AUDIO_PATH}", flush=True)
        sys.exit(1)

    threads = os.cpu_count() or 12
    print(f"\n[1/3] Memuat model Whisper 'large-v3-turbo' (CPU threads: {threads}, int8)...", flush=True)
    t0 = time.time()
    model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=threads)
    print(f"Model berhasil dimuat dalam {time.time() - t0:.2f} detik!", flush=True)

    prompt_panduan = (
        "Transkrip percakapan bimbingan Tugas Akhir Sistem Informasi ITK antara Dosen Pembimbing Pak Arif Rahman dan mahasiswa Ariel (10221074). "
        "Topik: Rancang bangun sistem informasi manajemen operasional Bimbel Artha Balikpapan multicabang. "
        "Istilah: PxP, Personal Extreme Programming, Bab 1, Bab 2, Bab 3, sempro, seminar proposal, revisi, jurnal, penelitian terdahulu, "
        "kuota rombel, kelompok belajar, kasir cabang, rekonsiliasi kas bank, mutasi rekening, kuitansi digital, UAT, black box testing, "
        "delapan cabang, buku besar, Bu Ayu, Pak Arif."
    )

    print("\n[2/3] Memulai proses transkripsi penuh...", flush=True)
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
            condition_on_previous_text=False,
            repetition_penalty=1.2,
            no_repeat_ngram_size=3,
            beam_size=1
        )

        print(f"Bahasa terdeteksi: {info.language} (probabilitas: {info.language_probability:.2f})", flush=True)
        print(f"Total durasi audio: {info.duration:.2f} detik ({info.duration / 60:.2f} menit)", flush=True)
        print("Sedang menulis segmen transkrip ke file secara real-time...\n", flush=True)

        last_report_sec = 0.0

        for seg in segments:
            text = seg.text.strip()
            if not text:
                continue

            total_segments += 1
            start_str = format_timestamp(seg.start)
            end_str = format_timestamp(seg.end)

            ts_line = f"[{start_str} - {end_str}] {text}\n"
            plain_line = f"{text}\n"

            ts_file.write(ts_line)
            plain_file.write(plain_line)
            ts_file.flush()
            plain_file.flush()

            # Laporan progres setiap 60 detik audio atau kelipatan segmen
            if seg.end - last_report_sec >= 60.0 or total_segments % 25 == 0:
                last_report_sec = seg.end
                pct = (seg.end / info.duration) * 100 if info.duration > 0 else 0
                now_str = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"[{now_str}] Progres: {seg.end/60:.1f}/{info.duration/60:.1f} m ({pct:.1f}%) | Segmen #{total_segments:04d}: [{start_str} - {end_str}] {text[:60]}...", flush=True)

    finally:
        ts_file.close()
        plain_file.close()

    elapsed = time.time() - t_start
    print("\n" + "=" * 70, flush=True)
    print(f"[3/3] TRANSKRIPSI SELESAI dalam waktu {elapsed/60:.2f} menit ({elapsed:.1f} detik)!", flush=True)
    print(f"Total Segmen: {total_segments}", flush=True)
    print(f"File Hasil Disimpan di:", flush=True)
    print(f"1. {OUTPUT_WITH_TS} ({os.path.getsize(OUTPUT_WITH_TS):,} bytes)", flush=True)
    print(f"2. {OUTPUT_PLAIN} ({os.path.getsize(OUTPUT_PLAIN):,} bytes)", flush=True)
    print("=" * 70, flush=True)

if __name__ == "__main__":
    main()

