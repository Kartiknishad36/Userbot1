"""Global ban helpers"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_GBANNED: set[int] = set()


@app.on_message(ub_cmd("gban"))
@sudo_only
async def gban_cmd(client, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user:
        uid = message.reply_to_message.from_user.id
        name = message.reply_to_message.from_user.first_name
    else:
        parts = (message.text or "").split(maxsplit=1)
        if len(parts) < 2:
            return await message.reply_text("Reply or: <code>.gban user_id</code>")
        try:
            uid = int(parts[1])
            name = str(uid)
        except ValueError:
            try:
                u = await client.get_users(parts[1])
                uid, name = u.id, u.first_name
            except Exception:
                return await message.reply_text("User not found.")
    _GBANNED.add(uid)
    # try ban in current chat
    try:
        if message.chat.type.name in ("GROUP", "SUPERGROUP"):
            await client.ban_chat_member(message.chat.id, uid)
    except Exception:
        pass
    await message.reply_text(f"🔨 GBan: <b>{name}</b> (<code>{uid}</code>)")


@app.on_message(ub_cmd("ungban"))
@sudo_only
async def ungban_cmd(client, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user:
        uid = message.reply_to_message.from_user.id
    else:
        parts = (message.text or "").split(maxsplit=1)
        if len(parts) < 2:
            return await message.reply_text("Reply or give user id.")
        try:
            uid = int(parts[1])
        except ValueError:
            return await message.reply_text("Invalid id.")
    _GBANNED.discard(uid)
    try:
        if message.chat.type.name in ("GROUP", "SUPERGROUP"):
            await client.unban_chat_member(message.chat.id, uid)
    except Exception:
        pass
    await message.reply_text(f"✅ UnGBan <code>{uid}</code>")


@app.on_message(ub_cmd("gbanlist"))
@sudo_only
async def gbanlist_cmd(client, message: Message):
    if not _GBANNED:
        return await message.reply_text("Empty gban list.")
    text = "🔨 <b>GBan list</b>\n" + "\n".join(f"• <code>{i}</code>" for i in _GBANNED)
    await message.reply_text(text)
