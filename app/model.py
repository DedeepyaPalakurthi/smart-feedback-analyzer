from textblob import TextBlob

def get_sentiment(text: str):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    label = (
        "positive" if polarity > 0 
        else "negative" if polarity < 0 
        else "neutral"
    )
    return {
        "sentiment": label,
        "confidence": round(abs(polarity), 2)
    }
