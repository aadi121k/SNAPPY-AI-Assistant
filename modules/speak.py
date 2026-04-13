from gtts import gTTS
from playsound import playsound
import uuid
import os
import time

def speak(text):
    try:
        filename = f"voice_{uuid.uuid4()}.mp3"

        tts = gTTS(text=text, lang='en')
        tts.save(filename)

        playsound(filename)

        time.sleep(0.5)
        os.remove(filename)

    except:
        pass
