"""Chat moderation: ban kick mute promote pin purge"""
from pyrogram.types import Message, ChatPermissions
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only


def _target(message: Message):
    if message.reply_to_message and message.reply_to_message.from_user:
        return message.reply_to_message.from_user.id
    parts = (message.text or "").split(maxsplit=1)
    if len(parts) > 1:
        try:
            return int(parts[1])
        except ValueError:
            return parts[1]
    return None


@app.on_message(ub_cmd("ban"))
@sudo_only
async def ban_cmd(client, message: Message):
    uid = _target(message)
    if not uid:
        return await message.reply_text("Reply or give user id.")
    try:
        user = await client.get_users(uid)
        await client.ban_chat_member(message.chat.id, user.id)
        await message.reply_text(f"🔨 Banned <b>{user.first_name}</b> (<code>{user.id}</code>)")
    except Exception as e:
        await message.reply_text(f"❌ {e}")


@app.on_message(ub_cmd("unban"))
@sudo_only
async def unban_cmd(client, message: Message):
    uid = _target(message)
    if not uid:
        return await message.reply_text("Reply or give user id.")
    try:
        user = await client.get_users(uid)
        await client.unban_chat_member(message.chat.id, user.id)
        await message.reply_text(f"✅ Unbanned <code>{user.id}</code>")
    except Exception as e:
        await message.reply_text(f"❌ {e}")


@app.on_message(ub_cmd("kick"))
@sudo_only
async def kick_cmd(client, message: Message):
    uid = _target(message)
    if not uid:
        return await message.reply_text("Reply to user.")
    try:
        user = await client.get_users(uid)
        await client.ban_chat_member(message.chat.id, user.id)
        await client.unban_chat_member(message.chat.id, user.id)
        await message.reply_text(f"👢 Kicked <b>{user.first_name}</b>")
    except Exception as e:
        await message.reply_text(f"❌ {e}")


@app.on_message(ub_cmd("mute"))
@sudo_only
async def mute_cmd(client, message: Message):
    uid = _target(message)
    if not uid:
        return await message.reply_text("Reply to user.")
    try:
        user = await client.get_users(uid)
        await client.restrict_chat_member(
            message.chat.id, user.id, ChatPermissions(can_send_messages=False)
        )
        await message.reply_text(f"🔇 Muted <b>{user.first_name}</b>")
    except Exception as e:
        await message.reply_text(f"❌ {e}")


@app.on_message(ub_cmd("unmute"))
@sudo_only
async def unmute_cmd(client, message: Message):
    uid = _target(message)
    if not uid:
        return await message.reply_text("Reply to user.")
    try:
        user = await client.get_users(uid)
        await client.restrict_chat_member(
            message.chat.id,
            user.id,
            ChatPermissions(
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
            ),
        )
        await message.reply_text(f"🔊 Unmuted <b>{user.first_name}</b>")
    except Exception as e:
        await message.reply_text(f"❌ {e}")


@app.on_message(ub_cmd("promote"))
@sudo_only
async def promote_cmd(client, message: Message):
    uid = _target(message)
    if not uid:
        return await message.reply_text("Reply to user.")
    try:
        user = await client.get_users(uid)
        await client.promote_chat_member(
            message.chat.id,
            user.id,
            can_manage_chat=True,
            can_delete_messages=True,
            can_restrict_members=True,
            can_invite_users=True,
            can_pin_messages=True,
        )
        await message.reply_text(f"⬆️ Promoted <b>{user.first_name}</b>")
    except Exception as e:
        await message.reply_text(f"❌ {e}")


@app.on_message(ub_cmd("demote"))
@sudo_only
async def demote_cmd(client, message: Message):
    uid = _target(message)
    if not uid:
        return await message.reply_text("Reply to user.")
    try:
        user = await client.get_users(uid)
        await client.promote_chat_member(
            message.chat.id,
            user.id,
            can_manage_chat=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_invite_users=False,
            can_pin_messages=False,
        )
        await message.reply_text(f"⬇️ Demoted <b>{user.first_name}</b>")
    except Exception as e:
        await message.reply_text(f"❌ {e}")


@app.on_message(ub_cmd("pin"))
@sudo_only
async def pin_cmd(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to pin.")
    await client.pin_chat_message(message.chat.id, message.reply_to_message.id)
    await message.reply_text("📌 Pinned.")


@app.on_message(ub_cmd("unpin"))
@sudo_only
async def unpin_cmd(client, message: Message):
    await client.unpin_chat_message(message.chat.id)
    await message.reply_text("📌 Unpinned.")


@app.on_message(ub_cmd("del", "delete"))
@sudo_only
async def del_cmd(client, message: Message):
    if message.reply_to_message:
        try:
            await message.reply_to_message.delete()
        except Exception:
            pass
    try:
        await message.delete()
    except Exception:
        pass


@app.on_message(ub_cmd("purge"))
@sudo_only
async def purge_cmd(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to start message.")
    ids = []
    async for m in client.get_chat_history(message.chat.id, limit=200):
        if m.id < message.reply_to_message.id:
            break
        ids.append(m.id)
        if m.id == message.reply_to_message.id:
            break
    ids.append(message.id)
    try:
        await client.delete_messages(message.chat.id, ids)
    except Exception as e:
        await message.reply_text(f"Purge error: {e}")
