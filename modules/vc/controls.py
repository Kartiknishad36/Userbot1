"""VC Controls"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("skip", "pause", "resume", "stop", "queue"))
@sudo_only
async def controls_cmd(client, message: Message):
    await message.reply_text("⏯️ VC Controls module loaded.")
