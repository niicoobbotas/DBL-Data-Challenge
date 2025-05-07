import os
import json

# === Set your input and output folders ===
input_folder = r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Quartile 4\DBL Data Challenge\Dataset"
output_folder = r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Quartile 4\DBL Data Challenge\JSON Arrays Raw Dataset"

os.makedirs(output_folder, exist_ok=True)

files = [f for f in os.listdir(input_folder) if f.endswith('.json')]

print(f"🔄 Converting {len(files)} files...")

for i, filename in enumerate(files):
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)  # same name, different folder

    try:
        tweets = []
        with open(input_path, 'r', encoding='utf-8') as infile:
            for line in infile:
                try:
                    tweet = json.loads(line)
                    tweets.append(tweet)
                except json.JSONDecodeError:
                    continue

        # Save as JSON array
        with open(output_path, 'w', encoding='utf-8') as outfile:
            json.dump(tweets, outfile, ensure_ascii=False, indent=2)

        if (i + 1) % 10 == 0 or i == len(files) - 1:
            print(f"✅ Converted {i + 1}/{len(files)} files")

    except Exception as e:
        print(f"⚠️ Error in {filename}: {e}")

print("\n🎉 All files converted to JSON arrays!")
