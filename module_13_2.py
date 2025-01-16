from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7677049602:AAGg9-14ImQuY3YNjWXEQxdW3MbB7kTG74U'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, что бы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
