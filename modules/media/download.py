"""Download replied media"""
import os
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only


@app.on_message(ub_cmd("dl", "download"))
@sudo_only
async def download_cmd(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a media message.")
    r = message.reply_to_message
    status = await message.reply_text("⬇️ Downloading...")
    try:
        path = await r.download()
        if not path:
            return await status.edit_text("Nothing to download.")
        size = os.path.getsize(path)
        await status.edit_text(
            f"✅ Downloaded\n"
            f"📁 <code>{os.path.basename(path)}</code>\n"
            f"📦 {size / 1024:.1f} KB"
        )
        try:
            await message.reply_document(path, caption=os.path.basename(path))
        except Exception:
            pass
        try:
            os.remove(path)
        except Exception:
            pass
    except Exception as e:
        await status.edit_text(f"❌ {e}")
