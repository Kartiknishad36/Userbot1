"""Tag all members — .tagall .tag .all"""
import asyncio
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only


@app.on_message(ub_cmd("tagall", "tag", "all"))
@sudo_only
async def tagall_cmd(client, message: Message):
    if message.chat.type.name not in ("GROUP", "SUPERGROUP"):
        return await message.reply_text("❌ Only works in groups.")

    parts = (message.text or "").split(maxsplit=1)
    extra = parts[1] if len(parts) > 1 else "👋 Hi everyone!"

    status = await message.reply_text("⏳ Collecting members...")
    batch = []
    total = 0
    sent = 0

    try:
        async for member in client.get_chat_members(message.chat.id):
            u = member.user
            if not u or u.is_bot:
                continue
            name = u.first_name or "User"
            batch.append(f"<a href='tg://user?id={u.id}'>{name}</a>")
            total += 1
            if len(batch) >= 15:
                await message.reply_text(extra + "\n\n" + " ".join(batch))
                sent += 1
                batch = []
                await asyncio.sleep(0.7)
            if total >= 200:
                break

        if batch:
            await message.reply_text(extra + "\n\n" + " ".join(batch))
            sent += 1

        try:
            await status.edit_text(f"✅ Tagged <b>{total}</b> members in <b>{sent}</b> messages.")
        except Exception:
            pass
        try:
            await message.delete()
        except Exception:
            pass
    except Exception as e:
        await status.edit_text(f"❌ <code>{e}</code>")
