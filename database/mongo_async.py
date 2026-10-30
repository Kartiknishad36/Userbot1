"""Async MongoDB helper"""
from config import MONGO_URI, MONGO_DB

_db = None

async def get_db():
    global _db
    if _db is not None:
        return _db
    if not MONGO_URI:
        return None
    try:
        from motor.motor_asyncio import AsyncIOMotorClient
        client = AsyncIOMotorClient(MONGO_URI)
        _db = client[MONGO_DB]
        return _db
    except Exception as e:
        print(f"[mongo] {e}")
        return None
