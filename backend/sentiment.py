from textblob import TextBlob

def get_sentiment(text):

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    print("Text:", text)
    print("Polarity:", polarity)

    if polarity > 0.2:
        return "happy"
    elif polarity < -0.2:
        return "sad"
    else:
        return "neutral"
    
print(get_sentiment("I am very happy today"))