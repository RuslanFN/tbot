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
    name = State()
    job = State()
    place_job = State()
    participation_format = State()
    Is_SMI = State()
    Cuntry = State()
    subject_RF = State()
    Town = State()
    Email = State()
    accept = State()
    Done = State()
    


@dp.message_handler(commands=['start'])
async def process_start_command(message):
    KB = await buttons.StartButtons()
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text="Выберете нужный раздел", reply_markup=KB)

@dp.callback_query_handler(text='start')
async def start_message(query):
    if query.data == 'start':
        KB = await buttons.StartButtons()
        user_id = query.from_user.id
        await bot.send_message(chat_id=user_id, text="Выберете нужный раздел", reply_markup=KB)

@dp.message_handler(state=UserState.name)
async def get_username(message: types.Message, state):
    await state.update_data(name=message.text)
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text='Введите Вашу должность')
    await UserState.job.set()

@dp.message_handler(state=UserState.job)
async def get_Job(message: types.Message, state):
    await state.update_data(job=message.text)
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text='Введите Ваше место работы')
    await UserState.place_job.set()
    
@dp.message_handler(state=UserState.place_job)
async def get_PlaceJob(message: types.Message, state):
    await state.update_data(place_job=message.text)
    KB = await buttons.format_p()
    user_id = message.from_user.id
    await state.update_data(chat_id=user_id)
    await bot.send_message(chat_id=user_id, text='Введите формат участия в мероприятии', reply_markup=KB)
    
@dp.callback_query_handler(lambda c: c.data.__eq__('full-time'), state=UserState.place_job)
@dp.callback_query_handler(lambda c: c.data == 'absentia', state=UserState.place_job)
async def get_participation_format(query, state):
    if query.data == 'full-time':
        await state.update_data(participation_format='Очно')
    if query.data == 'absentia':
        await state.update_data(participation_format='Заочно')
    data = await state.get_data()
    user_id = data['chat_id']
    await bot.send_message(chat_id=user_id, text='Вы представитель СМИ?', reply_markup= await buttons.Is_SMI())
    await UserState.Is_SMI.set()

@dp.callback_query_handler(lambda c: c.data.__eq__('IsSMI'), state=UserState.Is_SMI)
@dp.callback_query_handler(lambda c: c.data == 'NotSMI', state=UserState.Is_SMI)
async def get_participation_format(query, state):
    if query.data == 'IsSmi':
        await state.update_data(IsSmi='Да')
    if query.data == 'NotSmi':
        await state.update_data(IsSmi='Нет')
    await query.message.reply("В какой стране вы проживаете?")
    await UserState.Cuntry.set()

@dp.message_handler(state=UserState.Cuntry)
async def get_subject(message: types.Message, state):
    await state.update_data(Cuntry=message.text)
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text='Введите Вашу область')
    await UserState.subject_RF.set()

@dp.message_handler(state=UserState.subject_RF)
async def get_Town(message: types.Message, state):
    await state.update_data(Subject=message.text)
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text='Введите Ваш город')
    await UserState.Town.set()

@dp.message_handler(state=UserState.Town)
async def get_Email(message: types.Message, state):
    await state.update_data(Town=message.text)
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text='Введите Ваш Email')
    await UserState.Email.set()

@dp.message_handler(state=UserState.Email)
async def get_accept(message: types.Message, state):
    await state.update_data(Email=message.text)
    user_id = message.from_user.id
    KB = await buttons.PersonalData()
    await bot.send_message(chat_id=user_id, text='Вы согласны на обработку персональных данных', reply_markup=KB)
    
@dp.callback_query_handler(lambda c: c.data == 'Yes', state=UserState.Email)
@dp.callback_query_handler(lambda c: c.data == 'No', state=UserState.Email)
async def get_participation_format(query, state):
    if query.data == 'Yes':
        await state.update_data(accept='Да')
    if query.data == 'No':
        await state.update_data(accept='Нет')
    data = await state.get_data()
    user_id = data['chat_id']
    DATA={'name': data['name'], 'job':data['job'], 'place_job':data['place_job'], 
    'participation_format':data['participation_format'], 'IsSmi':data['IsSmi'], 
    'Cuntry':data['Cuntry'], 'Subject':data['Subject'], 'Town':data['Town'],
    'Email':data['Email'], 'Email':data['Email'], 'accept':data['accept']}
    await state.finish()
    await bot.send_message(chat_id=user_id, text='Вы успешно зарегестрированы!', reply_markup=await buttons.HomeButton()) 
    
@dp.callback_query_handler()
async def Menu(query: types.CallbackQuery):
    if query.data == 'About Event':
        KB = await buttons.HomeButton()
        await query.message.reply("ITFESTINFO", reply_markup=KB)

    if query.data == 'Spickers':
        KB =await  buttons.HomeButton()
        await query.message.reply("Спикеры", reply_markup=KB)
        
    if query.data == 'Programm event':
        KB =await buttons.HomeButton()
        await query.message.reply("Программа мероприятия", reply_markup=KB)

    if query.data == 'singup':
        user_id = query.from_user.id
        await bot.send_message(chat_id=user_id, text='Введите Ваши ФИО в формате:\nФамилия Имя Отчество')
        await UserState.name.set()
   


if __name__ == '__main__':
    executor.start_polling(dp)