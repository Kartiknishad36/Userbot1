"""Download helpers"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("dl", "download"))
@sudo_only
async def download_cmd(client, message: Message):
    await message.reply_text("⬇️ Download module loaded.")
