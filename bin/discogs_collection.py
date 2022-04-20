import json
import discogs_client
from dotenv import dotenv_values

config = dotenv_values(".env")

d = discogs_client.Client('stvnrlly/0.1', user_token=config['DISCOGS_TOKEN'])

discogs_collection = d.user('stvnrlly').collection_folders[0].releases
collection = []

for r in discogs_collection:
    collection.append(r.data['basic_information']['id'])

with open('./data/discogs.json', 'w') as f:
    json.dump(collection, f, ensure_ascii=False, indent=4)
