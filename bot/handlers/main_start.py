from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp, bot
from bot.keyboards.reply import user_menu
from bot.data.config import lang_ru as texts

#Обработка команды /start
@dp.message_handler(commands=['start'], state="*")
async def func_main_start(message: Message, state: FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id, texts.welcome, reply_markup=await user_menu(message.from_user.id))