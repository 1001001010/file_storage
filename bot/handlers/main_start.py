from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.config import db
from bot.data.loader import dp, bot
from bot.keyboards.reply import user_menu
from bot.keyboards.inline import choose_languages_kb
from bot.data.config import db, lang_ru, lang_en
from bot.utils.utils_functions import get_language

#Обработка команды /start
@dp.message_handler(commands=['start'], state="*")
async def func_main_start(message: Message, state: FSMContext):
    await state.finish()
    lang = await get_language(message.from_user.id)
    await bot.send_message(message.from_user.id, lang.welcome, reply_markup=await user_menu(message.from_user.id, texts=lang))
    
# Переключение языка
@dp.callback_query_handler(text='change_language', state="*")
async def change_language(call: CallbackQuery, state: FSMContext):
    await state.finish()
    lang = await get_language(call.from_user.id)
    await call.message.delete()
    await call.message.answer(lang.choose_language, reply_markup=await choose_languages_kb(texts=lang))

@dp.callback_query_handler(text_startswith="change_language:", state="*")
async def change_language_(call: CallbackQuery, state: FSMContext):
    await state.finish()
    lang_short_name = call.data.split(":")[1]
    await db.update_user(id=call.from_user.id, language=lang_short_name)
    await call.message.delete()
    
# Переключение языка
@dp.callback_query_handler(text='back_to_m', state="*")
async def change_language(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    lang = await get_language(call.from_user.id)
    await bot.send_message(call.from_user.id, lang.welcome, reply_markup=await user_menu(call.from_user.id, texts=lang))