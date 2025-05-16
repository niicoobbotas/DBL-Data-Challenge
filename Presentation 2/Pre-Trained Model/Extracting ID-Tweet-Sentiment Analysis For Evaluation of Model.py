import json

# Load the full JSON array of tweets
with open(r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Quartile 4\DBL Data Challenge\Presentation 2\Output Folder for Pruebas with xtr-roberta cardiff NLP\airlines_with_sentiment_2.json", "r", encoding="utf-8") as f:
    tweets = json.load(f)

# Extract relevant fields from each tweet
filtered_tweets = []
for tweet in tweets:
    filtered = {
        "id": tweet.get("id"),
        "tweet": tweet.get("text"),
        "sentiment_label": tweet.get("sentiment_label"),
        "sentiment_score": tweet.get("sentiment_score")
    }
    filtered_tweets.append(filtered)

# Save the filtered result into a new JSON file
with open("extracted_necessaryinfo.json", "w", encoding="utf-8") as f:
    json.dump(filtered_tweets, f, indent=2, ensure_ascii=False)

print("Filtered tweets saved to filtered_tweets.json")
