#from aiogram import Bot, Dispatcher, executor, types
import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = aiogram.Bot(token = api)
dp = aiogram.Dispatcher(bot, storage=MemoryStorage())#aiogram.contrib.fsm_storage.memory.MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.' )

@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    aiogram.executor.start_polling(dp, skip_updates=True)
