from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Завантажити')



kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.row(b1)