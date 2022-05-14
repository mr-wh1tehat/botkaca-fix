from pyrogram import Client, filters
from bot import LOCAL, STATUS, COMMAND, CONFIG

@Client.on_message(filters.command(COMMAND.UPLOAD_AS_DOC)& (filters.channel | filters.group | filters.user(CONFIG.SUDO_USERS)))
async def func(client, message):
    STATUS.UPLOAD_AS_DOC = not STATUS.UPLOAD_AS_DOC
    await message.reply_text(LOCAL.UPLOAD_AS_DOC.format(status=STATUS.UPLOAD_AS_DOC))
