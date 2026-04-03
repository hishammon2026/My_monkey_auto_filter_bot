import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'LuciferMoringstar_Robot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

BROADCAST_CHANNEL = int(os.environ.get("BROADCAST_CHANNEL", "0"))
ADMIN_ID = set(int(x) for x in os.environ.get("ADMIN_ID", "").split())

# --- ഡാറ്റാബേസ് സെക്ഷൻ (ഇവിടെയാണ് മാറ്റം വരുത്തിയത്) ---
# നിന്റെ മെയിൻ ലിങ്ക് താഴെ നേരിട്ട് നൽകിയിരിക്കുന്നു
MONGO_URL = "mongodb+srv://hishammon:hishammon@cluster0.2g7bqyf.mongodb.net/?appName=Cluster0"

DB_URL = environ.get("DATABASE_1", MONGO_URL) # ബ്രോഡ്കാസ്റ്റിന്
DATABASE_URI = environ.get('DATABASE_2', MONGO_URL) # മെയിൻ ഫിൽറ്ററിന്
DATABASE_NAME = environ.get('BOT_NAME', 'Cluster0')
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
# ---------------------------------------------------

BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST", True))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('FORCES_SUB')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

TUTORIAL = "https://t.me/bothelpersosupport/28"

# Messages
default_start_msg = """
**Hi, I'm Auto Filter V3**
Send me the name of movie to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)
FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "4f08a979")

API_KEY = OMDB_API_KEY.strip() if OMDB_API_KEY.strip() else None
CUSTOM_FILE_CAPTION = FILE_CAPTION.strip() if FILE_CAPTION.strip() else None
