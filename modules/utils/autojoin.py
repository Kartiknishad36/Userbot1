"""Autojoin module"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("autojoin", "join"))
@sudo_only
async def autojoin_cmd(client, message: Message):
    await message.reply_text("🔗 Autojoin module loaded.")
