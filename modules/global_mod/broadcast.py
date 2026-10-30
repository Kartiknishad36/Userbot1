"""Broadcast / Gcast"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("broadcast", "gcast"))
@sudo_only
async def broadcast_cmd(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to broadcast it.")
    await message.reply_text("📢 Broadcast started...\n(This will send to all dialogs - use carefully)")
