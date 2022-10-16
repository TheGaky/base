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


a_score = {}
b_score = {}
c_score = {}
d_score = {}
e_score = {}
f_score = {}
g_score = {}
h_score = {}


type_a = {}
type_b = {}
type_c = {}
type_d = {}
type_e = {}
type_f = {}
type_g = {}
type_h = {}


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
    AY = State()


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
    a_score[message.from_user.id] = 0
    b_score[message.from_user.id] = 0
    c_score[message.from_user.id] = 0
    d_score[message.from_user.id] = 0
    e_score[message.from_user.id] = 0
    f_score[message.from_user.id] = 0
    g_score[message.from_user.id] = 0
    h_score[message.from_user.id] = 0

    msg = await bot.send_message(message.from_user.id, text="Оказавшись в трудной ситуации, я...\n", reply_markup=decision)
    msg2 = await bot.send_message(message.from_user.id, text="...сосредотачиваюсь на том, что мне нужно сделать дальше – на следующем шаге")
    await Form.A.set()
    await message.delete()

    fuck_msg[message.from_user.id] = msg
    latest_msg[message.from_user.id] = msg2


@dp.message_handler(state=Form.A)
async def sub(call: CallbackQuery):
    type_c[call.from_user.id] = call.text()
    await edit_msg(call, "…начинаю что-то делать, зная, что это все равно не будет работать, главное – делать хоть что-нибудь")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.B)
async def sub(call: CallbackQuery):
    type_a[call.from_user.id] = call.text()
    await edit_msg(call, "…пытаюсь склонить вышестоящих к тому, чтобы они изменили свое мнение")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.C)
async def sub(call: CallbackQuery):
    type_a[call.from_user.id] = call.text()
    await edit_msg(call, "…говорю с другими, чтобы побольше узнать о ситуации")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.D)
async def sub(call: CallbackQuery):
    type_a[call.from_user.id] = call.text()
    await edit_msg(call, "…критикую и укоряю себя")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.E)
async def sub(call: CallbackQuery):
    type_a[call.from_user.id] = call.text()
    await edit_msg(call, "…говорю с другими, чтобы побольше узнать о ситуации")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.F)
async def sub(call: CallbackQuery):
    type_a[call.from_user.id] = call.text()
    await edit_msg(call, "…пытаюсь не сжигать за собой мосты, оставляя все, как оно есть")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.G)
async def sub(call: CallbackQuery):
    type_a[call.from_user.id] = call.text()
    await edit_msg(call, "…надеюсь на чудо")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.H)
async def sub(call: CallbackQuery):
    type_b[call.from_user.id] = call.text()
    await edit_msg(call, "… смиряюсь с судьбой: бывает, что мне просто не везет")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.I)
async def sub(call: CallbackQuery):
    type_b[call.from_user.id] = call.text()
    await edit_msg(call, "…веду себя так, как будто ничего не произошло")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.J)
async def sub(call: CallbackQuery):
    type_b[call.from_user.id] = call.text()
    await edit_msg(call, "… стараюсь не показывать своих чувств")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.K)
async def sub(call: CallbackQuery):
    type_b[call.from_user.id] = call.text()
    await edit_msg(call, "…пытаюсь увидеть в ситуации что-то положительное")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.L)
async def sub(call: CallbackQuery):
    type_b[call.from_user.id] = call.text()
    await edit_msg(call, "…сплю больше обычного")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.M)
async def sub(call: CallbackQuery):
    type_b[call.from_user.id] = call.text()
    await edit_msg(call, "…срываю свою досаду на тех, кто навлек на меня проблемы")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.N)
async def sub(call: CallbackQuery):
    type_c[call.from_user.id] = call.text()
    await edit_msg(call, "…ищу сочувствия и понимания у кого-нибудь")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.O)
async def sub(call: CallbackQuery):
    type_c[call.from_user.id] = call.text()
    await edit_msg(call, "…во мне возникает потребность выразить себя творчески")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.P)
async def sub(call: CallbackQuery):
    type_c[call.from_user.id] = call.text()
    await edit_msg(call, "…пытаюсь забыть все")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.Q)
async def sub(call: CallbackQuery):
    type_c[call.from_user.id] = call.text()
    await edit_msg(call, "…обращаюсь за помощью к специалистам")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.R)
async def sub(call: CallbackQuery):
    type_c[call.from_user.id] = call.text()
    await edit_msg(call, "…меняюсь или расту как личность в положительную сторону")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.S)
async def sub(call: CallbackQuery):
    type_d[call.from_user.id] = call.text()
    await edit_msg(call, "…извиняюсь или стараюсь все сгладить")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.T)
async def sub(call: CallbackQuery):
    type_d[call.from_user.id] = call.text()
    await edit_msg(call, "… составляю план действий")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.U)
async def sub(call: CallbackQuery):
    type_d[call.from_user.id] = call.text()
    await edit_msg(call, "…стараюсь дать какой-то выход своим чувствам")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.V)
async def sub(call: CallbackQuery):
    type_d[call.from_user.id] = call.text()
    await edit_msg(call, "… понимаю, что сам вызвал эту проблему")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.W)
async def sub(call: CallbackQuery):
    type_d[call.from_user.id] = call.text()
    await edit_msg(call, "…набираюсь опыта в этой ситуации")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.X)
async def sub(call: CallbackQuery):
    type_d[call.from_user.id] = call.text()
    await edit_msg(call, "…говорю с кем-либо, кто может конкретно помочь в этой ситуации")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.Y)
async def sub(call: CallbackQuery):
    type_d[call.from_user.id] = call.text()
    await edit_msg(call, "…пытаюсь улучшить свое самочувствие едой, выпивкой, курением или лекарствами")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.Z)
async def sub(call: CallbackQuery):
    type_e[call.from_user.id] = call.text()
    await edit_msg(call, "…рискую напропалую")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AB)
async def sub(call: CallbackQuery):
    type_e[call.from_user.id] = call.text()
    await edit_msg(call, "…стараюсь действовать не слишком поспешно, доверяясь первому порыву")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AC)
async def sub(call: CallbackQuery):
    type_e[call.from_user.id] = call.text()
    await edit_msg(call, "…нахожу новую веру во что-то")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AD)
async def sub(call: CallbackQuery):
    type_e[call.from_user.id] = call.text()
    await edit_msg(call, "…вновь открываю для себя что-то важное")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AE)
async def sub(call: CallbackQuery):
    type_e[call.from_user.id] = call.text()
    await edit_msg(call, "…что-то меняю так. Что все улаживается")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AF)
async def sub(call: CallbackQuery):
    type_e[call.from_user.id] = call.text()
    await edit_msg(call, "…в целом избегаю общения с людьми")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AG)
async def sub(call: CallbackQuery):
    type_f[call.from_user.id] = call.text()
    await edit_msg(call, "…не допускаю этого до себя, стараюсь об этом особенно не задумываться")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AH)
async def sub(call: CallbackQuery):
    type_f[call.from_user.id] = call.text()
    await edit_msg(call, "…спрашиваю совета у родственника или друга, которых уважаю")
    await Form.next()
    await call.delete()



@dp.message_handler(state=Form.AI)
async def sub(call: CallbackQuery):
    type_f[call.from_user.id] = call.text()
    await edit_msg(call, "…стараюсь, чтобы другие не узнали, как плохо обстоят дела")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AJ)
async def sub(call: CallbackQuery):
    type_f[call.from_user.id] = call.text()
    await edit_msg(call, "…отказываюсь воспринимать это слишком серьезно")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AK)
async def sub(call: CallbackQuery):
    type_f[call.from_user.id] = call.text()
    await edit_msg(call, "…говорю о том, что чувствую")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AL)
async def sub(call: CallbackQuery):
    type_f[call.from_user.id] = call.text()
    await edit_msg(call, "…стою на своем, и борюсь за то, что хочу")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AM)
async def sub(call: CallbackQuery):
    type_f[call.from_user.id] = call.text()
    await edit_msg(call, "..вымещаю это на других людях")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AN)
async def sub(call: CallbackQuery):
    type_g[call.from_user.id] = call.text()
    await edit_msg(call, "…пользуюсь прошлым опытом – мне приходилось уже попадать в такие ситуации")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AO)
async def sub(call: CallbackQuery):
    type_g[call.from_user.id] = call.text()
    await edit_msg(call, "…знаю, что надо делать и удваиваю свои усилия, чтобы все наладить")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AP)
async def sub(call: CallbackQuery):
    type_g[call.from_user.id] = call.text()
    await edit_msg(call, "...отказываюсь верить, что это действительно произошло")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AQ)
async def sub(call: CallbackQuery):
    type_g[call.from_user.id] = call.text()
    await edit_msg(call, "…я даю обещание, что в следующий раз все будет по-другому")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AR)
async def sub(call: CallbackQuery):
    type_h[call.from_user.id] = call.text()
    await edit_msg(call, "…нахожу пару других способов решения проблемы")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AS)
async def sub(call: CallbackQuery):
    type_h[call.from_user.id] = call.text()
    await edit_msg(call, "…стараюсь, чтобы мои эмоции не слишком мешали мне в других делах")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AT)
async def sub(call: CallbackQuery):
    type_h[call.from_user.id] = call.text()
    await edit_msg(call, "…что-то меняю в себе")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AU)
async def sub(call: CallbackQuery):
    type_h[call.from_user.id] = call.text()
    await edit_msg(call, "…хочу, чтобы все это скорее как-то образовалось или кончилось")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AV)
async def sub(call: CallbackQuery):
    type_h[call.from_user.id] = call.text()
    await edit_msg(call, "…представляю себе, фантазирую, как все это могло бы обернуться")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AW)
async def sub(call: CallbackQuery):
    type_h[call.from_user.id] = call.text()
    await edit_msg(call, "…молюсь")
    await Form.next()
    await call.delete()



@dp.message_handler(state=Form.AW)
async def sub(call: CallbackQuery):
    type_h[call.from_user.id] = call.text()
    await edit_msg(call, "…прокручиваю в уме, что мне сказать или сделать")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AX)
async def sub(call: CallbackQuery):
    type_h[call.from_user.id] = call.text()
    await edit_msg(call, "…думаю о том, как бы в данной ситуации действовал человек, которым я восхищаюсь, и стараюсь подражать ему")
    await Form.next()
    await call.delete()


@dp.message_handler(state=Form.AY)
async def count(call: CallbackQuery):
    await latest_msg[call.from_user.id].delete()
    await fuck_msg[call.from_user.id].delete()


    for i in type_a:
        if i == "Никогда":
            a_score[call.from_user.id] += 0
        if i == "Редко":
            a_score[call.from_user.id] += 1
        if i == "Иногда":
            a_score[call.from_user.id] += 2
        if i == "Часто":
            a_score[call.from_user.id] += 3

    for i in type_b:
        if i == "Никогда":
            b_score[call.from_user.id] += 0
        if i == "Редко":
            b_score[call.from_user.id] += 1
        if i == "Иногда":
            b_score[call.from_user.id] += 2
        if i == "Часто":
            b_score[call.from_user.id] += 3

    for i in type_c:
        if i == "Никогда":
            c_score[call.from_user.id] += 0
        if i == "Редко":
            c_score[call.from_user.id] += 1
        if i == "Иногда":
            c_score[call.from_user.id] += 2
        if i == "Часто":
            c_score[call.from_user.id] += 3

    for i in type_d:
        if i == "Никогда":
            d_score[call.from_user.id] += 0
        if i == "Редко":
            d_score[call.from_user.id] += 1
        if i == "Иногда":
            d_score[call.from_user.id] += 2
        if i == "Часто":
            d_score[call.from_user.id] += 3

    for i in type_e:
        if i == "Никогда":
            e_score[call.from_user.id] += 0
        if i == "Редко":
            e_score[call.from_user.id] += 1
        if i == "Иногда":
            e_score[call.from_user.id] += 2
        if i == "Часто":
            e_score[call.from_user.id] += 3

    for i in type_f:
        if i == "Никогда":
            f_score[call.from_user.id] += 0
        if i == "Редко":
            f_score[call.from_user.id] += 1
        if i == "Иногда":
            f_score[call.from_user.id] += 2
        if i == "Часто":
            f_score[call.from_user.id] += 3

    for i in type_g:
        if i == "Никогда":
            g_score[call.from_user.id] += 0
        if i == "Редко":
            g_score[call.from_user.id] += 1
        if i == "Иногда":
            g_score[call.from_user.id] += 2
        if i == "Часто":
            g_score[call.from_user.id] += 3

    for i in type_h:
        if i == "Никогда":
            h_score[call.from_user.id] += 0
        if i == "Редко":
            h_score[call.from_user.id] += 1
        if i == "Иногда":
            h_score[call.from_user.id] += 2
        if i == "Часто":
            h_score[call.from_user.id] += 3

    await bot.send_message(call.from_user.id, text=f"Ваш результат: A - {a_score[call.from_user.id]}, B - {b_score[call.from_user.id]}, C - {c_score[call.from_user.id]}, D - {d_score[call.from_user.id]}, E - {e_score[call.from_user.id]}, F - {f_score[call.from_user.id]}, G - {g_score[call.from_user.id]}, H - {h_score[call.from_user.id]}")