"""AFK mode"""
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_AFK = {"on": False, "reason": "", "since": None}


@app.on_message(ub_cmd("afk"))
@sudo_only
async def afk_on(client, message: Message):
    parts = (message.text or "").split(maxsplit=1)
    reason = parts[1] if len(parts) > 1 else "AFK"
    _AFK["on"] = True
    _AFK["reason"] = reason
    _AFK["since"] = datetime.now()
    await message.reply_text(f"💤 AFK on\nReason: <b>{reason}</b>")


@app.on_message(ub_cmd("unafk"))
@sudo_only
async def afk_off(client, message: Message):
    _AFK["on"] = False
    await message.reply_text("✅ Back online (AFK off).")


@app.on_message(filters.mentioned & filters.incoming & ~filters.bot)
async def afk_reply(client, message: Message):
    if not _AFK["on"]:
        return
    since = _AFK["since"]
    dur = ""
    if since:
        secs = int((datetime.now() - since).total_seconds())
        m, s = divmod(secs, 60)
        h, m = divmod(m, 60)
        dur = f"{h}h {m}m" if h else f"{m}m {s}s"
    await message.reply_text(
        f"💤 Owner is AFK\nReason: <b>{_AFK['reason']}</b>\nSince: <code>{dur}</code>"
    )
