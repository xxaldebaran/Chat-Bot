from aiogram import Bot, Dispatcher, F
import asyncio
from app.handlers import router
from dotenv import load_dotenv 
import os

load_dotenv(os.getenv('TOKEN'))

async def main():
    bot = Bot(token = '7476823431:AAFz1K2IsXWugeX5MXe-jVXQ8-R_GEOLD0Q')
    disp = Dispatcher()

    disp.include_router(router)
    await disp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is down.")