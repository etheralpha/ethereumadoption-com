# compares the current day's adoption list to the previous days to check if anything new has been added
# new additions are added to adoption-newly-added.json
# new additions have the `is_recent` property with `True` or `False` values
# `True` means it was added as a new news (more recent than the most recent additon from the previous day)
# `False` means it was an old event that was missing from the list

import os
import time
from datetime import datetime, timezone
import json
import requests



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



