"""Sudo users and command filters for userbot"""
from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID, PREFIXES

SUDO_USERS: set[int] = set()
ME_ID: int = 0

def set_me_id(uid: int):
    global ME_ID
    ME_ID = int(uid)
    SUDO_USERS.add(ME_ID)

async def load_sudoers():
    if OWNER_ID:
        SUDO_USERS.add(int(OWNER_ID))

def is_sudo(uid: int) -> bool:
    try:
        uid = int(uid)
    except Exception:
        return False
    return uid in SUDO_USERS or uid == OWNER_ID or uid == ME_ID

def ub_cmd(*cmds):
    """Userbot command filter — works for outgoing messages from the session account."""
    prefixes = list(PREFIXES) if PREFIXES else [".", "!"]
    cmd_filter = filters.command(list(cmds), prefixes=prefixes)
    # Accept if message is outgoing (from the userbot account) or from sudo
    async def _check(_, __, message: Message):
        if not message or not message.from_user:
            return False
        if message.outgoing:
            return True
        return is_sudo(message.from_user.id)
    return cmd_filter & filters.create(_check)

def sudo_only(func):
    async def wrapper(client, message: Message):
        uid = message.from_user.id if message.from_user else 0
        if message.outgoing or is_sudo(uid):
            return await func(client, message)
        return
    return wrapper

@filters.create
async def sudo_filter(_, __, message: Message):
    if not message or not message.from_user:
        return False
    return is_sudo(message.from_user.id) or message.outgoing
