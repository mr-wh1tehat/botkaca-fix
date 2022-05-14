import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create /list handler

from os.path import join as os_path_join
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aria2p import Download
from bot import LOCAL, STATUS, CONFIG, COMMAND
from bot.plugins import aria2

@Client.on_message(filters.command(COMMAND.LEECH_LIST)& (filters.group | filters.user(CONFIG.SUDO_USERS)))
async def func(client, message):
    dir = os_path_join(CONFIG.ROOT, CONFIG.ARIA2_DIR)
    STATUS.ARIA2_API = STATUS.ARIA2_API or aria2.aria2(
        config={
            'dir' : dir
        }
    )
    aria2_api = STATUS.ARIA2_API
    await aria2_api.start()

    downloads = aria2_api.get_downloads()
    text = LOCAL.LEECH_LIST_MESSAGE_HEADER + '\n'
    for download in downloads:
        text += LOCAL.LEECH_LIST_FORMAT.format(
            name = download.name,
            status = download.status,
            gid = download.gid
        )
    await message.reply(text)
