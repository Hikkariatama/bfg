# bot version: 1.3.4,1

import config as cfg
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(cfg.7526333379:AAGStsBN5Z950Cne1HxIPmfg4UmT1dhLQ7o, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
