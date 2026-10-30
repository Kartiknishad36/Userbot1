"""Download media / links"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("dl", "download"))
@sudo_only
async def download_cmd(client, message: Message):
    if message.reply_to_message:
        await message.reply_text("⬇️ Downloading replied media...")
    else:
        parts = (message.text or "").split(maxsplit=1)
        if len(parts) > 1:
            await message.reply_text(f"⬇️ Downloading: {parts[1]}")
        else:
            await message.reply_text("Usage: .dl <reply or link>")
