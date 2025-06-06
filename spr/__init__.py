from os.path import exists
from sqlite3 import connect

from aiohttp import ClientSession
from pyrogram import Client
from Python_ARQ import ARQ

import asyncio  # Needed to create a running event loop

SESSION_NAME = "spr"
DB_NAME = "db.sqlite3"
API_ID = 6
API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
ARQ_API_URL = "https://arq.hamker.dev"

if exists("config.py"):
    from config import *
else:
    from sample_config import *

# Async setup function for session and ARQ
arq = None
session = None

async def setup_arq():
    global session, arq
    session = ClientSession()
    arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)

# Run setup before using ARQ
asyncio.get_event_loop().run_until_complete(setup_arq())

conn = connect(DB_NAME)

spr = Client(
    SESSION_NAME,
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
)

with spr:
    bot = spr.get_me()
    BOT_ID = bot.id
    BOT_USERNAME = bot.username