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

@Client.on_message(command("ytoynat") & other_filters)
@errors
async def ytoynat(_, message: Message):

    lel = await message.reply("â¢ **Ä°Åð»ð´ð¼ð´ ð°ð»ð¸ð½ð³ð¸** ðð´ð...")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ð£ ðºð°ð½ð°ð»",
                        url=f"https://t.me/SohbetDestek"),
                    InlineKeyboardButton(
                        text="â DÃ¼znleyen",
                        url=f"https://t.me/Mahoaga")
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"â á´ Éªá´á´á´s Êá´É´É¢á´Ê á´Êá´É´ {DURATION_LIMIT} á´ÉªÉ´á´á´á´(s) á´Êá´É´'á´ á´ÊÊá´á´¡á´á´ á´á´ á´Êá´Ê!"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("â¨ ð±ð°ð½ð° ðð´ð ð³ð¾ððð°ðð¸ð½ð¸ ðð´ðð° ðoutuBe ð±ð°Äð»ð°ð½ðð¸ðð¸ð½ð¸ ðð´ðð¼ð´ð³Ä°ð½Ä°ð!")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo=f"{QUE_IMG}",
        reply_markup=keyboard,
        caption=f"#â Ä°ððð´ð½ð´ð½ Åð°ððºð¸ **SÄ±raya** ðºð¾ð½ðð¼ð³ð° ð´ðºð»ð´ð½ð³Ä° {position}!\n\nâ ðð¾ðððð±ð´ ðð°ðð°ðµð¸ð½ð³ð°ð½ ð³ð´ððð´ðºð»ð´ð½ð¼ð´ðºðð´ð³Ä°ð {bn}")
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        costumer = message.from_user.mention
        await message.reply_photo(
        photo=f"{AUD_IMG}",
        reply_markup=keyboard,
        caption=f"ð§ **ÅÄ°ð¼ð³Ä° ð¾ðð½ððð¾ð** Ä°ððð´ð½Ä°ð»ð´ð½ ð±Ä°ð Åð°ððºð¸ {costumer} !\n\nâ ðð°ð»Ä°ð° ð¼ÃðÄ°ðº ðð°ðð°ðµð¸ð½ð³ð°ð½ ð³ð´ððð´ðºð»ð´ð½ð¼ð´ðºðð´ð³Ä°ð {bn}"
        )   
        return await lel.delete()
