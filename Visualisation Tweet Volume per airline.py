import os
import json
from collections import defaultdict
import matplotlib.pyplot as plt

airline_usernames = {
    "klm", "airfrance", "british_airways", "americanair", "lufthansa",
    "airberlin", "easyjet", "ryanair", "singaporeair",
    "qantas", "etihadairways", "virginatlantic"
}

folder_path = r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Quartile 4\DBL Data Challenge\Cleaned Dataset"


airline_counts = defaultdict(int)

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                tweets = json.load(f)
                for tweet in tweets:
                    mentions = tweet.get("entities", {}).get("user_mentions", [])
                    for mention in mentions:
                        screen_name = mention.get("screen_name", "").lower()
                        if screen_name in airline_usernames:
                            airline_counts[screen_name] += 1
            except Exception as e:
                print(f"Skipping file {filename}: {e}")


sorted_airlines = sorted(airline_counts.items(), key=lambda x: x[1], reverse=True)
labels = [a[0] for a in sorted_airlines]
counts = [a[1] for a in sorted_airlines]

plt.figure(figsize=(10, 6))
colors = ['orange' if name == 'lufthansa' else '#4169e1' for name in labels]
plt.bar(labels, counts, color=colors, edgecolor='black')


plt.title("Tweet Volume per Airline ")
plt.xlabel("Airline")
plt.ylabel("Number of Mentions")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.2)
plt.tight_layout()
plt.show()
