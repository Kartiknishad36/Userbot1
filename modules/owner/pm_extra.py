"""PM extra tools"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("pminfo", "pmextra"))
@sudo_only
async def pm_extra_cmd(client, message: Message):
    await message.reply_text("📬 PM Extra tools loaded.")
