"""Profile clone / back"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_original_profile = {}

@app.on_message(ub_cmd("clone"))
@sudo_only
async def clone_cmd(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply_text("Reply to a user to clone their profile.")
    target = message.reply_to_message.from_user
    try:
        me = await client.get_me()
        # Save original
        _original_profile["first_name"] = me.first_name
        _original_profile["last_name"] = me.last_name
        _original_profile["bio"] = getattr(await client.get_chat("me"), "bio", None)
        # Clone
        await client.update_profile(first_name=target.first_name or "Cloned", last_name=target.last_name or "")
        await message.reply_text(f"👤 Cloned profile of {target.first_name} (@{target.username or target.id})")
    except Exception as e:
        await message.reply_text(f"Clone failed: {e}")

@app.on_message(ub_cmd("back"))
@sudo_only
async def back_cmd(client, message: Message):
    if not _original_profile:
        return await message.reply_text("No original profile saved. Clone someone first.")
    try:
        await client.update_profile(
            first_name=_original_profile.get("first_name") or "User",
            last_name=_original_profile.get("last_name") or ""
        )
        await message.reply_text("🔄 Profile restored.")
    except Exception as e:
        await message.reply_text(f"Restore failed: {e}")
