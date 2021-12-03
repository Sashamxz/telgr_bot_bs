# from aiogram import types
# from aiogram.dispatcher.dispatcher import Dispatcher
# from create_bot import dp, bot
# from keyboards import kb_client

# @dp.message_handler(commands=['start', 'help'])
# async def command_start(message : types.Message):
#     try:
        
#         await bot.send_message(message.from_user.id, f'Я бот. Hello, {message.from_user.first_name}', reply_markup=kb_client)
#         await message.delete()
#     except:
#         await message.reply('Общение с ботом через ЛС, написать : \nhttps://t.me/Pizza_HBot')    


# @dp.message_handler(commands=['Режим_роботи'])
# async def pizza_open_command(message : types.Message):
# 	await bot.send_message(message.from_user.id, 'пн-чт з 9:00 до 20:00, пт-сб з 10:00 до 20:00, недiля вихiдний')


# @dp.message_handler(commands=['Розташування'])
# async def pizza_place_command(message : types.Message):
# 	await bot.send_message(message.from_user.id, 'Street')


# @dp.message_handler(commands=['Меню'])
# async def pizza_place_command(message : types.Message):
# 	await bot.send_message(message.from_user.id, 'Меню')


# def registrate_hndl_client(dp : Dispatcher):
#     dp.register_message_handler(command_start, commands=['start', 'help'])    
#     dp.register_message_handler(pizza_open_command, commands=['Режим_роботи'])
#     dp.register_message_handler(pizza_place_command, commands=['Розташування'])
  