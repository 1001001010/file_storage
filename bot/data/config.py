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

# aaio
aaio_client = AsyncAaio(apikey='OGFlMjQzNmEtMjgxZi00NmUzLThlNzgtNmJkMTAwMzI4OGM4OkJaMTBOUGFDdyUwbmR5RUlrOVFkKWZKYkhVUSRsNTEx', shopid='919cbf63-a3d7-47ba-98f3-e040e612a3e2', secretkey='23fd87ccb9e933804c22c7c4d3ed8240')