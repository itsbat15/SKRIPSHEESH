import os
import time
from faster_whisper import WhisperModel

FFMPEG_DIR = r"C:\Users\ARIEL\AppData\Roaming\Python\Python313\site-packages\imageio_ffmpeg\binaries"
if os.path.exists(FFMPEG_DIR) and FFMPEG_DIR not in os.environ.get("PATH", ""):
    os.environ["PATH"] = FFMPEG_DIR + ";" + os.environ.get("PATH", "")

AUDIO_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU\REKAMAN AUDIO (M4A)\BIMBINGAN KEDUA (BU AYU).m4a"

print("Loading faster-whisper large-v3-turbo (cpu, int8)...")
t0 = time.time()
model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8", cpu_threads=12)
t1 = time.time()
print(f"Model loaded in {t1 - t0:.2f}s")

# Test on first 120 seconds of audio
print("Transcribing first 120 seconds with VAD filter...")
t2 = time.time()
segments, info = model.transcribe(
    AUDIO_PATH,
    language="id",
    vad_filter=True,
    vad_parameters=dict(min_silence_duration_ms=500),
    initial_prompt="Transkrip bimbingan Tugas Akhir Sistem Informasi ITK antara dosen Bu Ayu dan mahasiswa Ariel. Membahas sistem informasi manajemen Bimbel Artha Balikpapan multicabang, PxP, metode, bab 1, latar belakang.",
    temperature=0.0
)

count = 0
for seg in segments:
    print(f"  [{seg.start:.2f} - {seg.end:.2f}] {seg.text.strip()}")
    count += 1
    if seg.end >= 120:
        break

t3 = time.time()
print(f"Transcribed up to {seg.end:.1f}s in {t3 - t2:.2f}s! Total segments: {count}")
