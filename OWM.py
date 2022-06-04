import asyncio

from yaweather import Russia, YaWeatherAsync
import logging
from aiogram import Bot, Dispatcher, executor, types

from ya import y

y = Ya(api_key='8bcd756d-1b23-465a-b405-788021b3a951')
API_TOKEN = '5159579275:AAFhg7CwKSqrAmXGH91E-leHvZS8vGMSXfo'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(content_types=['text'])
async def echo(message):
    res = await y.forecast(Russia.Moscow)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    place = input("В каком городе?")

    answer = ("В городе" + message.text + "сейчас" + w.detailed_status + "\n")

    answer += ("Температура сейчас в районе" + str(temp) + "\n\n")


    await message.answer(answer)



if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)