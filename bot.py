
from pyrogram import Client
from pyroaddon import listen
import os
API_ID = 28153993
API_HASH = "976fd7cc4958ad84181a53b41919564b"
BOT_TOKEN = os.environ.get('6794987860:AAFf7DESafzmz0AfaZJMVMjeK3wCpqcYazE')
bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
