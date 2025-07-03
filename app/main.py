from fastapi import FastAPI
from .model import get_sentiment
from .schemas import FeedbackRequest, SentimentResponse

app = FastAPI()

@app.post("/predict", response_model=SentimentResponse)
def predict_sentiment(feedback: FeedbackRequest):
    return get_sentiment(feedback.text)
