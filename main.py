import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.executor import start_webhook

BOT_TOKEN = "6708441310:AAHJlsxJtOlzrlqePiyNHTGCdr-KeSx1fPE"


# webhook settings
WEBHOOK_HOST = 'https://gaky.alwaysdata.net/'
WEBHOOK_PATH = '/bot/'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '::'
WEBAPP_PORT = 8350


bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())



dp.message_handler()


Admin_ID = 751989890

async def edit_msg(call, text):
    global latest_msg
    try:
        await latest_msg[call.from_user.id].edit_text(text)
    except Exception as e:
        logging.error(f"During {call.data} there was exception {e}")


@dp.message_handler(Command("start"))
async def show_items(message: Message):
    await bot.send_message(message.from_user.id,
                                  text="Здраствуйте! Пожалуйста, пришлите файл")

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def get_file_id_p(message: Message):
    await message.reply("Спасибо")
    # await message.reply(message.photo[-1].file_id)
    await bot.send_message(Admin_ID, message)
    await bot.send_document(Admin_ID, message.document.file_id)




async def on_startup(dp):
    logging.warning(
        'Starting connection. ')
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dp):
    logging.warning('Bye! Shutting down webhook connection')

def shit():
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

shit()
