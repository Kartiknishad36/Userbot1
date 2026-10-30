"""Basic commands: .ping .alive"""
from datetime import datetime
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only
from config import BOT_NAME

@app.on_message(ub_cmd("ping", "alive"))
@sudo_only
async def ping_cmd(client, message: Message):
    start = datetime.now()
    msg = await message.reply_text("⚡ Pinging...")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit_text(
        f"⚡ <b>{BOT_NAME or 'Yashika'}</b>\n"
        f"Ping: <code>{ms:.2f} ms</code>\n"
        f"Status: Running ✅"
    )
