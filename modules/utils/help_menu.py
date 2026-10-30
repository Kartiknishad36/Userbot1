"""Premium help menu"""
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only
from config import BOT_NAME

@app.on_message(ub_cmd("help", "menu"))
@sudo_only
async def help_cmd(client, message: Message):
    text = f"💎 <b>{BOT_NAME or 'Yashika'} Help Menu</b>\n\nSelect a category:"
    buttons = [
        [InlineKeyboardButton("Owner", callback_data="help_owner"),
         InlineKeyboardButton("Mod", callback_data="help_mod")],
        [InlineKeyboardButton("Utils", callback_data="help_utils"),
         InlineKeyboardButton("Fun", callback_data="help_fun")],
        [InlineKeyboardButton("Music", callback_data="help_music")],
    ]
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))
