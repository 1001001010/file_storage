# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.data.config import db
from bot.data.config import lang_ru as texts

#Админ меню
def admin_menu():
   keyboard = InlineKeyboardMarkup()
   kb = []
   kb.append(InlineKeyboardButton(texts.admin_menu_1, callback_data="resources"))
   kb.append(InlineKeyboardButton(texts.admin_menu_2, callback_data="newsletter"))
   keyboard.add(kb[0])
   keyboard.add(kb[1])

   return keyboard

def back_to_adm():
   keyboard = InlineKeyboardMarkup()
   kb = []
   kb.append(InlineKeyboardButton(texts.back_adm_m, callback_data="back_to_adm_m"))
   keyboard.add(kb[0])

   return keyboard