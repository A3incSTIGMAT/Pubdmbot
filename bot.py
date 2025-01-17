from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import logging

API_TOKEN = 'YOUR_API_TOKEN'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to the bot!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
