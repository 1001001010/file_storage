from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp
# from bot.keyboards.reply import user_menu
from bot.keyboards.inline import admin_menu, back_to_adm
from bot.data.config import lang_ru as texts
from bot.filters.filters import IsAdmin

@dp.message_handler(IsAdmin(), text=texts.admin_button, state="*")
async def func_admin_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer(texts.admin, reply_markup=admin_menu())
    
@dp.callback_query_handler(IsAdmin(), text="newsletter", state="*")
async def func_newsletter(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer(texts.admin_newsletter, reply_markup=back_to_adm())