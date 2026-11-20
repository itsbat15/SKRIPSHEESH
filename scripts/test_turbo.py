import os
import time
import torch
import whisper

FFMPEG_DIR = r"C:\Users\ARIEL\AppData\Roaming\Python\Python313\site-packages\imageio_ffmpeg\binaries"
if os.path.exists(FFMPEG_DIR) and FFMPEG_DIR not in os.environ.get("PATH", ""):
    os.environ["PATH"] = FFMPEG_DIR + ";" + os.environ.get("PATH", "")

AUDIO_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU\REKAMAN AUDIO (M4A)\BIMBINGAN KEDUA (BU AYU).m4a"

torch.set_num_threads(os.cpu_count() or 12)
audio = whisper.load_audio(AUDIO_PATH)
sample_audio = audio[int(30 * 16000) : int(90 * 16000)]

prompt_panduan = (
    "Transkrip percakapan bimbingan Tugas Akhir Sistem Informasi ITK antara dosen Bu Ayu dan mahasiswa Ariel. "
    "Membahas sistem informasi manajemen Bimbel Artha Balikpapan multicabang, PxP, metode, bab 1, latar belakang."
)

m = whisper.load_model("large-v3-turbo")
t2 = time.time()
res = m.transcribe(
    sample_audio,
    language="id",
    initial_prompt=prompt_panduan,
    temperature=0.0,
    no_speech_threshold=0.6,
    logprob_threshold=-1.0,
    compression_ratio_threshold=2.4,
    condition_on_previous_text=False
)
t3 = time.time()
print(f"large-v3-turbo took {t3 - t2:.2f}s")
for seg in res.get("segments", [])[:6]:
    print(f"  [{seg['start']:.1f} - {seg['end']:.1f}] {seg['text'].strip()}")
