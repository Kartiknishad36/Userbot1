"""Chat mod tools"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("purge", "del", "pin", "unpin"))
@sudo_only
async def chatmod_cmd(client, message: Message):
    await message.reply_text("🛠️ Chatmod module loaded.")
