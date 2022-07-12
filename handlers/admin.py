from typing import Text
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot, dp                
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_bottn
from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup , reply_keyboard
from keyboards import kb_client


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
    await bot.send_message(message.from_user.id, 'Вхід в панель адміністратора виконано', reply_markup= admin_bottn.kb_case_admin)
    await message.delete()    

 



#вхід в "машину стану" , завантаження фото 
async def cm_start(message : types.Message):
    if message.from_user.id == ID:    
        await FSMAdmin.photo.set()
        await message.reply('Завантажити фото') 


#передчасний вихід з "машини станів" без збереження 
async def cancel_hndl(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:      
        current_state = await state.get_state()
        if current_state is None:
            return 0
        await state.finish()
        await message.reply('ok')    



#вихід з панелі адміністратора з передчасним  завершенням  всіх незбережених форм
async def exit_admin(message: types.Message, state: FSMContext):
    curent_state = await  state.get_state()
    
    if curent_state is None:
        await bot.send_message(message.from_user.id, 'Вихід з меню адмінстратора1 ', reply_markup=kb_client)
    
    else:
        await cancel_hndl(message, state)
        await bot.send_message(message.from_user.id, 'Вихід з меню адмінстратора2 ', reply_markup=kb_client)
        await message.reply('створення об\'єкта скасовано')




async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("dell ", "")} видалено.',show_alert=True)



#видалення  позиції з бази данних  
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОпис: {ret[2]}\nЦіна {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                add(InlineKeyboardButton(f'Видалити {ret[1]}', callback_data=f'del {ret[1]}'))) 


#відповідь від користувача , машина стану "назва"
async def load_photo(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:      
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Ввести назву:')    


#2th відповідь від користувача
async def load_name(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:      
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Ввести описання:')    


#3th відповідь від користувача
async def load_description(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Вкажіть ціну:')    


#4th відповідь від користувача  
@dp.message_handler(state=FSMAdmin.price)
async def load_price(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.isdigit(): 
            data['price'] = float(message.text)
        else:
            await bot.send_message(message.from_user.id, 'введіть коректну ціну ')   
    await sqlite_db.sql_add_command(state)
    await state.finish()
    await bot.send_message(message.from_user.id, 'Успішно додано.')



def registrate_hndl_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands='Завантажити', state=None)    
    dp.register_message_handler(cancel_hndl, state='*', commands='Відмінити')
    dp.register_message_handler(cancel_hndl,Text(equals='Відмінити', ignore_case = True), state='*')
    dp.register_message_handler(exit_admin,  state='*', commands='Вийти')
    dp.register_message_handler(exit_admin, Text(equals='Вийти', ignore_case = True),  state='*')
    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))
    dp.register_message_handler(delete_item, commands='Видалити')
    dp.register_message_handler(load_photo, content_types=['photo'], state= FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)    
   