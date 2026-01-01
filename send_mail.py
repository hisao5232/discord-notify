import os
import resend
from dotenv import load_dotenv

load_dotenv()

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_REPLY_TO = os.getenv("EMAIL_REPLY_TO")

resend.api_key = RESEND_API_KEY

def send_email(subject: str, html: str):
    if not RESEND_API_KEY or not EMAIL_TO:
        raise ValueError("RESEND_API_KEY または EMAIL_TO が設定されていません")

    error_html = f"""
        <div style="color: red; margin-top: 20px;">
            <strong>⚠ エラーが発生しました</strong><br>
            {html}
        </div>
    """

    r = resend.Emails.send({
        "from": EMAIL_FROM,
        "to": EMAIL_TO,
        "subject": subject,
        "html": error_html,
        "reply_to": EMAIL_REPLY_TO,
    })

    print("メール送信結果:", r)
    return r

# --------------------------------------------
# 🔥 テスト実行用
# --------------------------------------------
if __name__ == "__main__":
    send_email(
        subject="テストメール - send_mail.py から送信",
        html="これはテスト送信です。エラー通知ではありません。"
    )