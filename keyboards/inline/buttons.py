from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from aiogram.utils.callback_data import CallbackData

get_callback = CallbackData("get", "item_name")


start = ReplyKeyboardMarkup()


like_start = KeyboardButton(text="Начать", callback_data=get_callback.new(item_name="start"))
start.insert(like_start)


decision = ReplyKeyboardMarkup()


never = KeyboardButton(text="Никогда", callback_data=get_callback.new(item_name="never"))
seldom = KeyboardButton(text="Редко", callback_data=get_callback.new(item_name="seldom"))
sometimes = KeyboardButton(text="Иногда", callback_data=get_callback.new(item_name="sometimes"))
often = KeyboardButton(text="Часто", callback_data=get_callback.new(item_name="often"))

decision.insert(never)
decision.insert(seldom)
decision.insert(sometimes)
decision.insert(often)


dick = InlineKeyboardMarkup()

sick = InlineKeyboardButton(text="Никогда", callback_data=get_callback.new(item_name="sick"))
dick.insert(sick)