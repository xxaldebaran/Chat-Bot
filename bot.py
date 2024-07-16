from aiogram import Bot, Dispatcher, F
import asyncio
from aiogram.types import Message 
from aiogram.filters import CommandStart, Command 

bot = Bot(token = '')
disp = Dispatcher()

@disp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi there!")
    await message.reply("What`s poping?")

@disp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("How can I help you?")

@disp.message(F.text == "Tell a dad`s joke!")
async def dad_joke(message: Message):
    await message.answer("Do you know why you never see elephants hiding in trees? It`s because they`re so good at it.")

async def main():
    await disp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())