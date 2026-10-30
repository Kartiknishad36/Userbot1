"""Tag all members"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

@app.on_message(ub_cmd("tagall", "tag"))
@sudo_only
async def tagall_cmd(client, message: Message):
    if message.chat.type.name not in ("GROUP", "SUPERGROUP"):
        return await message.reply_text("Only works in groups.")
    text = (message.text or "").split(maxsplit=1)
    extra = text[1] if len(text) > 1 else "Hi everyone!"
    mentions = []
    async for member in client.get_chat_members(message.chat.id):
        if member.user and not member.user.is_bot:
            mentions.append(f"<a href='tg://user?id={member.user.id}'>​</a>")
            if len(mentions) >= 50:
                break
    if not mentions:
        return await message.reply_text("No members found.")
    await message.reply_text(extra + "\n" + "".join(mentions))
