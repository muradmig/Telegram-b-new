# Telegram Bot для приёма заявок на автозапчасти

## 📌 Возможности:
- Принимает текстовые заявки от пользователей (в формате CSV)
- Пересылает заявки в Telegram (на @eurasianpart)
- Логирует заявки в Google Sheets

## ⚙️ Настройка:
1. Получи токен у @BotFather и задай переменную окружения `BOT_TOKEN`
2. Получи ID Google таблицы и задай переменную `SPREADSHEET_ID`
3. Загрузи `credentials.json` с ключом сервисного аккаунта

## ▶️ Запуск:
```bash
pip install -r requirements.txt
python main.py
```