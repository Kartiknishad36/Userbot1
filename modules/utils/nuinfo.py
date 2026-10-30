"""Number info / phone lookup"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("nuinfo", "phone"))
@sudo_only
async def nuinfo_cmd(client, message: Message):
    await message.reply_text("📱 Nuinfo (phone lookup) module loaded.")
