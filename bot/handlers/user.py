from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp, bot
from bot.data.config import db, cryptoBot
from bot.data.config import lang_ru, lang_en
from bot.utils.utils_functions import get_language
from bot.keyboards.inline import group_list_buy, plategi_inl, choose_asset_crypto, refill_open_inl
from bot.utils.utils_functions import ded
from bot.data import config
from AsyncPayments.cryptoBot import AsyncCryptoBot
from bot.utils.utils_functions import send_admins

#Открытие меню
@dp.message_handler(text=lang_ru.user_button, state="*")
@dp.message_handler(text=lang_en.user_button, state="*")
async def func_admin_menu(message: Message, state: FSMContext):
    await state.finish()
    lang = await get_language(message.from_user.id)
    await message.answer(lang.user, reply_markup=await group_list_buy(texts=lang))
    
@dp.callback_query_handler(text_startswith="buy_group", state="*")
async def func_buy_group(call: CallbackQuery, state: FSMContext):
    await state.finish()
    group_id = call.data.split(":")[1]
    await call.message.delete()
    lang = await get_language(call.from_user.id)
    group_info = await db.get_group(id=group_id)
    await bot.send_message(call.from_user.id, ded(lang.buy_text.format(name=group_info['name'], price=group_info['price'])), reply_markup=plategi_inl(group_id=group_info['id'], texts=lang))
    
@dp.callback_query_handler(text_startswith="Crypto_bot", state="*")
async def func_one_group_info(call: CallbackQuery, state: FSMContext):
    await state.finish()
    group_id = call.data.split(":")[1]
    await bot.send_message(call.from_user.id, "Выберите валюту", reply_markup=choose_asset_crypto(pos_id=group_id))
    
@dp.callback_query_handler(text_startswith="refill", state="*")
async def func_one_group_info(call: CallbackQuery, state: FSMContext):
    await state.finish()
    lang = await get_language(call.from_user.id)
    group_id = call.data.split(":")[3]
    group_info = await db.get_group(id=group_id)
    cheack = await cryptoBot.create_invoice(amount=group_info['price'], currency_type="fiat", fiat="RUB", description=group_info['name'])
    pay_url = cheack.pay_url
    amount = cheack.amount
    fiat = cheack.fiat
    invoice_id = cheack.invoice_id
    await bot.send_message(call.from_user.id, lang.refill_gen_text(way="Crypto Bot", amount=amount, curr=fiat), reply_markup=refill_open_inl(texts=lang, link=pay_url, invoice_id=invoice_id, group_id=group_id))
    
@dp.callback_query_handler(text_startswith="check_opl", state="*")
async def func_one_group_info(call: CallbackQuery, state: FSMContext):
    await state.finish()
    lang = await get_language(call.from_user.id)
    amount = call.data.split(":")[1]
    group_id = call.data.split(":")[2]
    cheack = await cryptoBot.get_invoices(invoice_ids=amount)
    if cheack[0].status == 'active':
        await call.answer(lang.ne_oplat)
    elif cheack[0].status == 'paid':
        group_info = await db.get_group(id=group_id)
        await bot.send_message(call.from_user.id, lang.tovar(name=group_info['name'], desc=group_info['content']))
        name = call.from_user.username
        if call.from_user.username == "":
            us = await bot.get_chat(call.from_user.id)
            name = us.get_mention(as_html=True)
        await send_admins(f"💎 Пользователь @{name} приобрел {group_info['name']}")
    else:
        await call.answer(lang.ne_oplat)