from aiogram import Bot, Dispatcher
import asyncio
from aiogram.types import Message 

bot = Bot(token = '')
disp = Dispatcher()

@disp.message()
async def cmd_start(message: Message):
    await message.answer("Hi there!")
    await message.reply("What`s poping?")

async def main():
    await disp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
