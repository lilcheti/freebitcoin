from telethon import TelegramClient
from telethon.sessions import StringSession
from datetime import timedelta
import config,sys
# Remember to use your own values from my.telegram.org!
session= os.environ.get("SESSION")
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
client = TelegramClient(StringSession(session), api_id, api_hash)

async def main():
    for i in range(100):
        await client.send_message('kirtoharchikose', '/tip 10', reply_to=255,schedule=timedelta(minutes=60+60*i) )

with client:
    client.loop.run_until_complete(main())
