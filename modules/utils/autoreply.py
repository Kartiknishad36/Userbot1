"""Autoreply / style scan"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

async def boot_style_scan():
    pass

@app.on_message(ub_cmd("autoreply"))
@sudo_only
async def autoreply_cmd(client, message: Message):
    await message.reply_text("💬 Autoreply module loaded.")
