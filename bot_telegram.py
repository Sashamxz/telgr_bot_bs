#!/usr/bin/python3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor
from configs import TOKEN   
# from client import  commands_start 

bot = Bot(token=TOKEN)
dp = Dispatcher(bot) 

async def on_startup(_):
    print('bot onlibe')



@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        
        await bot.send_message(message.from_user.id, f'Я бот. Hello, {message.from_user.first_name}')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, написать : \nhttps://t.me/Pizza_HBot')    

@dp.message_handler(commands=['Режим_роботи'])
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'пн-чт з 9:00 до 20:00, пт-сб з 10:00 до 20:00, недiля вихiдний')

@dp.message_handler(commands=['Розташування'])
async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Street')



@dp.message_handler(content_types=['text'])
async def get_text_messages(message: types.Message):
   if message.text.lower() == 'привет':
       await message.answer('Привет!')
   else:
       await message.answer('Не понимаю, что это значит.')


@dp.message_handler()
async def  echo(message : types.Message):
    await message.answer("///")
    


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)