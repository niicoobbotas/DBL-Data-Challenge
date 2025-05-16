import json
import random

# Replace with your actual file path
file_path = r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Quartile 4\DBL Data Challenge\Complete Dataset\Cleaned Dataset\cleaned_airlines-1583859446632.json"

# Load the JSON array
with open(file_path, 'r', encoding='utf-8') as f:
    tweets = json.load(f)

# Shuffle and sample 100 tweets
random.shuffle(tweets)
sampled = tweets[:100]

# Extract the 'text' field
texts = [tweet['text'] for tweet in sampled]

# Split into 4 groups of 25
groups = [texts[i:i+45] for i in range(0, 100, 45)]

# Save each group to its own file
for i, group in enumerate(groups, start=1):
    filename = f"group{i}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        for line in group:
            f.write(line.strip().replace("\n", " ") + "\n")  # Avoid newlines in tweets
    print(f"Saved: {filename}")
