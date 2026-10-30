# 💎 Userbot1 — Premium Hybrid

Telegram **Bot + Userbot** (Kurigram/Pyrogram) · Owner-only · Railway / Render ready

**Repo:** https://github.com/Kartiknishad36/Userbot1

---

## Quick Start

```bash
git clone https://github.com/Kartiknishad36/Userbot1.git
cd Userbot1
pip install -r requirements.txt
cp .env.example .env
# fill API_ID API_HASH OWNER_ID BOT_TOKEN STRING_SESSION
python generate_session.py   # optional
python main.py
```

---

## Required Env

| Variable | Required | Description |
|----------|----------|-------------|
| `API_ID` | ✅ | my.telegram.org |
| `API_HASH` | ✅ | my.telegram.org |
| `OWNER_ID` | ✅ | Your Telegram user id |
| `BOT_TOKEN` | Bot mode | @BotFather |
| `STRING_SESSION` | Userbot `.` cmds | `generate_session.py` |
| `MONGO_URI` | ○ | Optional persistence |
| `LOG_GROUP_ID` | ○ | Log group `-100...` |
| `BOT_NAME` | ○ | Default `Userbot1` |
| `AUTO_DELETE` | ○ | Default true |
| `DELETE_DELAY` | ○ | Seconds (default 1) |

---

## Commands (prefix `.` or `!`)

| Category | Commands |
|----------|----------|
| **Core** | `.help` `.menu` `.ping` `.alive` `.id` |
| **Info** | `.info` `.whois` `.nuinfo` |
| **Mod** | `.tagall` `.gban` `.warn` `.broadcast` `.welcome` |
| **Fun** | `.bro` `.unbro` `.cat` `.dog` `.rose` `.joke` `.decide` |
| **Owner** | `.clone` `.back` `.eval` `.exec` `.restart` |
| **Tools** | `.calc` `.reverse` `.tr` `.afk` `.notes` |
| **Music** | `.play` `.skip` `.pause` `.stop` (needs VC setup) |

Bot side: `/help` `/start` (if `BOT_TOKEN` set)

---

## Deploy

- **Railway / Render:** Background **Worker** · start `python main.py`
- **Procfile:** `worker: python3 main.py`
- **Docker:** `docker build -t userbot1 . && docker run --env-file .env userbot1`

Flask health on `PORT` for web-style hosts: `/` and `/health`.

---

## Structure

```
Userbot1/
├── main.py
├── config.py
├── core/          clients, autodelete, calls, notify
├── database/      mongo async
├── modules/
│   ├── bot/
│   ├── owner/
│   ├── global_mod/
│   ├── utils/
│   ├── media/
│   └── vc/
└── requirements.txt
```

---

## Notes

- Owner-only userbot filters (`ub_cmd` + sudo)
- No third-party upstream auto-pull
- Never share `STRING_SESSION` / `BOT_TOKEN`
- Spam/raid tools can ban accounts — use carefully

**License:** MIT
