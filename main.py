from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from flask import Flask, request
import os

TOKEN = "ВАШ_БОТ_ТОКЕН"
WEBHOOK_URL = "https://ВАШ_ХОСТИНГ/webhook"  # Замените на URL вашего сервера

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
app = Flask(__name__)

# Обработка команд
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Это тестовый бот с вебхуком.")

# Flask-обработчик для Telegram webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.json, bot)
    dp.feed_update(bot, update)
    return "OK", 200

# Установить вебхук
async def set_webhook():
    await bot.set_webhook(WEBHOOK_URL)

if __name__ == "__main__":
    from aiogram import executor

    # Устанавливаем вебхук
    import asyncio
    asyncio.run(set_webhook())

    # Запускаем Flask
    app.run(host="0.0.0.0", port=8443)
