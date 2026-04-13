# SNAPPY: Smart NLP-powered Assistant for Personalized Productivity and Yield

### Voice-Controlled AI Assistant 🤖

---

## Overview

SNAPPY is a voice-controlled AI assistant that understands user commands through both audio and text. It detects intent and performs actions such as opening websites, fetching news, summarizing text, and generating intelligent responses.

---

## Features

* 🎤 Speech-to-Text using Whisper
* 🔊 Text-to-Speech using gTTS
* 🧠 Intent Detection using NLP (intents.json)
* 🌐 Open websites (YouTube, Google)
* 📰 Fetch latest news using API
* 📚 Wikipedia search
* 💻 File creation and code generation
* ✂️ Text summarization
* 🤖 AI fallback response system

---

## Tech Stack

* Python
* Streamlit
* Whisper (Speech Recognition)
* gTTS (Text-to-Speech)
* FFmpeg (Audio Processing)
* JSON (Intent Handling)

---

## Project Structure

SNAPPY/
│── app.py
│── intents.json
│── README.md
│── modules/
│   ├── automation.py
│   ├── intent_engine.py
│   ├── speak.py
│   ├── ai.py
│   ├── stt.py

---

## How to Run

1. Install dependencies:

```
py -m pip install -r requirements.txt
```

2. Run the application:

```
py -m streamlit run app.py
```

---

## Demo Flow

User Input (Voice/Text)
→ Speech-to-Text (Whisper)
→ Intent Detection
→ Action Execution
→ Voice + Text Output

---

## Example Commands

* "open youtube"
* "tell me news"
* "what is artificial intelligence"

---

## Author

Aditya Kumar Upadhyay
