import webbrowser
import datetime
import wikipedia
import os


def open_youtube():
    webbrowser.open("https://www.youtube.com")


def open_google():
    webbrowser.open("https://www.google.com")


def tell_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M")


def wikipedia_search(query):
    try:
        query = query.lower()
        query = query.replace("who is", "")
        query = query.replace("what is", "")
        query = query.replace("tell me about", "")
        query = query.strip()

        result = wikipedia.summary(query, sentences=2)
        return result

    except:
        return "Sorry, I could not find information."


def google_search(query):
    query = query.replace("search", "")
    query = query.strip()

    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


def get_news():
    import requests

    api_key = "425e823e209a46ee98df268a8b22269b"

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    try:
        response = requests.get(url)
        news = response.json()

        if news.get("status") != "ok":
            return ["Error fetching news."]

        articles = news.get("articles", [])[:5]

        headlines = []
        for article in articles:
            if article.get("title"):
                headlines.append(article["title"])

        if not headlines:
            return ["No news found."]

        return headlines

    except:
        return ["Failed to fetch news."]


OUTPUT_DIR = "output"


def create_file(filename="file.txt"):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w") as f:
        f.write("")

    return f"File '{filename}' created successfully."


def write_code(filename="code.py"):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    code = """def retry(func, attempts=3):
    for i in range(attempts):
        try:
            return func()
        except:
            continue
    return None
"""

    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w") as f:
        f.write(code)

    return f"Code written to '{filename}'."


def summarize_text(text):
    words = text.split()
    summary = " ".join(words[:20])
    return summary
