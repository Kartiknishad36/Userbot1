#!/usr/bin/env python3
"""
Yashika Session String Generator
Run this once locally to get STRING_SESSION for userbot features.

Usage:
  pip install kurigram tgcrypto
  python generate_session.py
"""

import asyncio
import sys

try:
    from pyrogram import Client
except ImportError:
    print("Install first:  pip install kurigram tgcrypto")
    sys.exit(1)


async def main():
    print("=" * 50)
    print("  Yashika · STRING_SESSION Generator")
    print("=" * 50)
    print()
    print("Get API_ID and API_HASH from → https://my.telegram.org")
    print()

    try:
        api_id = int(input("API_ID: ").strip())
    except ValueError:
        print("API_ID must be a number")
        return

    api_hash = input("API_HASH: ").strip()
    if not api_hash:
        print("API_HASH required")
        return

    print("\nA Telegram login code will be sent to your account...")
    print("Enter phone number with country code (e.g. +919876543210)\n")

    async with Client(
        name="yashika_session",
        api_id=api_id,
        api_hash=api_hash,
        in_memory=True,
    ) as app:
        me = await app.get_me()
        session = await app.export_session_string()
        print("\n" + "=" * 50)
        print(f"Logged in as: {me.first_name} (@{me.username or '—'}) id={me.id}")
        print("=" * 50)
        print("\nYour STRING_SESSION (copy everything):\n")
        print(session)
        print("\n" + "=" * 50)
        print("Paste this into your .env as STRING_SESSION=...")
        print("Keep it secret. Never share publicly.")
        print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())
