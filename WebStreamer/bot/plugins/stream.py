# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

import logging
from pyrogram import filters, errors
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot, logger
from WebStreamer.utils import get_hash, get_name
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant


@StreamBot.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.audio
        | filters.animation
        | filters.voice
        | filters.video_note
        | filters.photo
        | filters.sticker
    ),
    group=4,
)
async def media_receive_handler(_, m: Message):
    banned_users = Var.BANNED_USERS.split() if Var.BANNED_USERS else []
    if str(m.from_user.id) in banned_users:
        return await m.reply("You are banned from using this bot.", quote=True)

    try:
        user = await _.get_chat_member(Var.UPDATES_CHANNEL_ID, user_id=m.from_user.id)
    except UserNotParticipant:
        return await m.reply(text="""<i>Join The Update Channel By Tapping The Join Now Button, To Use The Bot.</i>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Now", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ],
                ))
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply("You are not <b>allowed to use</b> Join @HashHackers to use me.", quote=True)
    try:
        log_msg = await m.copy(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}{Var.BIN_CHANNEL_WITHOUT_MINUS}/{log_msg.id}"
        short_link = f"{Var.URL}{Var.BIN_CHANNEL_WITHOUT_MINUS}/{log_msg.id}"
        rm = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Open", url=stream_link)]]
        )
        if Var.FQDN == Var.BIND_ADDRESS:
            # dkabl
            rm = None
        await m.reply_text(
            text="<code>{}</code>\n(<a href='{}'>shortened</a>)".format(
                stream_link, short_link
        ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=rm,
        )
        
    except Exception as e:
        logger.exception(e) # Log the error
        await m.reply("Something went wrong. Please contact the bot admins at @Username for support.", quote=True)
