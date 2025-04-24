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
from dotenv import load_dotenv


load_dotenv()
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")


current_time = round(time.time()) # seconds
date = datetime.now(timezone.utc).strftime('%Y-%m-%d') # yyyy-mm-dd
print(f"Epoch: {current_time}")
print(f"Date: {date}")


def send_announcement(msg):
  msg = msg.strip()
  if msg != "":
    print(repr(msg))
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
      'chat_id': '-1002400345737', # @ethereumadoption
      'text': msg,
      'reply_markup': json.dumps({
        'inline_keyboard': [[{
          'text': 'EthereumAdoption.com',
          'url': 'https://ethereumadoption.com/built-on-ethereum/'
        }]]
      })
    }
    print(requests.get(url=url, params=params).json())
  else:
    print("Error: Announcement message is blank")



send_announcement("""UBISOFT ANNOUNCES MIGHT & MAGIC CARD EXCHANGE WITH SUPPORT FOR IMMUTABLE X

https://collectorclub.co.uk/trading-cards/ubisoft-announces-new-trading-card-game-might-magic-fates/
""")



