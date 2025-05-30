import logging
import telebot
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# === НАСТРОЙКИ ===

BOT_TOKEN = '7785373251:AAH0DDXN3nJdXvERWlxOOcSqF-KHydlMEYA'
ADMIN_USERNAME = '@eurasianpart'
SPREADSHEET_ID = '1D2ayHbqJjHy7YapWi8a-FN3mHMa0aIb1qjQwRPG2i6o'

# === ИНИЦИАЛИЗАЦИЯ ===

bot = telebot.TeleBot(BOT_TOKEN)

# Авторизация в Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# Логирование
logging.basicConfig(level=logging.INFO)

# === ОБРАБОТКА СООБЩЕНИЙ ===

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Отправь заявку в формате:\n\nМарка\nМодель\nГод\nVIN или описание детали")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user = message.from_user.username or message.from_user.id
    text = message.text.strip()

    # Отправка админу
    bot.send_message(ADMIN_USERNAME, f"🔧 Новая заявка:\n\n{text}\n\nОт: @{user}")

    # Логирование в таблицу
    sheet.append_row([str(message.date), str(user), text])

    # Ответ пользователю
    bot.send_message(message.chat.id, "✅ Спасибо! Заявка отправлена.")

# === ЗАПУСК ===

bot.polling(none_stop=True)
