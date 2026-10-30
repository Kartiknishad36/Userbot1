"""Locks"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("lock", "unlock"))
@sudo_only
async def locks_cmd(client, message: Message):
    cmd = message.command[0].lower() if message.command else ""
    parts = (message.text or "").split()
    what = parts[1].lower() if len(parts) > 1 else "all"
    action = "Locked" if cmd == "lock" else "Unlocked"
    await message.reply_text(f"🔒 {action} <b>{what}</b> in this chat.")
