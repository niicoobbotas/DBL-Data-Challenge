import json
import os
from tqdm import tqdm

# Dosya yollarını buraya kendine göre ayarla:
json_dir_path = "/Users/adil/Desktop/data"  # Mac örneği
output_dir_path = "/Users/adil/Desktop/datacleaned_tweets"

# Klasör yoksa oluştur
os.makedirs(output_dir_path, exist_ok=True)

# Filtrelemek istediğimiz havayolu şirketi adları
airline_keywords = [
    "KLM", "Lufthansa", "AirFrance", "British_Airways", "easyJet",
    "AmericanAir", "Delta", "United", "AlaskaAir", "SouthwestAir",
    "JetBlue", "Ryanair", "TurkishAirlines", "PegasusAirlines"
]

# Havayolu adı içeriyor mu?
def contains_airline_name(text):
    if not text:
        return False
    text_lower = text.lower()
    return any(airline.lower() in text_lower for airline in airline_keywords)

# Tweetten gerekli bilgileri çıkar
def extract_relevant_info(tweet):
    urls = tweet.get('entities', {}).get('urls', [])
    cleaned_urls = [{'url': url.get('url'), 'display_url': url.get('display_url')} for url in urls]

    return {
        'created_at': tweet.get('created_at'),
        'id': tweet.get('id'),
        'in_reply_to_status_id': tweet.get('in_reply_to_status_id'),
        'text': tweet.get('text') or tweet.get('extended_tweet', {}).get('full_text'),
        'lang': tweet.get('lang'),
        'retweet_count': tweet.get('retweet_count'),
        'favorite_count': tweet.get('favorite_count'),
        'user': {
            'id': tweet.get('user', {}).get('id'),
            'screen_name': tweet.get('user', {}).get('screen_name'),
            'name': tweet.get('user', {}).get('name'),
            'followers_count': tweet.get('user', {}).get('followers_count'),
            'friends_count': tweet.get('user', {}).get('friends_count'),
            'favourites_count': tweet.get('user', {}).get('favourites_count'),
            'statuses_count': tweet.get('user', {}).get('statuses_count'),
            'verified': tweet.get('user', {}).get('verified'),
            'location': tweet.get('user', {}).get('location'),
            'created_at': tweet.get('user', {}).get('created_at')
        },
        'entities': {
            'hashtags': tweet.get('entities', {}).get('hashtags'),
            'user_mentions': tweet.get('entities', {}).get('user_mentions'),
            'urls': cleaned_urls,
            'symbols': tweet.get('entities', {}).get('symbols'),
        }
    }

# Tüm JSON dosyaları üzerinde dön
for filename in tqdm(os.listdir(json_dir_path), desc="Dosyalar işleniyor"):
    if filename.endswith('.json'):
        json_file_path = os.path.join(json_dir_path, filename)
        output_file_path = os.path.join(output_dir_path, f"cleaned_{filename}")

        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                first_pass_tweets = []
                havayolu_tweet_ids = set()

                for line in file:
                    try:
                        tweet = json.loads(line.strip())
                        cleaned_tweet = extract_relevant_info(tweet)
                        first_pass_tweets.append(cleaned_tweet)

                        if contains_airline_name(cleaned_tweet['text']):
                            havayolu_tweet_ids.add(cleaned_tweet['id'])
                    except json.JSONDecodeError as e:
                        print(f"Skipping invalid JSON in {filename}: {e}")

            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                for tweet in first_pass_tweets:
                    if (
                        contains_airline_name(tweet['text']) or
                        tweet.get("in_reply_to_status_id") in havayolu_tweet_ids
                    ):
                        output_file.write(json.dumps(tweet, ensure_ascii=False) + '\n')

        except FileNotFoundError:
            print(f"File not found: {json_file_path}")
