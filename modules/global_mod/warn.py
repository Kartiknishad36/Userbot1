"""Warn system"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_warns: dict[tuple[int, int], int] = {}

@app.on_message(ub_cmd("warn"))
@sudo_only
async def warn_cmd(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply_text("Reply to a user to warn.")
    uid = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    key = (chat_id, uid)
    _warns[key] = _warns.get(key, 0) + 1
    count = _warns[key]
    await message.reply_text(f"⚠️ User warned. Total warns: <b>{count}</b>")

@app.on_message(ub_cmd("resetwarns", "delwarns"))
@sudo_only
async def resetwarns_cmd(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply_text("Reply to a user.")
    uid = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    _warns.pop((chat_id, uid), None)
    await message.reply_text("✅ Warns reset.")
