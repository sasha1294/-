from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

botton1 = KeyboardButton('Video')
botton2 = KeyboardButton('Skreenshot')

KD_test2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
KD_test2.add(botton1).add(botton2)