from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import tsukanoff

token = tsukanoff.token
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Открыть клавиатуру', callback_data='open_menu')
kb.add(button)

start_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Запуск'), KeyboardButton(text='Отмена')],
              [KeyboardButton(text='Одна кнопка')],
              [KeyboardButton(text='Продать'), KeyboardButton(text='Держать'), KeyboardButton(text='Купить')]],
    resize_keyboard=True
)

@dp.message_handler(commands=['start'])
async def starter(message):
    await message.answer('Рады Вас видеть!', reply_markup=kb)

@dp.callback_query_handler(text='open_menu')
async def information(call):
    await call.message.answer('Меню кнопок', reply_markup=start_menu)
    await call.answer()  # для деактивации кнопки после нажатия

@dp.message_handler()
async def all_messages(message):
    print(f'Получено: {message.text}')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)