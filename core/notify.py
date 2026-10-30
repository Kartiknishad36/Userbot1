"""Notify owner helper."""
from config import OWNER_ID, LOG_GROUP_ID


async def notify_owner(client, text: str):
    targets = []
    if OWNER_ID:
        targets.append(OWNER_ID)
    if LOG_GROUP_ID:
        targets.append(LOG_GROUP_ID)
    for chat_id in targets:
        try:
            await client.send_message(chat_id, text)
        except Exception:
            pass
