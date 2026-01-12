import re
import os
from os import environ, getenv
from Script import script

# --- Helper Functions ---
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "on"]:
        return True
    elif value.lower() in ["false", "no", "0", "off"]:
        return False
    return default

# =========================================================
# 🤖 BOT INFO & CREDENTIALS
# =========================================================
SESSION = environ.get('SESSION', 'Webavbot')
API_ID = int(environ.get('API_ID', '10660564'))
API_HASH = environ.get('API_HASH', '527e6297989f4e7cda5091f5bf41d0e4')
BOT_TOKEN = environ.get('BOT_TOKEN', '7239597095:AAHUIBW1u-HIpOFbYWzbLR1Ze_xZqV49mJI')

# Admin Settings
ADMINS = [int(x) for x in environ.get('ADMINS', '7737048829').split()]
OWNER_USERNAME = environ.get("OWNER_USERNAME", 'PRESIDENTIND7')

# =========================================================
# 🗄️ DATABASE CONNECTION
# =========================================================
DB_URL = environ.get('DATABASE_URI', "mongodb+srv://dasniru929:dasniru123@cluster0.51p5e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get('DATABASE_NAME', "testing")

# =========================================================
# 📢 CHANNELS & LOGS
# =========================================================
# Mandatory Channels
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", '-1002755386002'))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '-1002755386002'))

# Feature Specific Logs
PREMIUM_LOGS = int(environ.get("PREMIUM_LOGS", '-1002755386002'))
VERIFIED_LOG = int(environ.get('VERIFIED_LOG', '-1002755386002'))
SUPPORT_GROUP = int(environ.get("SUPPORT_GROUP", "-1002372458634"))

# Auth Channels (Safe Parsing)
auth_channel_str = environ.get("AUTH_CHANNEL", "-1002386857422")
AUTH_CHANNEL = [int(x) for x in auth_channel_str.split()] if auth_channel_str else []

# =========================================================
# 🔗 LINKS & URLS
# =========================================================
CHANNEL = environ.get('CHANNEL', 'https://t.me/Radha_Rani_Backup')
SUPPORT = environ.get('SUPPORT', 'https://t.me/Ez_Request_Grp')
TUTORIAL_LINK_1 = environ.get('TUTORIAL_LINK_1', 'https://t.me/1')
TUTORIAL_LINK_2 = environ.get('TUTORIAL_LINK_2', 'https://t.me/2')

# =========================================================
# 🔐 VERIFICATION & SHORTENER
# =========================================================
IS_VERIFY = is_enabled(environ.get("IS_VERIFY", "False"), True)
IS_SECOND_VERIFY = is_enabled(environ.get("IS_SECOND_VERIFY", "False"), True)
IS_SHORTLINK = is_enabled(environ.get('IS_SHORTLINK', "False"), True)

# Verification Config
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 60)) # In Minutes/Hours based on logic
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'mdiskshortner.link')
SHORTLINK_API = environ.get('SHORTLINK_API', '96a3c0e8ae1b1abd429906762e38a40d3f2ec56c')

# Second Verification Config
SHORTLINK_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "mdiskshortner.link")
SHORTLINK_API2 = environ.get("SHORTENER_API2", "96a3c0e8ae1b1abd429906762e38a40d3f2ec56c")

# =========================================================
# ⚙️ SETTINGS & LIMITS
# =========================================================
FSUB = is_enabled(environ.get("FSUB", "True"), True)
ENABLE_LIMIT = is_enabled(environ.get("ENABLE_LIMIT", "True"), True)
MAINTENANCE_MODE = is_enabled(environ.get("MAINTENANCE_MODE", "False"), False)

# Time & Rate Limits
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
RATE_LIMIT_TIMEOUT = int(environ.get("RATE_LIMIT_TIMEOUT", "600"))

# File Limits
MAX_FILES = int(environ.get("MAX_FILES", "5"))
BATCH_LIMIT = int(environ.get('BATCH_LIMIT', 60))

# =========================================================
# 🖼️ MEDIA & CAPTIONS
# =========================================================
QR_CODE = environ.get('QR_CODE', 'https://i.ibb.co/4nT0x43P/Img2url-bot.jpg')
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
AUTH_PICS = environ.get('AUTH_PICS', 'https://indicamps.in/uploads/file_253.jpg')
PICS = environ.get('PICS', 'https://ibb.co/VpTJNNCN')
FILE_PIC = environ.get('FILE_PIC', 'https://i.ibb.co/bj4My0bW/photo-2025-07-21-02-15-21-7529360175656861700.jpg')

FILE_CAPTION = environ.get('FILE_CAPTION', script.CAPTION)

# =========================================================
# 🌐 SERVER & APP CONFIG
# =========================================================
WORKERS = int(getenv('WORKERS', '4'))
MULTI_CLIENT = False
name = str(environ.get('name', 'avbotz'))

# Heroku & Port Config
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))
else:
    ON_HEROKU = False
    APP_NAME = None

PORT = int(getenv('PORT', '2626'))
NO_PORT = is_enabled(getenv("NO_PORT", "False"), False)
HAS_SSL = is_enabled(getenv("HAS_SSL", "False"), False)
BIND_ADDRESS = getenv("WEB_SERVER_BIND_ADDRESS", "127.0.0.1")

# URL Generation
# Use provided URL from env, or generate based on FQDN/IP
custom_url = environ.get("URL")
if custom_url:
    URL = custom_url
else:
    FQDN = getenv("FQDN", BIND_ADDRESS)
    PROTOCOL = "https" if HAS_SSL else "http"
    PORT_SEGMENT = "" if NO_PORT else f":{PORT}"
    URL = f"{PROTOCOL}://{FQDN}{PORT_SEGMENT}/"

# Default fallback if nothing works (Matches your provided koyeb link)
if not URL or URL == "/":
    URL = "https://forward-jolyn-vnnmbs-62200c9e.koyeb.app/"
    
