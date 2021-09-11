from pyrogram import Client, idle
import os
from Bot.video_stream import app
API_ID = os.environ.get("API_ID",12345)
API_HASH = os.environ.get("API_HASH","")
TOKEN = os.environ.get("TOKEN","")

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="Bot"),
)
bot.start()
app.start()
idle()
