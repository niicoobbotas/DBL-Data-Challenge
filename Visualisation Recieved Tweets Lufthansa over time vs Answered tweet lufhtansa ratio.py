import os
import json
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt

# 🔁 Replace with your actual cleaned JSON dataset folder path
folder_path = r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Quartile 4\DBL Data Challenge\Cleaned Dataset"

# Initialize counters
mentions_per_month = defaultdict(int)
replies_per_month = defaultdict(int)

# Loop through each .json file
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                tweets = json.load(f)
                for tweet in tweets:
                    created_at = tweet.get('created_at')
                    if not created_at:
                        continue
                    try:
                        dt = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
                        month_key = dt.strftime('%Y-%m')
                    except ValueError:
                        continue

                    # Count tweets that mention Lufthansa
                    mentions = tweet.get("entities", {}).get("user_mentions", [])
                    for mention in mentions:
                        if mention.get("screen_name", "").lower() == "lufthansa":
                            mentions_per_month[month_key] += 1
                            break

                    # Count replies from Lufthansa
                    user_screen = tweet.get("user", {}).get("screen_name", "").lower()
                    if user_screen == "lufthansa" and tweet.get("in_reply_to_status_id"):
                        replies_per_month[month_key] += 1
            except Exception as e:
                print(f"Skipping file {filename}: {e}")


# Total replies and mentions
total_mentions = sum(mentions_per_month.values())
total_replies = sum(replies_per_month.values())

# Compute overall reply ratio
if total_mentions > 0:
    reply_ratio = total_replies / total_mentions
    print(f"Lufthansa replied to {total_replies:,} out of {total_mentions:,} mentions.")
    print(f"➡️ Overall reply ratio: {reply_ratio:.2%} (approx. 1 reply per {1/reply_ratio:.1f} mentions)")
else:
    print("No mentions of Lufthansa found.")

            
        

# Align months for consistent plotting
all_months = sorted(set(mentions_per_month.keys()).union(replies_per_month.keys()))
mention_counts = [mentions_per_month.get(m, 0) for m in all_months]
reply_counts = [replies_per_month.get(m, 0) for m in all_months]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(all_months, mention_counts, marker='o', label="Mentions of Lufthansa", color='steelblue')
plt.plot(all_months, reply_counts, marker='s', label="Replies from Lufthansa", color='darkorange')
plt.title("Monthly Lufthansa Tweet Mentions vs Replies")
plt.xlabel("Month")
plt.ylabel("Tweet Count")
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend()
plt.tight_layout()
plt.show()


