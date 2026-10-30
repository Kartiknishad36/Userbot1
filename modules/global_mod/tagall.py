"""Tagall module"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("tagall", "tag"))
@sudo_only
async def tagall_cmd(client, message: Message):
    await message.reply_text("👥 Tagall module loaded. Use .tagall to mention all.")
