import whisper

model = whisper.load_model("base")

def speech_to_text(audio_path):
    try:
        result = model.transcribe(
            audio_path,
            language="en",        # force English
            fp16=False            # important for CPU
        )
        return result["text"].strip().lower()
    except Exception as e:
        print("STT Error:", e)
        return ""
