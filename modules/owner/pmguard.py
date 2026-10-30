"""PM Guard - approve / disapprove"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_approved: set[int] = set()
_pmguard_on = True

@app.on_message(ub_cmd("pmguard"))
@sudo_only
async def pmguard_toggle(client, message: Message):
    global _pmguard_on
    parts = (message.text or "").split()
    arg = parts[1].lower() if len(parts) > 1 else ""
    if arg in ("on", "enable"):
        _pmguard_on = True
        await message.reply_text("🛡️ PM Guard: <b>ON</b>")
    elif arg in ("off", "disable"):
        _pmguard_on = False
        await message.reply_text("🛡️ PM Guard: <b>OFF</b>")
    else:
        status = "ON" if _pmguard_on else "OFF"
        await message.reply_text(f"PM Guard is <b>{status}</b>\n.approve / .disapprove (reply)")

@app.on_message(ub_cmd("approve"))
@sudo_only
async def approve_cmd(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply_text("Reply to a user to approve.")
    uid = message.reply_to_message.from_user.id
    _approved.add(uid)
    await message.reply_text(f"✅ Approved <code>{uid}</code>")

@app.on_message(ub_cmd("disapprove"))
@sudo_only
async def disapprove_cmd(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply_text("Reply to a user to disapprove.")
    uid = message.reply_to_message.from_user.id
    _approved.discard(uid)
    await message.reply_text(f"❌ Disapproved <code>{uid}</code>")
