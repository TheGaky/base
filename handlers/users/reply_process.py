import logging

from aiogram.dispatcher.filters import Command

from aiogram.types import Message, CallbackQuery

from keyboards.inline.buttons import start, decision

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


from loader import dp, bot

dp.message_handler()

latest_msg = {}
latest_user_msg = {}


class Form(StatesGroup):
    A = State()
    B = State()
    C = State()
    D = State()
    E = State()
    F = State()


async def edit_msg(call, text, reply_markup):
    global latest_msg
    try:
        await latest_msg[call.from_user.id].edit_text(text, reply_markup=reply_markup)
    except Exception as e:
        logging.error(f"During {call.data} there was exception {e}")


@dp.message_handler(Command("start"))
async def show_items(message: Message):
    await Form.A.set()
    msg = await message.answer(
        text="Самое время найти немного географических данных.\nВас интересуют данные о городе или стране? \n", reply_markup=start)
    global latest_msg
    latest_msg[message.from_user.id] = msg
    await message.delete()


@dp.callback_query_handler(state=Form.A)
async def sub(call: CallbackQuery):

    await call.delete()
    await edit_msg(call, "...сосредотачиваюсь на том, что мне нужно сделать дальше – на следующем шаге", decision)
    await Form.B.set()


@dp.callback_query_handler(state=Form.B)
async def sub(call: CallbackQuery):

    await call.delete()
    await edit_msg(call, "…начинаю что-то делать, зная, что это все равно не будет работать, главное – делать хоть что-нибудь", decision)
    await Form.C.set()


@dp.callback_query_handler(state=Form.C)
async def sub(call: CallbackQuery):

    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)
    await Form.D.set()