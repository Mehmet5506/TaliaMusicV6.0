import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Talia Müzik Projesi")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cd0b87484429704c7b935.png")
THUMB_IMG = getenv("THUMB_IMG", "https://i.ibb.co/VQd4HSH/Photo-1629477903701.jpg")
AUD_IMG = getenv("AUD_IMG", "https://i.ibb.co/VQd4HSH/Photo-1629477903701.jpg")
QUE_IMG = getenv("QUE_IMG", "https://i.ibb.co/VQd4HSH/Photo-1629477903701.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "Mp3dinleme_Bot ")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SesMusicAsistan")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Sohbetdestek")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "EfsaneMusicProject")
OWNER_NAME = getenv("OWNER_NAME", "Mahoaga") # kullanıcı adınızı semboller olmadan doldurma @
DEV_NAME = getenv("DEV_NAME", "Badboyanim")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
