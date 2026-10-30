"""Online tracker"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("track", "untrack"))
@sudo_only
async def tracker_cmd(client, message: Message):
    await message.reply_text("📍 Tracker module loaded.")
