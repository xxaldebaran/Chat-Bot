from aiogram import F, Router 
from aiogram.types import Message 
from aiogram.filters import CommandStart, Command 

import app.buttons as buttons

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi there!", reply_markup=buttons.main)
    await message.reply("What`s poping?")

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("How can I help you?")

@router.message(F.text == "Tell a dad`s joke!")
async def dad_joke(message: Message):
    await message.answer("Do you know why you never see elephants hiding in trees? It`s because they`re so good at it.")

@router.message(F.text == "List")
async def list(message: Message):
    await message.answer("Pick an option.", reply_markup=buttons.list)
