import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")
HELPER_TOKEN = os.getenv("TOKEN_HELPER")
CHAT_ID = os.getenv("ADMIN_ID")

