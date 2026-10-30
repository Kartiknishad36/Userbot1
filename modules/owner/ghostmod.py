"""Ghost mode"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("ghost"))
@sudo_only
async def ghost_cmd(client, message: Message):
    await message.reply_text("👻 Ghost mode module loaded.")
