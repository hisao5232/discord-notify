Discord Notify (Docker + Cron)

Docker コンテナを使って Discord の Webhook に通知 を送る最小構成プロジェクトです。
メッセージ内容や Webhook URL は ".env" に記載し、ホスト側の cron から
"docker compose run" を実行することで定期通知できます。

---

📁 ディレクトリ構成

discord-notify/
├── docker-compose.yml
├── Dockerfile
├── notify.py
├── .env.example
├── .gitignore
└── README.md

---

🔧 ".env" の設定

".env.example" をコピー：

cp .env.example .env

そして以下を記入：

DISCORD_WEBHOOK_URL=あなたのWebhookURL
TITLE=お知らせタイトル
DETAIL=ここに複数行の詳細メッセージを記述できます。
LINK_URL=https://example.com

メッセージは Discord マークダウン に対応しています。

---

▶️ 実行方法（手動）

docker compose run --rm notify

---

⏰ cron による定期実行（例：2日に1回 朝7時）

ホスト側のcronに下記を追加：

crontab -e

0 7 */2 * * cd /home/youruser/discord-notify && docker compose run --rm notify

---

🐳 Docker Compose

手動実行と同じく "notify" サービスが単発で起動し、完了すると終了します。

---

📘 送信される Discord メッセージ形式

**タイトル**

詳細メッセージ（複数行可）

👉 アクセスはこちら: https://example.com

---

🔑 GitHub への push

SSH 推奨：

git remote set-url origin git@github.com:yourname/discord-notify.git
git push -u origin main

---

📄 ライセンス

MIT License
自由に改造して使用できます。
