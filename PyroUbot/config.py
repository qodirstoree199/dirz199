import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "8666828711").split()))

API_ID = int(os.getenv("API_ID", "33293640"))

API_HASH = os.getenv("API_HASH", "d400da6f153cff9dcdb83db861f9159a")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8941223793:AAGw2KQSbLs8nRb9m-0FGlORGqAHqxAnADM")

OWNER_ID = int(os.getenv("OWNER_ID", "8666828711"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1004309612408 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "a6q")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://dirz:<db_password>@cluster0.jdpywvd.mongodb.net/?appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1004309612408"))
