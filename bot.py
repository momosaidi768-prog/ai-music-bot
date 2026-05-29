import random
import os
import requests

# ================= TELEGRAM =================
TOKEN = "8202293986:AAFEmxYfIbVn6q27j0ibvEOElQF4Y68VPzQ"
CHAT_ID = "6675176280"

# ================= STYLES =================
styles = {
    "afro": "Afrobeat, summer vibe, catchy rhythm, male vocal",
    "rai": "Modern Moroccan Rai, emotional male voice, romantic",
    "dystinct": "Afro-pop / Rai fusion, catchy hook, emotional, danceable"
}

lyrics_pool = [
"""Ya lili ya lila
this night is ours
feel the rhythm flow""",

"""Ya habibi stay with me
فهاد الليل غير أنت
music in my soul""",

"""Every night I think about you
قلبي باقي معاك
under the moonlight
we shine so bright"""
]

# ================= GENERATE CONTENT =================
def generate_content():
    style_key = random.choice(list(styles.keys()))
    lyrics = random.choice(lyrics_pool)
    prompt = styles[style_key]

    print(f"STYLE: {style_key}")
    print(f"LYRICS: {lyrics}")
    print(f"PROMPT: {prompt}")

    return style_key, lyrics, prompt

# ================= CREATE VIDEO =================
def create_video():
    cmd = (
        "ffmpeg -y -loop 1 -i bg.jpg -i audio.mp3 "
        "-c:v libx264 -c:a aac -shortest -pix_fmt yuv420p final.mp4"
    )

    print("Running ffmpeg...")
    os.system(cmd)

    print("Video created ✔")

# ================= SEND VIDEO =================
def send_video():
    if not os.path.exists("final.mp4"):
        print("❌ final.mp4 not found")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"

    with open("final.mp4", "rb") as video:
        r = requests.post(
            url,
            data={"chat_id": CHAT_ID},
            files={"video": video}
        )

    print("Telegram response:", r.text)

# ================= MAIN =================
def main():
    style, lyrics, prompt = generate_content()

    create_video()

    send_video()

main()
