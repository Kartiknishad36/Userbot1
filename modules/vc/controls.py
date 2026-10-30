"""VC Controls"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only
from core.call_manager import stop_stream, pause_stream, resume_stream

@app.on_message(ub_cmd("skip", "stop"))
@sudo_only
async def stop_cmd(client, message: Message):
    try:
        await stop_stream(client, message.chat.id)
        await message.reply_text("⏹️ Stopped.")
    except Exception as e:
        await message.reply_text(f"Error: {e}")

@app.on_message(ub_cmd("pause"))
@sudo_only
async def pause_cmd(client, message: Message):
    try:
        await pause_stream(client, message.chat.id)
        await message.reply_text("⏸️ Paused.")
    except Exception as e:
        await message.reply_text(f"Error: {e}")

@app.on_message(ub_cmd("resume"))
@sudo_only
async def resume_cmd(client, message: Message):
    try:
        await resume_stream(client, message.chat.id)
        await message.reply_text("▶️ Resumed.")
    except Exception as e:
        await message.reply_text(f"Error: {e}")
