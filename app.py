import os
import requests
from dotenv import load_dotenv
from send_mail import send_email   # ← 追加

# .env 読み込み
load_dotenv()

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
TITLE = os.getenv("DISCORD_TITLE", "")
DETAIL = os.getenv("DISCORD_DETAIL", "")
LINK_URL = os.getenv("DISCORD_LINK_URL", "")

def send_discord_message():
    if not WEBHOOK_URL:
        error_msg = "DISCORD_WEBHOOK_URL が設定されていません"
        send_email(
            subject="Discord 通知エラー",
            html=f"<p>{error_msg}</p>"
        )
        raise ValueError(error_msg)

    # Discord Markdown 形式のメッセージ
    message = f"""**{TITLE}**

{DETAIL}

🔗 **アクセスリンク**
{LINK_URL}
"""

    payload = {"content": message}

    try:
        response = requests.post(WEBHOOK_URL, json=payload)

        if response.status_code not in (200, 204):
            error_msg = f"Discord Webhook エラー: {response.status_code} {response.text}"
            print(error_msg)

            # 🔥 エラー時にメール送信
            send_email(
                subject="Discord Webhook エラー発生",
                html=f"<p>{error_msg}</p>"
            )

        else:
            print("送信成功！")

    except Exception as e:
        # 🔥 例外発生時にもメール送信
        error_msg = f"例外が発生しました: {str(e)}"
        print(error_msg)

        send_email(
            subject="Discord 通知処理で例外発生",
            html=f"<p>{error_msg}</p>"
        )

if __name__ == "__main__":
    send_discord_message()
