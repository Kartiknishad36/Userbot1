"""Auto-delete helpers for bot and userbot replies."""
import asyncio
from pyrogram import Client
from pyrogram.types import Message
from config import AUTO_DELETE, DELETE_DELAY


def register_bot_autodelete(client: Client):
    if not AUTO_DELETE:
        return

    @client.on_message()
    async def _bot_autodelete(_, message: Message):
        if message.outgoing or not message.from_user or not message.from_user.is_self:
            return
        # only auto-delete bot's own replies that look like command responses
        try:
            await asyncio.sleep(DELETE_DELAY)
            await message.delete()
        except Exception:
            pass


def register_trigger_autodelete(client: Client, enabled: bool = True):
    if not enabled or not AUTO_DELETE:
        return

    @client.on_message()
    async def _ub_autodelete(_, message: Message):
        if not message.outgoing:
            return
        # delete after delay for command-like messages
        text = (message.text or message.caption or "").strip()
        if text.startswith((".", "!", "/")):
            try:
                await asyncio.sleep(DELETE_DELAY)
                await message.delete()
            except Exception:
                pass
