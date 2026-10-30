"""Raid / spam controls (owner only - use responsibly)"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("raid", "spam"))
@sudo_only
async def raid_cmd(client, message: Message):
    await message.reply_text(
        "⚠️ Raid/Spam module loaded.\n"
        "This feature can violate Telegram ToS if misused.\n"
        "Use only on your own accounts and chats."
    )
