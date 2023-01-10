from pyrogram import Client, filters
from . import var

@Client.on_message(filters.command("start") & filters.user(var.admins))
def start(_, message):
    message.reply_text("Hello Master")