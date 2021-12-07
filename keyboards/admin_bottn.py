from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_load = KeyboardButton('/Завантажити')
button_delete = KeyboardButton('/Видалити')



kb_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)