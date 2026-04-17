from textblob import TextBlob

def get_sentiment(text):
    return round(TextBlob(str(text)).sentiment.polarity, 2)

def apply_sentiment(df):
    df["Sentiment"] = df["Feedback"].apply(get_sentiment)
    return df