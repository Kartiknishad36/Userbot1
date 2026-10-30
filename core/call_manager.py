"""PyTgCalls manager for VC"""
from core.clients import app

_pytg = None
_started = False

async def ensure_started(client=None):
    global _started
    if not _started:
        try:
            from pytgcalls import PyTgCalls
            global _pytg
            _pytg = PyTgCalls(app)
            await _pytg.start()
            _started = True
        except Exception as e:
            print(f"[call_manager] {e}")

def get_pytgcalls():
    return _pytg
