#!/usr/bin/python3

from aiogram.utils import executor
from create_bot import dp




async def on_startup(_):
    print('bot online')

from handlers import client, admin, others

client.registrate_hndl_client(dp)
admin.registrate_hndl_admin(dp)
others.registrate_hndl_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)