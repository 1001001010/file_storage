from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp, bot
from bot.data.config import db
from bot.utils.utils_functions import send_admins, is_number, ded
from bot.keyboards.inline import admin_menu, back_to_adm, group_list
from bot.data.config import lang_ru as texts
from bot.filters.filters import IsAdmin
from bot.state.admin import Newsletter, NewGroup

#Открытие меню
@dp.message_handler(IsAdmin(), text=texts.admin_button, state="*")
async def func_admin_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer(texts.admin, reply_markup=admin_menu())

@dp.callback_query_handler(IsAdmin(), text="back_to_adm_m", state="*")
async def func_admin_menu(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await bot.send_message(call.from_user.id, texts.admin, reply_markup=admin_menu())

#Рассылка
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
    
#Работа с группами
@dp.callback_query_handler(IsAdmin(), text="resources", state="*")
async def func_group(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer(texts.admin_list_resources, reply_markup=await group_list())
    await Newsletter.msg.set()

@dp.callback_query_handler(IsAdmin(), text="add_group", state="*")
async def func_new_group(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer(texts.adm_group_name, reply_markup=back_to_adm())
    await NewGroup.name.set()

@dp.message_handler(state=NewGroup.name)
async def func_group_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(texts.adm_group_price, reply_markup=back_to_adm())
    await NewGroup.price.set()
    
@dp.message_handler(state=NewGroup.price)
async def func_group_name(message: Message, state: FSMContext):
    if is_number(message.text):
        await state.update_data(price=message.text)
        await message.answer(texts.adm_group_content, reply_markup=back_to_adm())
        await NewGroup.content.set()
    else: 
        await message.answer(texts.adm_group_no_price)
        await message.answer(texts.adm_group_price, reply_markup=back_to_adm())
        await NewGroup.price.set()

@dp.message_handler(state=NewGroup.content)
async def func_group_name(message: Message, state: FSMContext):
    await state.update_data(content=message.text)
    data = await state.get_data()
    await db.new_group(name = data['name'], price = data['price'], content=data['content'])
    await message.answer(texts.success_save)
    await state.finish()
    
#Открытие группы 
@dp.callback_query_handler(text_startswith="group", state="*")
async def func_one_group_info(call: CallbackQuery, state: FSMContext):
    await state.finish()
    group_id = call.data.split(":")[1]
    group_info = await db.get_group(id=group_id)
    await bot.send_message(call.from_user.id, ded(texts.group_msg.format(id=group_info['id'], name=group_info['name'], price=group_info['price'], content=group_info['content'])))
    