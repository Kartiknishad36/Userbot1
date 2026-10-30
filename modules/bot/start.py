"""Bot /start handler"""
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME, OWNER_USERNAME, SUPPORT_CHAT, UPDATE_CHANNEL
from core.clients import bot

NAME = BOT_NAME or "Userbot1"


@bot.on_message(filters.command(["start"]) & filters.private)
async def start_cmd(client, message: Message):
    text = (
        f"💎 <b>{NAME}</b>\n\n"
        "Hybrid <b>Bot + Userbot</b>.\n"
        "User account commands use prefix <code>.</code>\n"
        "Bot commands use <code>/</code>.\n\n"
        "• /help — menu\n"
        "• /login — session helper (owner)\n"
    )
    buttons = []
    row = []
    if SUPPORT_CHAT:
        row.append(InlineKeyboardButton("Support", url=SUPPORT_CHAT if SUPPORT_CHAT.startswith("http") else f"https://t.me/{SUPPORT_CHAT.lstrip('@')}"))
    if UPDATE_CHANNEL:
        row.append(InlineKeyboardButton("Updates", url=UPDATE_CHANNEL if UPDATE_CHANNEL.startswith("http") else f"https://t.me/{UPDATE_CHANNEL.lstrip('@')}"))
    if row:
        buttons.append(row)
    if OWNER_USERNAME:
        buttons.append([InlineKeyboardButton("Owner", url=f"https://t.me/{OWNER_USERNAME}")])
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons) if buttons else None)
