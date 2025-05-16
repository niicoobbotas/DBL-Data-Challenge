import os
import json
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from tqdm import tqdm

# === Load model ===

model_name = "cardiffnlp/twitter-xlm-roberta-base-sentiment"

# Force use of the slow tokenizer to avoid tiktoken/sentencepiece errors
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


# === Define input and output ===
input_path = r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Quartile 4\DBL Data Challenge\Complete Dataset\Cleaned Dataset\cleaned_airlines-1583859446632.json"
output_folder = r"C:\Users\20243314\OneDrive - TU Eindhoven\Desktop\Quartile 4\DBL Data Challenge\Presentation 2\Output Folder for Pruebas with xtr-roberta cardiff NLP"
output_filename = "airlines_with_sentiment_2.json"
output_path = os.path.join(output_folder, output_filename)

# === Create output folder if it doesn't exist ===
os.makedirs(output_folder, exist_ok=True)

# === Load data ===
with open(input_path, "r", encoding="utf-8") as file:
    tweets = json.load(file)

# === Process tweets ===
for tweet in tqdm(tweets, desc="Analyzing tweets"):
    text = tweet.get("text", "")
    if not text.strip():
        tweet["sentiment_label"] = None
        tweet["sentiment_score"] = None
        continue

    try:
        result = classifier(text)[0]
        tweet["sentiment_label"] = result["label"]
        tweet["sentiment_score"] = round(result["score"], 4)
    except Exception:
        tweet["sentiment_label"] = "ERROR"
        tweet["sentiment_score"] = 0.0

# === Save enriched tweets to output folder ===
with open(output_path, "w", encoding="utf-8") as file:
    json.dump(tweets, file, indent=2, ensure_ascii=False)

print(f"✅ Enriched tweets saved to: {output_path}")
