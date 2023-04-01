from aiogram import Bot, Dispatcher, executor, types

token = '6007030410:AAGoQhqNUzPo7nLjt0ePEozjzL2aDaTOXBQ'
bot = Bot(token)
dp = Dispatcher(bot)


# @dp.message_handler(commands=['start'])  #
@dp.message_handler(content_types=['text'])  # text input only
async def start(message: types.Message):
    await message.answer('Hello')


executor.start_polling(dp)