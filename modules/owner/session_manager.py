"""Multi-session manager"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

async def boot_saved_sessions():
    pass

@app.on_message(ub_cmd("sessions", "session"))
@sudo_only
async def sessions_cmd(client, message: Message):
    await message.reply_text("🔑 Session manager loaded.")
