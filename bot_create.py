from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot
import os
TOKEN = '6213098654:AAGLDr_a0ED6behDV_fOfck_XVcEs5Ljj_o'
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
