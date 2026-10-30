"""Dark spy / monitor helpers"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("spy", "darkspy"))
@sudo_only
async def darkspy_cmd(client, message: Message):
    await message.reply_text(
        "🕵️ <b>Dark Spy</b>\n\n"
        "Monitoring helpers loaded.\n"
        "Use with caution and only on accounts you own."
    )
