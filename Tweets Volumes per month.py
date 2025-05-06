import os
import json
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

folder_path = r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Quartile 4\DBL Data Challenge\Cleaned Dataset"

# Count tweets per month
tweet_counts_by_month = defaultdict(int)

# Loop through all JSON files
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                tweets = json.load(f)
                for tweet in tweets:
                    created_at = tweet.get('created_at')
                    if created_at:
                        dt = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
                        key = dt.strftime('%Y-%m')
                        tweet_counts_by_month[key] += 1
            except Exception as e:
                print(f"Skipping file {filename} due to error: {e}")

# Sort by time
sorted_months = sorted(tweet_counts_by_month)
counts = [tweet_counts_by_month[m] for m in sorted_months]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(sorted_months, counts, marker='o', linestyle='-', color='steelblue')
plt.title("Monthly Tweet Volume")
plt.xlabel("Month")
plt.ylabel("Number of Tweets")
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
