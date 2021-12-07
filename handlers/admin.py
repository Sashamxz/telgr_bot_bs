from typing import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import   types
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.types import reply_keyboard
from create_bot import bot, dp                
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from data_base.sqlite_db import sql_add_command
from keyboards import admin_bottn



ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

#Получаем ID текущего модератора         
@dp.message_handler(commands=['moderator'], is_chat_admin=True) 
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Перевірку пройдено', reply_keyboard= admin_bottn.kb_case_admin)
    await message.delete()    

#загрузка нового пункта меню
@dp.message_handler(commands='Завантажити', state=None)
async def cm_start(message : types.Message):
    if message.from_user.id == ID:    
        await FSMAdmin.photo.set()
        await message.reply('Завантажити фото') 

# @dp.message_handler(state='*', commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_hndl(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:      
        current_state = await state.get_state()
        if current_state is None:
            return 0
        await state.finish()
        await message.reply('ok')    



#ответ от пользоваетеля
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:      
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Ввести назву:')    


#второй ответ от пользователя 
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:      
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Ввести описання:')    


#тритий ответ от пользователя 
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Вкажіть ціну:')    


#тритий ответ от пользователя 
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    await sqlite_db.sql_add_command(state)
    await state.finish()
    



def registrate_hndl_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['Завантажити'], state=None)    
    dp.register_message_handler(cancel_hndl, state='*', commands='Відміна')
    dp.register_message_handler(cancel_hndl,Text(equals='Відміна', ignore_case = True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state= FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)    