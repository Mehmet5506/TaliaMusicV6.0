from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from helpers.decorators import authorized_users_only, errors
from callsmusic.callsmusic import client as USER
from config import SUDO_USERS


@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>önce beni yönetici yap!</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "helper"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "🤖: sesli sohbette müzik çalmak için buraya katıldım")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>sohbetinizde zaten yardımcıyım</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} userbot için yoğun katılım istekleri nedeniyle grubunuza katılamadım! Kullanıcının grupta yasaklı olmadığından emin olun."
            "\n\nVeya Grubunuza el ile Asisstant ekleyin ve yeniden deneyin</b>",
        )
        return
    await message.reply_text(
        "<b>yardımcı userbot sohbetinize katıldı</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>User couldn't leave your group! May be floodwaits."
            "\n\nYa da beni manuel olarak grubunuza tekmelersiniz.</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Asistan ayrılıyor... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Asistan ayrılıyor... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")

# Idon'tknowwhatisthis
