"""Locks"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("lock", "unlock"))
@sudo_only
async def locks_cmd(client, message: Message):
    await message.reply_text("🔒 Locks module loaded.")
