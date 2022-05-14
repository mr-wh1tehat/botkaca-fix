from os.path import join as os_path_join
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from bot import CONFIG, COMMAND, LOCAL, LOGGER, STATUS
from bot.handlers import *
import logging
from pyromod import listen
import asyncio


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("log.txt")],
)

client = Client(
    "Bot",
    bot_token=CONFIG.BOT_TOKEN,
    api_id=CONFIG.API_ID,
    api_hash=CONFIG.API_HASH,
    workdir=os_path_join(CONFIG.ROOT, CONFIG.WORKDIR),
    plugins=dict(root="bot/handlers")
)

if __name__ == "__main__":
    client.run()
