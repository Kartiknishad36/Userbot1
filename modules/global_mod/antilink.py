"""Anti-link module"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("antilink"))
@sudo_only
async def antilink_cmd(client, message: Message):
    await message.reply_text("🔗 Anti-link module loaded.")
