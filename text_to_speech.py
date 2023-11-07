from gtts import gTTS
from langdetect import detect
from io import BytesIO


def text_to_speech(text):
    detected_language = detect(text)
    speech = gTTS(text=text, lang=detected_language, slow=False)
    mp3_fp = BytesIO()
    speech.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp
