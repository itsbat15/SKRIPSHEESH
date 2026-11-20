import os
import whisper

FFMPEG_DIR = r"C:\Users\ARIEL\AppData\Roaming\Python\Python313\site-packages\imageio_ffmpeg\binaries"
if os.path.exists(FFMPEG_DIR) and FFMPEG_DIR not in os.environ.get("PATH", ""):
    os.environ["PATH"] = FFMPEG_DIR + ";" + os.environ.get("PATH", "")

AUDIO_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU\REKAMAN AUDIO (M4A)\BIMBINGAN KEDUA (BU AYU).m4a"

audio = whisper.load_audio(AUDIO_PATH)
duration_sec = len(audio) / 16000
print(f"Duration: {duration_sec:.2f} seconds ({duration_sec / 60:.2f} minutes / {duration_sec / 3600:.2f} hours)")
