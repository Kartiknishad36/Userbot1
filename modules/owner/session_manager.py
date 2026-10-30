"""Multi-session manager"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

async def boot_saved_sessions():
    """Load any saved extra sessions on boot."""
    pass

@app.on_message(ub_cmd("sessions", "session"))
@sudo_only
async def sessions_cmd(client, message: Message):
    me = await client.get_me()
    text = (
        f"🔑 <b>Session Manager</b>\n\n"
        f"Current account: <b>{me.first_name}</b>\n"
        f"ID: <code>{me.id}</code>\n"
        f"Username: @{me.username or '—'}\n\n"
        "Commands:\n"
        ".sessions - show current\n"
        "Use /login on the bot to generate new STRING_SESSION"
    )
    await message.reply_text(text)
