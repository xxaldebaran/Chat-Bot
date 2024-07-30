from aiogram import Bot, Dispatcher
import asyncio
from app.handlers import router
from app.db.models import async_main 
from app.config import TG_TOKEN


async def main():
    await async_main() 
    bot = Bot(token = TG_TOKEN)
    disp = Dispatcher()

    disp.include_router(router)
    await disp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot is down.")