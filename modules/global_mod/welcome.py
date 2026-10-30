"""Welcome"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_welcome_text = "Welcome {mention} to the group!"

@app.on_message(ub_cmd("setwelcome", "welcome"))
@sudo_only
async def welcome_cmd(client, message: Message):
    global _welcome_text
    parts = (message.text or "").split(maxsplit=1)
    if len(parts) > 1:
        _welcome_text = parts[1]
        await message.reply_text("✅ Welcome message updated.")
    else:
        await message.reply_text(f"Current welcome:\n<code>{_welcome_text}</code>")
