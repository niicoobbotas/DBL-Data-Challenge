from textblob import TextBlob

# Example text input
text = input("Enter a sentence for sentiment analysis: ")

# Create TextBlob object
blob = TextBlob(text)

# Sentiment result
sentiment = blob.sentiment

# Output
print(f"\nText: {text}")
print(f"Polarity ([-1, 1]): {sentiment.polarity}")
print(f"Subjectivity ([0, 1]): {sentiment.subjectivity}")

# Optional: interpret the sentiment
if sentiment.polarity > 0:
    print("Overall Sentiment: Positive 😊")
elif sentiment.polarity < 0:
    print("Overall Sentiment: Negative 😞")
else:
    print("Overall Sentiment: Neutral 😐")
