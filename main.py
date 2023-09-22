import asyncio
from search_fun import *
from MKB_dict import letters_set
from config import BOT_TOKEN, HELPER_TOKEN, CHAT_ID
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# import logging
# logging.basicConfig(level=logging.INFO)

MESS_MAX_LENGTH = 4096

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
bot_helper = Bot(HELPER_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)


@dp.message_handler(commands=["start"])
async def start(message: Message):
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="/start")
            ],
            [
                KeyboardButton(text="/help"),
                KeyboardButton(text="/info")
            ],
        ],
        resize_keyboard=True
    )
    mess = f"Привет, <b>{message.from_user.first_name} </b>, введи код МКБ или тескт и я покажу, что я знаю" \
           f"\n {'_' * 14} " \
           f"\n <i>by</i> cynacmam"
    await message.answer(text=mess, reply_markup=menu, parse_mode="html")


@dp.message_handler(commands=["help"])
async def help(message: Message):
    mess = f"\n- <b>Обратная связь</b> - начни сообщение с //" \
           f"\n   <i>(пример - //не работет поиск)</i>" \
           f"\n {'_' * 14} " \
           f"\n <i>by</i> cynacmam"
    await message.answer(text=mess, parse_mode="html")


@dp.message_handler(commands=["info"])
async def info(message: Message):
    mess = f"- При поиске по кодам исспользуйте <b>латиницу</b>" \
           f"\n   <i>(пример - D36, С50.1)</i>" \
           f"\n- <b>Регистр не учитывается</b>" \
           f"\n - При слишком длинном ответе, попробуйте уточнить запрос" \
           f"\n   <i>(пример - не <b>нос</b>, а <b>носа</b>)</i>" \
           f"\n {'_' * 14} " \
           f"\n <i>by</i> cynacmam"
    await message.answer(text=mess, parse_mode="html")


@dp.message_handler()
async def user_text(message: Message):

    if len(message.text) > 2:
        if message.text.startswith("//"):
            await bot_helper.send_message(chat_id=CHAT_ID,
                                          text=f"{message.text} - {message.from_user.first_name}: {message.from_user.id}")
        # отправляет ответ по запросу с кодом МКБ
        elif message.text[:1].upper() in letters_set:
            await bot.send_message(message.chat.id, f"{search_mkb(message.text)}", parse_mode="html")
        else:
            # (1) разделяет сообщения при превышении допустимого количества символов MESS_MAX_LENGTH
            # и отправляет ответ по запросу с текстом
            if len(searh_text(message.text)) == 0:
                await message.answer(text="***Неверный запрос***", parse_mode="html")
            elif len(searh_text(message.text)) > MESS_MAX_LENGTH:
                for x in range(0, len(searh_text(message.text)), MESS_MAX_LENGTH):
                    mess = searh_text(message.text)[x: x + MESS_MAX_LENGTH]
                    await bot.send_message(message.chat.id, mess, parse_mode="html")
            else:
                await bot.send_message(message.chat.id, searh_text(message.text), parse_mode="html")
    else:
        await bot.send_message(message.chat.id, "***Слишком короткий запрос. Попробуй снова***")


async def send_to_admin(dp):
    await bot.send_message(chat_id=CHAT_ID, text="Бот запущен")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=send_to_admin, skip_updates=True)
