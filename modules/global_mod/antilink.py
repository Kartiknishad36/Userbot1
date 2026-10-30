"""Anti-link"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_antilink_chats: set[int] = set()

@app.on_message(ub_cmd("antilink"))
@sudo_only
async def antilink_cmd(client, message: Message):
    chat_id = message.chat.id
    parts = (message.text or "").split()
    arg = parts[1].lower() if len(parts) > 1 else ""
    if arg in ("on", "enable"):
        _antilink_chats.add(chat_id)
        await message.reply_text("🔗 Anti-link: <b>ON</b> for this chat")
    elif arg in ("off", "disable"):
        _antilink_chats.discard(chat_id)
        await message.reply_text("🔗 Anti-link: <b>OFF</b> for this chat")
    else:
        status = "ON" if chat_id in _antilink_chats else "OFF"
        await message.reply_text(f"Anti-link is <b>{status}</b>\nUsage: .antilink on/off")
