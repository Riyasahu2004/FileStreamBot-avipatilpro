from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("25285117"))
    API_HASH = str(env.get("5c25c8dd95fb74a843aaa62af4324771"))
    BOT_TOKEN = str(env.get("6731498553:AAGS7yR3hYRKk3h6qcHNtzIWb9arG60FKhY"))
    OWNER_ID = int(env.get('OWNER_ID', '827547960'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('mongodb+srv://Violetstreambot:hOGAanYYjGzBC8lQ@violetstreambot.mvq3bnj.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "Telegram"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_UPDATES_CHANNEL = env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_UPDATES_CHANNEL = True if str(FORCE_UPDATES_CHANNEL).lower() == "False" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    IMAGE_FILEID = env.get('IMAGE_FILEID', "https://telegra.ph/file/5bb9935be0229adf98b73.jpg")
    MULTI_CLIENT = False
    LOG_CHANNEL = int(
        env.get("BIN_CHANNEL", None)
    )  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )
    KEEP_ALIVE = str(env.get("KEEP_ALIVE", "0").lower()) in ("1", "true", "t", "yes", "y")


