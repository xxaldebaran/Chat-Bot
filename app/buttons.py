from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'List')],
                                     [KeyboardButton(text = 'Basket')],
                                     [KeyboardButton(text = 'Contacts'), KeyboardButton(text = 'About Us')]], 
                                     resize_keyboard=True,
                                     input_field_placeholder='What do you want to do?')

list = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Option 1', callback_data='option-1')], 
    [InlineKeyboardButton(text = 'Option 2', callback_data='option-2')]])