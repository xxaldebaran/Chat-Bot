from aiogram import Bot, Dispatcher
import asyncio
from aiogram.types import Message 

bot = Bot(token = '')
disp = Dispatcher()

async def main():
    await disp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())