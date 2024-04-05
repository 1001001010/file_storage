# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup

from bot.utils.utils_functions import get_admins
from bot.data.config import lang_ru as texts

#Главное меню
async def user_menu(user_id):
    main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    main_menu.row(texts.user_button)
    if user_id in get_admins():
        main_menu.row(texts.admin_button)
    return main_menu