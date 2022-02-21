import asyncio
from email import message
from telethon import TelegramClient,events
import config
k=5

level = 0
netwin=30
bet=30
loss=0
# Remember to use your own values from my.telegram.org!
api_id = config.api_id
api_hash = config.api_hash
client = TelegramClient('an', api_id, api_hash)

@client.on(events.NewMessage(from_users="dopeassweed"))
async def handler(event):
    print(event.message.message)
    if(event.message.message=='stop'):
        await client.disconnect()
    elif(event.message.message=='reset'):
        global loss,level,bet,netwin
        level = 0
        netwin=30
        bet=30
        loss=0

@client.on(events.NewMessage(from_users="lntxbot",pattern="(?i)You've lost.+"))
async def handler(event):
    # Respond whenever someone says "Hello" and something else
    global loss,level,bet,netwin
    level +=1
    loss += bet + 10 
    netwin += k
    bet=loss+netwin
    await event.reply('level: '+str(level)+'\n'+'total loss: '+str(loss)+'\n'+'net win: '+str(netwin)+'\n'+'bet: '+str(bet))
    await client.send_message('lncasino','/coinflip '+str(bet))
    
@client.on(events.NewMessage(from_users="lntxbot",pattern="(?i)You're the winner.+"))
async def handler(event):
    # Respond whenever someone says "Hello" and something else
    global loss,level,bet,netwin
    level = 0
    netwin=30
    bet=30
    loss=0
    await client.send_message('lncasino','/coinflip '+str(bet))


client.start()
client.run_until_disconnected()
