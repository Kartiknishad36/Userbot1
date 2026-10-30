"""Shayari / romantic lines"""
import random
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only

SHAYARI = [
    "Teri muskaan mein chhupa hai mera jahaan,\nDil se dua hai tu rahe muskurata hamesha.",
    "Raat ki khamoshi mein tera khayal aata hai,\nNeend bhi sharma ke door chali jaati hai.",
    "Mohabbat sirf lafzon ka khel nahi,\nYeh dil se dil tak ka safar hai.",
    "Tum paas ho to har lamha ehm hai,\nTum door ho to har saans adhoori si lagti hai.",
    "Chand bhi sharma jaye teri roshni se,\nItni haseen hai teri yeh zindagi se.",
    "Dil ke kone mein ek khamoshi si hai,\nShayad wahi jagah hai jahan tu rehta hai.",
    "Waqt badal jata hai, log badal jate hain,\nPar kuch yaadein hamesha dil ke paas rehti hain.",
    "Tere bina adhoora sa lagta hai yeh sheher,\nHar gali mein teri kami si mehsoos hoti hai.",
]


@app.on_message(ub_cmd("shayari", "shayri", "love"))
@sudo_only
async def shayari_cmd(client, message: Message):
    await message.reply_text(f"💫 <i>{random.choice(SHAYARI)}</i>")
