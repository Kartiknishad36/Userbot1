"""Fun commands"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("fun", "cat", "dog", "meme"))
@sudo_only
async def fun_cmd(client, message: Message):
    await message.reply_text("🎉 Fun module loaded.")
