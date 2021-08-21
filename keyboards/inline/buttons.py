from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from aiogram.utils.callback_data import CallbackData

get_callback = CallbackData("get", "item_name")


start = ReplyKeyboardMarkup(row_width=2)
country = KeyboardButton(text="Страна", callback_data=get_callback.new(item_name="country"))

start.insert(country)

city = KeyboardButton(text="Город", callback_data=get_callback.new(item_name="city"))
start.insert(city)