from aiogram import Bot, Dispatcher, F
import asyncio
from app.handlers import router
import os

async def main():
    bot = Bot(token = '')
    disp = Dispatcher()

    disp.include_router(router)
    await disp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is down.")