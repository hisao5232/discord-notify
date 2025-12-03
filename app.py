import os
import requests
from dotenv import load_dotenv

# .env 読み込み
load_dotenv()

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
TITLE = os.getenv("DISCORD_TITLE", "")
DETAIL = os.getenv("DISCORD_DETAIL", "")
LINK_URL = os.getenv("DISCORD_LINK_URL", "")

def send_discord_message():
    if not WEBHOOK_URL:
        raise ValueError("DISCORD_WEBHOOK_URL が設定されていません")

    # Discord Markdown 形式でメッセージ構築
    message = f"""**{TITLE}**

{DETAIL}

🔗 **アクセスリンク**
{LINK_URL}
"""

    payload = {"content": message}

    response = requests.post(WEBHOOK_URL, json=payload)

    if response.status_code not in (200, 204):
        print("送信エラー:", response.status_code, response.text)
    else:
        print("送信成功！")

if __name__ == "__main__":
    send_discord_message()
