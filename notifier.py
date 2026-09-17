import random
import requests
import config

ALL_QUOTES = [
    # Motivation / Discipline / Goals
    "⚠️ FocusShield Alert!\n\nTo become a star, you must burn. Focus on your goal! 🔥",
    "⚠️ FocusShield Alert!\n\nOnce you see the results of your hard work, it becomes an addiction. Don't waste your time!",
    "⚠️ FocusShield Alert!\n\nDestroy what destroys you ⚔️ Eliminate distractions and chase your goal!",
    "⚠️ FocusShield Alert!\n\nA winner is someone who doesn't make excuses. Keep working!",
    "⚠️ FocusShield Alert!\n\nWhat you don't change, you choose. Get back to work!",
    "⚠️ FocusShield Alert!\n\nPut off until tomorrow only what you are willing to die leaving undone.",
    "⚠️ FocusShield Alert!\n\nYou will never unlock your potential if cheap dopamine is always available.",
    "⚠️ FocusShield Alert!\n\nKeep moving and focus on the result! 🎯",
    "⚠️ FocusShield Alert!\n\nRemember, you were born to win 👑 Stop getting distracted!",
    "⚠️ FocusShield Alert!\n\nYour result is waiting for you on the screen. Look straight ahead!",
    "⚠️ FocusShield Alert!\n\nEven ideas have an expiration date. Sluggishness is the silent killer of opportunity!",
    "⚠️ FocusShield Alert!\n\nAre you ready to die for an idea, but not ready to fight for it? Get back to work!",
    "⚠️ FocusShield Alert!\n\nMotivation is a push. Discipline is a relentless push every single day!",
    "⚠️ FocusShield Alert!\n\nToscanini recorded one piece 65 times and said: 'Better than before, but could be better.' Keep refining!",
    "⚠️ FocusShield Alert!\n\nA winner is someone who doesn't make excuses ⚡ Get back to your desk!",
    "⚠️ FocusShield Alert!\n\nKeep going! Every lost minute moves you away from your goal.",
    "⚠️ FocusShield Alert!\n\nDid you run away from the problem that fast? Get back to work!",
    "⚠️ FocusShield Alert!\n\nThe lesson will repeat itself until you learn it. Return to your desk!",
    "⚠️ FocusShield Alert!\n\nOnly those who risk going too far can possibly find out how far they can go.",
    "⚠️ FocusShield Alert!\n\nBelieve in luck: the more you try, the luckier you get. Keep working!"
]

LAST_MESSAGE = None

def get_telegram_creds():
    token = getattr(config, 'TELEGRAM_TOKEN', None)
    chat_id = getattr(config, 'CHAT_ID', None)
    return token, chat_id

def send_alert():
    """Sends a random motivational quote from the pool when the user is absent."""
    global LAST_MESSAGE
    token, chat_id = get_telegram_creds()

    if not token or not chat_id:
        print("[ALERT]: Absence detected, but Telegram credentials are not set.")
        return

    available_messages = [msg for msg in ALL_QUOTES if msg != LAST_MESSAGE]
    if not available_messages:
        available_messages = ALL_QUOTES

    message = random.choice(available_messages)
    LAST_MESSAGE = message

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}

    try:
        requests.post(url, json=payload, timeout=3)
    except Exception as e:
        print(f"Error sending Telegram notification: {e}")

def send_stats_summary(present_sec, absent_sec):
    """Sends the final session report to Telegram."""
    token, chat_id = get_telegram_creds()
    
    if not token or not chat_id:
        print("[STATS]: Unable to send report, missing Telegram credentials.")
        return

    total_sec = present_sec + absent_sec
    p_min, p_s = divmod(int(present_sec), 60)
    a_min, a_s = divmod(int(absent_sec), 60)
    
    focus_rate = (present_sec / total_sec * 100) if total_sec > 0 else 0

    text = (
        "📊 *FocusShield Session Report*\n\n"
        f"🎯 *Focus Time:* {p_min}m {p_s}s\n"
        f"🏃 *Away Time:* {a_min}m {a_s}s\n"
        f"📈 *Focus Efficiency:* {focus_rate:.1f}%\n\n"
        "Great work! Keep pushing forward ⚔️"
    )

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }

    try:
        requests.post(url, json=payload, timeout=3)
        print("📲 Final session statistics successfully sent to Telegram!")
    except Exception as e:
        print(f"Error sending stats to Telegram: {e}")