from aiogram import F, Router 
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart, Command 
from aiogram.fsm.context import FSMContext
import app.buttons as buttons

router = Router()

class RegisterHandler(StatesGroup):
    name = State()
    email = State()

@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(RegisterHandler.name)
    await message.answer("Enter your credentials.")

@router.message(RegisterHandler.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(RegisterHandler.email)
    await message.answer("Enter your email.")

@router.message(RegisterHandler.email)
async def register_email(message: Message, state: FSMContext):
    await state.update_data(email = message.text)
    data = await state.get_data()
    await message.answer(f"Your name is {data['name']} and your email is {data['email']}.")
    await state.clear()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hi there!", reply_markup=buttons.main)
    # await message.reply("What`s poping?")

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("How can I help you?")

@router.message(F.text == "Tell a dad`s joke!")
async def dad_joke(message: Message):
    await message.answer("Do you know why you never see elephants hiding in trees? It`s because they`re so good at it.")

@router.message(F.text == "STEM 🔭")
async def stem(message: Message):
    await message.answer("Pick an option.", reply_markup=buttons.stem)


@router.callback_query(F.data == "ai")
async def ai(callback: CallbackQuery):
    await callback.answer("You picked option AI.")
    await callback.message.answer("You picked AI.")

@router.callback_query(F.data == "cs")
async def cs(callback: CallbackQuery):
    await callback.answer("You picked option CS.")
    await callback.message.answer("You picked CS.")
 
@router.callback_query(F.data == "physics")
async def physics(callback: CallbackQuery):
    await callback.answer("You picked option Physics.")
    await callback.message.answer("You picked Physics.")

@router.message(F.text == "About Us 🛈")
async def aboutus(message: Message):
    await message.answer("This bot is created by Daria.")
    
@router.message(F.text == "Contacts 📱")
async def contacts(message: Message):
    await message.answer("My email: darinkatovstogan@gmail.com")