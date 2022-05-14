from pyrogram import Client, filters
from bot import LOCAL, STATUS, COMMAND, CONFIG

@Client.on_message(filters.command(COMMAND.UPLOAD_AS_ZIP)& (filters.channel | filters.group | filters.user(CONFIG.SUDO_USERS)))
async def func(client, message):
    STATUS.UPLOAD_AS_ZIP = not STATUS.UPLOAD_AS_ZIP
    await message.reply_text(LOCAL.UPLOAD_AS_ZIP.format(status=STATUS.UPLOAD_AS_ZIP))
