# Copyright (C) 2021 TaliaMusicProject


from asyncio import QueueEmpty
from config import que
from pyrogram import Client, filters
from pyrogram.types import Message

from cache.admins import admins
from helpers.channelmusic import get_chat_id
from helpers.decorators import authorized_users_only, errors
from helpers.filters import command, other_filters
from callsmusic import callsmusic
from callsmusic.queues import queues


@Client.on_message(filters.command("reload"))
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text("โ ๐ฑ๐พ๐ ** ๐ณ๐พ๐ถ๐๐ ๐ร๐บ๐ป๐ด๐ฝ๐ณฤฐ ! **\nโ **๐ร๐ฝ๐ด๐ฤฐ๐ฒฤฐ ๐ปฤฐ๐๐๐ด๐ฤฐ** ๐ณ๐พฤ๐๐ **Gรผncellenmiล!**")


@Client.on_message(command("durdur") & other_filters)
@errors
@authorized_users_only
async def durdur(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "paused"
    ):
        await message.reply_text("โ ๐ฐ๐บ๐ธล๐๐ฐ ๐ทฤฐร๐ฑฤฐ๐ ล๐ด๐ ๐๐พ๐บ!")
    else:
        callsmusic.pytgcalls.pause_stream(chat_id)
        await message.reply_text("โ Mรผzik duraklatฤฑldฤฑ!")


@Client.on_message(command("devam") & other_filters)
@errors
@authorized_users_only
async def devam(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "playing"
    ):
        await message.reply_text("โ Akฤฑล durdurulmasฤฑ..!")
    else:
        callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text("โ Mรผzik Devam Etti!")


@Client.on_message(command("son") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("โ ๐ฐ๐บ๐ธล๐๐ฐ ๐ทฤฐร๐ฑฤฐ๐ ล๐ด๐ ๐๐พ๐บ!")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("โ Yayฤฑn Akฤฑลฤฑ Kapatฤฑldฤฑ!")


@Client.on_message(command("atla") & other_filters)
@errors
@authorized_users_only
async def atla(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("โ ๐ฐ๐บ๐ธล๐๐ฐ ๐ทฤฐร๐ฑฤฐ๐ ล๐ด๐ ๐๐พ๐บ ๐!")
    else:
        queues.task_done(chat_id)

        if queues.is_empty(chat_id):
            callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            callsmusic.pytgcalls.change_stream(
                chat_id, queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"โ Atlatฤฑldฤฑ: **{skip[0]}**\nโ ลimdi Oynatฤฑlฤฑyor: **{qeue[0][0]}**")


@Client.on_message(filters.command("yetki"))
@authorized_users_only
async def authenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("Kullanฤฑcฤฑya Yetkล Vermek iรงin yanฤฑtlayฤฑnฤฑz!")
        return
    if message.reply_to_message.from_user.id not in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.append(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("kullanฤฑcฤฑ yetkili.")
    else:
        await message.reply("โ Kullanฤฑcฤฑ Zaten Yetkili!")


@Client.on_message(filters.command("yetkial"))
@authorized_users_only
async def deautenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("โ Kullanฤฑcฤฑyฤฑ yetkisizleลtirmek iรงin mesaj atฤฑnฤฑz!")
        return
    if message.reply_to_message.from_user.id in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.remove(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("kullanฤฑcฤฑ yetkisiz")
    else:
        await message.reply("โ Kullanฤฑcฤฑnฤฑn yetkisi alฤฑndฤฑ!")
