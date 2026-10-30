"""PM Guard"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("pmguard", "approve", "disapprove"))
@sudo_only
async def pmguard_cmd(client, message: Message):
    await message.reply_text("🛡️ PM Guard module loaded.")
