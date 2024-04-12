# - *- coding: utf- 8 - *-
import configparser
import asyncio
from datetime import datetime, timedelta
from bot.data.lang import ru
from AsyncPayments.cryptoBot import AsyncCryptoBot
from AsyncPayments.aaio import AsyncAaio

from bot.data.db import DB
from bot.data.lang import en

# Создание экземпляра бд 
async def main_db():
    db = await DB()

    return db

lang_ru = ru.Texts()
lang_en = en.Texts()

loop = asyncio.get_event_loop()
task = loop.create_task(main_db())
db = loop.run_until_complete(task)

# Чтение конфига
read_config = configparser.ConfigParser()
read_config.read("settings.ini")

bot_token = read_config['settings']['token'].strip().replace(" ", "")  # Токен бота
path_database = "tgbot/data/database.db"  # Путь к Базе Данных

# CryptoBot
cryptoBot = AsyncCryptoBot(read_config['settings']['crypto_bot_token'].strip().replace(" ", ""))

# Aaio
aaio_api_key = read_config['settings']['aaio_api_key'].strip().replace(" ", "") # api ключ
aaio_id_shop = read_config['settings']['aaio_id_shop'].strip().replace(" ", "") # id магазина
aaio_secret_key_1 = read_config['settings']['aaio_secret_key'].strip().replace(" ", "") # первый секретный ключ
aaio_client = AsyncAaio(apikey=aaio_api_key, shopid=aaio_id_shop, secretkey=aaio_secret_key_1)

# ЮMoney
yoomoney_token = read_config['settings']['yoomoney_token'].strip().replace(" ", "") # юмани токен
yoomoney_number = read_config['settings']['yoomoney_number'].strip().replace(" ", "") # юмани номер