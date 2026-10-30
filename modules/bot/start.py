"""Bot /start and basic handlers"""
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME, OWNER_ID, OWNER_USERNAME, SUPPORT_CHAT, UPDATE_CHANNEL
from core.clients import bot


@bot.on_message(filters.command(["start", "help"]) & filters.private)
async def start_cmd(client: Client, message: Message):
    text = (
        f"✨ <b>{BOT_NAME or 'Yashika'} Premium</b>\n\n"
        "Bot + Userbot hybrid.\n"
        "Owner-only commands use <code>.</code> prefix on the user account.\n\n"
        "Use /login to generate STRING_SESSION (private chat only)."
    )
    buttons = []
    if SUPPORT_CHAT:
        buttons.append([InlineKeyboardButton("Support", url=SUPPORT_CHAT)])
    if UPDATE_CHANNEL:
        buttons.append([InlineKeyboardButton("Updates", url=UPDATE_CHANNEL)])
    if OWNER_USERNAME:
        buttons.append([InlineKeyboardButton("Owner", url=f"https://t.me/{OWNER_USERNAME}")])
    markup = InlineKeyboardMarkup(buttons) if buttons else None
    await message.reply_text(text, reply_markup=markup)
