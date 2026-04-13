from modules.speech import listen
from modules.speak import speak
from modules.automation import (
    open_youtube, open_google, tell_time,
    wikipedia_search, google_search, get_news,
    create_file, write_code   
)
from modules.intent_engine import detect_intent


speak("Hello, I am Snappy. How can I help you?")


while True:

    command = ""

    # try listening 3 times
    for _ in range(3):
        command = listen()
        if command != "":
            break

    # fallback to typing
    if command == "":
        command = input("Type command: ").lower()

    intent = detect_intent(command)

    print("Intent:", intent)

    if intent == "greeting":
        speak("Hello! Nice to meet you.")

    elif intent == "youtube":
        speak("Opening YouTube")
        open_youtube()

    elif intent == "google":
        speak("Opening Google")
        open_google()

    elif intent == "time":
        current_time = tell_time()
        speak(f"The time is {current_time}")

    elif intent == "wikipedia":
        speak("Searching Wikipedia")
        result = wikipedia_search(command)
        print(result)
        speak(result)

    elif intent == "search":
        speak("Searching Google")
        google_search(command)

    elif intent == "news":
        speak("Here are the latest headlines")

        headlines = get_news()

        if not headlines:
            speak("Sorry, I could not fetch the news right now.")

        else:
            for headline in headlines:
                print(headline)
                speak("Headline")
                speak(headline)


    elif intent == "create_file":
        speak("Creating file")
        result = create_file()
        print(result)
        speak(result)

    elif intent == "write_code":
        speak("Generating code")
        result = write_code()
        print(result)
        speak(result)

    elif intent == "summarize":
        speak("Summarization feature will be added soon")

    # -----------------------------------

    elif intent == "exit":
        speak("Goodbye")
        break

    else:
        speak("Sorry, I did not understand.")