from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from torch import load, device

import config
import logging

# Configure logging
from model import Generator

logging.basicConfig(level=logging.INFO)

# Initialize bot, storage and dispatcher
storage = MemoryStorage()
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot, storage=storage)

# load model
model = Generator()
model.load_state_dict(load(config.STATE_DICT_PATH, map_location=device('cpu')))
model.eval()
