# Using telethon to check for incoming messages starting with Hi

from telethon import TelegramClient, events, sync

# Remember to use your own values from my.telegram.org!
api_id = ...
api_hash = '...'
client = TelegramClient('anon', api_id, api_hash)

client.start()

# change the pattern field if you want to monitor other stuff


@client.on(events.NewMessage(pattern='(?i)Hi '))
async def my_event_handler(event):
    print(event.raw_text)
    await client.send_message('input Handle here', 'input message sent here')


client.run_until_disconnected()
