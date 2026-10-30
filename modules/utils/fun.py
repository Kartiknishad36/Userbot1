"""Fun ASCII and random commands"""
import random
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

ASCII_ARTS = {
    "cat": " /\\_/\\ \n( o.o )\n > ^ <",
    "dog": "  __      _\n o'')}____//\n  `_/      )\n  (_(_/-(_/",
    "rose": "@}>--,--'--",
    "moon": "  .---.\n /     \\\n|  o o  |\n \\  ^  /\n  '---'",
}

@app.on_message(ub_cmd("fun", "ascii"))
@sudo_only
async def fun_cmd(client, message: Message):
    parts = (message.text or "").split(maxsplit=1)
    key = parts[1].strip().lower() if len(parts) > 1 else random.choice(list(ASCII_ARTS.keys()))
    art = ASCII_ARTS.get(key, ASCII_ARTS["cat"])
    await message.reply_text(f"<pre>{art}</pre>")

@app.on_message(ub_cmd("cat", "dog", "rose", "moon"))
@sudo_only
async def art_cmd(client, message: Message):
    cmd = (message.command[0] if message.command else "cat").lower()
    art = ASCII_ARTS.get(cmd, ASCII_ARTS["cat"])
    await message.reply_text(f"<pre>{art}</pre>")
