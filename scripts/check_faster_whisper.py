try:
    import faster_whisper
    print("faster_whisper available:", faster_whisper.__file__)
except ImportError:
    print("faster_whisper NOT available")

try:
    import ctranslate2
    print("ctranslate2 available:", ctranslate2.__file__)
except ImportError:
    print("ctranslate2 NOT available")
