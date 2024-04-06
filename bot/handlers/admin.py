from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp, bot
from bot.data.config import db
from bot.utils.utils_functions import send_admins
from bot.keyboards.inline import admin_menu, back_to_adm
from bot.data.config import lang_ru as texts
from bot.filters.filters import IsAdmin
from bot.state.admin import Newsletter

@dp.message_handler(IsAdmin(), text=texts.admin_button, state="*")
async def func_admin_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer(texts.admin, reply_markup=admin_menu())
    
@dp.callback_query_handler(IsAdmin(), text="newsletter", state="*")
async def func_newsletter(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer(texts.admin_newsletter, reply_markup=back_to_adm())
    await Newsletter.msg.set()
    
@dp.message_handler(state=Newsletter.msg)
async def func_newsletter_text(message: Message, state: FSMContext):
    await state.update_data(msg=message.text)
    data = await state.get_data()
    await send_admins(f"<b>❗ Администратор @{message.from_user.username} запустил рассылку!</b>")
    users = await db.all_users()
    yes_users, no_users = 0, 0
    for user in users:
        user_id = user['id']
        try:
            user_id = user['user_id']
            await bot.send_message(chat_id=user_id, text=data['msg'])
            yes_users += 1
        except:
            no_users += 1

    new_msg = f"""
<b>💎 Всего пользователей: <code>{len(await db.all_users())}</code>
✅ Отправлено: <code>{yes_users}</code>
❌ Не отправлено (Бот заблокирован): <code>{no_users}</code></b>
    """

    await message.answer(new_msg)