"""Multi-session manager"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

async def boot_saved_sessions():
    """Called on startup to load any saved extra sessions."""
    pass

@app.on_message(ub_cmd("sessions", "session"))
@sudo_only
async def sessions_cmd(client, message: Message):
    me = await client.get_me()
    text = (
        f"🔑 <b>Session Manager</b>\n\n"
        f"Current: {me.first_name} (<code>{me.id}</code>)\n"
        f"Username: @{me.username or '—'}\n\n"
        "Extra multi-session support can be extended with Mongo."
    )
    await message.reply_text(text)
