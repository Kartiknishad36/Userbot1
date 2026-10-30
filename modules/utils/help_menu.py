"""Premium button help menu — .help / .menu"""
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from core.clients import app, bot
from modules.owner.sudoers import ub_cmd, sudo_only
from config import BOT_NAME, PREFIXES

NAME = BOT_NAME or "Userbot1"
P = (PREFIXES or ".")[0]

HELP_TEXT = {
    "owner": (
        f"👑 <b>Owner</b>\n\n"
        f"<code>{P}clone</code> / <code>{P}back</code> — profile clone\n"
        f"<code>{P}track</code> — user tracker\n"
        f"<code>{P}ghost</code> — ghost mode\n"
        f"<code>{P}sessions</code> — multi session\n"
        f"<code>{P}pmguard</code> — PM protect\n"
        f"<code>{P}eval</code> / <code>{P}restart</code> — system"
    ),
    "mod": (
        f"🛡️ <b>Moderation</b>\n\n"
        f"<code>{P}tagall</code> / <code>{P}tag</code> — mention all\n"
        f"<code>{P}gban</code> / <code>{P}warn</code>\n"
        f"<code>{P}antilink</code> <code>{P}antiflood</code>\n"
        f"<code>{P}nightmode</code> <code>{P}zombies</code>\n"
        f"<code>{P}welcome</code> <code>{P}broadcast</code>"
    ),
    "utils": (
        f"🛠️ <b>Utils</b>\n\n"
        f"<code>{P}info</code> / <code>{P}whois</code> — full user report\n"
        f"<code>{P}nuinfo</code> — phone intel\n"
        f"<code>{P}id</code> <code>{P}ping</code> <code>{P}alive</code>\n"
        f"<code>{P}afk</code> <code>{P}notes</code> <code>{P}intel</code>\n"
        f"<code>{P}calc</code> <code>{P}tr</code> <code>{P}paste</code>"
    ),
    "fun": (
        f"🎉 <b>Fun</b>\n\n"
        f"<code>{P}bro</code> / <code>{P}unbro</code> / <code>{P}brolist</code>\n"
        f"<code>{P}shayari</code> <code>{P}fun</code>\n"
        f"<code>{P}cat</code> <code>{P}dog</code> <code>{P}rose</code>"
    ),
    "music": (
        f"🎵 <b>Music / VC</b>\n\n"
        f"<code>{P}play</code> <code>{P}skip</code>\n"
        f"<code>{P}pause</code> <code>{P}resume</code>\n"
        f"<code>{P}stop</code> <code>{P}queue</code>"
    ),
}


def _menu_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("👑 Owner", callback_data="ub1_help_owner"),
            InlineKeyboardButton("🛡️ Mod", callback_data="ub1_help_mod"),
        ],
        [
            InlineKeyboardButton("🛠️ Utils", callback_data="ub1_help_utils"),
            InlineKeyboardButton("🎉 Fun", callback_data="ub1_help_fun"),
        ],
        [InlineKeyboardButton("🎵 Music", callback_data="ub1_help_music")],
        [InlineKeyboardButton("❌ Close", callback_data="ub1_help_close")],
    ])


def _register_help(client):
    if client is None:
        return

    @client.on_message(ub_cmd("help", "menu") if client is app else filters.command(["help", "menu"], prefixes=["/", "."]))
    async def help_cmd(c, message: Message):
        if client is app:
            # sudo check already in ub_cmd path when using decorator — manual for bot
            pass
        text = (
            f"💎 <b>{NAME} Premium Help</b>\n\n"
            f"Prefix: <code>{P}</code>\n"
            f"Select a category below:"
        )
        await message.reply_text(text, reply_markup=_menu_keyboard())

    @client.on_callback_query(filters.regex(r"^ub1_help_"))
    async def help_callback(c, query: CallbackQuery):
        data = query.data or ""
        if data == "ub1_help_close":
            try:
                await query.message.delete()
            except Exception:
                pass
            return
        key = data.replace("ub1_help_", "")
        text = HELP_TEXT.get(key, "No info.")
        try:
            await query.message.edit_text(text, reply_markup=_menu_keyboard())
        except Exception:
            pass
        await query.answer()


if app is not None:
    @app.on_message(ub_cmd("help", "menu"))
    @sudo_only
    async def ub_help(client, message: Message):
        text = (
            f"💎 <b>{NAME} Premium Help</b>\n\n"
            f"Prefix: <code>{P}</code>\n"
            f"Select a category:"
        )
        await message.reply_text(text, reply_markup=_menu_keyboard())

    @app.on_callback_query(filters.regex(r"^ub1_help_"))
    async def ub_help_cb(client, query: CallbackQuery):
        data = query.data or ""
        if data == "ub1_help_close":
            try:
                await query.message.delete()
            except Exception:
                pass
            return
        key = data.replace("ub1_help_", "")
        text = HELP_TEXT.get(key, "No info.")
        try:
            await query.message.edit_text(text, reply_markup=_menu_keyboard())
        except Exception:
            pass
        try:
            await query.answer()
        except Exception:
            pass

if bot is not None:
    @bot.on_message(filters.command(["help", "menu", "start"], prefixes=["/", "."]))
    async def bot_help(client, message: Message):
        if message.command and message.command[0] == "start":
            await message.reply_text(
                f"👋 <b>{NAME}</b> online.\nUse /help for menu."
            )
            return
        text = f"💎 <b>{NAME} Help</b>\n\nSelect:"
        await message.reply_text(text, reply_markup=_menu_keyboard())

    @bot.on_callback_query(filters.regex(r"^ub1_help_"))
    async def bot_help_cb(client, query: CallbackQuery):
        data = query.data or ""
        if data == "ub1_help_close":
            try:
                await query.message.delete()
            except Exception:
                pass
            return
        key = data.replace("ub1_help_", "")
        text = HELP_TEXT.get(key, "No info.")
        try:
            await query.message.edit_text(text, reply_markup=_menu_keyboard())
        except Exception:
            pass
        try:
            await query.answer()
        except Exception:
            pass
