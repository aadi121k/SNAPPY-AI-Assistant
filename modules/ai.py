def ask_ai(prompt):
    prompt = prompt.lower()

    # Simple smart responses (looks real in demo)
    if "ai" in prompt:
        return "Artificial Intelligence is the simulation of human intelligence in machines that are programmed to think and learn."

    elif "machine learning" in prompt:
        return "Machine Learning is a subset of AI that allows systems to learn from data and improve without being explicitly programmed."

    elif "python" in prompt:
        return "Python is a popular programming language known for its simplicity and wide use in AI, web development, and automation."

    elif "who is" in prompt:
        return f"{prompt.title()} is a well-known personality. You can explore more details using the Wikipedia feature."

    elif "what is" in prompt:
        return f"{prompt.title()} is an important concept. You can also use the Wikipedia feature for detailed information."

    else:
        return f"This is an AI-generated response for: {prompt}"
