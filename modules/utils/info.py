"""
.info / .whois — full Telegram user report
"""
import html
from datetime import datetime, timezone
from pyrogram.types import Message
from pyrogram.enums import ChatType, ChatMemberStatus, UserStatus
from core.clients import app
from config import OWNER_ID
from modules.owner.sudoers import ub_cmd, sudo_only

DC_MAP = {1: "Miami, FL, USA", 2: "Amsterdam, NL", 3: "Miami, FL, USA", 4: "Amsterdam, NL", 5: "Singapore"}

def _yn(v):
    return "✅ Yes" if v else "❌ No"

def _esc(s):
    return html.escape(str(s)) if s is not None else "—"

def _status_line(status):
    if status is None:
        return "Hidden / Unknown"
    if status == UserStatus.ONLINE:
        return "🟢 Online"
    if status == UserStatus.OFFLINE:
        return "⚫ Offline"
    if status == UserStatus.RECENTLY:
        return "🟡 Recently"
    if status == UserStatus.LAST_WEEK:
        return "🟠 Last week"
    if status == UserStatus.LAST_MONTH:
        return "🔴 Last month"
    return str(status)

@app.on_message(ub_cmd("info", "whois"))
@sudo_only
async def info_cmd(client, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
    else:
        parts = (message.text or "").split()
        target = parts[1].lstrip("@") if len(parts) > 1 else "me"

    status_msg = await message.reply_text("⏳ <b>Scanning...</b>")
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

        lines = [
            "💎 <b>YASHIKA FULL USER INFO</b>",
            "",
            f"👤 Name: <b>{_esc(full) or '—'}</b>",
            f"🔖 Username: @{_esc(user.username) if user.username else '—'}",
            f"🆔 User ID: <code>{user.id}</code>",
            f"📱 Phone: <code>{_esc(getattr(user, 'phone_number', None) or '— (privacy)')}</code>",
            f"📡 Status: {status}",
            f"🏛️ DC: <code>{dc or '—'}</code> ({dc_loc})",
            f"📝 Bio: {_esc(str(bio)[:300])}",
            "",
            f"⭐ Premium: {_yn(getattr(user, 'is_premium', False))}",
            f"✅ Verified: {_yn(getattr(user, 'is_verified', False))}",
            f"🤖 Bot: {_yn(user.is_bot)}",
            f"🗑️ Deleted: {_yn(getattr(user, 'is_deleted', False))}",
            f"🎭 Fake: {_yn(getattr(user, 'is_fake', False))}",
            f"⚠️ Scam: {_yn(getattr(user, 'is_scam', False))}",
            f"👥 Common chats: <code>{len(common_list)}</code>",
            f"👑 Is OWNER: {_yn(is_owner)}",
            "",
            f"⏱️ Generated: <code>{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}</code>",
            "💎 <b>Yashika Premium</b>",
        ]
        text = "\n".join(lines)
        try:
            await status_msg.delete()
        except Exception:
            pass
        await message.reply_text(text)
    except Exception as e:
        try:
            await status_msg.edit_text(f"❌ <code>{e}</code>")
        except Exception:
            await message.reply_text(f"❌ <code>{e}</code>")
