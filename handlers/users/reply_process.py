import logging
import time

from aiogram.dispatcher.filters import Command

from aiogram.types import Message, CallbackQuery, ContentType

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import pandas as pd

from base.loader import dp, bot

dp.message_handler()

latest_msg = {}

Admin_ID = 751989890

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class States():
    AWAITING_USER_ACTION = 'awaiting_user_action'


async def edit_msg(call, text):
    global latest_msg
    try:
        await latest_msg[call.from_user.id].edit_text(text)
    except Exception as e:
        logging.error(f"During {call.data} there was exception {e}")

counter = 2

@dp.message_handler(Command("start"))
async def show_items(message: Message, state: FSMContext):
    await message.delete()
    table_path = "/Users/gaky/PycharmProjects/Anonymous Poll/base/Опросник для Гаки 3.xlsx"
    exel_data = pd.read_excel(table_path)
    columns = exel_data.columns.tolist()
    question = columns[0][2]
    answers = []

    for j in range(1, len(columns)):
        answers.append(exel_data[columns[j]][2])


    #creating keyboard
    keyboard = InlineKeyboardMarkup()

    # Add buttons to the keyboard
    button1 = InlineKeyboardButton(answers[0], callback_data='button1')
    button2 = InlineKeyboardButton(answers[1], callback_data='button2')
    button3 = InlineKeyboardButton(answers[2], callback_data='button1')
    button4 = InlineKeyboardButton(answers[3], callback_data='button2')

    # Add buttons to the row
    keyboard.add(button1, button2, button3, button4)

    msg = await message.answer(question, reply_markup=keyboard)
    latest_msg[message.from_user.id] = msg


    # Set the state to AWAITING_USER_ACTION
    await States.AWAITING_USER_ACTION.set()


async def handle_user_action(message: types.Message, state: FSMContext):
    if (await state.get_state()) == States.AWAITING_USER_ACTION:

        global counter
        counter += 1
        table_path = "/Users/gaky/PycharmProjects/Anonymous Poll/base/Опросник для Гаки 3.xlsx"
        exel_data = pd.read_excel(table_path)
        columns = exel_data.columns.tolist()
        question = columns[0][counter]
        answers = []


        for j in range(1, len(columns)):
            answers.append(exel_data[columns[j]][counter])

        # creating keyboard
        keyboard = InlineKeyboardMarkup()

        # Add buttons to the keyboard
        button1 = InlineKeyboardButton(answers[0], callback_data='button1')
        button2 = InlineKeyboardButton(answers[1], callback_data='button2')
        button3 = InlineKeyboardButton(answers[2], callback_data='button1')
        button4 = InlineKeyboardButton(answers[3], callback_data='button2')

        # Add buttons to the row
        keyboard.add(button1, button2, button3, button4)

        await latest_msg[message.from_user.id].delete()

        await message.answer(question, reply_markup=keyboard)

        # Set the state to AWAITING_USER_ACTION
        await States.AWAITING_USER_ACTION.set()


# Add handlers to the dispatcher
#dp.register_message_handler(start_command, commands=['start'])
#dp.register_message_handler(handle_user_action, state=States.AWAITING_USER_ACTION)

def get_data(table_path):
    exel_data = pd.read_excel(table_path)
    columns = exel_data.columns.tolist()

    for i in range(3, 30):
        question = columns[0][i]
        answers = []

        for j in range(1, 4):
            answers.append(columns[i][j])











"""@dp.message_handler(content_types=ContentType.PHOTO)
async def get_file_id_p(message: Message):
    await message.reply("Спасибо")
    # await message.reply(message.photo[-1].file_id)
    await bot.send_photo([Admin_ID], message.photo[-1].file_id)

"""



"""@dp.message_handler(Command("start"))
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
"""