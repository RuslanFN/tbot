import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
dotenv_path = os.path.join(os.path.dirname(__file__), 'env.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.environ.get('TOKEN')
URL = 'https://api.telegram.org/bot'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message):
    KB = ReplyKeyboardMarkup(resize_keyboard=True)
    KB.row(
        KeyboardButton(text="О мероприятии"),
        types.KeyboardButton(text="Программа мероприятия"))
    KB.row(types.KeyboardButton(text="Программа мероприятия"))
    KB.row(
        types.KeyboardButton(text="Спикеры"),
        types.KeyboardButton(text='Задать вопрос'))
    
    await message.answer("Пожалуйста, выберете интересующий Вас раздел", reply_markup=KB)

if __name__ == '__main__':
    executor.start_polling(dp)