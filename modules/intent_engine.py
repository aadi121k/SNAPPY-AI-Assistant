import json

def detect_intent(command):
    with open("intents.json") as file:
        data = json.load(file)

    command = command.lower()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern in command:
                return intent["tag"]

    return None
