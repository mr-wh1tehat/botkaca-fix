from pyrogram import Client, filters
from os.path import join as os_path_join
from bot import COMMAND, LOCAL, CONFIG
from bot.plugins import thumbnail_video

thumbnail_path = os_path_join(CONFIG.ROOT, CONFIG.WORKDIR, CONFIG.THUMBNAIL_NAME)

@Client.on_message(filters.command(COMMAND.SET_THUMBNAIL)& (filters.channel | filters.group | filters.user(CONFIG.SUDO_USERS)))
async def set(client, message):
    if not message.reply_to_message:
        return await message.reply_text(LOCAL.THUMBNAIL_NO_PHOTO.format(cmd_set_thumbnail = COMMAND.SET_THUMBNAIL))
    reply = await message.reply_text(LOCAL.THUMBNAIL_DOWNLOADING)
    await message.reply_to_message.download(
        file_name = thumbnail_path
    )
    await reply.edit_text(LOCAL.THUMBNAIL_DOWNLOADED)
    await thumbnail_video.set(thumbnail_path)
    await reply.edit_text(LOCAL.THUMBNAIL_APPLIED)

@Client.on_message(filters.command(COMMAND.RESET_THUMBNAIL)& (filters.channel | filters.group | filters.user(CONFIG.SUDO_USERS)))
async def reset(client, message):
    reply = await message.reply_text(LOCAL.THUMBNAIL_DELETING)
    await thumbnail_video.reset(thumbnail_path)
    await reply.edit_text(LOCAL.THUMBNAIL_RESET)

