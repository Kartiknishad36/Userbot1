"""Nightmode"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_nightmode_chats: set[int] = set()

@app.on_message(ub_cmd("nightmode"))
@sudo_only
async def nightmode_cmd(client, message: Message):
    chat_id = message.chat.id
    parts = (message.text or "").split()
    arg = parts[1].lower() if len(parts) > 1 else ""
    if arg in ("on", "enable"):
        _nightmode_chats.add(chat_id)
        await message.reply_text("🌙 Nightmode: <b>ON</b>")
    elif arg in ("off", "disable"):
        _nightmode_chats.discard(chat_id)
        await message.reply_text("🌙 Nightmode: <b>OFF</b>")
    else:
        status = "ON" if chat_id in _nightmode_chats else "OFF"
        await message.reply_text(f"Nightmode is <b>{status}</b>")
