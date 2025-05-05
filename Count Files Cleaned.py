import os
import json

def count_tweets(folder_path):
    total_tweets = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".json"):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            total_tweets += len(data)
                        elif isinstance(data, dict):
                            total_tweets += 1
                except json.JSONDecodeError:
                    print(f"Failed to decode JSON in {file_path}")
    return total_tweets

folder = r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Quartile 4\DBL Data Challenge\Cleaned Dataset"
print(f"Total tweets: {count_tweets(folder)}")
