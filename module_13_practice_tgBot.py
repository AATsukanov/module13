from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = '***'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    user_address = State()

@dp.message_handler(text=['Заказать', 'заказать'])
async def buy(message):
    await message.answer('Напишите, пожалуйста, Ваш адрес для доставки')
    await UserState.user_address.set()

@dp.message_handler(state=UserState.user_address)
async def fsm_handler(message, state):
    await state.update_data(first_param=message.text)
    data = await state.get_data()
    await message.answer(f'Заказ будет отправлен по адресу: {data["first_param"]}')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)