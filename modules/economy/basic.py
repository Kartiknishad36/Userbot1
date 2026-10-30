"""Basic economy commands"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

# Placeholder - full economy can be expanded
@app.on_message(ub_cmd("balance", "bal", "wallet"))
@sudo_only
async def balance_cmd(client, message: Message):
    await message.reply_text("💰 Economy module loaded. Balance system ready.")
