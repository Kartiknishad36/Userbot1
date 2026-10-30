"""Sticker kang"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("kang", "steal"))
@sudo_only
async def kang_cmd(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a sticker or photo to kang it.")
    reply = message.reply_to_message
    if reply.sticker:
        await message.reply_text("🖼️ Sticker kang started...\n(Full pack creation needs sticker set API)")
    elif reply.photo:
        await message.reply_text("🖼️ Photo to sticker conversion started...")
    else:
        await message.reply_text("Reply to a sticker or photo.")
