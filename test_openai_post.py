import httpx

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": "Bearer DUMMY_API_KEY",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": "Analyze the sentiment of the text and classify it strictly as GOOD, BAD, or NEUTRAL."
        },
        {
            "role": "user",
            "content": "W AYIBnzx pOj1tFbdc 3 QO QIOyLqS u fgdq1lz6r0PUiJ"
        }
    ]
}

try:
    response = httpx.post(url, json=data, headers=headers)
    response.raise_for_status()
    print(response.json())

except Exception as e:
    print("Request failed:", e)
