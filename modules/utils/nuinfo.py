"""
.nuinfo — phone number intelligence (libphonenumber)
"""
import html
from pyrogram.types import Message
from core.clients import app
from modules.owner.sudoers import ub_cmd, sudo_only
from config import BOT_NAME, NUMLOOKUP_API_KEY

NAME = BOT_NAME or "Userbot1"


@app.on_message(ub_cmd("nuinfo", "phone", "numinfo"))
@sudo_only
async def nuinfo_cmd(client, message: Message):
    parts = (message.text or "").split(maxsplit=1)
    raw = parts[1].strip() if len(parts) > 1 else ""
    if not raw and message.reply_to_message:
        raw = (message.reply_to_message.text or "").strip()
    if not raw:
        return await message.reply_text(
            "Usage: <code>.nuinfo +919876543210</code>\n"
            "or reply to a message containing a number."
        )

    # Extract digits / plus
    num = "".join(c for c in raw if c.isdigit() or c == "+")
    if not num:
        return await message.reply_text("No valid number found.")

    status = await message.reply_text("⏳ Looking up number...")
    lines = [f"📱 <b>{NAME} — Number Info</b>", "━━━━━━━━━━━━━━━━━━"]

    try:
        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone as tzmod, number_type, PhoneNumberType

        parsed = phonenumbers.parse(num, None if num.startswith("+") else "IN")
        valid = phonenumbers.is_valid_number(parsed)
        possible = phonenumbers.is_possible_number(parsed)
        e164 = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        intl = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        natl = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
        region = phonenumbers.region_code_for_number(parsed)
        loc = geocoder.description_for_number(parsed, "en") or "—"
        car = carrier.name_for_number(parsed, "en") or "—"
        zones = tzmod.time_zones_for_number(parsed) or []
        ntype = number_type(parsed)
        type_map = {
            PhoneNumberType.MOBILE: "Mobile",
            PhoneNumberType.FIXED_LINE: "Fixed line",
            PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed/Mobile",
            PhoneNumberType.TOLL_FREE: "Toll free",
            PhoneNumberType.PREMIUM_RATE: "Premium rate",
            PhoneNumberType.VOIP: "VoIP",
            PhoneNumberType.UNKNOWN: "Unknown",
        }
        lines += [
            f"📞 <b>Input:</b> <code>{html.escape(raw)}</code>",
            f"✅ <b>Valid:</b> {'Yes' if valid else 'No'}",
            f"🔎 <b>Possible:</b> {'Yes' if possible else 'No'}",
            f"🌍 <b>E.164:</b> <code>{e164}</code>",
            f"🌐 <b>International:</b> <code>{intl}</code>",
            f"🏠 <b>National:</b> <code>{natl}</code>",
            f"🏳️ <b>Region:</b> <code>{region or '—'}</code>",
            f"📍 <b>Location:</b> {html.escape(str(loc))}",
            f"📡 <b>Carrier:</b> {html.escape(str(car))}",
            f"☎️ <b>Type:</b> {type_map.get(ntype, str(ntype))}",
            f"🕒 <b>Timezones:</b> {', '.join(zones) if zones else '—'}",
            f"🔢 <b>Country code:</b> +{parsed.country_code}",
            f"🔢 <b>National number:</b> {parsed.national_number}",
        ]
    except Exception as e:
        lines.append(f"❌ Parse error: <code>{html.escape(str(e))}</code>")
        lines.append("Tip: use full international format e.g. <code>+91...</code>")

    if NUMLOOKUP_API_KEY:
        lines.append("")
        lines.append("🔑 External API key set — enhanced lookup available when API endpoint configured.")

    lines += ["━━━━━━━━━━━━━━━━━━", f"💎 <b>{NAME}</b>"]
    try:
        await status.edit_text("\n".join(lines))
    except Exception:
        await message.reply_text("\n".join(lines))
