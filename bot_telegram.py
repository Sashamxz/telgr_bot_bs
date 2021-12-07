#!/usr/bin/python3

from aiogram.utils import executor
from create_bot import dp

from data_base import sqlite_db


async def on_startup(_):
    print('bot online')
    sqlite_db.sql_start()

from handlers import  admin, client, others


client.registrate_hndl_client(dp)
admin.registrate_hndl_admin(dp)
others.registrate_hndl_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)