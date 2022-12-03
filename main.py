import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import buttons

dotenv_path = os.path.join(os.path.dirname(__file__), 'env.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

storage = MemoryStorage()
TOKEN = os.environ.get('TOKEN')
URL = 'https://api.telegram.org/bot'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    start = State()
    sing_up = State()
    f_name = State()
    s_name = State()
    l_name = State()



@dp.message_handler(commands=['start'])
async def process_start_command(message):
    KB = await buttons.StartButtons()
    await message.reply("Выберете нужный раздел", reply_markup=KB)

@dp.callback_query_handler(text='start')
async def start_message(query):
    if query.data == 'start':
        KB = await buttons.StartButtons()
        await query.message.reply("Выберете нужный раздел", reply_markup=KB)

@dp.callback_query_handler()
async def Menu(query: types.CallbackQuery):
    if query.data == 'About Event':
        KB = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton(text='Вернуться в меню', callback_data='start'))
        await query.message.reply("ITFESTINFO", reply_markup=KB)
        UserState.start.set()

    if query.data == 'Spickers':
        KB = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton(text='Вернуться в меню', callback_data='start'))
        await query.message.reply("Спикеры", reply_markup=KB)
        UserState.start.set()
        
    if query.data == 'Programm event':
        KB = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton(text='Вернуться в меню', callback_data='start'))
        await query.message.reply("Программа мероприятия", reply_markup=KB)
        UserState.start.set()
        
    


if __name__ == '__main__':
    executor.start_polling(dp)