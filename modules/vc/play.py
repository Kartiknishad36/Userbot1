"""VC Play"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("play", "vplay"))
@sudo_only
async def play_cmd(client, message: Message):
    await message.reply_text("🎵 Play module loaded. Use .play <query>")
