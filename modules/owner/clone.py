"""Profile clone / back — saves name + bio"""
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

_original = {}


@app.on_message(ub_cmd("clone"))
@sudo_only
async def clone_cmd(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply_text("Reply to a user to clone their profile.")
    target = message.reply_to_message.from_user
    try:
        me = await client.get_me()
        try:
            my_chat = await client.get_chat("me")
            bio = getattr(my_chat, "bio", None) or ""
        except Exception:
            bio = ""
        _original["first_name"] = me.first_name or "User"
        _original["last_name"] = me.last_name or ""
        _original["bio"] = bio

        await client.update_profile(
            first_name=(target.first_name or "Cloned")[:64],
            last_name=(target.last_name or "")[:64],
        )
        # bio from target if public
        try:
            tchat = await client.get_chat(target.id)
            tbio = getattr(tchat, "bio", None)
            if tbio:
                await client.update_profile(bio=tbio[:70])
        except Exception:
            pass

        await message.reply_text(
            f"👤 Cloned <b>{target.first_name}</b> "
            f"(@{target.username or target.id})\n"
            f"Use <code>.back</code> to restore."
        )
    except Exception as e:
        await message.reply_text(f"Clone failed: <code>{e}</code>")


@app.on_message(ub_cmd("back"))
@sudo_only
async def back_cmd(client, message: Message):
    if not _original:
        return await message.reply_text("No original profile saved. Clone someone first.")
    try:
        await client.update_profile(
            first_name=_original.get("first_name") or "User",
            last_name=_original.get("last_name") or "",
            bio=_original.get("bio") or "",
        )
        await message.reply_text("🔄 Profile restored to original.")
    except Exception as e:
        await message.reply_text(f"Restore failed: <code>{e}</code>")
