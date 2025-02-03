from config import *
from keyboards import *
from  crud_functions import *
import texts
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

all_products = get_all_products()

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text='Арендовать')
async def get_buying_list(message):
    a,b,c = 1,2,3
    for i in range(4):
        await message.answer(f'Название: {all_products[i][a]} |Описание: {all_products[i][b]} | Цена: {all_products[i][c]}')
        with open(f'Scrins/{i}.jpg', 'rb') as img:
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

#_______________________________________________________________________________
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

class UserState(StatesGroup):
    age = State()  # Возраст
    growth = State()  # Рост
    weight = State()  # Вес

#Фукнции цепочки состояний RegistrationState____________________________________

@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state = RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text) == False:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data_user = await state.get_data()#Создается словарь
    add_user(data_user['username'], data_user['email'], data_user['age'])
    await message.answer('Регистрация прошла успешно')
    await state.finish()
#Конец цепочки состояний RegistrationState_________________________________________


#Функции цепочки состояний UserState_______________________________________________

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

#Конец цепочки состояний UserState___________________________________________
@dp.message_handler()
async def all_messages(message):
    await message.answer(texts.all_messages_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
