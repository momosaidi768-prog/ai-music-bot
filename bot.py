import time
import requests
from playwright.sync_api import sync_playwright

TOKEN = "8202293986:AAFEmxYfIbVn6q27j0ibvEOElQF4Y68VPzQ"
CHAT_ID = "6675176280"

PROMPTS = [
    "Afrobeat summer vibe, catchy rhythm, male vocal, emotional chorus",
    "Modern Moroccan Rai, emotional male voice, romantic fusion beat",
    "Afro-pop DYSTINCT style, catchy hook, danceable vibe"
]

def generate_prompt():
    import random
    return random.choice(PROMPTS)

# ================= SUNO AUTOMATION =================
def run_suno(prompt):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("🌐 Opening Suno...")
        page.goto("https://suno.com")

        print("⏳ WAIT: login manually if needed")
        time.sleep(20)  # تعطيك وقت تدخل للحساب

        print("🎤 Writing prompt...")
        page.fill("textarea", prompt)

        print("🚀 Clicking generate...")
        page.keyboard.press("Enter")

        print("⏳ Wait for generation...")
        time.sleep(60)  # وقت توليد الأغنية

        print("✅ Done - download song manually")
        browser.close()

# ================= TELEGRAM =================
def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

# ================= MAIN =================
def run():
    prompt = generate_prompt()

    send_message(f"""
🎧 SUNO AUTO BOT

🔥 PROMPT:
{prompt}

➡️ Go to Suno and check result
""")

    run_suno(prompt)

run()
