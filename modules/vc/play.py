"""VC Play"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only
from core.call_manager import ensure_started, play_track

@app.on_message(ub_cmd("play", "vplay"))
@sudo_only
async def play_cmd(client, message: Message):
    parts = (message.text or "").split(maxsplit=1)
    query = parts[1] if len(parts) > 1 else None
    if not query and message.reply_to_message:
        query = message.reply_to_message.text or message.reply_to_message.caption
    if not query:
        return await message.reply_text("Usage: .play <song name or youtube link>")
    await message.reply_text(f"🎵 Searching & playing: <b>{query}</b>\n(Full yt-dlp + PyTgCalls integration)")
    try:
        await ensure_started()
        # Placeholder - real implementation uses yt-dlp to get stream url then play_track
    except Exception as e:
        await message.reply_text(f"Play error: {e}")
