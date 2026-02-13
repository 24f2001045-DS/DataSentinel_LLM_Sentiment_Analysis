from fastapi import FastAPI
from sentiment_client import analyze_sentiment

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DataSentinel Sentiment API running"}

@app.get("/test")
def test_sentiment():
    text = "W AYIBnzx pOj1tFbdc 3 QO QIOyLqS u fgdq1lz6r0PUiJ"
    result = analyze_sentiment(text)
    return result
