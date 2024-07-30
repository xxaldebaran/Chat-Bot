from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from app.db.requests import get_categories, get_category_item
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='STEM 🔭')],
                                     [KeyboardButton(text='Contacts 📱'),
                                      KeyboardButton(text='About Us 🛈')]],
                           resize_keyboard=True,
                           input_field_placeholder='What do you want to do?')


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    keyboard.add(InlineKeyboardButton(text='On main', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text='On main', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

# stem = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text = 'AI 🤖', callback_data='ai')], 
#     [InlineKeyboardButton(text = 'CS 💻', callback_data='cs')],
#     [InlineKeyboardButton(text = 'Physics 🪐', callback_data='physics')]])

# async def categories():
#     all_categories = await get_categories()
#     keyboard = InlineKeyboardBuilder()

#     for category in all_categories:
#         keyboard.add(InlineKeyboardButton(text = category.name, callback_data= f"category_{category.id}" ))
#     keyboard.add(InlineKeyboardButton(text = 'Back', callback_data='to_main'))
#     return keyboard.adjust(2).as_markup()


# async def items(category_id):
#     all_items = await get_category_item(category_id)
#     keyboard = InlineKeyboardBuilder()

#     for item in all_items:
#         keyboard.add(InlineKeyboardButton(text = item.name, callback_data= f"item_{item.id}" ))
#     keyboard.add(InlineKeyboardButton(text = 'Back', callback_data='to_main'))
#     return keyboard.adjust(2).as_markup()