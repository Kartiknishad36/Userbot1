"""
.bro / .broall / .brodm / .brogroup / .unbro / .brolist
Full roast list (200+) — pahle jesa
"""
import asyncio
import json
import random
from pathlib import Path

from pyrogram.types import Message
from pyrogram.enums import ChatType

from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

# Load roast lists if present
_BRO_LISTS = []
for part in ["bro_part_2.json", "bro_part_3.json", "bro_part_4.json"]:
    p = Path(__file__).parent / part
    if p.exists():
        try:
            with open(p, encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    _BRO_LISTS.extend(data)
                elif isinstance(data, dict) and "roasts" in data:
                    _BRO_LISTS.extend(data["roasts"])
        except Exception:
            pass

if not _BRO_LISTS:
    _BRO_LISTS = [
        "Bhai tu toh full comedy kar raha hai",
        "Itna attitude kahan se laaya",
        "Chal nikal yahan se",
        "Tera dimaag toh bilkul khali hai",
    ]

_active_bros = set()  # simple in-memory targets

@app.on_message(ub_cmd("bro"))
@sudo_only
async def bro_cmd(client, message: Message):
    target = None
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
    else:
        parts = (message.text or "").split(maxsplit=1)
        if len(parts) > 1:
            try:
                target = int(parts[1])
            except ValueError:
                target = parts[1]
    if not target:
        return await message.reply_text("Reply to a user or give user id/username.\nUsage: .bro <reply|id>")
    _active_bros.add(str(target))
    roast = random.choice(_BRO_LISTS)
    await message.reply_text(f"👫 Bro activated on <code>{target}</code>\n\n{roast}")

@app.on_message(ub_cmd("unbro"))
@sudo_only
async def unbro_cmd(client, message: Message):
    target = None
    if message.reply_to_message and message.reply_to_message.from_user:
        target = str(message.reply_to_message.from_user.id)
    else:
        parts = (message.text or "").split(maxsplit=1)
        if len(parts) > 1:
            target = parts[1].strip()
    if target and target in _active_bros:
        _active_bros.discard(target)
        await message.reply_text(f"Unbro done for <code>{target}</code>")
    else:
        await message.reply_text("No active bro found for that target.")

@app.on_message(ub_cmd("brolist"))
@sudo_only
async def brolist_cmd(client, message: Message):
    if not _active_bros:
        return await message.reply_text("No active bros.")
    text = "👫 Active Bros:\n" + "\n".join(f"• <code>{t}</code>" for t in _active_bros)
    await message.reply_text(text)
