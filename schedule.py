from telethon import TelegramClient
from datetime import timedelta
import config
# Remember to use your own values from my.telegram.org!
api_id = config.api_id
api_hash = config.api_hash
client = TelegramClient('an', api_id, api_hash)

async def main():
    for i in range(100):
        await client.send_message('kirtoharchikose', '/tip 10', reply_to=255,schedule=timedelta(minutes=60+60*i) )

with client:
    client.loop.run_until_complete(main())