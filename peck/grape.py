import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5491837862:AAFf6AbaXTjbHxJiN4ELkFJG_V_3wYyQal8'

odin_doma = 'https://yandex.ru/images/search?from=tabbar&text=%D0%BE%D0%B4%D0%B8%D0%BD%20%D0%B4%D0%BE%D0%BC%D0%B0&pos=5&img_url=https%3A%2F%2Fodin-doma-film.ru%2Fwp-content%2Fuploads%2F2019%2F11%2F1545628680-6vdjkwvjry.jpg&rpt=simage&lr=213&rlt_url=https%3A%2F%2Fbusinessman.ru%2Fstatic%2Fimg%2Fn%2F2%2F1%2F6%2F1%2F9%2F8%2F0%2Fi%2F2161980.jpg&ogl_url=https%3A%2F%2Fodin-doma-film.ru%2Fwp-content%2Fuploads%2F2019%2F11%2F1545628680-6vdjkwvjry.jpg'
ono = "https://trikky.ru/wp-content/blogs.dir/1/files/2021/12/02/s-6f1af4d99def54e83f6e312f35e941cc9c64f58c.jpg"
avatar = "https://mobimg.b-cdn.net/v3/fetch/a3/a3b4e5ed83e97a654d4831cccb1d7e6a.jpeg?w=1470"
igra_prestolov = "https://avatars.mds.yandex.net/get-zen_doc/1548443/pub_6026bc51241d462d4482422b_6026bced331cb763521c5442/scale_1200"
dostat_noji = 'https://yandex.ru/images/search?from=tabbar&text=%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D1%82%D1%8C%20%D0%BD%D0%BE%D0%B6%D0%B8&pos=6&img_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FEKake4KWwAAfXXN.jpg&rpt=simage&lr=120472'

#Configure logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Приветик!\nЯ Дори!\nМогу помочь с поиском фильма!")

@dp.message_handler()
async def echo(message: types.Message):
    if message.text == "Да, пожалуйста":
        await message.answer("Выбирайте жанр")


@dp.message_handler(commands=["detective"])
async def send_detective(message: types.Message):
    await message.reply("Достать ножи")
    await bot.send_photo(message.chat.id, photo=dostat_noji)


@dp.message_handler(commands=["comedy"])
async def send_detective(message: types.Message):
    await message.reply("Один дома")
    await bot.send_photo(message.chat.id, photo=odin_doma)


@dp.message_handler(commands=["horror"])
async def send_detective(message: types.Message):
    await message.reply("Оно")
    await bot.send_photo(message.chat.id, photo=ono)


@dp.message_handler(commands=["fiction"])
async def send_detective(message: types.Message):
    await message.reply("Аватар")
    await bot.send_photo(message.chat.id, photo=avatar)


@dp.message_handler(commands=["fantasy"])
async def send_detective(message: types.Message):
    await message.reply("Игра Престолов")
    await bot.send_photo(message.chat.id, photo=igra_prestolov)

