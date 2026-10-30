"""Simple notes store"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_NOTES: dict[str, str] = {}


@app.on_message(ub_cmd("save"))
@sudo_only
async def save_note(client, message: Message):
    parts = (message.text or "").split(maxsplit=2)
    if len(parts) < 3 and not (message.reply_to_message and len(parts) >= 2):
        return await message.reply_text("Usage: <code>.save name content</code>")
    name = parts[1].lower()
    if len(parts) >= 3:
        content = parts[2]
    else:
        content = message.reply_to_message.text or message.reply_to_message.caption or ""
    _NOTES[name] = content
    await message.reply_text(f"✅ Note <code>{name}</code> saved.")


@app.on_message(ub_cmd("get"))
@sudo_only
async def get_note(client, message: Message):
    parts = (message.text or "").split(maxsplit=1)
    if len(parts) < 2:
        return await message.reply_text("Usage: <code>.get name</code>")
    name = parts[1].lower().strip()
    if name not in _NOTES:
        return await message.reply_text("Note not found.")
    await message.reply_text(_NOTES[name])


@app.on_message(ub_cmd("clear"))
@sudo_only
async def clear_note(client, message: Message):
    parts = (message.text or "").split(maxsplit=1)
    if len(parts) < 2:
        return await message.reply_text("Usage: <code>.clear name</code>")
    name = parts[1].lower().strip()
    _NOTES.pop(name, None)
    await message.reply_text(f"🗑️ Cleared <code>{name}</code>")


@app.on_message(ub_cmd("notes"))
@sudo_only
async def list_notes(client, message: Message):
    if not _NOTES:
        return await message.reply_text("No notes.")
    text = "📝 <b>Notes</b>\n" + "\n".join(f"• <code>{k}</code>" for k in _NOTES)
    await message.reply_text(text)
