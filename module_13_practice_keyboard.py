from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher import FSMContext
# для клавиатур:
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = '***'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Начало')
kb.add(button1)
kb.add(button2)
# kb.row..., kb.insert...

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет!', reply_markup=kb)

@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Здесь будет информация о боте...')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)