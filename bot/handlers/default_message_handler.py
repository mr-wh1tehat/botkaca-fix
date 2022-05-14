from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot import COMMAND
from bot.handlers import leech_handler

@Client.on_message(filters.private & ~filters.regex(r'^/'))
async def func(client, message):
    message.text = "/" + COMMAND.LEECH + " " + message.text
    return await leech_handler.func(client, message)
