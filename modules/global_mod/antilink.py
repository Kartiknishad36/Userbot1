"""Anti-link"""
import re
from pyrogram import filters
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only, is_sudo

_enabled = set()
LINK_RE = re.compile(r"(https?://|t\.me/|telegram\.me/)", re.I)


@app.on_message(ub_cmd("antilink"))
@sudo_only
async def antilink_cmd(client, message: Message):
    parts = (message.text or "").split()
    chat = message.chat.id
    if len(parts) > 1 and parts[1].lower() == "on":
        _enabled.add(chat)
        return await message.reply_text("🔗 Anti-link ON")
    if len(parts) > 1 and parts[1].lower() == "off":
        _enabled.discard(chat)
        return await message.reply_text("Anti-link OFF")
    state = "ON" if chat in _enabled else "OFF"
    await message.reply_text(f"Anti-link: <b>{state}</b>\nUsage: <code>.antilink on/off</code>")


@app.on_message(filters.group & filters.incoming & ~filters.service)
async def antilink_watch(client, message: Message):
    if message.chat.id not in _enabled:
        return
    if message.from_user and is_sudo(message.from_user.id):
        return
    text = message.text or message.caption or ""
    if LINK_RE.search(text):
        try:
            await message.delete()
        except Exception:
            pass
