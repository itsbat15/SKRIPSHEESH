import os
import sys

AUDIO_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\BIMBINGAN\BU AYU\REKAMAN AUDIO (M4A)\BIMBINGAN KEDUA (BU AYU).m4a"

print(f"Audio exists: {os.path.exists(AUDIO_PATH)}")
print(f"Audio size: {os.path.getsize(AUDIO_PATH) / 1024 / 1024:.2f} MB")

# Check whisper and ffmpeg
try:
    import whisper
    print("whisper module found:", whisper.__file__)
except ImportError as e:
    print("whisper import failed:", e)

FFMPEG_DIR = r"C:\Users\ARIEL\AppData\Roaming\Python\Python313\site-packages\imageio_ffmpeg\binaries"
print(f"FFMPEG_DIR exists: {os.path.exists(FFMPEG_DIR)}")
if os.path.exists(FFMPEG_DIR):
    for f in os.listdir(FFMPEG_DIR):
        print("  Found ffmpeg binary:", f)
