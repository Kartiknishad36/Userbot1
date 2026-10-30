"""Basic commands: .ping .alive"""
from datetime import datetime
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only
from config import BOT_NAME, BOT_VERSION if False else None
from config import BOT_NAME as BN

NAME = BN or "Userbot1"
START = datetime.now()


@app.on_message(ub_cmd("ping", "alive"))
@sudo_only
async def ping_cmd(client, message: Message):
    t0 = datetime.now()
    msg = await message.reply_text("⚡ Pinging...")
    ms = (datetime.now() - t0).total_seconds() * 1000
    up = datetime.now() - START
    hours, rem = divmod(int(up.total_seconds()), 3600)
    mins, secs = divmod(rem, 60)
    uptime = f"{hours}h {mins}m {secs}s" if hours else f"{mins}m {secs}s"
    me = await client.get_me()
    await msg.edit_text(
        f"💎 <b>{NAME}</b>\n"
        f"━━━━━━━━━━━━\n"
        f"⚡ Ping: <code>{ms:.0f} ms</code>\n"
        f"⏱ Uptime: <code>{uptime}</code>\n"
        f"👤 Account: <b>{me.first_name}</b>\n"
        f"🆔 <code>{me.id}</code>\n"
        f"✅ Status: <b>ONLINE</b>"
    )
