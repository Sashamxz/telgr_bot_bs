from bot_telegram import *

@dp.message_handler(commands=['start', 'help'])
async def commands_start(message : type.Message):
    try:
        await bot.send_message(message.from_user.id, ' Good')
        await bot.send_message (f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
        await message.delete()
    except:
        await message.reple('Общение с ботом через ЛС, написать : \nhttps://t.me/Pizza_HBot')    