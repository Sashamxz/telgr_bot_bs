from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from configs import TOKEN  
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage=MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage) 