"""Warn system"""
from collections import defaultdict
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_WARNS: dict[int, dict[int, int]] = defaultdict(lambda: defaultdict(int))
MAX_WARNS = 3


@app.on_message(ub_cmd("warn"))
@sudo_only
async def warn_cmd(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply_text("Reply to a user to warn.")
    if message.chat.type.name not in ("GROUP", "SUPERGROUP"):
        return await message.reply_text("Groups only.")
    uid = message.reply_to_message.from_user.id
    chat = message.chat.id
    _WARNS[chat][uid] += 1
    count = _WARNS[chat][uid]
    await message.reply_text(
        f"⚠️ Warned <code>{uid}</code>\n"
        f"Count: <b>{count}/{MAX_WARNS}</b>"
    )
    if count >= MAX_WARNS:
        try:
            await client.ban_chat_member(chat, uid)
            await message.reply_text(f"🔨 Auto-banned after {MAX_WARNS} warns.")
            _WARNS[chat][uid] = 0
        except Exception as e:
            await message.reply_text(f"Ban failed: {e}")


@app.on_message(ub_cmd("unwarn", "resetwarns"))
@sudo_only
async def unwarn_cmd(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply_text("Reply to user.")
    uid = message.reply_to_message.from_user.id
    chat = message.chat.id
    _WARNS[chat][uid] = 0
    await message.reply_text(f"✅ Warns reset for <code>{uid}</code>")


@app.on_message(ub_cmd("warns"))
@sudo_only
async def warns_cmd(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply_text("Reply to user.")
    uid = message.reply_to_message.from_user.id
    chat = message.chat.id
    c = _WARNS[chat][uid]
    await message.reply_text(f"⚠️ <code>{uid}</code> has <b>{c}</b> warn(s).")
