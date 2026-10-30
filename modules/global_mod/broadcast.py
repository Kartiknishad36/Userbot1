"""Broadcast to dialogs — owner"""
import asyncio
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only
from config import OWNER_ID


@app.on_message(ub_cmd("broadcast", "gcast"))
@sudo_only
async def broadcast_cmd(client, message: Message):
    if OWNER_ID and message.from_user and message.from_user.id != OWNER_ID and not message.outgoing:
        return
    text = ""
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption or ""
    else:
        parts = (message.text or "").split(maxsplit=1)
        if len(parts) > 1:
            text = parts[1]
    if not text:
        return await message.reply_text("Reply to a message or: <code>.broadcast text</code>")

    status = await message.reply_text("📣 Broadcasting...")
    ok = fail = 0
    async for dialog in client.get_dialogs():
        chat = dialog.chat
        if chat.type.name not in ("GROUP", "SUPERGROUP", "CHANNEL"):
            continue
        try:
            await client.send_message(chat.id, text)
            ok += 1
            await asyncio.sleep(0.4)
        except Exception:
            fail += 1
        if ok + fail >= 50:
            break
    await status.edit_text(f"📣 Done. Sent: <b>{ok}</b> | Failed: <b>{fail}</b>")
