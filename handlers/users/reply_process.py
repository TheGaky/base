import logging

from aiogram.dispatcher.filters import Command

from aiogram.types import Message, CallbackQuery

from keyboards.inline.buttons import start
from loader import dp, bot
from sql import insert_user
dp.message_handler()

latest_msg = {}




async def edit_msg(call, text, reply_markup):
    global latest_msg
    try:
        await latest_msg[call.from_user.id].edit_text(text, reply_markup=reply_markup)
    except Exception as e:
        logging.error(f"During {call.data} there was exception {e}")


@dp.message_handler(Command("start"))
async def show_items(message: Message):
    msg = await message.answer(
        text="Самое время найти немного географических данных.\nВас интересуют данные о городе или стране? \n", reply_markup=start)
    global latest_msg
    latest_msg[message.from_user.id] = msg
    if insert_user(message.from_user.username, message.from_user.id):
        logging.info(f"Hooray! We have a new user {message.from_user.username} with id {message.from_user.id}. It was successfully added to our database.")
    else:
        logging.warning(f"User {message.from_user.username} with id {message.from_user.id} already exists in the database or another error occurred!")


@dp.callback_query_handler(
    text_contains="city")
async def sub(call: CallbackQuery):
    await call.answer(cache_time=60)
    await edit_msg(call, "SHIT", start)