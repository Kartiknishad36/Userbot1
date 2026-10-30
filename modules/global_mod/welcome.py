"""Welcome / goodbye system"""
from pyrogram import filters
from pyrogram.types import Message, ChatMemberUpdated
from pyrogram.enums import ChatMemberStatus
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_welcome = {}
_goodbye = {}
_enabled = set()


def _fmt(template: str, user, chat) -> str:
    name = user.first_name or "User"
    mention = f"<a href='tg://user?id={user.id}'>{name}</a>"
    return (
        template.replace("{mention}", mention)
        .replace("{name}", name)
        .replace("{id}", str(user.id))
        .replace("{chat}", getattr(chat, "title", "") or "Group")
        .replace("{username}", f"@{user.username}" if user.username else name)
    )


@app.on_message(ub_cmd("setwelcome"))
@sudo_only
async def set_welcome(client, message: Message):
    parts = (message.text or "").split(maxsplit=1)
    if len(parts) < 2:
        return await message.reply_text(
            "Usage: <code>.setwelcome Welcome {mention} to {chat}!</code>\n"
            "Vars: {mention} {name} {id} {chat} {username}"
        )
    _welcome[message.chat.id] = parts[1]
    _enabled.add(message.chat.id)
    await message.reply_text("✅ Welcome message set for this chat.")


@app.on_message(ub_cmd("setgoodbye"))
@sudo_only
async def set_goodbye(client, message: Message):
    parts = (message.text or "").split(maxsplit=1)
    if len(parts) < 2:
        return await message.reply_text("Usage: <code>.setgoodbye Bye {name}!</code>")
    _goodbye[message.chat.id] = parts[1]
    await message.reply_text("✅ Goodbye message set.")


@app.on_message(ub_cmd("welcome"))
@sudo_only
async def welcome_toggle(client, message: Message):
    parts = (message.text or "").split()
    chat_id = message.chat.id
    if len(parts) > 1 and parts[1].lower() in ("on", "off"):
        if parts[1].lower() == "on":
            _enabled.add(chat_id)
            await message.reply_text("✅ Welcome ON in this chat.")
        else:
            _enabled.discard(chat_id)
            await message.reply_text("⛔ Welcome OFF in this chat.")
        return
    cur = _welcome.get(chat_id, "Welcome {mention} to {chat}!")
    state = "ON" if chat_id in _enabled else "OFF"
    await message.reply_text(f"Welcome is <b>{state}</b>\n<code>{cur}</code>")


@app.on_chat_member_updated()
async def on_member_update(client, update: ChatMemberUpdated):
    if not update.new_chat_member or not update.new_chat_member.user:
        return
    user = update.new_chat_member.user
    if user.is_bot:
        return
    chat = update.chat
    old = update.old_chat_member.status if update.old_chat_member else None
    new = update.new_chat_member.status
    # joined
    if new in (ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR) and (
        old in (None, ChatMemberStatus.LEFT, ChatMemberStatus.BANNED)
    ):
        if chat.id not in _enabled and chat.id not in _welcome:
            return
        if chat.id in _enabled or chat.id in _welcome:
            tpl = _welcome.get(chat.id, "👋 Welcome {mention} to <b>{chat}</b>!")
            try:
                await client.send_message(chat.id, _fmt(tpl, user, chat))
            except Exception:
                pass
    # left
    if new in (ChatMemberStatus.LEFT, ChatMemberStatus.BANNED) and chat.id in _goodbye:
        try:
            await client.send_message(chat.id, _fmt(_goodbye[chat.id], user, chat))
        except Exception:
            pass
