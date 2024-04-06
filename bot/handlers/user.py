from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp, bot
from bot.data.config import db
from bot.data.config import lang_ru, lang_en
from bot.utils.utils_functions import get_language
from bot.keyboards.inline import group_list_buy

#Открытие меню
@dp.message_handler(text=lang_ru.user_button, state="*")
@dp.message_handler(text=lang_en.user_button, state="*")
async def func_admin_menu(message: Message, state: FSMContext):
    await state.finish()
    lang = await get_language(message.from_user.id)
    await message.answer(lang.user, reply_markup=await group_list_buy(texts=lang))