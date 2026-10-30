"""Social media download helpers"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("insta", "ig", "tiktok", "yt"))
@sudo_only
async def social_cmd(client, message: Message):
    parts = (message.text or "").split(maxsplit=1)
    if len(parts) < 2:
        return await message.reply_text("Usage: .insta / .tiktok / .yt <link>")
    await message.reply_text(f"📱 Processing: {parts[1]}")
