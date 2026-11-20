"""
transcribe_pak_arif_3_and_4.py
==============================
Ekstraksi transkripsi otomatis audio rekaman bimbingan Pak Arif:
1. Bimbingan Ke 3 (Pak Arif).m4a (durasi ~25.4 menit)
2. BIMBINGAN KE-4 (Pak Arif).m4a (durasi ~31.6 menit)

Menggunakan faster-whisper large-v3-turbo (int8, CPU multi-threading).
Anti-halusinasi: condition_on_previous_text=False, repetition_penalty=1.2, no_repeat_ngram_size=3, beam_size=1.
Output disimpan secara streaming (real-time flush) ke:
- BIMBINGAN KE 3 (PAK ARIF)_WITH_TIMESTAMPS.txt & BIMBINGAN KE 3 (PAK ARIF).txt
- BIMBINGAN KE 4 (PAK ARIF)_WITH_TIMESTAMPS.txt & BIMBINGAN KE 4 (PAK ARIF).txt
di folder: c:\\Users\\ARIEL\\OneDrive - MSFT\\Documents\\ARTHA\\BIMBINGAN\\PAK ARIF\\TRANSKRIP TEKS (TXT)\\
"""

import os
import sys
import time
import datetime
from faster_whisper import WhisperModel

FFMPEG_DIR = r"C:\Users\ARIEL\AppData\Roaming\Python\Python313\site-packages\imageio_ffmpeg\binaries"
if os.path.exists(FFMPEG_DIR) and FFMPEG_DIR not in os.environ.get("PATH", ""):
    os.environ["PATH"] = FFMPEG_DIR + ";" + os.environ.get("PATH", "")

AUDIO_DIR = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\PAK ARIF\REKAMAN AUDIO (M4A)"
OUTPUT_DIR = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\PAK ARIF\TRANSKRIP TEKS (TXT)"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hours > 0:
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"

TASKS = [
    {
        "audio_name": "Bimbingan Ke 3 (Pak Arif).m4a",
        "out_ts": "BIMBINGAN KE 3 (PAK ARIF)_WITH_TIMESTAMPS.txt",
        "out_plain": "BIMBINGAN KE 3 (PAK ARIF).txt",
        "label": "BIMBINGAN KE-3 PAK ARIF"
    },
    {
        "audio_name": "BIMBINGAN KE-4 (Pak Arif).m4a",
        "out_ts": "BIMBINGAN KE 4 (PAK ARIF)_WITH_TIMESTAMPS.txt",
        "out_plain": "BIMBINGAN KE 4 (PAK ARIF).txt",
        "label": "BIMBINGAN KE-4 PAK ARIF"
    }
]

prompt_panduan = (
    "Transkrip percakapan bimbingan Tugas Akhir Sistem Informasi ITK antara Dosen Pembimbing Pak Arif Rahman dan mahasiswa Ariel (10221074). "
    "Topik: Rancang bangun sistem informasi manajemen operasional Bimbel Artha Balikpapan multicabang. "
    "Istilah: PxP, Personal Extreme Programming, Bab 1, Bab 2, Bab 3, sempro, seminar proposal, revisi, jurnal, penelitian terdahulu, "
    "kuota rombel, kelompok belajar, kasir cabang, rekonsiliasi kas bank, mutasi rekening, kuitansi digital, UAT, black box testing, "
    "delapan cabang, buku besar, Bu Ayu, Pak Arif, peran pengguna, aktor, use case, alur operasional."
)

def main():
    threads = os.cpu_count() or 12
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Memuat model faster-whisper 'large-v3-turbo' (threads: {threads})...", flush=True)
    t0 = time.time()
    model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=threads)
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Model siap dalam {time.time() - t0:.2f} detik.\n", flush=True)

    for item in TASKS:
        audio_path = os.path.join(AUDIO_DIR, item["audio_name"])
        out_ts_path = os.path.join(OUTPUT_DIR, item["out_ts"])
        out_plain_path = os.path.join(OUTPUT_DIR, item["out_plain"])

        print("=" * 70, flush=True)
        print(f"MEMULAI PROSES: {item['label']}", flush=True)
        print(f"File Audio  : {audio_path}", flush=True)
        print(f"Target TS   : {out_ts_path}", flush=True)
        print(f"Target Plain: {out_plain_path}", flush=True)
        print("=" * 70, flush=True)

        if not os.path.exists(audio_path):
            print(f"ERROR: Audio file tidak ditemukan: {audio_path}", flush=True)
            continue

        t_start = time.time()
        ts_f = open(out_ts_path, "w", encoding="utf-8", buffering=1)
        plain_f = open(out_plain_path, "w", encoding="utf-8", buffering=1)

        try:
            segments, info = model.transcribe(
                audio_path,
                language="id",
                vad_filter=True,
                vad_parameters=dict(min_silence_duration_ms=500),
                initial_prompt=prompt_panduan,
                condition_on_previous_text=False,
                repetition_penalty=1.2,
                no_repeat_ngram_size=3,
                beam_size=1
            )

            print(f"Durasi Audio: {info.duration / 60:.2f} menit. Mulai transkripsi...", flush=True)
            total_seg = 0
            last_log_sec = 0.0

            for seg in segments:
                text = seg.text.strip()
                if not text:
                    continue
                total_seg += 1
                s_str = format_timestamp(seg.start)
                e_str = format_timestamp(seg.end)
                ts_f.write(f"[{s_str} - {e_str}] {text}\n")
                plain_f.write(f"{text}\n")

                if seg.end - last_log_sec >= 120.0:
                    last_log_sec = seg.end
                    elapsed = time.time() - t_start
                    speed = seg.end / elapsed if elapsed > 0 else 0
                    print(f"  -> Progress: {format_timestamp(seg.end)} / {format_timestamp(info.duration)} ({speed:.2f}x speed)", flush=True)

            ts_f.flush()
            plain_f.flush()
            ts_f.close()
            plain_f.close()

            dur_total = time.time() - t_start
            print(f"SELESAI: {item['label']} dalam {dur_total / 60:.2f} menit ({total_seg} baris kalimat).\n", flush=True)

        except Exception as e:
            print(f"ERROR saat transkripsi {item['label']}: {e}", flush=True)
            if not ts_f.closed:
                ts_f.close()
            if not plain_f.closed:
                plain_f.close()

    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] SELURUH TUGAS TRANSKRIPSI SELESAI!", flush=True)

if __name__ == "__main__":
    main()

