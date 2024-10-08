# ставим python 3.9
# ставим aiogram 2.25.1

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api_key = '...'
bot = Bot(token=api_key)
dsp = Dispatcher(bot=bot, storage=MemoryStorage())

@dsp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я -- бот помогающий твоему здоровью.')

@dsp.message_handler()
async def all_messages(message):
    # print(type(message))
    # print(f'Получено сообщение: {message}')
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dsp, skip_updates=True)

'''
Цель: написать простейшего телеграм-бота, используя асинхронные функции.

Подготовка:
Выполните все действия представленные в предыдущих видео модуля, создав и подготовив Telegram-бот для дальнейших заданий.

Задача "Бот поддержки (Начало)":
К коду из подготовительного видео напишите две асинхронные функции:
start(message) - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.' 
Запускается только когда написана команда '/start' в чате с ботом (используйте соответствующий декоратор).

all_massages(message) - печатает строку в консоли 'Введите команду /start, чтобы начать общение.'. 
Запускается при любом обращении не описанном ранее. (используйте соответствующий декоратор)
Запустите ваш Telegram-бот и проверьте его на работоспособность.
Пример результата выполнения программы:
Ввод в чат Telegram:
Хэй!
/start
Вывод в консоль:
Updates were skipped successfully.
Введите команду /start, чтобы начать общение.
Привет! Я бот помогающий твоему здоровью.
'''

