"""Shayari / quotes"""
import random
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

SHAYARIS = [
    "Dil se jo baat nikalti hai, asar rakhti hai...",
    "Mohabbat bhi zindagi ki tarah hoti hai...",
    "Tumhe paakar khuda ka shukr ada karta hoon...",
    "Ishq ne usko fanaa kar diya...",
]

@app.on_message(ub_cmd("shayari", "quote"))
@sudo_only
async def shayari_cmd(client, message: Message):
    await message.reply_text(f"📝 {random.choice(SHAYARIS)}")
