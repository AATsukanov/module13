from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import tsukanoff

token = tsukanoff.token
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Информация', callback_data='info')
kb.add(button)

@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer('Рады Вас видеть!', reply_markup=kb)

@dp.callback_query_handler(text='info')
async def information(call):
    await call.message.answer('Какая-то любая информация о боте...')
    await call.answer()  # для деактивации кнопки после нажатия

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)