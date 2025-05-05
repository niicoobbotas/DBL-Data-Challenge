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
                        for line in f:
                            line = line.strip()
                            if line:  # avoid counting empty lines
                                try:
                                    json.loads(line)
                                    total_tweets += 1
                                except json.JSONDecodeError:
                                    print(f"Invalid JSON line in {file_path}")
                except Exception as e:
                    print(f"Failed to open or read file {file_path}: {e}")
    return total_tweets

folder = r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Quartile 4\DBL Data Challenge\Dataset"
print(f"Total tweets: {count_tweets(folder)}")
