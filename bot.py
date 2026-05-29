import random
import os
import requests

# ================= TELEGRAM =================
TOKEN = "8202293986:AAFEmxYfIbVn6q27j0ibvEOElQF4Y68VPzQ"
CHAT_ID = "6675176280"

# ================= STYLES =================
styles = {
    "afro": "Afrobeat, summer vibe, catchy rhythm, male vocal, danceable",
    "rai": "Modern Moroccan Rai, emotional male voice, romantic fusion beat",
    "dystinct": "Afro-pop / Rai fusion, catchy hook, emotional, danceable"
}

lyrics_pool = [
"""Ya lili ya lila
this night is ours
feel the rhythm flow
don't let me go""",

"""Ya habibi stay with me
فهاد الليل غير أنت
music in my soul
and I feel alive""",

"""Every night I think about you
قلبي باقي معاك
under the moonlight
we shine so bright"""
]

# ================= GENERATE =================
def generate_content():
    style_key = random.choice(list(styles.keys()))
    lyrics = random.choice(lyrics_pool)
    prompt = styles[style_key]

    text = f"""
🎧 STYLE: {style_key.upper()}

🎤 LYRICS:
{lyrics}

🔥 PROMPT:
{prompt}
"""

    print(text)

    return style_key, lyrics, prompt

# ================= CREATE VIDEO =================
def create_video():
    # ffmpeg: image + audio => video
    os.system(
        "ffmpeg -y -loop 1 -i bg.jpg -i audio.mp3 "
        "-c:v libx264 -c:a aac -shortest -pix_fmt yuv420p final.mp4"
    )

# ================= SEND TELEGRAM =================
def send_video():
    url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"

    with open("final.mp4", "rb") as video:
        requests.post(
            url,
            data={"chat_id": CHAT_ID},
            files={"video": video}
        )

# ================= MAIN =================
def main():
    generate_content()

    # video build
    create_video()

    # send to Telegram
    send_video()

    print("DONE ✔")

main()
