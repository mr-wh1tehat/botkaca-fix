from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot import COMMAND, LOCAL, CONFIG

@Client.on_message(filters.command(COMMAND.HELP)& (filters.group | filters.user(CONFIG.SUDO_USERS)))
async def func(client, message):
    text = LOCAL.HELP_MESSAGE_HEADER + "\n"
    for cmd_code, cmd in COMMAND:
        info = LOCAL.NO_HELP_INFO
        cmd_local = f'COMMAND_{cmd_code}' 
        if cmd_local in dict(LOCAL):
            info = getattr(LOCAL, cmd_local)
        text += f'/{cmd} - {info}\n'
    await message.reply_text(text)
