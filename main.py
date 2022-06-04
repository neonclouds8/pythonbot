import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5159579275:AAFhg7CwKSqrAmXGH91E-leHvZS8vGMSXfo'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/Сайт", "/Телеграмм"]
    keyboard.add(*buttons)
    await message.answer("?", reply_markup=keyboard)


@dp.message_handler(commands="Сайт")
async def cmd_inline_url(message: types.Message):
    button = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*button)
    await message.answer("Кнопка-ссылка", reply_markup=keyboard)

@dp.message_handler(commands="Телеграмм")
async def cmd_inline_url(message: types.Message):
    button = [
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*button)
    await message.answer("Кнопка-ссылка", reply_markup=keyboard)



@dp.message_handler()
async def echo(message: types.Message):
	await message.answer(message.text)


if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)
