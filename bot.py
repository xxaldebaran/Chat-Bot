from aiogram import Bot, Dispatcher, F
import asyncio
from app.handlers import router
from app.db.models import async_main 

async def main():
    await async_main()  # Connect to the database. This should be done before starting the bot polling.
    bot = Bot(token = '')
    disp = Dispatcher()

    disp.include_router(router)
    await disp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is down.")