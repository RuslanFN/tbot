from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

async def StartButtons():
    KB = InlineKeyboardMarkup()
    buttons = [InlineKeyboardButton('Регистрация', callback_data='singup'), InlineKeyboardButton('О мероприятии', callback_data='About Event'), InlineKeyboardButton(text='Спикеры', callback_data='Spickers'), InlineKeyboardButton(text='Программа мероприятия', callback_data='Programm event')]
    for i in buttons:
        KB.add(i)
    return KB

async def HomeButton():
     KB = InlineKeyboardMarkup().add(InlineKeyboardButton('Вернуться в меню', callback_data='start'))
     return KB

async def format_p():
     KB = InlineKeyboardMarkup().add(InlineKeyboardButton('Очно', callback_data='full-time'), InlineKeyboardButton('Заочно', callback_data='absentia'))
     return KB

async def Is_SMI():
     KB = InlineKeyboardMarkup().add(InlineKeyboardButton('Да', callback_data='IsSMI'), InlineKeyboardButton('Нет', callback_data='NotSMI'))
     return KB

async def PersonalData():
     KB = InlineKeyboardMarkup().add(InlineKeyboardButton('Да', callback_data='Yes'), InlineKeyboardButton('Нет', callback_data='No'))
     return KB