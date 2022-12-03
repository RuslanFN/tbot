import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
dotenv_path = os.path.join(os.path.dirname(__file__), 'env.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.environ.get('TOKEN')
URL = 'https://api.telegram.org/bot'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message):
    KB = InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [InlineKeyboardButton('О мероприятии', callback_data='About Event'), InlineKeyboardButton(text='Спикеры', callback_data='Spickers'), InlineKeyboardButton(text='Программа мероприятия', callback_data='Programm event')]
    KB.add(*buttons)
    await message.reply("Выберете нужный раздел", reply_markup=KB)

@dp.callback_query_handler()
async def Menu(query: types.CallbackQuery):
    if query.data == 'About Event':
        KB = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton(text='Вернуться в меню', callback_data='start'))
        await query.message.reply("ITFESTINFO", reply_markup=KB)
        
    if query.data == 'Spickers':
        KB = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton(text='Вернуться в меню', callback_data='start'))
        await query.message.reply("Спикеры", reply_markup=KB)
        
    if query.data == 'Programm event':
        KB = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton(text='Вернуться в меню', callback_data='start'))
        await query.message.reply("Программа мероприятия", reply_markup=KB)
        
    


if __name__ == '__main__':
    executor.start_polling(dp)