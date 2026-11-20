import os
import time
import torch
import whisper

FFMPEG_DIR = r"C:\Users\ARIEL\AppData\Roaming\Python\Python313\site-packages\imageio_ffmpeg\binaries"
if os.path.exists(FFMPEG_DIR) and FFMPEG_DIR not in os.environ.get("PATH", ""):
    os.environ["PATH"] = FFMPEG_DIR + ";" + os.environ.get("PATH", "")

AUDIO_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU\REKAMAN AUDIO (M4A)\BIMBINGAN KEDUA (BU AYU).m4a"

num_threads = os.cpu_count() or 8
torch.set_num_threads(num_threads)
print(f"CPU threads set to: {num_threads}")

# Load 30s of audio
audio = whisper.load_audio(AUDIO_PATH)
audio_30s = audio[: 30 * 16000]

print("Loading large-v3-turbo...")
t0 = time.time()
model = whisper.load_model("large-v3-turbo")
t1 = time.time()
print(f"Model loaded in {t1 - t0:.2f}s")

print("Transcribing 30s audio...")
t2 = time.time()
res = model.transcribe(
    audio_30s,
    language="id",
    initial_prompt="Transkrip bimbingan Tugas Akhir Sistem Informasi ITK antara Bu Ayu dan Ariel. Topik: Sistem Informasi Bimbel Artha Balikpapan.",
    temperature=0.0
)
t3 = time.time()
elapsed = t3 - t2
print(f"30s audio transcribed in {elapsed:.2f}s (Speed: {30 / elapsed:.2f}x real-time)")
print("Text sample:", res.get("text", "")[:200])
