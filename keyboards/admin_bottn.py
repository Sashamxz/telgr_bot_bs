from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


button_load = KeyboardButton('Завантажити')
button_delete = KeyboardButton('Видалити')
button_exit = KeyboardButton('Вийти')
button_cancel = KeyboardButton('Відмінити')

kb_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete).row(button_cancel,button_exit)