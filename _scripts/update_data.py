# compares the current day's adoption list to the previous days to check if anything new has been added
# new additions are added to adoption-newly-added.json
# new additions have the `is_recent` property with `True` or `False` values
# `True` means it was added as a new news (more recent than the most recent addition from the previous day)
# `False` means it was an old event that was missing from the list

import os
import time
from datetime import datetime, timezone
import json
import yaml
import requests
from urllib.parse import quote
from dotenv import load_dotenv


load_dotenv()
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")


current_time = round(time.time()) # seconds
date = datetime.now(timezone.utc).strftime('%Y-%m-%d') # yyyy-mm-dd
print(f"Epoch: {current_time}")
print(f"Date: {date}")


# load/sort old adoption list
repo_root = os.path.abspath(__file__ + '/../../')
old_adoption_list_path = repo_root + '/_data/adoption-old.json'
with open(old_adoption_list_path, 'r') as old_adoption_list_file:
  old_adoption_list = json.load(old_adoption_list_file)
  old_adoption_list = sorted(old_adoption_list, key=lambda x: x['date'], reverse=True)
print(f"old_adoption_list count: {len(old_adoption_list)}")


# load/sort current adoption list
request = requests.get('https://ethereumadoption.com/adoption.json')
current_adoption_list = request.json()
current_adoption_list = sorted(current_adoption_list, key=lambda x: x['date'], reverse=True)
print(f"current_adoption_list count: {len(current_adoption_list)}")



# create list of new entries
new_entries = []
is_recent = True
for current_entry in current_adoption_list:
  has_match = False
  for old_entry in old_adoption_list:
    if current_entry == old_entry:
      has_match = True
      is_recent = False
  if has_match == False:
    new_entry = dict(current_entry)
    new_entry['is_recent'] = is_recent
    new_entries.append(new_entry)
print(f"new_entries count: {len(new_entries)}")


# save new entries to file
new_entries_path = repo_root + '/_data/adoption-new-entries.json'
with open(new_entries_path, "w") as new_entries_file:
  json.dump(new_entries, new_entries_file)


# save current list as old list for next update
with open(old_adoption_list_path, "w") as old_adoption_list_file:
  json.dump(current_adoption_list, old_adoption_list_file)


# post new entries to telegram
new_entries.reverse()
print(new_entries)


for entry in new_entries:
  if entry['is_recent']:
    status = ''
    # if entry['status'] == 'dev':
    #   status = '[dev] '
    entities = '/'.join(entry['entities'])
    products = ', '.join(entry['products'])
    source = entry['sources'][0]
    support = ''
    if entry['chains'][0] != None:
      chains = ', '.join(entry['chains'])
      support = f" with support for {chains}"
    # use endpoint to get channel id after interacting with bot (/start)
    # https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates
    chat_list = [
        "-1002400345737" # @ethereumadoption
      ]
    message = f"{status}{entities} announces {products}{support}"
    message = f"{message.upper()}\n\n{source}"
    for chat_id in chat_list:
      url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
      params = {
        'chat_id': chat_id,
        'text': message,
        'reply_markup': json.dumps({
          'inline_keyboard': [[{
            'text': 'EthereumAdoption.com',
            'url': 'https://ethereumadoption.com'
          }]]
        })
      }
      print(requests.get(url=url, params=params).json())
      time.sleep(1)


