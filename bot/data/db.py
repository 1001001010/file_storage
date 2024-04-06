import aiosqlite
from async_class import AsyncClass

path_db = 'bot/data/database.db'

#Преобразование результата в словарь
def dict_factory(cursor, row):
    save_dict = {}

    for idx, col in enumerate(cursor.description):
        save_dict[col[0]] = row[idx]

    return save_dict

# Форматирование запроса без аргументов
def query(sql, parameters: dict):
    if "XXX" not in sql: sql += " XXX "
    values = ", ".join([
        f"{item} = ?" for item in parameters
    ])
    sql = sql.replace("XXX", values)

    return sql, list(parameters.values())


# Форматирование запроса с аргументами
def query_args(sql, parameters: dict):
    sql = f"{sql} WHERE "

    sql += " AND ".join([
        f"{item} = ?" for item in parameters
    ])

    return sql, list(parameters.values())

#Проверка и создание бд
class DB(AsyncClass):
    async def __ainit__(self):
        self.con = await aiosqlite.connect(path_db)
        self.con.row_factory = dict_factory

    # Получение всех пользователей из БД
    async def all_users(self):
        row = await self.con.execute("SELECT * FROM users")
        return await row.fetchall()

    # Получение пользователя из БД
    async def get_user(self, **kwargs):
        queryy = "SELECT * FROM users"
        queryy, params = query_args(queryy, kwargs)
        row = await self.con.execute(queryy, params)
        return await row.fetchone()

    # Регистрация пользователя в БД
    async def register_user(self, user_id, user_name, first_name):
        await self.con.execute("INSERT INTO users("
                                "user_id, user_name, first_name, balance)"
                                "VALUES (?,?,?,?)",
                                [user_id, user_name, first_name, 0])
        await self.con.commit()

    # Редактирование пользователя
    async def update_user(self, id, **kwargs):
        queryy = f"UPDATE users SET"
        queryy, params = query(queryy, kwargs)
        params.append(id)
        await self.con.execute(queryy + "WHERE user_id = ?", params)
        await self.con.commit()
        
    #Список всех груп
    async def get_all_group(self, page):
        offset = (page - 1) * 10
        row = await self.con.execute("SELECT * FROM groups LIMIT 10 OFFSET ?", (offset,))
        return await row.fetchall()

    #Проверка на существование бд и ее создание
    async def create_db(self):
        users_info = await self.con.execute("PRAGMA table_info(users)")
        if len(await users_info.fetchall()) == 5:
            print("database was found (Users | 1/2)")
        else:
            await self.con.execute("CREATE TABLE users ("
                                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                   "user_id INTEGER,"
                                   "user_name TEXT,"
                                   "first_name TEXT,"
                                   "balance INTEGER)")
            print("database was not found (Users | 1/2), creating...")
            await self.con.commit()
        
        groups_info = await self.con.execute("PRAGMA table_info(groups)")
        if len(await groups_info.fetchall()) == 4:
            print("database was found (Groups | 2/2)")
        else:
            await self.con.execute("CREATE TABLE groups ("
                                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                   "name TEXT,"
                                   "price INTEGER,"
                                   "content TEXT)")
            print("database was not found (Groups | 2/2), creating...")
            
            await self.con.commit()