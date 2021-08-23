from os import getenv, environ
from dotenv import load_dotenv

# bot settings
load_dotenv()
API_TOKEN = getenv("API_TOKEN")
STATE_DICT_PATH = getenv("STATE_DICT_PATH")
IMAGE_FORMATS = ['png', 'jpg', 'jpeg']

# webhook settings
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{API_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'  # or ip
WEBAPP_PORT = int(getenv("PORT"))
