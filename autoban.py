import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", 8451490))
API_HASH = os.environ.get("API_HASH", "")

bot = Client(
        "hide",
        bot_token=BOT_TOKEN,
	api_hash=API_HASH,
        api_id=API_ID
    )

@bot.on_message(filters.command('start'))
async def start(bot, message):
	text = 'Hey, Iam Autoban Bot'
	await message.reply(text, quote=True)

@bot.on_message(filters.new_chat_members)
async def welcome(bot, message):
	
try: new_chat_members.kick
	
bot.run()
