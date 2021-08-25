from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ **𝙷𝙾Ş𝙶𝙴𝙻𝙳İ𝙽İ𝚉 {message.from_user.first_name}** \n
💭 **[Talia Müzik](https://t.me/Efsanestar_bot) 𝚈𝙴𝙽İ 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼'𝙸𝙽 𝚂𝙴𝚂𝙻İ 𝚂𝙾𝙷𝙱𝙴𝚃𝙻𝙴𝚁İ𝚈𝙻𝙴 𝙶𝚁𝚄𝙿𝙻𝙰𝚁𝙸𝙽𝙳𝙰 𝙼Ü𝚉İ𝙺 Ç𝙰𝙻𝙼𝙰𝚂𝙸𝙽𝙰 İ𝚉İ𝙽 𝚅𝙴𝚁İ𝙽!**

💡 **Ü𝚉𝙴𝚁İ𝙽𝙴 𝚃𝙸𝙺𝙻𝙰𝚈𝙰𝚁𝙰𝙺 𝙱𝙾𝚃'𝚄𝙽 𝚃Ü𝙼 𝙺𝙾𝙼𝚄𝚃𝙻𝙰𝚁𝙸𝙽𝙸 𝚅𝙴 𝙽𝙰𝚂𝙸𝙻 Ç𝙰𝙻𝙸Ş𝚃𝙸Ğ𝙸𝙽𝙸 ÖĞ𝚁𝙴𝙽İ𝙽. » 📚 𝙺𝙾𝙼𝚄𝚃𝙻𝙰𝚁 𝙳ÜĞ𝙼𝙴𝚂İ!**

❓ **𝙱𝚄 𝙱𝙾𝚃'𝚄𝙽 𝚃Ü𝙼 Ö𝚉𝙴𝙻𝙻İ𝙺𝙻𝙴𝚁İ 𝙷𝙰𝙺𝙺𝙸𝙽𝙳𝙰 𝙳𝙰𝙷𝙰 𝙵𝙰𝚉𝙻𝙰 𝙱İ𝙻𝙶İ İÇİ𝙽, 𝚂𝙰𝙳𝙴𝙲𝙴 𝙱𝙰𝚂𝙸𝙽𝙸𝚉 /help**

✂ **𝚅𝙲𝙶'𝙳𝙴 𝙼Ü𝚉İ𝙺 Ç𝙰𝙻𝙼𝙰𝙺 İÇİ𝙽 [𝙼𝙰𝙷𝙾 𝙰Ğ𝙰](hptts://t.me/Mahoaga) 𝚃𝙰𝚁𝙰𝙵𝙸𝙽𝙳𝙰𝙽 𝚈𝙰𝙿𝙸𝙻𝙼𝙸Ş𝚃𝙸𝚁.**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ 𝙱𝙴𝙽İ 𝙶𝚁𝚄𝙱𝚄𝙽𝙰 𝙴𝙺𝙻𝙴 ➕", url=f"https://t.me/Efsanestar_bot?startgroup=true")
                ],[
                    InlineKeyboardButton(
                         "📚 𝙺𝙾𝙼𝚄𝚃𝙻𝙰𝚁", url="https://t.me/KanalEfsanestar"
                    ),
                    InlineKeyboardButton(
                        "🖥️ 𝙳Ü𝚉𝙴𝙽𝙻𝙴𝙼𝙴 𝚈𝙰𝙿𝙰𝙽", url=f"https://t.me/Furkanbeyy")
                ],[
                    InlineKeyboardButton(
                        "👥 𝚁𝙴𝚂𝙼İ 𝙶𝚁𝚄𝙿", url=f"https://t.me/Taliasohbet"
                    ),
                    InlineKeyboardButton(
                        "📣 𝚁𝙴𝚂𝙼İ 𝙺𝙰𝙽𝙰𝙻", url=f"https://t.me/SohbetDestek")               
                 ],[
                    InlineKeyboardButton(
                        "🧪 𝙺𝙰𝚈𝙽𝙰𝙺 𝙺𝙾𝙳𝚄 🧪", url="https://t.me/Mahoaga"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@Efsanestar_bot"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✔ **ʙᴏᴛ ɪs ʀᴜɴɴɪɴɢ**\n<b>☣ **ᴜᴘᴛɪᴍᴇ:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☢ 𝙶𝚁𝚄𝙿", url=f"https://t.me/SohbetSkayfall"
                    ),
                    InlineKeyboardButton(
                        "📣 𝙺𝙰𝙽𝙰𝙻", url=f"https://t.me/SohbetDestek"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@Efsanestar_bot"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>☢ ʜᴇʟʟᴏ {message.from_user.mention()}, ᴘʟᴇᴀsᴇ ᴛᴀᴘ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ sᴇᴇ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇssᴀɢᴇ ʏᴏᴜ ᴄᴀɴ ʀᴇᴀᴅ ғᴏʀ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✔ 𝙱𝙴𝙽İ 𝙽𝙰𝚂𝙸𝙻 𝙺𝚄𝙻𝙻𝙰𝙽𝙸𝚁𝚂𝙸𝙽", url=f"https://t.me/Efsanestar_bot?start=help"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Merhaba {message.from_user.mention()}, yardım menüsüne hoş geldiniz✨
\n📙 𝙱𝙴𝙽İ 𝙽𝙰𝚂𝙸𝙻 𝙺𝚄𝙻𝙻𝙰𝙽𝙸𝚁𝚂𝙸𝙽?
\n1. önce beni grubunuza ekleyin.
2. beni yönetici olarak tanıtın ve tüm izinleri verin.
3. ardından, @taliaMusicasistant grubunuza veya türünüze /userbotjoin.
3. müzik çalmaya başlamadan önce sesli sohbeti açtığınızdan emin olun.
\n💁🏻‍♀️ **tüm kullanıcı için komutlar:**
\n/play (song name) - youtube'dan şarkı çalmak
/oynat (reply to audio) - ses dosyasını kullanarak şarkı çalma youtube linki veya Mp3 oynatıcı
/playlist - listedeki şarkıyı sırada gösterme
/song (song name) - youtube'dan şarkı indirme
/search (video name) - youtube'dan video arama detayı
/vsong (video name) - youtube'dan video indirme ayrıntılı
/lyric - (song name) şarkı sözleri scrapper 
/vk (song name) - şarkıyı satır içi moddan indirme
\n👷🏻‍♂️ **yöneticiler için komutlar:**
\n/player - müzik çalar ayarları panelini açma
/pause - müzik akışını duraklatma
/resume - devam et müzik duraklatıldı 
/skip - sonraki şarkıya atlamak 
/end - müzik akışını durdurma 
/userbotjoin - grubunuza asistan katılmayı davet etme 
/reload - yönetici listesini yenilemek için 
/cache - temizlenmiş yönetici önbelleği için 
/auth - müzik botu kullanmak için yetkili kullanıcı 
/deauth - müzik botu kullanmak için yetkisiz 
/musicplayer (on / off) - devre dışı bırakmak / etkinleştirmek grubunuzdaki müzik çalar için
\n🎧 kanal akışı komutları:
\n/cplay - kanal sesli sohbetinde müzik akışı 
/cplayer - şarkıyı akışta gösterme 
/cpause - müzik akışını duraklatma 
/cresume - akışın duraklatıldığını sürdürme 
/cskip - akışı bir sonraki şarkıya atlamak 
/cend - müzik akışını sonlandırmak 
/admincache - yönetici önbelleğini yenileme 
\n🧙‍♂️ sudo kullanıcıları için komut:
\n/userbotleaveall - asistanın tüm gruptan ayrılmasını emretmek 
/gcast - yayın iletisi gönderme yardımcıya göre 
\n🎊 **eğlence için komutlar:**
\n/chika - kendiniz kontrol edin 
/wibu - kendiniz kontrol edin 
/asupan - kendiniz kontrol edin
/truth - kendiniz kontrol edin
/dare - kendiniz kontrol edin
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☣ 𝙶𝚁𝚄𝙿", url=f"https://t.me/Sohbetneresi"
                    ),
                    InlineKeyboardButton(
                        "📣 𝙺𝙰𝙽𝙰𝙻", url=f"https://t.me/SohbetDestek"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "♞🏻‍💻 𝙶𝙴𝙻İŞ𝚃İ𝚁İ𝙲İ", url=f"https://t.me/Mahoaga"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@Efsanestar_bot"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "✈ `ᴘᴏɴɢ!!`\n"
        f"☣ `{delta_ping * 1000:.3f} ᴍs`"
    )


@Client.on_message(command(["uptime", f"uptime@Efsanestar_bot"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 ʙᴏᴛ sᴛᴀᴛᴜs:\n"
        f"➤ **ᴜᴘᴛɪᴍᴇ:** `{uptime}`\n"
        f"➤ **sᴛᴀʀᴛ ᴛɪᴍᴇ:** `{START_TIME_ISO}`"
    )
