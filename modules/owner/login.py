"""Userbot login helpers"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("login"))
@sudo_only
async def login_cmd(client, message: Message):
    await message.reply_text("Use /login on the bot for interactive session generation.")
