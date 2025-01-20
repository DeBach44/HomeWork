from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kl = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Расчитать')
button_2 = KeyboardButton(text='Информация')
kl.add(button_1)
kl.add(button_2)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kl)


class UserState(StatesGroup):
    age = State()  # Возраст
    growth = State()  # Рост
    weight = State()  # Вес


# Функции для обработки состояний

@dp.message_handler(text='Расчитать')
async def set_age(message):
    await message.answer('Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    # Мужская норма
    your_calories_norm = float(10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5)
    await message.answer(f'Ваша норма калорий в день:{your_calories_norm}')
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, что бы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
