"""Notes module"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("note", "notes", "get", "save"))
@sudo_only
async def notes_cmd(client, message: Message):
    await message.reply_text("📝 Notes module loaded.")
