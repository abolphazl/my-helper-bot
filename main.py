from dotenv import load_dotenv
from pyrogram import Client
import os


# create 'assets/' dirs, if not exists
if not os.path.exists("assets/"):
    os.makedirs("assets/")

# authorization
load_dotenv()
bot = Client(
    "./assets/bot",
    api_id    = os.getenv("API_ID"),
    api_hash  = os.getenv("API_HASH"),
    bot_token = os.getenv("BOT_TOKEN"),
    plugins   = dict(root="plugins"),
)

# start session
if __name__ == "__main__":
    with bot:
        print(f"@{bot.get_me().username} running.")
    bot.run()