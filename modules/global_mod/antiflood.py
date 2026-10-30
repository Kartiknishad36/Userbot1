"""Anti-flood"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_antiflood_chats: dict[int, int] = {}

@app.on_message(ub_cmd("antiflood"))
@sudo_only
async def antiflood_cmd(client, message: Message):
    chat_id = message.chat.id
    parts = (message.text or "").split()
    arg = parts[1].lower() if len(parts) > 1 else ""
    if arg in ("on", "enable"):
        _antiflood_chats[chat_id] = 5
        await message.reply_text("🛡️ Anti-flood: <b>ON</b> (limit 5)")
    elif arg in ("off", "disable"):
        _antiflood_chats.pop(chat_id, None)
        await message.reply_text("🛡️ Anti-flood: <b>OFF</b>")
    else:
        status = "ON" if chat_id in _antiflood_chats else "OFF"
        await message.reply_text(f"Anti-flood is <b>{status}</b>")
