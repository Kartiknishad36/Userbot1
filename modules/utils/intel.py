"""Intel / user scan"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("intel", "user"))
@sudo_only
async def intel_cmd(client, message: Message):
    await message.reply_text("🔍 Intel module loaded.")
