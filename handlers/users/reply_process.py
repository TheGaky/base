import logging
import time

from aiogram.dispatcher.filters import Command

from aiogram.types import Message, CallbackQuery

from keyboards.inline.buttons import start, decision, dick

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


from loader import dp, bot

dp.message_handler()

latest_msg = {}
fuck_msg = {}


class Form(StatesGroup):
    A = State()
    B = State()
    C = State()
    D = State()
    E = State()
    F = State()
    G = State()
    H = State()
    I = State()
    J = State()
    K = State()
    L = State()
    M = State()
    N = State()
    O = State()
    P = State()
    Q = State()
    R = State()
    S = State()
    T = State()
    U = State()
    V = State()
    W = State()
    X = State()
    Y = State()
    Z = State()
    AB = State()
    AC = State()
    AD = State()
    AE = State()
    AF = State()
    AG = State()
    AH = State()
    AI = State()
    AJ = State()
    AK = State()
    AL = State()
    AM = State()
    AN = State()
    AO = State()
    AP = State()
    AQ = State()
    AR = State()
    AS = State()
    AT = State()
    AU = State()
    AV = State()
    AW = State()
    AX = State()


"""async def edit_msg(call, text, reply_markup):
    global latest_msg
    try:
        await latest_msg[call.from_user.id].edit_text(text, reply_markup=reply_markup)
    except Exception as e:
        logging.error(f"During {call.data} there was exception {e}")
"""

async def edit_msg(call, text):
    global latest_msg
    try:
        await latest_msg[call.from_user.id].edit_text(text)
    except Exception as e:
        logging.error(f"During {call.data} there was exception {e}")


@dp.message_handler(Command("start"))
async def show_items(message: Message, state: FSMContext):
    msg = await bot.send_message(message.from_user.id, text="Оказавшись в трудной ситуации, я...\n", reply_markup=decision)
    msg2 = await bot.send_message(message.from_user.id, text="...сосредотачиваюсь на том, что мне нужно сделать дальше – на следующем шаге")
    await Form.A.set()
    await message.delete()

    fuck_msg[message.from_user.id] = msg
    latest_msg[message.from_user.id] = msg2


@dp.message_handler(state=Form.A)
async def sub(call: CallbackQuery):
    await edit_msg(call, "…начинаю что-то делать, зная, что это все равно не будет работать, главное – делать хоть что-нибудь")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.B)
async def sub(call: CallbackQuery):
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.D)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение")


@dp.message_handler(state=Form.F)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.G)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)



@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)



@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    await Form.next()
    await call.delete()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение", decision)