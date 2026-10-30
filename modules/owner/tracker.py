"""Online tracker"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_tracked = set()

@app.on_message(ub_cmd("track"))
@sudo_only
async def track_cmd(client, message: Message):
    target = None
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
    else:
        parts = (message.text or "").split(maxsplit=1)
        if len(parts) > 1:
            try:
                target = int(parts[1])
            except ValueError:
                target = parts[1]
    if not target:
        return await message.reply_text("Reply to user or give id/username.\n.track <reply|id>")
    _tracked.add(str(target))
    await message.reply_text(f"📍 Now tracking <code>{target}</code>")

@app.on_message(ub_cmd("untrack"))
@sudo_only
async def untrack_cmd(client, message: Message):
    target = None
    if message.reply_to_message and message.reply_to_message.from_user:
        target = str(message.reply_to_message.from_user.id)
    else:
        parts = (message.text or "").split(maxsplit=1)
        if len(parts) > 1:
            target = parts[1].strip()
    if target in _tracked:
        _tracked.discard(target)
        await message.reply_text(f"Stopped tracking <code>{target}</code>")
    else:
        await message.reply_text("Not tracking that user.")

@app.on_message(ub_cmd("tracklist"))
@sudo_only
async def tracklist_cmd(client, message: Message):
    if not _tracked:
        return await message.reply_text("No one is being tracked.")
    text = "📍 Tracking:\n" + "\n".join(f"• <code>{t}</code>" for t in _tracked)
    await message.reply_text(text)
