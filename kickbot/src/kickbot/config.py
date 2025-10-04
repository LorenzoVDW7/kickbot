import os

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
server_id = os.getenv("SERVER_ID")