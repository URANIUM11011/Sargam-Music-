from pyrogram import Client, enums, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPermissions, Message
from AnieXEricaMusic import app
from AnieXEricaMusic.misc import SUDOERS
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from AnieXEricaMusic import app, Userbot
from AnieXEricaMusic.utils.database import get_assistant
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant, ChatAdminRequired
from pyrogram.types import Message, ChatPrivileges
import asyncio
from typing import Optional
from random import randint
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.enums import ParseMode
from AnieXEricaMusic import app
from AnieXEricaMusic.utils.database import is_on_off
from config import LOG_GROUP_ID
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message, User, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

async def play_logs(message, streamtype):
    if await is_on_off(2):
        chat_members = await app.get_chat_members_count(message.chat.id)
        async for admin in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if admin.status == enums.ChatMemberStatus.OWNER:
                owner_AMBOT = admin.user.mention if hasattr(admin.user, 'mention') and admin.user.mention else "Is_Hide / Deleted"
                owner_AMBOT_id = admin.user.id if hasattr(admin.user, 'id') else "Is_Hide / Deleted"
        logger_text = f"""
<b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>
 
<b>⌯ ᴄʜᴀᴛ ɴᴀᴍᴇ :</b>{message.chat.title}
<b>⌯ ᴄʜᴀᴛ ɪᴅ :</b> <code>{message.chat.id}</code>
<b>⌯ ɴᴀᴍᴇ :</b> {message.from_user.mention}
<b>⌯ ᴜsᴇʀɴᴀᴍᴇ  :</b> @{message.from_user.username}
<b>⌯ ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>
<b>⌯ ᴄʜᴀᴛ ʟɪɴᴋ :</b> @{message.chat.username}
<b>⌯ ᴄʜᴀᴛ ᴍᴇᴍʙᴇʀs :</b> <code>{chat_members}</code>
<b>⌯ ᴄʜᴀᴛ ᴏᴡɴᴇʀ  :</b> {owner_AMBOT} 𝐈𝐝 ➪<code>{owner_AMBOT_id}</code>
<b>⌯ sᴇᴀʀᴄʜᴇᴅ :</b> <code>{message.text.split(None, 1)[1]}</code>
<b>⌯ sᴛʀᴇᴀᴍᴛʏᴘᴇ :</b> {streamtype}
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
