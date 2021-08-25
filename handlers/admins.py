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
    await message.reply_text("✔ 𝙱𝙾𝚃 ** 𝙳𝙾𝙶𝚁𝚄 𝚈Ü𝙺𝙻𝙴𝙽𝙳İ ! **\n✔ **𝚈Ö𝙽𝙴𝚃İ𝙲İ 𝙻İ𝚂𝚃𝙴𝚂İ** 𝙳𝙾Ğ𝚁𝚄 **Güncellenmiş!**")


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "paused"
    ):
        await message.reply_text("✘ 𝙰𝙺𝙸Ş𝚃𝙰 𝙷İÇ𝙱İ𝚁 Ş𝙴𝚈 𝚈𝙾𝙺!")
    else:
        callsmusic.pytgcalls.pause_stream(chat_id)
        await message.reply_text("✔ 𝙼Ü𝚉İ𝙺 𝙳𝚄𝚁𝙰𝙺𝙻𝙰𝚃𝙸𝙻𝙳𝙸!")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "playing"
    ):
        await message.reply_text("✘ 𝙷İÇ𝙱İ𝚁 Ş𝙴𝚈 𝙳𝚄𝚁𝙳𝚄𝚁𝚄𝙻𝙼𝙰𝚉!")
    else:
        callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text("✔ 𝙼Ü𝚉İ𝙺 𝙳𝙴𝚅𝙰𝙼 𝙴𝚃𝚃İ!")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("✘ 𝙰𝙺𝙸Ş𝚃𝙰 𝙷İÇ𝙱İ𝚁 Ş𝙴𝚈 𝚈𝙾𝙺!")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("✔ 𝚈𝙰𝚈𝙸𝙽 𝚂𝙾𝙽𝙰 𝙴𝚁𝙳İ!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("✘ 𝙰𝙺𝙸Ş𝚃𝙰 𝙷İÇ𝙱İ𝚁 Ş𝙴𝚈 𝚈𝙾𝙺 🙄!")
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
    await message.reply_text(f"✘ 𝙰𝚃𝙻𝙰𝚃𝙸𝙻𝙼𝙸Ş : **{skip[0]}**\n✔ Şİ𝙼𝙳İ 𝙾𝚈𝙽𝚄𝚈𝙾𝚁 : **{qeue[0][0]}**")


@Client.on_message(filters.command("auth"))
@authorized_users_only
async def authenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("✘ 𝙺𝚄𝙻𝙻𝙰𝙽𝙸𝙲𝙸𝚈𝙸 𝚈𝙴𝚃𝙺İ𝙻𝙴𝙽𝙳İ𝚁𝙼𝙴𝙺 İÇİ𝙽 𝙼𝙴𝚂𝙰𝙹𝙰 𝙲𝙴𝚅𝙰𝙿 𝚅𝙴𝚁İ𝙽!")
        return
    if message.reply_to_message.from_user.id not in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.append(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("user authorized.")
    else:
        await message.reply("✔ 𝙺𝚄𝙻𝙻𝙰𝙽𝙸𝙲𝙸 𝚉𝙰𝚃𝙴𝙽 𝚈𝙴𝚃𝙺İ𝙻İ!")


@Client.on_message(filters.command("deauth"))
@authorized_users_only
async def deautenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("✘ 𝙺𝚄𝙻𝙻𝙰𝙽𝙸𝙲𝙸𝚈𝙸 𝚈𝙴𝚃𝙺İ𝚂İ𝚉𝙻𝙴Ş𝚃İ𝚁𝙼𝙴𝙺 İÇİ𝙽 𝙼𝙴𝚂𝙰𝙹 𝙰𝚃𝙸𝙽!")
        return
    if message.reply_to_message.from_user.id in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.remove(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("user deauthorized")
    else:
        await message.reply("✔ KULLANICI ZATEN YETKİLENDİRİLDİ!")
