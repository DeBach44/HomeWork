from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import texts
import asyncio

api = ''

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

#kl - обычная клавиатура
kl = ReplyKeyboardMarkup(resize_keyboard=True)
button_kl_1 = KeyboardButton(text='Расчитать')
button_kl_2 = KeyboardButton(text='Информация')
button_kl_3 = KeyboardButton(text='Купить')
kl.add(button_kl_1, button_kl_2, button_kl_3)

#kb - инлайн клавиатура Расчет и Формула
kb = InlineKeyboardMarkup(resize_keyboard=True)
button_kb_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_kb_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb.add(button_kb_1, button_kb_2)

#menu_kb - Меню Продуктов
menu_kb = InlineKeyboardMarkup(resize_keyboard=True)
button_mn_1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button_mn_2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button_mn_3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button_mn_4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
menu_kb.add(button_mn_1, button_mn_2, button_mn_3, button_mn_4)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for number in range(1,5):
        await message.answer(f'Название: Product{number} |Описание: описание {number} | Цена: {number * 100}')
        with open(f'Scrins/{number}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer(texts.get_buying_list_text, reply_markup = menu_kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(texts.send_confirm_message_text)
    await call.answer()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(texts.start, reply_markup=kl)

@dp.message_handler(text='Расчитать')
async def set_age(message):
    await message.answer('Выберите опцию:', reply_markup=kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(texts.fomula_m_s)
    await call.answer()

class UserState(StatesGroup):
    age = State()  # Возраст
    growth = State()  # Рост
    weight = State()  # Вес


# Функции для обработки состояний

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
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
    your_calories_norm = float(10 * float(data['weight']) +
    6.25 * float(data['growth']) - 5 * float(data['age']) + 5)
    await message.answer(f'Ваша норма калорий в день:{your_calories_norm}')
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer(texts.all_messages_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
