'''Цель: научится создавать клавиатуры и кнопки на них в Telegram-bot.
Задача "Меньше текста, больше кликов":'''

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
# для клавиатур:
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

'''
Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах 
тела для расчёта калорий выдавались по нажатию кнопки.
Измените massage_handler для функции set_age. 
Теперь этот хэндлер будет реагировать на текст 'Рассчитать', а не на 'Calories'.
Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней 
со следующим текстом: 'Рассчитать' и 'Информация'. 
Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства 
при помощи параметра resize_keyboard.
Используйте ранее созданную клавиатуру в ответе функции start, 
используя параметр reply_markup.
В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками. 
При нажатии на кнопку с надписью 'Рассчитать' срабатывает функция set_age, 
с которой начинается работа машины состояний для age, growth и weight.
'''
api = '...'
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.row(button1, button2)
# kb.add..., kb.insert...

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я -- бот помогающий твоему здоровью.',
                         reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Я -- бот, рассчитывающий норму ккал по упрощенной формуле Миффлина-Сан Жеора.')


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост (см):')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес (кг):')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    try:
        age = float(data['age'])
        weight = float(data['weight'])
        growth = float(data['growth'])
    except:
        await message.answer(f'Не могу конвертировать введенные значения в числа.')
        await state.finish()
        return

    # Упрощенный вариант формулы Миффлина-Сан Жеора:
    # для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5
    calories_man = 10 * weight + 6.25 * growth - 5 * age + 5
    #для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161
    calories_wom = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f'Норма (муж.): {calories_man} ккал')
    await message.answer(f'Норма (жен.): {calories_wom} ккал')
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    print(f'Получено: {message.text}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
