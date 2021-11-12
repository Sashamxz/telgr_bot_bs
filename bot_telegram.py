#!/usr/bin/python3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from configs import TOKEN   
# from client import  commands_start 

bot = Bot(token=TOKEN)
dp = Dispatcher(bot) 





@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        
        await bot.send_message(f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, написать : \nhttps://t.me/Pizza_HBot')    



@dp.message_handler()
async def  echo(message : types.Message):
    await message.answer("///")
    


executor.start_polling(dp, skip_updates=True)