from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp, bot
from bot.data.config import db
from bot.services.crypto_bot import CryptoBot
from bot.data.config import lang_ru, lang_en
from bot.utils.utils_functions import get_language
from bot.keyboards.inline import group_list_buy, edit_group_inl
from bot.utils.utils_functions import ded
from bot.data import config

try:
    crypto = CryptoBot(api_token=config.crypto_bot_token)
except:
    pass

#Открытие меню
@dp.message_handler(text=lang_ru.user_button, state="*")
@dp.message_handler(text=lang_en.user_button, state="*")
async def func_admin_menu(message: Message, state: FSMContext):
    await state.finish()
    lang = await get_language(message.from_user.id)
    await message.answer(lang.user, reply_markup=await group_list_buy(texts=lang))
    
@dp.callback_query_handler(text_startswith="buy_group", state="*")
async def func_one_group_info(call: CallbackQuery, state: FSMContext):
    await state.finish()
    group_id = call.data.split(":")[1]
    await call.message.delete()
    lang = await get_language(call.from_user.id)
    group_info = await db.get_group(id=group_id)
    await bot.send_message(call.from_user.id, ded(lang.buy_text.format(name=group_info['name'], price=group_info['price'])), reply_markup=edit_group_inl(group_id=group_info['id'], texts=lang))
    
@dp.callback_query_handler(text_startswith="Crypto_bot", state="*")
async def func_one_group_info(call: CallbackQuery, state: FSMContext):
    group_id = call.data.split(":")[1]
    await call.message.delete()
    group_info = await db.get_group(id=group_id)
    way = "CryptoBot"
    bill = await crypto.create_bill(amount=group_info['price'], asset=group_info['id'])
    id = bill['result']['invoice_id']
    link = bill['result']['pay_url']
    lang = await get_language(call.from_user.id)
    await call.answer(call.refill_gen_text(way=way, amount=group_info['price'], id=id,
                                                       curr=config.currencies[curr]['sign']),
                                 reply_markup=refill_open_inl(texts=texts,
                                                              way=way,
                                                              amount=group_info['price'],
                                                              link=link, id=id, second_amount=call.text))
    await state.finish()