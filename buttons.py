from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

async def StartButtons():
    KB = InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [InlineKeyboardButton('О мероприятии', callback_data='About Event'), InlineKeyboardButton(text='Спикеры', callback_data='Spickers'), InlineKeyboardButton(text='Программа мероприятия', callback_data='Programm event')]
    KB.add(*buttons)
    return KB