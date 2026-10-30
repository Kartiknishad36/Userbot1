"""Anti-flood"""
import time
from collections import defaultdict
from pyrogram import filters
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only, is_sudo

_enabled = {}
_hits = defaultdict(list)  # (chat, user) -> timestamps


@app.on_message(ub_cmd("antiflood", "setflood"))
@sudo_only
async def antiflood_cmd(client, message: Message):
    parts = (message.text or "").split()
    chat = message.chat.id
    if len(parts) >= 2 and parts[1].lower() == "off":
        _enabled.pop(chat, None)
        return await message.reply_text("Anti-flood OFF")
    limit = 5
    if len(parts) >= 2 and parts[1].isdigit():
        limit = max(3, min(20, int(parts[1])))
    _enabled[chat] = limit
    await message.reply_text(f"🌊 Anti-flood ON — max <b>{limit}</b> msgs / 8s")


@app.on_message(filters.group & filters.incoming & ~filters.service)
async def flood_watch(client, message: Message):
    chat = message.chat.id
    if chat not in _enabled or not message.from_user:
        return
    if is_sudo(message.from_user.id):
        return
    uid = message.from_user.id
    now = time.time()
    key = (chat, uid)
    _hits[key] = [t for t in _hits[key] if now - t < 8]
    _hits[key].append(now)
    if len(_hits[key]) > _enabled[chat]:
        try:
            await message.delete()
        except Exception:
            pass
