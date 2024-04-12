from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp, bot
from bot.data.config import db, cryptoBot, aaio_client
from bot.data.config import lang_ru, lang_en
from bot.utils.utils_functions import get_language
from bot.keyboards.inline import group_list_buy, plategi_inl, refill_open_inl, bank_inl, refill_open_inl_aaio
from bot.utils.utils_functions import ded, get_unix
from bot.data import config
from AsyncPayments.cryptoBot import AsyncCryptoBot
from bot.utils.utils_functions import send_admins, format_rate
from datetime import datetime, timedelta
import ast
from bot.utils.aaio import Aaio

try:
    aaio = Aaio(
        aaio_api_key=config.aaio_api_key,
        aaio_id_shop=config.aaio_id_shop,
        aaio_secret_key=config.aaio_secret_key_1
    )
except:
    pass

#Открытие меню
@dp.message_handler(text=lang_ru.user_button, state="*")
@dp.message_handler(text=lang_en.user_button, state="*")
async def func_admin_menu(message: Message, state: FSMContext):
    await state.finish()
    lang = await get_language(message.from_user.id)
    await message.answer(lang.user, reply_markup=await group_list_buy(texts=lang))
    
@dp.callback_query_handler(text="back_to_list", state="*")
async def func_buy_group(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    lang = await get_language(call.from_user.id)
    await bot.send_message(call.from_user.id, lang.user, reply_markup=await group_list_buy(texts=lang))
    
@dp.callback_query_handler(text="close_menu", state="*")
async def func_buy_group(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    lang = await get_language(call.from_user.id)
    await bot.send_message(call.from_user.id, "Отменено")

@dp.callback_query_handler(text_startswith="buy_group", state="*")
async def func_buy_group(call: CallbackQuery, state: FSMContext):
    await state.finish()
    group_id = call.data.split(":")[1]
    await call.message.delete()
    lang = await get_language(call.from_user.id)
    group_info = await db.get_group(id=group_id)
    await bot.send_message(call.from_user.id, ded(lang.buy_text.format(name=group_info['name'], price=format_rate(group_info['price']), descr=group_info['descr'])), reply_markup=plategi_inl(group_id=group_info['id'], texts=lang))
    
@dp.callback_query_handler(text_startswith="Crypto_bot", state="*")
async def func_vibor_plat(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    lang = await get_language(call.from_user.id)
    group_id = call.data.split(":")[1]
    group_info = await db.get_group(id=group_id)
    cheack = await cryptoBot.create_invoice(amount=group_info['price'], currency_type="fiat", fiat="RUB", description=group_info['name'])
    pay_url = cheack.pay_url
    amount = cheack.amount
    fiat = cheack.fiat
    invoice_id = cheack.invoice_id
    await bot.send_message(call.from_user.id, lang.refill_gen_text(way="CryptoBot", amount=amount, curr=fiat), reply_markup=refill_open_inl(texts=lang, link=pay_url, invoice_id=invoice_id, group_id=group_id))
    
@dp.callback_query_handler(text_startswith="check_opl", state="*")
async def func_check_opl(call: CallbackQuery, state: FSMContext):
    await state.finish()
    lang = await get_language(call.from_user.id)
    amount = call.data.split(":")[1]
    group_id = call.data.split(":")[2]
    cheack = await cryptoBot.get_invoices(invoice_ids=amount)
    if cheack[0].status == 'active':
        await call.answer(lang.ne_oplat)
    elif cheack[0].status == 'paid':
    # if cheack[0].status == 'active':
        group_info = await db.get_group(id=group_id)
        arr = ast.literal_eval(group_info['content'])
        msg = """"""
        for i in arr:
            chat_id = i
            expire_date = datetime.now() + timedelta(days=1)
            link = await bot.create_chat_invite_link(chat_id, expire_date.timestamp, 1)
            msg += f"{link.invite_link}\n"
        await bot.send_message(call.from_user.id, lang.tovar(name=group_info['name'], desc=msg))
        name = call.from_user.username
        if call.from_user.username == "":
            us = await bot.get_chat(call.from_user.id)
            name = us.get_mention(as_html=True)
        await send_admins(f"💎 Пользователь @{name} приобрел товар {group_info['name']}")
        await call.message.delete()
    else:
        await call.answer(lang.ne_oplat)
        
@dp.callback_query_handler(text_startswith="oplata", state="*")
async def func_buy_group(call: CallbackQuery, state: FSMContext):
    await state.finish()
    group_id = call.data.split(":")[1]
    await call.message.delete()
    lang = await get_language(call.from_user.id)
    group_info = await db.get_group(id=group_id)
    await bot.send_message(call.from_user.id, lang.choose_bank, reply_markup=bank_inl(group_id=group_info['id'], texts=lang))
    
#aaio
@dp.callback_query_handler(text_startswith="aaio", state="*")
async def func_vibor_plat(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    group_id = call.data.split(":")[1]
    group_info = await db.get_group(id=group_id)
    lang = await get_language(call.from_user.id)
    unic = get_unix()
    print(unic)
    payment = await aaio_client.create_payment_url(amount=group_info['price'], order_id=unic, desc=group_info['name'])
    await bot.send_message(call.from_user.id, lang.refill_gen_text(way="aaio", amount=group_info['price'], curr='RUB'), reply_markup=refill_open_inl_aaio(texts=lang, link=payment, group_id=group_id, pay_id=unic))
    
@dp.callback_query_handler(text_startswith="check_aaio_opl", state="*")
async def func_check_opl(call: CallbackQuery, state: FSMContext):
    await state.finish()
    lang = await get_language(call.from_user.id)
    unic_id = call.data.split(":")[1]
    tovar_id = call.data.split(":")[2]
    status = await aaio.check_payment(order_id=unic_id)
    print(status)
    # if order_info.status == 'success':
    #     print("Payment is successful.")
    # elif order_info.status == 'pending':
    #     print("Payment is pending.")
    # else:
    #     print("Payment is unsuccessful.")