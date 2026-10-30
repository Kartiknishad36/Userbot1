"""Tools: .id .calc .reverse .tr .paste"""
import html
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only


@app.on_message(ub_cmd("id"))
@sudo_only
async def id_cmd(client, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user:
        u = message.reply_to_message.from_user
        await message.reply_text(
            f"👤 User: <code>{u.id}</code>\n"
            f"💬 Chat: <code>{message.chat.id}</code>\n"
            f"📝 Msg: <code>{message.reply_to_message.id}</code>"
        )
    else:
        await message.reply_text(
            f"💬 Chat: <code>{message.chat.id}</code>\n"
            f"👤 You: <code>{message.from_user.id if message.from_user else '—'}</code>"
        )


@app.on_message(ub_cmd("calc"))
@sudo_only
async def calc_cmd(client, message: Message):
    expr = (message.text or "").split(maxsplit=1)
    if len(expr) < 2:
        return await message.reply_text("Usage: <code>.calc 2+2*5</code>")
    expr = expr[1].strip()
    allowed = set("0123456789+-*/().% ")
    if not all(c in allowed for c in expr):
        return await message.reply_text("Invalid characters.")
    try:
        val = eval(expr, {"__builtins__": {}}, {})
        await message.reply_text(f"🧮 <code>{html.escape(expr)}</code> = <b>{val}</b>")
    except Exception as e:
        await message.reply_text(f"❌ <code>{e}</code>")


@app.on_message(ub_cmd("reverse"))
@sudo_only
async def reverse_cmd(client, message: Message):
    parts = (message.text or "").split(maxsplit=1)
    text = parts[1] if len(parts) > 1 else ""
    if not text and message.reply_to_message:
        text = message.reply_to_message.text or ""
    if not text:
        return await message.reply_text("Provide text or reply.")
    await message.reply_text(f"<code>{html.escape(text[::-1])}</code>")


@app.on_message(ub_cmd("tr", "translate"))
@sudo_only
async def tr_cmd(client, message: Message):
    """Simple translate via Google (unofficial)."""
    parts = (message.text or "").split(maxsplit=2)
    if len(parts) < 2:
        return await message.reply_text("Usage: <code>.tr en hello</code> or reply with <code>.tr hi</code>")
    lang = parts[1]
    text = parts[2] if len(parts) > 2 else ""
    if not text and message.reply_to_message:
        text = message.reply_to_message.text or ""
    if not text:
        return await message.reply_text("No text.")
    try:
        import urllib.parse
        import urllib.request
        q = urllib.parse.quote(text)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={urllib.parse.quote(lang)}&dt=t&q={q}"
        with urllib.request.urlopen(url, timeout=10) as r:
            import json
            data = json.loads(r.read().decode())
        out = "".join(part[0] for part in data[0] if part and part[0])
        await message.reply_text(f"🌐 <b>{lang}</b>\n{html.escape(out)}")
    except Exception as e:
        await message.reply_text(f"❌ Translate failed: <code>{e}</code>")
