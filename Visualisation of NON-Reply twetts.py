import os
import json
import matplotlib.pyplot as plt

# Folder path
folder_path = r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Quartile 4\DBL Data Challenge\Cleaned Dataset"

# Airline accounts
airline_usernames = {
    'klm', 'airfrance', 'british_airways', 'americanair', 'lufthansa',
    'airberlin', 'airberlin assist', 'easyjet', 'ryanair',
    'singaporeair', 'qantas', 'etihadairways', 'virginatlantic'
}

# Tracking
tweet_ids = set()
replied_to_ids = set()
verified_airline_reply_count = 0
total_tweet_count = 0

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
            try:
                tweets = json.load(f)
                for tweet in tweets:
                    total_tweet_count += 1
                    tweet_id = tweet.get('id')
                    in_reply_to = tweet.get('in_reply_to_status_id')
                    user = tweet.get('user', {})
                    screen_name = user.get('screen_name', '').lower()
                    is_verified = user.get('verified', False)

                    if tweet_id is not None:
                        if in_reply_to is None:
                            tweet_ids.add(tweet_id)
                        else:
                            replied_to_ids.add(in_reply_to)
                            if screen_name in airline_usernames and is_verified:
                                verified_airline_reply_count += 1
            except Exception as e:
                print(f"Error loading {filename}: {e}")

# Reply stats
replied_to_count = sum(1 for tweet_id in tweet_ids if tweet_id in replied_to_ids)
not_replied_to_count = len(tweet_ids) - replied_to_count

# Chart values and sorting
data = {
    'No Replies': not_replied_to_count,
    'Got Replies': replied_to_count,
    'Verified Airline Replies': verified_airline_reply_count
}

# Sort by value descending
sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
labels = [item[0] for item in sorted_items]
counts = [item[1] for item in sorted_items]
colors = ['orange', '#4169e1', 'green'] 

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(labels, counts, color=colors)

# Annotations
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:,}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom')

ax.set_title('Tweet Reply Status')
ax.set_ylabel('Number of Tweets(per million)')
ax.yaxis.grid(True, linestyle='--', alpha=0.2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
