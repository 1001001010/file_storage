from aiogram.dispatcher.filters.state import State, StatesGroup


class Newsletter(StatesGroup): #State на добавление новой книги
    message = State()