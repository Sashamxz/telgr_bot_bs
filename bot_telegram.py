#!/usr/bin/python3
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from configs import TOKEN   


bot = Bot(token=TOKEN)
dp = Dispatcher(bot) 

@dp.message_handler()
async def  echo(message : types.Message):
    await message.answer("BIM")
    


executor.start_polling(dp, skip_updates=True)