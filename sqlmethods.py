import sqlite3
async def connect_db():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS person(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT ,
                                    user_id TEXT NOT NULL,
                                    name TEXT NOT NULL,
                                    job TEXT NOT NULL,
                                    place_job TEXT NOT NULL,
                                    participation_format TEXT NOT NULL,
                                    Is_SMI TEXT NOT NULL,
                                    Cuntry TEXT NOT NULL,
                                    subject_RF TEXT NOT NULL,
                                    Town TEXT NOT NULL,
                                    Email TEXT NOT NULL,
                                    accept TEXT NOT NULL,
                                    joining_date datetime);'''

        cursor = sqlite_connection.cursor()
        await cursor.execute(sqlite_create_table_query)
        await sqlite_connection.commit()
    except sqlite3.Error as error:
        return f"Ошибка при подключении к sqlite {error}"
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            return "Соединение с SQLite закрыто"
        else:
            return "Соединение с SQLite не закрыто"

async def InTable(user_id, email):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        sqlite_create_table_query = f'''SELECT user_id, Email FROM person WHERE user_id = ? AND Email = ?'''

        cursor =  sqlite_connection.cursor()
        is_in_tablee =  cursor.execute(sqlite_create_table_query, (str(user_id), str(email))).fetchall()
        sqlite_connection.close()
        return is_in_tablee
    except sqlite3.Error as error:
        return f"Ошибка при подключении к sqlite {error}2"

async def insert_to(DATA):
    try:
        Data = list(map(lambda item: str(DATA[item]), DATA))
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        sqlite_insert_query = f"""INSERT INTO person
                            (name, job, place_job, participation_format, Is_SMI, Cuntry, subject_RF, Town, Email, accept, user_id)
                            VALUES(? ,? ,? ,? ,? ,? ,? ,? ,? ,? , ?);"""
       # sqlite_insert_query2 = f"INSERT INTO person (user_id) VALUES(\'dsgggsd\')"
        cursor.execute(sqlite_insert_query, Data)
       #cursor.execute(sqlite_insert_query2)
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        return f"Ошибка при подключении к sqlite {error}1"
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            return "Соединение с SQLite закрыто"
        else:
            return "Соединение с SQLite не закрыто"


    