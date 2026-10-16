import os
import sys
import time
import datetime
import whisper

AUDIO_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\WAWANCARA\WAWANCARA PERTAMA ARTHA.m4a"
OUTPUT_MD_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\WAWANCARA\WAWANCARA_PERTAMA_ARTHA.md"

def format_timestamp(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

def main():
    print(f"Checking audio file: {AUDIO_PATH}")
    if not os.path.exists(AUDIO_PATH):
        print("Error: Audio file not found!")
        sys.exit(1)

    print("Loading Whisper model ('medium' for high accuracy in Indonesian)...")
    start_time = time.time()
    # Try 'medium' first; fallback to 'small' if memory/time is constraint
    try:
        model = whisper.load_model("medium")
        print("Loaded 'medium' model successfully!")
    except Exception as e:
        print(f"Failed to load 'medium' model: {e}. Falling back to 'small'...")
        model = whisper.load_model("small")

    print(f"Starting transcription of 31:29 audio file in Indonesian...")
    result = model.transcribe(
        AUDIO_PATH,
        language="id",
        verbose=True,
        fp16=False
    )
    
    elapsed = time.time() - start_time
    print(f"\nTranscription completed in {elapsed:.2f} seconds.")

    segments = result.get("segments", [])
    full_text = result.get("text", "").strip()

    # Generate Markdown documentation
    md_lines = []
    md_lines.append("# Transkrip Lengkap Wawancara Pertama Bimbel Artha")
    md_lines.append("")
    md_lines.append("> **File Sumber**: `WAWANCARA PERTAMA ARTHA.m4a`  ")
    md_lines.append("> **Durasi Audio**: 31 Menit 29 Detik  ")
    md_lines.append("> **Bahasa**: Indonesia  ")
    md_lines.append(f"> **Tanggal Ekstraksi**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  ")
    md_lines.append("> **Status**: Transkrip Otomatis 100% Lengkap (Per Segmen Waktu)  ")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## 📝 Teks Transkrip Lengkap")
    md_lines.append("")

    for seg in segments:
        start_str = format_timestamp(seg["start"])
        end_str = format_timestamp(seg["end"])
        text = seg["text"].strip()
        md_lines.append(f"**[{start_str} - {end_str}]** {text}")
        md_lines.append("")

    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## 📄 Teks Keseluruhan (Full Text Continuous)")
    md_lines.append("")
    md_lines.append(full_text)
    md_lines.append("")

    with open(OUTPUT_MD_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"\nSaved complete transcript Markdown file to: {OUTPUT_MD_PATH}")

if __name__ == "__main__":
    main()
