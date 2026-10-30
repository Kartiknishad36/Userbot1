"""Owner system: .eval .exec .restart .logs"""
import asyncio
import os
import sys
import traceback
from io import StringIO

from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only
from config import OWNER_ID


@app.on_message(ub_cmd("eval"))
@sudo_only
async def eval_cmd(client, message: Message):
    if OWNER_ID and message.from_user and message.from_user.id not in (OWNER_ID,) and not message.outgoing:
        return
    code = (message.text or "").split(maxsplit=1)
    if len(code) < 2:
        return await message.reply_text("Usage: <code>.eval 1+1</code>")
    code = code[1]
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout = StringIO()
    sys.stderr = StringIO()
    result = None
    try:
        exec(
            "async def __eval_fn(client, message):\n" + "\n".join(f"    {l}" for l in code.splitlines()),
            globals(),
        )
        result = await locals()["__eval_fn"](client, message)
    except Exception:
        result = traceback.format_exc()
    out = sys.stdout.getvalue()
    err = sys.stderr.getvalue()
    sys.stdout, sys.stderr = old_out, old_err
    text = ""
    if out:
        text += out
    if err:
        text += err
    if result is not None:
        text += str(result)
    if not text.strip():
        text = "✅ Done"
    if len(text) > 4000:
        text = text[:4000] + "\n..."
    await message.reply_text(f"<pre>{text}</pre>")


@app.on_message(ub_cmd("exec", "sh"))
@sudo_only
async def exec_cmd(client, message: Message):
    cmd = (message.text or "").split(maxsplit=1)
    if len(cmd) < 2:
        return await message.reply_text("Usage: <code>.exec ls</code>")
    proc = await asyncio.create_subprocess_shell(
        cmd[1],
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    out = (stdout or b"").decode(errors="replace") + (stderr or b"").decode(errors="replace")
    if not out.strip():
        out = f"exit {proc.returncode}"
    if len(out) > 4000:
        out = out[:4000] + "\n..."
    await message.reply_text(f"<pre>{out}</pre>")


@app.on_message(ub_cmd("restart"))
@sudo_only
async def restart_cmd(client, message: Message):
    await message.reply_text("♻️ Restarting...")
    await asyncio.sleep(1)
    os.execl(sys.executable, sys.executable, *sys.argv)
