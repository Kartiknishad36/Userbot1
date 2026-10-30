"""Global ban"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_gbanned = set()

@app.on_message(ub_cmd("gban"))
@sudo_only
async def gban_cmd(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply_text("Reply to a user to gban.")
    uid = message.reply_to_message.from_user.id
    _gbanned.add(uid)
    await message.reply_text(f"🚫 Globally banned <code>{uid}</code>")

@app.on_message(ub_cmd("ungban"))
@sudo_only
async def ungban_cmd(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply_text("Reply to a user to ungban.")
    uid = message.reply_to_message.from_user.id
    _gbanned.discard(uid)
    await message.reply_text(f"✅ Ungban <code>{uid}</code>")
