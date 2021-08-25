# Module by https://github.com/tofikdn
# Copyright (C) 2021 TdMusic
# Ported by @Maho ağa for TaliaMusicBot

import requests
from pyrogram import Client
from config import BOT_USERNAME
from helpers.filters import command

@Client.on_message(command(["asupan", f"asupan@Efsanestar_bot"]))
async def asupan(client, message):
    try:
        resp = requests.get("https://tede-api.herokuapp.com/api/asupan/ptl").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("`Yanlış giden bir şey var...`")


@Client.on_message(command(["wibu", f"wibu@Efsanestar_bot"]))
async def wibu(client, message):
    try:
        resp = requests.get("https://tede-api.herokuapp.com/api/asupan/wibu").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("`Yanlış giden birşey var...`")


@Client.on_message(command(["chika", f"chika@Efsanestar_bot"]))
async def chika(client, message):
    try:
        resp = requests.get("https://tede-api.herokuapp.com/api/chika").json()
        results = f"{resp['url']}"
        return await client.send_video(message.chat.id, video=results)
    except Exception:
        await message.reply_text("`Yanlış giden birşey var...`")


@Client.on_message(command(["truth", f"truth@Efsanestar_bot"]))
async def truth(client, message):
    try:
        resp = requests.get("https://tede-api.herokuapp.com/api/truth").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("Yanlış giden birşey var...")


@Client.on_message(command(["dare", f"dare@Efsanestar_bot"]))
async def dare(client, message):
    try:
        resp = requests.get("https://tede-api.herokuapp.com/api/dare").json()
        results = f"{resp['message']}"
        return await message.reply_text(results)
    except Exception:
        await message.reply_text("Yanlış giden birşey var...")


@Client.on_message(command(["lyric", f"lyric@Efsanestar_bot"]))
async def lirik(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**ɢɪᴠᴇ ᴀ ʟʏʀɪᴄ ɴᴀᴍᴇ ᴛᴏᴏ !**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text("✈ **Arıyorum lyric...**")
        resp = requests.get(f"https://tede-api.herokuapp.com/api/lirik?l={query}").json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception:
        await rep.edit("**ʟʏʀɪᴄs ɴᴏᴛ ғᴏᴜɴᴅ.** ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴀ ᴠᴀʟɪᴅ sᴏɴɢ ɴᴀᴍᴇ !")
