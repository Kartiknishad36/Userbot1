"""Autoreply + style learning"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_style_enabled = False

async def boot_style_scan():
    pass

@app.on_message(ub_cmd("autoreply"))
@sudo_only
async def autoreply_cmd(client, message: Message):
    global _style_enabled
    parts = (message.text or "").split()
    arg = parts[1].lower() if len(parts) > 1 else ""
    if arg in ("on", "enable", "1", "true"):
        _style_enabled = True
        await message.reply_text("💬 Autoreply style learning: <b>ON</b>")
    elif arg in ("off", "disable", "0", "false"):
        _style_enabled = False
        await message.reply_text("💬 Autoreply style learning: <b>OFF</b>")
    else:
        status = "ON" if _style_enabled else "OFF"
        await message.reply_text(
            f"Autoreply is currently <b>{status}</b>\n"
            "Usage: .autoreply on / off"
        )
