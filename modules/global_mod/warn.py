"""Warn system"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("warn"))
@sudo_only
async def warn_cmd(client, message: Message):
    await message.reply_text("⚠️ Warn module loaded.")
