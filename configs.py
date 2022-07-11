import os 
from dotenv import load_dotenv



dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    

TOKEN = os.environ.get('BOT_TOKEN')


config_redis={
   
    'REDIS_HOST' : os.environ.get('REDIS_HOST'),
    'REDIS_PASSWORD' : os.environ.get('REDIS_PASSWORD'),
    'REDIS_PORT' : os.environ.get('REDIS_PORT'),
    'REDIS_DB'  : os.environ.get('REDIS_DB'),
    'REDIS_STORAGE' :os.environ.get('REDIS_STORAGE')
}


    