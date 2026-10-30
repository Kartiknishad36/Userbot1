"""Zombies cleaner"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("zombies"))
@sudo_only
async def zombies_cmd(client, message: Message):
    if message.chat.type.name not in ("GROUP", "SUPERGROUP"):
        return await message.reply_text("Only in groups.")
    await message.reply_text("🧟 Scanning for deleted accounts...")
    count = 0
    async for member in client.get_chat_members(message.chat.id):
        if member.user and getattr(member.user, "is_deleted", False):
            count += 1
    await message.reply_text(f"Found <b>{count}</b> deleted accounts.")
