"""Deep user / chat intel"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("intel", "user", "whois"))
@sudo_only
async def intel_cmd(client, message: Message):
    target = "me"
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
    else:
        parts = (message.text or "").split(maxsplit=1)
        if len(parts) > 1:
            target = parts[1].strip()
    try:
        user = await client.get_users(target)
        common = []
        try:
            common = await client.get_common_chats(user.id)
        except Exception:
            pass
        text = (
            f"🔍 <b>Intel Report</b>\n\n"
            f"Name: {user.first_name or ''} {user.last_name or ''}\n"
            f"Username: @{user.username or '—'}\n"
            f"ID: <code>{user.id}</code>\n"
            f"Premium: {'Yes' if getattr(user, 'is_premium', False) else 'No'}\n"
            f"Common chats: {len(common)}\n"
        )
        await message.reply_text(text)
    except Exception as e:
        await message.reply_text(f"Failed: {e}")
