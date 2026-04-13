# SNAPPY AI Assistant
# Developed by Aditya Kumar Upadhyay
# Original Project - Internship Submission

import streamlit as st
import os

from modules.intent_engine import detect_intent
from modules.automation import (
    open_youtube, open_google, tell_time,
    wikipedia_search, google_search, get_news,
    create_file, write_code, summarize_text
)

from modules.speak import speak
from modules.ai import ask_ai
from modules.stt import speech_to_text


if "last_response" not in st.session_state:
    st.session_state.last_response = ""


st.title("SNAPPY: Voice-Controlled AI Agent 🤖")

audio_file = st.file_uploader("Upload audio file", type=["wav", "mp3"])
text_input = st.text_input("Enter your command:")

command = ""


if audio_file is not None:
    st.info("Transcribing audio...")

    file_path = "temp_audio.wav"

    with open(file_path, "wb") as f:
        f.write(audio_file.read())

    command = speech_to_text(file_path)

    # cleanup temp file
    if os.path.exists(file_path):
        os.remove(file_path)

    if command:
        st.success(f"Transcribed: {command}")
    else:
        st.warning("Could not understand audio. Try again.")

else:
    command = text_input


if st.button("Run"):

    if not command.strip():
        st.warning("Please enter or upload input")
        st.stop()

    st.subheader("Pipeline")
    st.write("🔹 Input:", command)

    intent = detect_intent(command)
    st.write("🔹 Intent:", intent)

    try:
        if intent == "greeting":
            response = "Hello! Nice to meet you."

        elif intent == "youtube":
            open_youtube()
            response = "Opened YouTube"

        elif intent == "google":
            open_google()
            response = "Opened Google"

        elif intent == "time":
            result = tell_time()
            response = f"The time is {result}"

        elif intent == "wikipedia":
            response = wikipedia_search(command)

        elif intent == "search":
            google_search(command)
            response = "Searching Google"

        elif intent == "news":
            headlines = get_news()
            if headlines:
                response = ". ".join(headlines)
            else:
                response = "No news found."

        elif intent == "create_file":
            response = create_file()

        elif intent == "write_code":
            response = write_code()

        elif intent == "summarize":
            response = summarize_text(command)

        else:
            response = ask_ai(command)

        st.write("🔹 Output:", response)

    except Exception as e:
        response = "Something went wrong"
        st.error(response)

    if st.session_state.last_response != response:
        speak(response)
        st.session_state.last_response = response
