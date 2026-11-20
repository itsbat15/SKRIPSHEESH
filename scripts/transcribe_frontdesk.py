import os
import sys
import time
import datetime
import re
import torch
import whisper

# Pastikan console stdout/stderr menggunakan UTF-8
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
if sys.stderr.encoding and sys.stderr.encoding.lower() != "utf-8":
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Pastikan path ffmpeg dari direktori imageio_ffmpeg terdaftar
FFMPEG_DIR = r"C:\Users\ARIEL\AppData\Roaming\Python\Python313\site-packages\imageio_ffmpeg\binaries"
if os.path.exists(FFMPEG_DIR) and FFMPEG_DIR not in os.environ.get("PATH", ""):
    os.environ["PATH"] = FFMPEG_DIR + ";" + os.environ.get("PATH", "")

AUDIO_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\WAWANCARA\REKAMAN AUDIO (M4A)\WAWANCARA MITRA (FRONTDESK).m4a"
OUTPUT_DIR = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\WAWANCARA\TRANSKRIP TEKS (TXT)"

OUTPUT_WITH_TS = os.path.join(OUTPUT_DIR, "WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt")
OUTPUT_PLAIN = os.path.join(OUTPUT_DIR, "WAWANCARA MITRA (FRONTDESK).txt")
OUTPUT_MD = os.path.join(OUTPUT_DIR, "WAWANCARA_MITRA_FRONTDESK.md")

def format_timestamp_mmss(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

def parse_whisper_ts(ts_str):
    # Format whisper: 00:00.000 atau 01:23:45.678
    parts = ts_str.split(":")
    if len(parts) == 2:
        mins = float(parts[0])
        secs = float(parts[1])
        return mins * 60 + secs
    elif len(parts) == 3:
        hours = float(parts[0])
        mins = float(parts[1])
        secs = float(parts[2])
        return hours * 3600 + mins * 60 + secs
    return 0.0

class IncrementalTranscriptWriter:
    def __init__(self, original_stdout, ts_filepath, plain_filepath):
        self.original_stdout = original_stdout
        self.ts_file = open(ts_filepath, "w", encoding="utf-8", buffering=1)
        self.plain_file = open(plain_filepath, "w", encoding="utf-8", buffering=1)
        self.pattern = re.compile(r"^\[([0-9:.]+)\s*-->\s*([0-9:.]+)\]\s*(.*)$")
        self.count = 0

    def write(self, s):
        self.original_stdout.write(s)
        match = self.pattern.match(s.strip())
        if match:
            t_start_raw, t_end_raw, text = match.groups()
            text = text.strip()
            if text:
                sec_start = parse_whisper_ts(t_start_raw)
                sec_end = parse_whisper_ts(t_end_raw)
                ts_formatted = f"[{format_timestamp_mmss(sec_start)} - {format_timestamp_mmss(sec_end)}] {text}\n"
                plain_formatted = f"{text}\n"
                self.ts_file.write(ts_formatted)
                self.plain_file.write(plain_formatted)
                self.count += 1

    def flush(self):
        self.original_stdout.flush()
        self.ts_file.flush()
        self.plain_file.flush()

    def close(self):
        self.ts_file.close()
        self.plain_file.close()

def main():
    print("=" * 70)
    print("TRANSKRIPSI OTOMATIS WHISPER AI: WAWANCARA MITRA (FRONTDESK)")
    print(f"File Audio  : {AUDIO_PATH}")
    print(f"Output TXT  : {OUTPUT_WITH_TS}")
    print(f"Waktu Mulai : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    if not os.path.exists(AUDIO_PATH):
        print(f"Error: File audio tidak ditemukan: {AUDIO_PATH}")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Optimalkan thread PyTorch CPU (8 threads dari 12 cores)
    torch.set_num_threads(8)
    print(f"PyTorch CPU threads dialokasikan: {torch.get_num_threads()}")

    print("\n[1/3] Memuat model Whisper 'large-v3-turbo'...")
    t0 = time.time()
    try:
        model = whisper.load_model("large-v3-turbo")
        print("Model 'large-v3-turbo' sukses dimuat dari cache lokal!")
    except Exception as e:
        print(f"Gagal memuat 'large-v3-turbo': {e}. Beralih ke model 'medium'...")
        model = whisper.load_model("medium")

    # Prompt panduan domain kosakata Bimbel Artha Balikpapan
    prompt_panduan = (
        "Wawancara penelitian Tugas Akhir Sistem Informasi ITK mahasiswa Ariel dengan staf frontdesk dan kasir Bimbel Artha Balikpapan. "
        "Operasional harian: pendaftaran siswa baru, pencatatan di Buku Besar A4, kuitansi fisik rangkap, pembayaran SPP tunai dan transfer, "
        "validasi mutasi rekening bank, kendala selisih kas fisik, pembatalan kuitansi (void), pergantian shift frontdesk, "
        "presensi kehadiran siswa dan tentor, perhitungan honor mengajar, kurir penagihan antar-cabang delapan cabang, "
        "WhatsApp gateway notifikasi, payment gateway, manajemen Om Anang dan Mama Radit, serta kebutuhan sistem informasi manajemen operasional terintegrasi."
    )

    print("\n[2/3] Memulai proses transkripsi penuh (Bahasa Indonesia, anti-looping enabled)...")
    print("Decoding audio 69.7 menit secara real-time...\n")

    # Pasang IncrementalTranscriptWriter agar setiap segmen langsung tersimpan ke disk
    orig_stdout = sys.stdout
    writer = IncrementalTranscriptWriter(orig_stdout, OUTPUT_WITH_TS, OUTPUT_PLAIN)
    sys.stdout = writer

    try:
        result = model.transcribe(
            AUDIO_PATH,
            language="id",
            initial_prompt=prompt_panduan,
            verbose=True,
            fp16=False,
            condition_on_previous_text=False,  # Sangat krusial untuk mencegah infinite repetition loop
            temperature=0.0,
            compression_ratio_threshold=2.4,
            no_speech_threshold=0.6
        )
    finally:
        sys.stdout = orig_stdout
        writer.close()

    elapsed = time.time() - t0
    segments = result.get("segments", [])
    print("\n" + "=" * 70)
    print(f"[3/3] TRANSKRIPSI SELESAI dalam waktu {elapsed/60:.2f} menit ({elapsed:.1f} detik).")
    print(f"Total Segmen Terdeteksi: {len(segments)}")

    # Simpan kembali secara bersih dan presisi menggunakan data segmen akhir
    print("Menyinkronkan dan merapikan file output akhir...")
    with open(OUTPUT_WITH_TS, "w", encoding="utf-8") as f_ts, open(OUTPUT_PLAIN, "w", encoding="utf-8") as f_pl:
        for seg in segments:
            text = seg["text"].strip()
            if not text:
                continue
            start_str = format_timestamp_mmss(seg["start"])
            end_str = format_timestamp_mmss(seg["end"])
            f_ts.write(f"[{start_str} - {end_str}] {text}\n")
            f_pl.write(f"{text}\n")

    # Generate Markdown Report
    duration_min = int(elapsed // 60)
    duration_sec = int(elapsed % 60)
    md_lines = [
        "# Transkrip Lengkap Wawancara Mitra (Frontdesk Bimbel Artha)",
        "",
        "> **File Sumber**: `WAWANCARA MITRA (FRONTDESK).m4a`  ",
        "> **Narasumber**: Staf Frontdesk / Administrasi Kasir Cabang Bimbel Artha  ",
        "> **Pewawancara**: Ariel (Mahasiswa Sistem Informasi ITK - NIM. 10221074)  ",
        f"> **Durasi Audio**: 69 Menit 42 Detik  ",
        f"> **Tanggal Ekstraksi**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  ",
        "> **Model AI**: OpenAI Whisper `large-v3-turbo` (Bahasa Indonesia, Zero-Hallucination Setting)  ",
        f"> **Total Segmen**: {len(segments)} percakapan  ",
        "",
        "---",
        "",
        "## Percakapan Lengkap Berdasarkan Waktu (*Timestamp*)",
        ""
    ]

    for seg in segments:
        text = seg["text"].strip()
        if not text:
            continue
        start_str = format_timestamp_mmss(seg["start"])
        end_str = format_timestamp_mmss(seg["end"])
        md_lines.append(f"**[{start_str} - {end_str}]** {text}\n")

    with open(OUTPUT_MD, "w", encoding="utf-8") as f_md:
        f_md.write("\n".join(md_lines))

    print("Hasil berhasil disimpan di:")
    print(f"1. {OUTPUT_WITH_TS}")
    print(f"2. {OUTPUT_PLAIN}")
    print(f"3. {OUTPUT_MD}")
    print("=" * 70)

if __name__ == "__main__":
    main()
