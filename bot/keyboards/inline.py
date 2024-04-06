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

#Списко групп
async def group_list(page=1):
   keyboard = InlineKeyboardMarkup()
   kb = []
   list = await db.get_all_group(page)
   for btn in list:
      keyboard.add(InlineKeyboardButton(btn['name'], callback_data=f"group:{btn['id']}"))
   if page > 1:
      kb.append(InlineKeyboardButton("◀️ Предыдущая", callback_data=f"prev_page:{page - 1}"))
   if len(list) == 10:
      kb.append(InlineKeyboardButton("▶️ Следующая", callback_data=f"next_page:{page + 1}"))
   keyboard.add(*kb)
   list_kb = [
      InlineKeyboardButton("➕ Добавить группу", callback_data=f"add_group"),
      InlineKeyboardButton("🔍 Поиск", callback_data=f"search_group"),
      InlineKeyboardButton("🔙 Главное меню", callback_data="back_to_main_menu")
   ]
   keyboard.add(list_kb[0], list_kb[1])
   keyboard.add(list_kb[2])

   return keyboard