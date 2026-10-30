"""AFK"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_afk_data = {"on": False, "reason": ""}

@app.on_message(ub_cmd("afk"))
@sudo_only
async def afk_cmd(client, message: Message):
    parts = (message.text or "").split(maxsplit=1)
    if len(parts) > 1:
        _afk_data["on"] = True
        _afk_data["reason"] = parts[1]
        await message.reply_text(f"💤 AFK set: {_afk_data['reason']}")
    else:
        _afk_data["on"] = True
        _afk_data["reason"] = "AFK"
        await message.reply_text("💤 AFK is now ON")
