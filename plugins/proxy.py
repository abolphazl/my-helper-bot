from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from . import var
import re

proxy_regex = r"^.*server=(.*)&port=(.*)&secret=(.*)$"

@Client.on_message(filters.regex(proxy_regex))
def send_proxy(client, message):
    data   = re.match(proxy_regex, message.text)
    server = data.group(1)
    port   = data.group(2)
    secret = data.group(3)

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Connect",
                    url = message.text
                )
            ]
        ]
    )

    client.send_message(
        chat_id = var.proxy_channel,
        text = var.proxy_message.format(port=port, secret=secret),
        reply_markup = keyboard,
        disable_web_page_preview = True,
    )

    message.reply_text("sent.")
