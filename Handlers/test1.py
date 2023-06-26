from bot_create import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from Botton import test2
from Handlers import test3
from database import test4
class FSMuser:
    start_class = State()
    chosee1_state = State()
    video_state = State()
    scrin_state = State()


async def start(message: types.Message):
    await message.answer('Доброго временни суток!')
    await message.answer('Это бот для создания скринщотов и видеозаписей экрана')
    await message.answer('Приятного пользования')
    await FSMuser.start_class.set()

async def choses1(message: types.Message):
    await message.answer('Что вы хотите получить?', reply_markup=test2.KD_test2)
    await FSMuser.chosee1_state.set()

async def choses2(message: types.Message):
    if message.text == 'Video':
        await message.answer('Загрузка')
        await FSMuser.video_state.set()
    elif message.text == 'Skreenshot':
        await message.answer('Загрузка')
        await FSMuser.scrin_state.set()

async def video_result(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['video'] = message.text
    await test4.result1(message.text)
    await message.answer("Напишите длительность видео")

    await test3.DELETE()
    await message.answer("Перезапустите бота")
    await st
