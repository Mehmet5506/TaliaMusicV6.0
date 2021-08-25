from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

from callsmusic import callsmusic, queues

import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT, UPDATES_CHANNEL, AUD_IMG, QUE_IMG, OWNER_NAME
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(command("oynat") & other_filters)
@errors
async def oynat(_, message: Message):

    lel = await message.reply("☢ **İŞ𝙻𝙴𝙼𝙴 𝙰𝙻𝙸𝙽𝙳𝙸** 𝚂𝙴𝚂...")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="📣 𝙺𝙰𝙽𝙰𝙻",
                        url=f"https://t.me/SohbetDestek"),
                    InlineKeyboardButton(
                        text="♞ Düznleyen",
                        url=f"https://t.me/Mahoaga")
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"✘ ᴠɪᴅᴇᴏs ʟᴏɴɢᴇʀ ᴛʜᴀɴ {DURATION_LIMIT} ᴍɪɴᴜᴛᴇ(s) ᴀʀᴇɴ'ᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴘʟᴀʏ!"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("♨ 𝙱𝙰𝙽𝙰 𝚂𝙴𝚂 𝙳𝙾𝚂𝚈𝙰𝚂𝙸𝙽𝙸 𝚅𝙴𝚈𝙰 𝚈outuBe 𝙱𝙰Ğ𝙻𝙰𝙽𝚃𝙸𝚂𝙸𝙽𝙸 𝚅𝙴𝚁𝙼𝙴𝙳İ𝙽İ𝚉!")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo=f"{QUE_IMG}",
        reply_markup=keyboard,
        caption=f"#⌛ İ𝚂𝚃𝙴𝙽𝙴𝙽 Ş𝙰𝚁𝙺𝙸 **Sıraya** 𝙺𝙾𝙽𝚄𝙼𝙳𝙰 𝙴𝙺𝙻𝙴𝙽𝙳İ {position}!\n\n✈ 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚃𝙰𝚁𝙰𝙵𝙸𝙽𝙳𝙰𝙽 𝙳𝙴𝚂𝚃𝙴𝙺𝙻𝙴𝙽𝙼𝙴𝙺𝚃𝙴𝙳İ𝚁 {bn}")
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        costumer = message.from_user.mention
        await message.reply_photo(
        photo=f"{AUD_IMG}",
        reply_markup=keyboard,
        caption=f"🎧 **Şİ𝙼𝙳İ 𝙾𝚈𝙽𝚄𝚈𝙾𝚁** İ𝚂𝚃𝙴𝙽İ𝙻𝙴𝙽 𝙱İ𝚁 Ş𝙰𝚁𝙺𝙸 {costumer} !\n\n✈ 𝚃𝙰𝙻İ𝙰 𝙼Ü𝚉İ𝙺 𝚃𝙰𝚁𝙰𝙵𝙸𝙽𝙳𝙰𝙽 𝙳𝙴𝚂𝚃𝙴𝙺𝙻𝙴𝙽𝙼𝙴𝙺𝚃𝙴𝙳İ𝚁 {bn}"
        )   
        return await lel.delete()
