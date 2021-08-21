from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.utils.callback_data import CallbackData

get_callback = CallbackData("get", "item_name")


start = InlineKeyboardMarkup(row_width=2)
bruh = InlineKeyboardButton(text="Консульский отдел", callback_data=get_callback.new(item_name="bruh"))
start.insert(bruh)
