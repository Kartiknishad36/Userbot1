# ✨💎 YASHIKA PREMIUM 💎✨

### Telegram **Bot + Userbot** Hybrid · Owner-Only · Multi-Platform Ready

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Kurigram](https://img.shields.io/badge/Telegram-Kurigram-blue.svg)](https://github.com/KurimuzonAkuma/kurigram)

---

## 🚀 Quick Start (Local)

```bash
git clone https://github.com/Kartiknishad36/Userbot1.git
cd Userbot1
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your values
python generate_session.py   # optional - get STRING_SESSION
python main.py
```

---

## 🔐 Required Environment Variables

| Variable         | Required | Description                                      |
|------------------|----------|--------------------------------------------------|
| `API_ID`         | ✅       | From [my.telegram.org](https://my.telegram.org)  |
| `API_HASH`       | ✅       | From my.telegram.org                             |
| `BOT_TOKEN`      | ✅*      | From [@BotFather](https://t.me/BotFather)        |
| `OWNER_ID`       | ✅       | Your numeric Telegram ID                         |
| `STRING_SESSION` | ⚡       | Userbot session (generate with `generate_session.py`) |
| `LOG_GROUP_ID`   | ⚡       | Private log group (`-100...`)                    |
| `MONGO_URI`      | ○        | MongoDB (Atlas / Railway) – optional             |

> *Without `STRING_SESSION` → bot-only mode works.  
> Userbot commands (`.` prefix) require a valid session.

---

## ✨ Features

| Category       | Commands / Ability                                      |
|----------------|---------------------------------------------------------|
| **Core**       | Owner-only, premium button help menu, auto-delete       |
| **Info**       | `.info` / `.whois` full profile, `.nuinfo` phone lookup |
| **Moderation** | Gban, warn, tagall, antilink, nightmode, zombies        |
| **Music VC**   | `.play` YouTube, skip, pause, queue (PyTgCalls)         |
| **Owner**      | Clone profile, tracker, multi-session, PM Guard         |
| **Fun**        | Bro system, ASCII arts, autoreply style learning        |
| **Utils**      | Notes, filters, AFK, QR, paste, stats, etc.             |

---

## 📦 Repo Structure

```
Userbot1/
├── main.py                 # Boot loader
├── config.py               # Environment loader
├── generate_session.py     # Easy STRING_SESSION generator
├── core/                   # Clients, notify, autodelete, calls
├── database/               # Mongo + memory fallback
├── modules/
│   ├── bot/                # /start, /login, /help
│   ├── owner/              # Sudo, clone, tracker, sessions, PM guard
│   ├── global_mod/         # Tagall, bro, warn, anti-*, broadcast
│   ├── utils/              # Help, info, nuinfo, fun, tools
│   ├── media/              # Kang, download
│   ├── vc/                 # Music player
│   └── economy/            # Basic economy
├── requirements.txt
├── Dockerfile
├── Procfile
└── .env.example
```

---

## 🌐 Deploy Guides

### Best options (always-on worker needed)

| Platform     | Type              | Notes                          |
|--------------|-------------------|--------------------------------|
| **Railway**  | Background Worker | Recommended                    |
| **Render**   | Background Worker | Free tier available            |
| **Koyeb**    | Web Service       | Good free tier                 |
| **VPS**      | Any               | Most reliable long-term        |
| **Docker**   | Anywhere          | `docker build -t yashika .`    |

**Local / VPS example:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# fill .env
python main.py
```

**Docker:**
```bash
docker build -t yashika .
docker run -d --env-file .env --name yashika yashika
```

> Vercel / serverless platforms are **not suitable** (timeouts).

---

## 🎮 Important Commands

**Prefix:** `.` or `!` (configurable)

| Command          | Description                     |
|------------------|---------------------------------|
| `.help` / `.menu`| Premium button help menu        |
| `.ping` / `.alive`| Status                          |
| `.info` / `.whois`| Full user report                |
| `.play`          | Play music in VC                |
| `.tagall`        | Mention all members             |
| `.bro` / `.unbro`| Bro auto-reply system           |
| `.clone` / `.back`| Profile clone                   |
| `/login` (bot)   | Interactive session login       |

---

## ⚠️ Important Warnings

- This is an **owner-only** personal build. Do not share your `STRING_SESSION` or `BOT_TOKEN`.
- Features like phone lookup (`.nuinfo`), tracker, clone, raid tools can violate Telegram Terms of Service if misused.
- Use only on accounts you own. The authors are not responsible for bans or misuse.
- `.nuinfo` uses public telecom metadata (libphonenumber) + optional API. No Aadhaar / private KYC data.

---

## 🛠 Requirements

- Python **3.11+**
- `ffmpeg` (for music)
- Optional: MongoDB for persistent data
- Optional: `cookies.txt` for better YouTube support

Install:
```bash
pip install -r requirements.txt
# On Debian/Ubuntu:
sudo apt install ffmpeg
```

---

## 📄 License

MIT License – see [LICENSE](LICENSE)

---

**Star ⭐ the repo if it helps you.**

`python main.py` · Prefix **.** · Owner only
