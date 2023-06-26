from aiogram.utils import executor
from bot_create import dp
from database.test4 import start_db, DELETE
start_db()
DELETE()
print("бот вышел в онлайн")


executor.start_polling(dp, skip_updates=True)