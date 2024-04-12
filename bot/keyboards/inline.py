# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.data.config import db
# from bot.data.config import lang_ru as texts

#Админ меню
def admin_menu(texts):
   keyboard = InlineKeyboardMarkup()
   kb = []
   kb.append(InlineKeyboardButton(texts.admin_menu_1, callback_data="resources"))
   kb.append(InlineKeyboardButton(texts.admin_menu_2, callback_data="newsletter"))
   keyboard.add(kb[0])
   keyboard.add(kb[1])

   return keyboard

def back_to_adm(texts):
   keyboard = InlineKeyboardMarkup()
   kb = []
   kb.append(InlineKeyboardButton(texts.back_adm_m, callback_data="back_to_adm_m"))
   keyboard.add(kb[0])

   return keyboard

def back_to_menu(texts):
   keyboard = InlineKeyboardMarkup()
   kb = []
   kb.append(InlineKeyboardButton(texts.back_adm_m, callback_data="back_to_menu"))
   keyboard.add(kb[0])

   return keyboard

def back_to_profile(texts, id):
   keyboard = InlineKeyboardMarkup()
   kb = []
   kb.append(InlineKeyboardButton(texts.back_adm_m, callback_data=f"group:{id}"))
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
      InlineKeyboardButton("🔙 Главное меню", callback_data="back_to_adm_m")
   ]
   keyboard.add(list_kb[1], list_kb[0])

   return keyboard

async def choose_languages_kb():
    keyboard = InlineKeyboardMarkup(row_width=2)
    langs = await db.get_all_languages()

    for lang in langs:
        keyboard.add(InlineKeyboardButton(lang['name'], callback_data=f"change_language:{lang['language']}"))

    return keyboard
 
def edit_group_inl(id, texts):
   keyboard = InlineKeyboardMarkup()
   kb = []

   kb.append(InlineKeyboardButton(texts.adm_edit_pos1, callback_data=f"edit_price_grp:{id}"))
   kb.append(InlineKeyboardButton(texts.adm_edit_pos2, callback_data=f"edit_name_grp:{id}"))
   kb.append(InlineKeyboardButton(texts.adm_edit_pos3, callback_data=f"edit_cont_grp:{id}"))
   kb.append(InlineKeyboardButton(texts.adm_edit_pos5, callback_data=f"edit_descr_grp:{id}"))
   kb.append(InlineKeyboardButton(texts.adm_edit_pos4, callback_data=f"edit_del_grp:{id}"))

   keyboard.add(kb[1], kb[0])
   keyboard.add(kb[2], kb[3])
   keyboard.add(kb[4])
   keyboard.add(InlineKeyboardButton(texts.back_adm_m, callback_data=f"resources"))

   return keyboard

#Списко групп
async def group_list_buy(texts, page=1):
   keyboard = InlineKeyboardMarkup()
   kb = []
   list = await db.get_all_group(page)
   for btn in list:
      keyboard.add(InlineKeyboardButton(btn['name'], callback_data=f"buy_group:{btn['id']}"))
   if page > 1:
      kb.append(InlineKeyboardButton("◀️ Предыдущая", callback_data=f"prev_page:{page - 1}"))
   if len(list) == 10:
      kb.append(InlineKeyboardButton("▶️ Следующая", callback_data=f"next_page:{page + 1}"))
   keyboard.add(*kb)
   list_kb = [
      InlineKeyboardButton(texts.close, callback_data="close_menu")
   ]
   keyboard.add(list_kb[0])

   return keyboard

def plategi_inl(group_id, texts):
   keyboard = InlineKeyboardMarkup()
   kb = []

   kb.append(InlineKeyboardButton(texts.oplata, callback_data=f"oplata:{group_id}"))

   keyboard.add(kb[0])
   keyboard.add(InlineKeyboardButton(texts.back_adm_m, callback_data=f"back_to_list"))

   return keyboard

def bank_inl(group_id, texts):
   keyboard = InlineKeyboardMarkup()
   kb = []

   kb.append(InlineKeyboardButton("💳 Карта (РФ, УК, КЗ)", callback_data=f"aaio:{group_id}"))
   kb.append(InlineKeyboardButton("📌 ЮMoney", callback_data=f"yoo:{group_id}"))
   kb.append(InlineKeyboardButton("💎 CryptoBot", callback_data=f"Crypto_bot:{group_id}"))

   keyboard.add(kb[0])
   keyboard.add(kb[1])
   keyboard.add(kb[2])
   keyboard.add(InlineKeyboardButton(texts.back_adm_m, callback_data=f"buy_group:{group_id}"))

   return keyboard

def kb_tip_newsletter(texts):
   keyboard = InlineKeyboardMarkup()
   kb = []

   kb.append(InlineKeyboardButton(texts.only_text, callback_data=f"msg:text"))
   kb.append(InlineKeyboardButton(texts.text_photo, callback_data=f"msg:photo"))

   keyboard.add(kb[0], kb[1])
   keyboard.add(InlineKeyboardButton(texts.back_adm_m, callback_data=f"back_to_adm_m"))

   return keyboard

def refill_open_inl(texts, link, invoice_id, group_id):
   keyboard = InlineKeyboardMarkup()
   kb = []

   kb.append(InlineKeyboardButton(texts.refill_link_inl, url=link))
   kb.append(InlineKeyboardButton(texts.refill_check_inl, callback_data=f"check_opl:{invoice_id}:{group_id}"))

   keyboard.add(kb[0])
   keyboard.add(kb[1])

   return keyboard

def refill_open_inl_yoo(texts, link, group_id, pay_id):
   keyboard = InlineKeyboardMarkup()
   kb = []

   kb.append(InlineKeyboardButton(texts.refill_link_inl, url=link))
   kb.append(InlineKeyboardButton(texts.refill_check_inl, callback_data=f"check_yoo_opl:{pay_id}:{group_id}"))

   keyboard.add(kb[0])
   keyboard.add(kb[1])

   return keyboard

def refill_open_inl_aaio(texts, link, group_id, pay_id):
   keyboard = InlineKeyboardMarkup()
   kb = []

   kb.append(InlineKeyboardButton(texts.refill_link_inl, url=link))
   kb.append(InlineKeyboardButton(texts.refill_check_inl, callback_data=f"check_aaio_opl:{pay_id}:{group_id}"))

   keyboard.add(kb[0])
   keyboard.add(kb[1])

   return keyboard