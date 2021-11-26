import os 
import sys
from dotenv import load_dotenv



dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


TOKEN = os.environ.get('BOT_TOKEN')


    