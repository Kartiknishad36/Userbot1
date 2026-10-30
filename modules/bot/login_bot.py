"""Bot /login — phone → OTP → 2FA → session in LOG_GROUP + extra client"""
from typing import Any

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from pyrogram.errors import (
    PhoneCodeInvalid, PhoneCodeExpired, PhoneNumberInvalid,
    SessionPasswordNeeded, PasswordHashInvalid, FloodWait
)
from config import API_ID, API_HASH, LOG_GROUP_ID, OWNER_ID
from core.clients import bot
import asyncio

# Simple in-memory state for login flow
_login_state: dict[int, dict] = {}

@bot.on_message(filters.command("login") & filters.private)
async def login_start(client: Client, message: Message):
    if OWNER_ID and message.from_user.id != OWNER_ID:
        return await message.reply_text("Only owner can use /login.")
    _login_state[message.from_user.id] = {"step": "phone"}
    await message.reply_text(
        "📱 <b>Login Flow</b>\n\n"
        "Send your phone number with country code.\n"
        "Example: <code>+919876543210</code>\n\n"
        "Send /cancel to abort."
    )

@bot.on_message(filters.private & filters.text & ~filters.command(["login", "cancel", "start", "help"]))
async def login_flow(client: Client, message: Message):
    uid = message.from_user.id
    if uid not in _login_state:
        return
    state = _login_state[uid]
    text = (message.text or "").strip()

    if text.lower() == "/cancel":
        _login_state.pop(uid, None)
        return await message.reply_text("Login cancelled.")

    try:
        if state["step"] == "phone":
            phone = text
            temp = Client("temp_login", api_id=API_ID, api_hash=API_HASH, in_memory=True)
            await temp.connect()
            sent = await temp.send_code(phone)
            state.update({"step": "code", "phone": phone, "phone_code_hash": sent.phone_code_hash, "temp": temp})
            await message.reply_text("✅ Code sent! Enter the OTP you received.")
        elif state["step"] == "code":
            temp: Client = state["temp"]
            try:
                await temp.sign_in(state["phone"], state["phone_code_hash"], text)
            except SessionPasswordNeeded:
                state["step"] = "2fa"
                return await message.reply_text("2FA enabled. Send your cloud password.")
            session = await temp.export_session_string()
            await temp.disconnect()
            _login_state.pop(uid, None)
            await _send_session(client, message, session)
        elif state["step"] == "2fa":
            temp: Client = state["temp"]
            await temp.check_password(text)
            session = await temp.export_session_string()
            await temp.disconnect()
            _login_state.pop(uid, None)
            await _send_session(client, message, session)
    except FloodWait as e:
        await message.reply_text(f"FloodWait: wait {e.value} seconds.")
    except (PhoneCodeInvalid, PhoneCodeExpired, PhoneNumberInvalid, PasswordHashInvalid) as e:
        await message.reply_text(f"Error: {type(e).__name__}. Try /login again.")
        _login_state.pop(uid, None)
    except Exception as e:
        await message.reply_text(f"Failed: {type(e).__name__}: {e}")
        _login_state.pop(uid, None)

async def _send_session(client, message, session: str):
    text = (
        "✅ <b>STRING_SESSION generated</b>\n\n"
        f"<code>{session}</code>\n\n"
        "Put this in your .env as STRING_SESSION=..."
    )
    await message.reply_text(text)
    if LOG_GROUP_ID:
        try:
            await client.send_message(LOG_GROUP_ID, f"New session from {message.from_user.id}\n\n<code>{session}</code>")
        except Exception:
            pass
