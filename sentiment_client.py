import httpx
import os

OPENAI_URL = "https://api.openai.com/v1/chat/completions"

def analyze_sentiment(text: str):
    api_key = os.getenv("OPENAI_API_KEY", "DUMMY_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "Analyze the sentiment of the text and classify strictly as GOOD, BAD, or NEUTRAL."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    }

    response = httpx.post(OPENAI_URL, json=payload, headers=headers)
    response.raise_for_status()

    return response.json()
