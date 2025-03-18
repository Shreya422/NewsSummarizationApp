from textblob import TextBlob

def analyze_sentiment(text):
    """
    Performs sentiment analysis and classifies into Positive, Neutral, or Negative.
    """
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
