from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'STEM 🔭')],
                                     [KeyboardButton(text = 'Contacts 📱'), KeyboardButton(text = 'About Us 🛈')]], 
                                     resize_keyboard=True,
                                     input_field_placeholder='What do you want to do?')

stem = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'AI 🤖', callback_data='ai')], 
    [InlineKeyboardButton(text = 'CS 💻', callback_data='cs')],
    [InlineKeyboardButton(text = 'Physics 🪐', callback_data='physics')]])