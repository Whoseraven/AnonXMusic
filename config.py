import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

API_ID = "21370037"
API_HASH = "0b57036f40bb6da488d05b43e2d20dc1"
BOT_TOKEN = "7886128616:AAGF_fCRSn70msDo8gGMWPxP9Yc7gieMmQc"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002532030178))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7156398455))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Kaisan5/KafkaXMusicBot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Kirito_bots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Whosekirito_Support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFGFLUACz57THg8IKfkyKSWovZO4w5ye1mo1egXvK6jH4J_qSmfec0bXdrQoVL6I74D14G4rywNQTv7nBPYI72gPL530l_FbauSK8dwg2zNL9gFODo-sfjF1HVw9JfEvIbXs36Lcin0otb3cBaIvscOrW_mJv6H0Mbxs5Z7x4BBsiYQxV-sZ57sFhzWKpO7JbRW-88LO0wVQBMh3sT68ADbKUxBVKJFDgBpQ7JMgcmQbVjeLgM_LI_aRAPSpNXgBwV9TTXvTF6bHSX0trTZs81JyXCGj54J1NIOjBc1CmxEC4hgFqA8J7CKQJ01LYDKC7aY_b8vhrCLswR0_MbUmWb9RzXG4QAAAAG3ltq4AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/6d9b2841c30404ee456e3.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/18ff21e134beeceecfa99.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/b1386db0c650168c2761a.jpg"
STATS_IMG_URL = "https://telegra.ph/file/6d9b2841c30404ee456e3.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/b1386db0c650168c2761a.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/26a0a02dc137bfdb8cd5f.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/18ff21e134beeceecfa99.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/26a0a02dc137bfdb8cd5f.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/26a0a02dc137bfdb8cd5f.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/26a0a02dc137bfdb8cd5f.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/26a0a02dc137bfdb8cd5f.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 6000000**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
