from textblob import TextBlob

def analyze_sentiment(phrase):
    analysis = TextBlob(phrase)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity

    if polarity > 0:
        sentiment_label = "Positive"
    elif polarity < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    return sentiment_label, polarity, subjectivity