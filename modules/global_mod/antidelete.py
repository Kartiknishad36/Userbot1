"""Anti-delete"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_antidelete_chats: set[int] = set()

@app.on_message(ub_cmd("antidelete"))
@sudo_only
async def antidelete_cmd(client, message: Message):
    chat_id = message.chat.id
    parts = (message.text or "").split()
    arg = parts[1].lower() if len(parts) > 1 else ""
    if arg in ("on", "enable"):
        _antidelete_chats.add(chat_id)
        await message.reply_text("🛡️ Anti-delete: <b>ON</b>")
    elif arg in ("off", "disable"):
        _antidelete_chats.discard(chat_id)
        await message.reply_text("🛡️ Anti-delete: <b>OFF</b>")
    else:
        status = "ON" if chat_id in _antidelete_chats else "OFF"
        await message.reply_text(f"Anti-delete is <b>{status}</b>")
