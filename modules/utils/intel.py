"""Deep intel + chatinfo"""
import html
from pyrogram.types import Message
from pyrogram.enums import ChatType
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only
from config import BOT_NAME

NAME = BOT_NAME or "Userbot1"


@app.on_message(ub_cmd("intel", "user"))
@sudo_only
async def intel_cmd(client, message: Message):
    target = "me"
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
    else:
        parts = (message.text or "").split(maxsplit=1)
        if len(parts) > 1:
            target = parts[1].strip().lstrip("@")
    try:
        user = await client.get_users(target)
        common = []
        try:
            common = await client.get_common_chats(user.id)
        except Exception:
            pass
        full = f"{user.first_name or ''} {user.last_name or ''}".strip()
        text = (
            f"🔍 <b>{NAME} Intel Report</b>\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"👤 Name: <b>{html.escape(full)}</b>\n"
            f"🔖 Username: @{user.username or '—'}\n"
            f"🆔 ID: <code>{user.id}</code>\n"
            f"🔗 <a href=\"tg://user?id={user.id}\">Open DM</a>\n"
            f"⭐ Premium: {'Yes' if getattr(user, 'is_premium', False) else 'No'}\n"
            f"✅ Verified: {'Yes' if getattr(user, 'is_verified', False) else 'No'}\n"
            f"🤖 Bot: {'Yes' if user.is_bot else 'No'}\n"
            f"🗑️ Deleted: {'Yes' if getattr(user, 'is_deleted', False) else 'No'}\n"
            f"👥 Common chats: <code>{len(common)}</code>\n"
        )
        if common:
            text += "\n<b>Common (top 10):</b>\n"
            for c in common[:10]:
                title = getattr(c, "title", None) or getattr(c, "first_name", "?")
                text += f"• {html.escape(str(title))} (<code>{c.id}</code>)\n"
        await message.reply_text(text)
    except Exception as e:
        await message.reply_text(f"❌ <code>{e}</code>")


@app.on_message(ub_cmd("chatinfo", "groupinfo"))
@sudo_only
async def chatinfo_cmd(client, message: Message):
    chat = message.chat
    try:
        full = await client.get_chat(chat.id)
    except Exception:
        full = chat
    members = getattr(full, "members_count", None) or "—"
    text = (
        f"💬 <b>Chat Info</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"📌 Title: <b>{html.escape(getattr(full, 'title', None) or getattr(full, 'first_name', '—') or '—')}</b>\n"
        f"🆔 ID: <code>{full.id}</code>\n"
        f"📂 Type: <code>{full.type.name if hasattr(full.type, 'name') else full.type}</code>\n"
        f"👥 Members: <code>{members}</code>\n"
        f"🔖 Username: @{getattr(full, 'username', None) or '—'}\n"
        f"📝 Bio/Desc: {html.escape(str(getattr(full, 'description', None) or getattr(full, 'bio', None) or '—')[:300])}\n"
    )
    await message.reply_text(text)
