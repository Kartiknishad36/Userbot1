"""Remove deleted accounts"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only


@app.on_message(ub_cmd("zombies", "clean"))
@sudo_only
async def zombies_cmd(client, message: Message):
    if message.chat.type.name not in ("GROUP", "SUPERGROUP"):
        return await message.reply_text("Groups only.")
    status = await message.reply_text("🧹 Scanning deleted accounts...")
    removed = 0
    checked = 0
    async for member in client.get_chat_members(message.chat.id):
        checked += 1
        u = member.user
        if u and getattr(u, "is_deleted", False):
            try:
                await client.ban_chat_member(message.chat.id, u.id)
                await client.unban_chat_member(message.chat.id, u.id)
                removed += 1
            except Exception:
                pass
        if checked >= 500:
            break
    await status.edit_text(f"🧹 Checked <b>{checked}</b> | Removed zombies: <b>{removed}</b>")
