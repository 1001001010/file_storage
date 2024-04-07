from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.data.loader import dp, bot
from bot.data.config import db
from bot.utils.utils_functions import send_admins, is_number, ded
from bot.keyboards.inline import admin_menu, back_to_adm, group_list, edit_group_inl
from bot.data.config import lang_ru, lang_en
from bot.filters.filters import IsAdmin
from bot.state.admin import Newsletter, NewGroup, EditGroup
from bot.utils.utils_functions import get_language
from bot.data import config

#Открытие меню
@dp.message_handler(IsAdmin(), text=lang_ru.admin_button, state="*")
@dp.message_handler(IsAdmin(), text=lang_en.admin_button, state="*")
async def func_admin_menu(message: Message, state: FSMContext):
    await state.finish()
    lang = await get_language(message.from_user.id)
    await message.answer(lang.admin, reply_markup=admin_menu(texts=lang))

@dp.callback_query_handler(IsAdmin(), text="back_to_adm_m", state="*")
async def func_admin_menu(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    lang = await get_language(call.from_user.id)
    await bot.send_message(call.from_user.id, lang.admin, reply_markup=admin_menu(texts=lang))

#Рассылка
@dp.callback_query_handler(IsAdmin(), text="newsletter", state="*")
async def func_newsletter(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    lang = await get_language(call.from_user.id)
    await call.message.answer(lang.admin_newsletter, reply_markup=back_to_adm(texts=lang))
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
    lang = await get_language(call.from_user.id)
    await call.message.answer(lang.admin_list_resources, reply_markup=await group_list())
    await Newsletter.msg.set()

@dp.callback_query_handler(IsAdmin(), text="add_group", state="*")
async def func_new_group(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    lang = await get_language(call.from_user.id)
    await call.message.answer(lang.adm_group_name, reply_markup=back_to_adm(texts=lang))
    await NewGroup.name.set()

@dp.message_handler(state=NewGroup.name)
async def func_group_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    lang = await get_language(message.from_user.id)
    await message.answer(lang.adm_group_price, reply_markup=back_to_adm(texts=lang))
    await NewGroup.price.set()
    
@dp.message_handler(state=NewGroup.price)
async def func_group_name(message: Message, state: FSMContext):
    lang = await get_language(message.from_user.id)
    if is_number(message.text):
        await state.update_data(price=message.text)
        await message.answer(lang.adm_group_content, reply_markup=back_to_adm(texts=lang))
        await NewGroup.content.set()
    else: 
        await message.answer(lang.adm_group_no_price)
        await message.answer(lang.adm_group_price, reply_markup=back_to_adm(texts=lang))
        await NewGroup.price.set()

@dp.message_handler(state=NewGroup.content)
async def func_group_name(message: Message, state: FSMContext):
    await state.update_data(content=message.text)
    data = await state.get_data()
    lang = await get_language(message.from_user.id)
    await db.new_group(name = data['name'], price = data['price'], content=data['content'])
    await message.answer(lang.success_save)
    await state.finish()
    
#Открытие группы 
@dp.callback_query_handler(text_startswith="group", state="*")
async def func_one_group_info(call: CallbackQuery, state: FSMContext):
    await state.finish()
    group_id = call.data.split(":")[1]
    await call.message.delete()
    group_info = await db.get_group(id=group_id)
    lang = await get_language(call.from_user.id)
    await bot.send_message(call.from_user.id, ded(lang.group_msg.format(id=group_info['id'], name=group_info['name'], price=group_info['price'], content=group_info['content'])), reply_markup=edit_group_inl(id=group_id, texts=lang))
    
#Удаление группы
@dp.callback_query_handler(text_startswith="edit_del_grp", state="*")
async def func_one_group_info(call: CallbackQuery, state: FSMContext):
    await state.finish()
    group_id = call.data.split(":")[1]
    lang = await get_language(call.from_user.id)
    await db.del_group(id=group_id) 
    await call.message.delete()
    await bot.send_message(call.from_user.id, lang.success_del, reply_markup=back_to_adm(texts=lang))

#Изменение цены группы
@dp.callback_query_handler(text_startswith="edit_price_grp", state="*")
async def func_one_group_info(call: CallbackQuery, state: FSMContext):
    await state.finish()
    group_id = call.data.split(":")[1]
    lang = await get_language(call.from_user.id)
    await bot.send_message(call.from_user.id, lang.adm_ed_price, reply_markup=back_to_adm(texts=lang))
    await call.message.delete()
    await EditGroup.price.set()
    await state.update_data(id=group_id)
    
@dp.message_handler(state=EditGroup.price)
async def func_newsletter_text(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    lang = await get_language(message.from_user.id)
    if is_number(message.text):
        data = await state.get_data()
        await db.edit_price(id=data['id'], price=data['price'])
        await state.finish()
        await bot.send_message(message.from_user.id, lang.success_save, reply_markup=back_to_adm(texts=lang))
    else: 
        await message.answer(lang.adm_group_no_price)
        await message.answer(lang.adm_ed_price, reply_markup=back_to_adm(texts=lang))
        await EditGroup.price.set()
    
#Изменение название группы
@dp.callback_query_handler(text_startswith="edit_name_grp", state="*")
async def func_one_group_info(call: CallbackQuery, state: FSMContext):
    await state.finish()
    group_id = call.data.split(":")[1]
    lang = await get_language(call.from_user.id)
    await bot.send_message(call.from_user.id, lang.adm_ed_name, reply_markup=back_to_adm(texts=lang))
    await call.message.delete()
    await EditGroup.name.set()
    await state.update_data(id=group_id)
    
@dp.message_handler(state=EditGroup.name)
async def func_newsletter_text(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    lang = await get_language(message.from_user.id)
    await db.edit_price(id=data['id'], name=data['name'])
    await state.finish()
    await bot.send_message(message.from_user.id, lang.success_save, reply_markup=back_to_adm(texts=lang))
    
#Изменение Контента группы
@dp.callback_query_handler(text_startswith="edit_desc_grp", state="*")
async def func_one_group_info(call: CallbackQuery, state: FSMContext):
    await state.finish()
    group_id = call.data.split(":")[1]
    lang = await get_language(call.from_user.id)
    await bot.send_message(call.from_user.id, lang.adm_ed_content, reply_markup=back_to_adm(texts=lang))
    await call.message.delete()
    await EditGroup.content.set()
    await state.update_data(id=group_id)
    
@dp.message_handler(state=EditGroup.content)
async def func_newsletter_text(message: Message, state: FSMContext):
    await state.update_data(content=message.text)
    data = await state.get_data()
    lang = await get_language(message.from_user.id)
    await db.edit_price(id=data['id'], content=data['content'])
    await state.finish()
    await bot.send_message(message.from_user.id, lang.success_save, reply_markup=back_to_adm(texts=lang))