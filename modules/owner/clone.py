"""Profile clone commands"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("clone"))
@sudo_only
async def clone_cmd(client, message: Message):
    await message.reply_text("👤 Clone module loaded. Use .clone <reply/user> to clone profile.")

@app.on_message(ub_cmd("back"))
@sudo_only
async def back_cmd(client, message: Message):
    await message.reply_text("🔄 Revert clone - module loaded.")
