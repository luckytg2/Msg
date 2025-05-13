from pyrogram import Client
from pyrogram.errors import FloodWait
import time
import asyncio
import random

# Bot token and API details
API_ID = "19593445"
API_HASH = "f78a8ae025c9131d3cc57d9ca0fbbc30"
BOT_TOKEN = "7670235524:AAG8xvJ6ppR9ZHf3Df3Fd25pmKWAInbzhVM"

# Chat ID to send messages (replace with your chat ID or username)
CHAT_ID = "@india_best_crypto"

# Messages to send randomly
MESSAGES = [
    "JOIN THE GROUP AND CHECK YOUR DM\n\nAAPKO KUCH MILEGA MSG ME\nHA WAHI MILEGA JO AAPKO CHAHIYE",
    "ग्रुप को जॉइन करो और अपना मेसेज करो\n\nआपको कुछ मिलेगा\nवही मिलेगा जो आपको चाहिए"
]

# Create the bot client
app = Client("random_message_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def send_message_periodically():
    while True:
        try:
            # Choose a random message from the list
            message = random.choice(MESSAGES)
            await app.send_message(CHAT_ID, message)
            print("Message sent!")
            await asyncio.sleep(15)  # Wait for 15 seconds
        except FloodWait as e:
            print(f"Rate limit exceeded. Waiting for {e.value} seconds.")
            await asyncio.sleep(e.value)

@app.on_message()
async def handle_message(client, message):
    if message.text.lower() == "/start":
        await message.reply("Bot is now active and will send random messages every 15 seconds.")
    elif message.text.lower() == "/stop":
        await message.reply("Bot stopped.")
        exit()

async def main():
    async with app:
        await send_message_periodically()

if __name__ == "__main__":
    app.run(main())
