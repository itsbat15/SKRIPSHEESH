import os
import sys
import time
import datetime
import whisper

# Pastikan path ffmpeg dikenali dari direktori imageio_ffmpeg
FFMPEG_DIR = r"C:\Users\ARIEL\AppData\Roaming\Python\Python313\site-packages\imageio_ffmpeg\binaries"
if os.path.exists(FFMPEG_DIR) and FFMPEG_DIR not in os.environ.get("PATH", ""):
    os.environ["PATH"] = FFMPEG_DIR + ";" + os.environ.get("PATH", "")

AUDIO_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU\BIMBINGAN KE-1 (Bu Ayu).m4a"
OUTPUT_DIR = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU"
OUTPUT_WITH_TS = os.path.join(OUTPUT_DIR, "BIMBINGAN KE-1 (Bu Ayu)_WITH_TIMESTAMPS.txt")
OUTPUT_PLAIN = os.path.join(OUTPUT_DIR, "BIMBINGAN KE-1 (Bu Ayu).txt")
OUTPUT_MD = os.path.join(OUTPUT_DIR, "BIMBINGAN_KE_1_BU_AYU.md")

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hours > 0:
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
    return f"{mins:02d}:{secs:02d}"

def main():
    print("=" * 60)
    print("TRANSKRIPSI WHISPER AI - BIMBINGAN KE-1 (BU AYU)")
    print(f"File Audio: {AUDIO_PATH}")
    print(f"Waktu Mulai: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    if not os.path.exists(AUDIO_PATH):
        print(f"Error: File audio tidak ditemukan di: {AUDIO_PATH}")
        sys.exit(1)

    print("\n[1/3] Memuat model Whisper 'large-v3-turbo'...")
    start_time = time.time()
    try:
        model = whisper.load_model("large-v3-turbo")
        print("Model 'large-v3-turbo' berhasil dimuat!")
    except Exception as e:
        print(f"Gagal memuat 'large-v3-turbo': {e}. Beralih ke 'medium'...")
        model = whisper.load_model("medium")

    # Prompt panduan kosakata agar istilah teknis, nama orang, dan bahasa Inggris tertangkap akurat
    prompt_panduan = (
        "Transkrip bimbingan Tugas Akhir Sistem Informasi ITK antara dosen pembimbing Bu Ayu dan mahasiswa Ariel. "
        "Topik: Rancang bangun sistem informasi manajemen operasional Bimbel Artha Balikpapan multicabang. "
        "Istilah: PxP, Personal Extreme Programming, website, dashboard, prototype, proyek, database, user story, "
        "Next.js, Laravel, RESTful API, tentor, admin cabang, super admin, kasir, SPP, WhatsApp, mutasi bank, "
        "rekonsiliasi, overcapacity, requirements, iterative, planning."
    )

    print("\n[2/3] Memulai proses transkripsi audio penuh (Bahasa Indonesia & istilah Inggris)...")
    print("Proses decoding sedang berlangsung per segmen...")
    
    # Buka file output secara incremental agar tersimpan real-time
    ts_file = open(OUTPUT_WITH_TS, "w", encoding="utf-8", buffering=1)
    plain_file = open(OUTPUT_PLAIN, "w", encoding="utf-8", buffering=1)

    segments_all = []

    try:
        result = model.transcribe(
            AUDIO_PATH,
            language="id",
            initial_prompt=prompt_panduan,
            verbose=True,
            fp16=False,
            condition_on_previous_text=True,
            temperature=0.0
        )
        
        segments = result.get("segments", [])
        for seg in segments:
            start_str = format_timestamp(seg["start"])
            end_str = format_timestamp(seg["end"])
            text = seg["text"].strip()
            
            ts_line = f"[{start_str} - {end_str}] {text}\n"
            plain_line = f"{text}\n"
            
            ts_file.write(ts_line)
            plain_file.write(plain_line)
            segments_all.append(seg)
            
    finally:
        ts_file.close()
        plain_file.close()

    elapsed = time.time() - start_time
    print("\n" + "=" * 60)
    print(f"[3/3] Transkripsi SELESAI dalam waktu {elapsed/60:.2f} menit ({elapsed:.1f} detik).")
    print(f"Total Segmen: {len(segments_all)}")
    print(f"Hasil disimpan di:")
    print(f" - {OUTPUT_WITH_TS}")
    print(f" - {OUTPUT_PLAIN}")

    # Buat ringkasan versi Markdown yang rapi
    md_lines = [
        "# 🎙️ Transkrip Lengkap Bimbingan Ke-1 (Bu Ayu)",
        "",
        f"- **File Sumber**: `BIMBINGAN KE-1 (Bu Ayu).m4a`",
        f"- **Dosen Pembimbing**: Bu Sri Rahayu Natasia, S.Kom., M.Si., M.Sc. (Bu Ayu)",
        f"- **Mahasiswa**: Ariel",
        f"- **Tanggal Transkripsi**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- **Model AI**: Whisper `large-v3-turbo` (Full High-Resolution Extraction)",
        f"- **Total Segmen**: {len(segments_all)}",
        "",
        "---",
        "",
        "## 📝 Percakapan Lengkap Berdasarkan Waktu (*Timestamp*)",
        ""
    ]
    for seg in segments_all:
        start_str = format_timestamp(seg["start"])
        end_str = format_timestamp(seg["end"])
        text = seg["text"].strip()
        md_lines.append(f"**[{start_str} - {end_str}]** {text}\n")

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f" - {OUTPUT_MD}")
    print("=" * 60)

if __name__ == "__main__":
    main()
