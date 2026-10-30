"""Fun / art commands"""
import random
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

ARTS = {
    "cat": [
        " /\\_/\\ \n( o.o )\n > ^ <",
        "  /\\_/\\  \n ( o.o ) \n  > ^ <",
    ],
    "dog": [
        "  __      _\n o-''|\\_____/)\n  \\_/|_)     )\n     \\  __  /\n      (_/ (_/",
    ],
    "rose": [
        "@}}}-,-`-",
        "      _\n     / )\n    / /\n   / /\n  / /\n / /\n( (\n \\ \\\n  \\ \\\n   \\_\\",
    ],
    "moon": [
        "    _..._\n  .'     '.\n /  _   _  \\\n|  (o) (o)  |\n \\    <    /\n  '. === .'\n    '---'",
    ],
    "heart": [
        "  **  **\n ******\n  ****\n   **",
    ],
}

JOKES = [
    "Programmer: It works on my machine.\nBoss: We are not shipping your machine.",
    "There are 10 types of people: those who know binary and those who don't.",
    "A SQL query walks into a bar, walks up to two tables and asks: Can I JOIN you?",
]


@app.on_message(ub_cmd("fun", "joke"))
@sudo_only
async def joke_cmd(client, message: Message):
    await message.reply_text(f"😂 {random.choice(JOKES)}")


@app.on_message(ub_cmd("cat", "dog", "rose", "moon", "heart"))
@sudo_only
async def art_cmd(client, message: Message):
    cmd = (message.command[0] if message.command else "cat").lower()
    art = random.choice(ARTS.get(cmd, ARTS["cat"]))
    await message.reply_text(f"<pre>{art}</pre>")


@app.on_message(ub_cmd("decide"))
@sudo_only
async def decide_cmd(client, message: Message):
    await message.reply_text(f"🎲 <b>{random.choice(['Yes', 'No', 'Maybe', 'Definitely', 'Never'])}</b>")


@app.on_message(ub_cmd("choose"))
@sudo_only
async def choose_cmd(client, message: Message):
    parts = (message.text or "").split()[1:]
    if len(parts) < 2:
        return await message.reply_text("Usage: <code>.choose a b c</code>")
    await message.reply_text(f"🎯 I choose: <b>{random.choice(parts)}</b>")
