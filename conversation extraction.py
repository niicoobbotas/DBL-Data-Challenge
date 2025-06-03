import json
import os
from collections import defaultdict

json_dir_path = "C:\\Users\\nicol\\OneDrive - TU Eindhoven\\Desktop\\Data Challenge\\datacleanedtweets"

output_dir_path = "C:\\Users\\nicol\\OneDrive - TU Eindhoven\\Desktop\\Data Challenge\\extracted_conversations"
os.makedirs(output_dir_path, exist_ok=True)

airline_ids = {
    56377143, 106062176, 18332190, 22536055, 124476322, 26223583,
    2182373406, 38676903, 1542862735, 253340062, 218730857, 45621423, 20626359
}

def extract_conversations(tweets):
    conversations = []
    processed_tweets = set()

    replies_index = defaultdict(list)
    for tweet in tweets:
        if tweet['in_reply_to_status_id'] is not None:
            replies_index[tweet['in_reply_to_status_id']].append(tweet)

    for tweet in tweets:
        if tweet['id'] in processed_tweets:
            continue

        if tweet['user']['id'] not in airline_ids:
            conversation = [tweet]
            processed_tweets.add(tweet['id'])

            current_tweet = tweet
            while True:
                replies = replies_index.get(current_tweet['id'], [])

                valid_replies = [
                    reply for reply in replies
                    if reply['user']['id'] in airline_ids or reply['user']['id'] == tweet['user']['id']
                ]

                if valid_replies:
                    reply = valid_replies[0]
                    conversation.append(reply)
                    processed_tweets.add(reply['id'])
                    current_tweet = reply
                else:
                    break

            airline_replies = [t for t in conversation if t['user']['id'] in airline_ids]
            if airline_replies:
                for airline_reply in airline_replies:
                    airline_index = conversation.index(airline_reply)
                    if (
                        airline_index > 0 and 
                        airline_index < len(conversation) - 1 and  
                        conversation[airline_index - 1]['user']['id'] == conversation[airline_index + 1]['user']['id'] == tweet['user']['id']
                    ):
                        conversations.append(conversation)
                        break  

    return conversations

for filename in os.listdir(json_dir_path):
    if filename.endswith('.json'):
        json_file_path = os.path.join(json_dir_path, filename)
        output_file_path = os.path.join(output_dir_path, f"conversations_{filename}")

        print(f"Processing file: {filename}")

        if os.stat(json_file_path).st_size == 0:
            print(f"Skipping empty file: {filename}")
            continue

        with open(json_file_path, 'r', encoding='utf-8') as file:
            try:
                tweets = json.load(file)
                print(f"Number of tweets loaded: {len(tweets)}")

                conversations = extract_conversations(tweets)
                print(f"Number of conversations extracted: {len(conversations)}")

                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    json.dump(conversations, output_file, ensure_ascii=False, indent=4)

                print(f"Extracted {len(conversations)} conversations from {filename}")

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in file {filename}: {e}")
                continue
            except Exception as e:
                print(f"Unexpected error processing file {filename}: {e}")
                continue

print("Processing complete.")
