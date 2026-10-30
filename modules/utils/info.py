"""
.info / .whois — detailed Telegram user report
"""
import html
from datetime import datetime, timezone
from pyrogram.types import Message
from pyrogram.enums import UserStatus
from core.clients import app
from config import OWNER_ID, BOT_NAME
from modules.owner.sudoers import ub_cmd, sudo_only

DC_MAP = {
    1: "Miami, FL, USA",
    2: "Amsterdam, NL",
    3: "Miami, FL, USA",
    4: "Amsterdam, NL",
    5: "Singapore",
}

NAME = BOT_NAME or "Userbot1"


def _yn(v):
    return "✅ Yes" if v else "❌ No"


def _esc(s):
    return html.escape(str(s)) if s is not None else "—"


def _status_line(status):
    if status is None:
        return "Hidden / Unknown"
    mapping = {
        UserStatus.ONLINE: "🟢 Online",
        UserStatus.OFFLINE: "⚫ Offline",
        UserStatus.RECENTLY: "🟡 Recently",
        UserStatus.LAST_WEEK: "🟠 Last week",
        UserStatus.LAST_MONTH: "🔴 Last month",
    }
    return mapping.get(status, str(status))


@app.on_message(ub_cmd("info", "whois"))
@sudo_only
async def info_cmd(client, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
    else:
        parts = (message.text or "").split()
        target = parts[1].lstrip("@") if len(parts) > 1 else "me"

    status_msg = await message.reply_text("⏳ <b>Scanning user...</b>")
    try:
        user = await client.get_users(target)
        try:
            chat = await client.get_chat(user.id)
        except Exception:
            chat = None

        common_list = []
        try:
            common_list = await client.get_common_chats(user.id)
        except Exception:
            pass

        full = (user.first_name or "") + (f" {user.last_name}" if user.last_name else "")
        bio = getattr(chat, "bio", None) or "—"
        status = _status_line(getattr(user, "status", None))
        is_owner = bool(OWNER_ID and user.id == OWNER_ID)
        dc = getattr(user, "dc_id", None)
        dc_loc = DC_MAP.get(dc, "Unknown") if dc else "—"

        # Group status if in group
        member_line = ""
        if message.chat and message.chat.type.name in ("GROUP", "SUPERGROUP"):
            try:
                m = await client.get_chat_member(message.chat.id, user.id)
                member_line = f"📌 Status in this chat: <code>{m.status.value if hasattr(m.status, 'value') else m.status}</code>"
            except Exception:
                member_line = "📌 Status in this chat: Not a member / hidden"

        common_preview = ""
        if common_list:
            names = []
            for c in common_list[:8]:
                title = getattr(c, "title", None) or getattr(c, "first_name", None) or str(c.id)
                names.append(f"• {_esc(title)}")
            common_preview = "\n".join(names)
            if len(common_list) > 8:
                common_preview += f"\n• ... +{len(common_list) - 8} more"

        lines = [
            f"💎 <b>{NAME} — FULL USER INFO</b>",
            "━━━━━━━━━━━━━━━━━━",
            f"👤 <b>Name:</b> {_esc(full) or '—'}",
            f"🔖 <b>Username:</b> @{_esc(user.username) if user.username else '—'}",
            f"🆔 <b>User ID:</b> <code>{user.id}</code>",
            f"🔗 <b>Link:</b> <a href=\"tg://user?id={user.id}\">Open profile</a>",
            f"📱 <b>Phone:</b> <code>{_esc(getattr(user, 'phone_number', None) or '— (privacy)')}</code>",
            f"📡 <b>Status:</b> {status}",
            f"🏛️ <b>DC ID:</b> <code>{dc or '—'}</code> ({dc_loc})",
            f"🌐 <b>Language:</b> <code>{getattr(user, 'language_code', None) or '—'}</code>",
            f"📝 <b>Bio:</b> {_esc(str(bio)[:400])}",
            "━━━━━━━━━━━━━━━━━━",
            f"⭐ <b>Premium:</b> {_yn(getattr(user, 'is_premium', False))}",
            f"✅ <b>Verified:</b> {_yn(getattr(user, 'is_verified', False))}",
            f"🤖 <b>Bot:</b> {_yn(user.is_bot)}",
            f"🗑️ <b>Deleted:</b> {_yn(getattr(user, 'is_deleted', False))}",
            f"🎭 <b>Fake:</b> {_yn(getattr(user, 'is_fake', False))}",
            f"⚠️ <b>Scam:</b> {_yn(getattr(user, 'is_scam', False))}",
            f"🚫 <b>Restricted:</b> {_yn(getattr(user, 'is_restricted', False))}",
            f"📎 <b>Support:</b> {_yn(getattr(user, 'is_support', False))}",
            f"👥 <b>Common chats:</b> <code>{len(common_list)}</code>",
            f"👑 <b>Is OWNER:</b> {_yn(is_owner)}",
        ]
        if member_line:
            lines.append(member_line)
        if common_preview:
            lines.append("")
            lines.append("<b>Common chats preview:</b>")
            lines.append(common_preview)
        lines += [
            "━━━━━━━━━━━━━━━━━━",
            f"⏱️ <code>{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}</code>",
            f"💎 <b>{NAME}</b>",
        ]
        text = "\n".join(lines)
        try:
            await status_msg.delete()
        except Exception:
            pass
        await message.reply_text(text)
    except Exception as e:
        try:
            await status_msg.edit_text(f"❌ <code>{html.escape(str(e))}</code>")
        except Exception:
            await message.reply_text(f"❌ <code>{html.escape(str(e))}</code>")
