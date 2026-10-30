"""Premium button help menu"""
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from core.clients import app, bot
from modules.owner.sudoers import ub_cmd, sudo_only
from config import BOT_NAME

HELP_TEXT = {
    "owner": "👑 <b>Owner</b>\n.clone .back .track .ghost .sessions .pmguard",
    "mod": "🛡️ <b>Moderation</b>\n.tagall .gban .warn .antilink .nightmode .zombies .welcome",
    "utils": "🛠️ <b>Utils</b>\n.info .nuinfo .afk .notes .intel .protect",
    "fun": "🎉 <b>Fun</b>\n.bro .fun .cat .dog .rose .moon",
    "music": "🎵 <b>Music</b>\n.play .skip .pause .resume .stop .queue",
}

def _menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Owner", callback_data="help_owner"),
         InlineKeyboardButton("Mod", callback_data="help_mod")],
        [InlineKeyboardButton("Utils", callback_data="help_utils"),
         InlineKeyboardButton("Fun", callback_data="help_fun")],
        [InlineKeyboardButton("Music", callback_data="help_music")],
        [InlineKeyboardButton("Close", callback_data="help_close")],
    ])

@app.on_message(ub_cmd("help", "menu"))
@sudo_only
async def help_cmd(client, message: Message):
    text = f"💎 <b>{BOT_NAME or 'Yashika'} Premium Help</b>\n\nSelect a category:"
    await message.reply_text(text, reply_markup=_menu_keyboard())

@app.on_callback_query()
async def help_callback(client, query: CallbackQuery):
    data = query.data or ""
    if data == "help_close":
        await query.message.delete()
        return
    if data.startswith("help_"):
        key = data.replace("help_", "")
        text = HELP_TEXT.get(key, "No info.")
        await query.message.edit_text(text, reply_markup=_menu_keyboard())
        await query.answer()
