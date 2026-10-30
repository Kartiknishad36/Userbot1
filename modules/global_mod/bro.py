"""Bro system"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("bro", "unbro"))
@sudo_only
async def bro_cmd(client, message: Message):
    await message.reply_text("👫 Bro system loaded.")
