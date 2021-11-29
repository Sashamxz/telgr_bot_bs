from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Розташування')
b2 = KeyboardButton(' /Режим_роботи')
b3 = KeyboardButton ('/Меню')
b4 = KeyboardButton('Номер телефрну', request_contact=True)
b5 = KeyboardButton('Де я',request_location=True)



kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1,b2,b3).add(b4).add(b5)