"""Sudo and command filters"""
from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID, PREFIXES

SUDO_USERS = set()
ME_ID = 0

def set_me_id(uid: int):
    global ME_ID
    ME_ID = uid
    SUDO_USERS.add(uid)

async def load_sudoers():
    # Can load from mongo later
    if OWNER_ID:
        SUDO_USERS.add(OWNER_ID)

def is_sudo(uid: int) -> bool:
    return uid in SUDO_USERS or uid == OWNER_ID or uid == ME_ID

def ub_cmd(*cmds):
    """Userbot command filter with prefixes"""
    prefixes = list(PREFIXES) if PREFIXES else [".", "!"]
    return filters.command(list(cmds), prefixes=prefixes) & filters.me

def sudo_only(func):
    async def wrapper(client, message: Message):
        uid = message.from_user.id if message.from_user else 0
        if not is_sudo(uid) and not message.outgoing:
            return
        return await func(client, message)
    return wrapper
