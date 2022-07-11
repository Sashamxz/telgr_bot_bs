import logging
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from configs import config_redis, TOKEN 
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.middlewares.logging import LoggingMiddleware


storage=RedisStorage2(
    host=config_redis.get('REDIS_HOST'), 
    port=config_redis.get('REDIS_PORT'),
    db=config_redis.get('REDIS_DB'),
    password=config_redis.get('REDIS_PASSWORD'),
    storage = config_redis.get('REDIS_STORAGE')
)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage) 
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)