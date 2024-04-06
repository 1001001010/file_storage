from aiogram.dispatcher.filters.state import State, StatesGroup


class Newsletter(StatesGroup): #State на рассылку
    msg = State()
    
class NewGroup(StatesGroup): #State на добавление новой группы
    name = State()
    price = State()
    content = State()
    
class EditGroup(StatesGroup): #State на добавление новой группы
    id = State()
    name = State()
    price = State()
    content = State()