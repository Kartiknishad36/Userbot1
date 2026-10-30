# Contributing to Yashika Premium

Thanks for your interest!

## Guidelines

1. This is primarily an **owner-only personal userbot**. Keep it focused.
2. Do not add features that clearly violate Telegram Terms of Service in a way that encourages mass abuse.
3. Test changes with both bot-only and full userbot modes.
4. Prefer graceful degradation when MongoDB is missing.
5. Keep dependencies minimal and pinned when possible.

## Development

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# fill values
python main.py
```

## Pull Requests

- One feature / fix per PR
- Update README if you add user-facing commands
- No secrets in commits
