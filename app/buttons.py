from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from app.db.requests import get_categories
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'STEM 🔭')],
                                     [KeyboardButton(text = 'Cataloge 📚'), KeyboardButton(text = 'Help 🆘')],
                                     [KeyboardButton(text = 'Contacts 📱'), KeyboardButton(text = 'About Us 🛈')]], 
                                     resize_keyboard=True,
                                     input_field_placeholder='What do you want to do?')

# stem = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text = 'AI 🤖', callback_data='ai')], 
#     [InlineKeyboardButton(text = 'CS 💻', callback_data='cs')],
#     [InlineKeyboardButton(text = 'Physics 🪐', callback_data='physics')]])

async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()

    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text = category.name, callback_data= f"category_{category.id}" ))
    keyboard.add(InlineKeyboardButton(text = 'Back', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()