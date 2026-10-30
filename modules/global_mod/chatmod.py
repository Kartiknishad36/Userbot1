"""Chat moderation tools"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("purge"))
@sudo_only
async def purge_cmd(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to start purge from there.")
    try:
        msg_ids = list(range(message.reply_to_message.id, message.id))
        await client.delete_messages(message.chat.id, msg_ids)
        await message.reply_text(f"🗑️ Purged {len(msg_ids)} messages.")
    except Exception as e:
        await message.reply_text(f"Purge failed: {e}")

@app.on_message(ub_cmd("del", "delete"))
@sudo_only
async def del_cmd(client, message: Message):
    if message.reply_to_message:
        try:
            await message.reply_to_message.delete()
            await message.delete()
        except Exception as e:
            await message.reply_text(f"Delete failed: {e}")
    else:
        await message.reply_text("Reply to a message to delete it.")
