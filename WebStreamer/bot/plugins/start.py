# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

import logging
from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from WebStreamer.utils import get_hash, get_name
from pyrogram.enums.parse_mode import ParseMode
from WebStreamer.vars import Var
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@StreamBot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(_, m: Message):
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
             "You are not in the allowed list of users who can use me. \
            Join @HashHackers to use me.",
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
        f'Hello {m.from_user.mention(style="md")},\n\nSend me a file or You can just add me any Telegram Channel and Use.\n\nFollow @HashHackers for Support.'
    )
