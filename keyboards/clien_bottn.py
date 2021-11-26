from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Розташування')
b2 = KeyboardButton('/Режим роботи')
b3 = KeyboardButton ('/Меню')

kb_client = ReplyKeyboardMarkup()
kb_client.add(b1).add(b2).add(b3)