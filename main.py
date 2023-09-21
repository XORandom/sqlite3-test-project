import sqlite3

# try:
#     sqlite_connection = sqlite3.connect('sqlite_example.db')  # Подключение к БД
#     cursor = sqlite_connection.cursor()  # Создаем курсор, который отвечает за выполнение запроса
#     print('База создана, база подключена к sqlite')
#     sqlite_select_query = 'select sqlite_version();'
#     cursor.execute(sqlite_select_query) # Выполнение запроса
#     result = cursor.fetchall()
#     print('Версия БД Sqlite:', result)
#     cursor.close()
# except sqlite3.Error as e:
#     print('Ошибка подключения к sqlite', e)
# finally:
#     if sqlite_connection:
#         sqlite_connection.close()
#         print('Подключение закрыто')

try:
    sqlite_connection = sqlite3.connect('sqlite_example.db')  # Подключение к БД
    sqlite_create_table_query = '''
    CREATE TABLE programmers(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        start_date  DATETIME,
        salary REAL NOT NULL);    
    '''
    cursor = sqlite_connection.cursor()  # Создаем курсор, который отвечает за выполнение запроса
    cursor.execute(sqlite_create_table_query) # Выполнение запроса
    sqlite_connection.commit()
    print('Таблица programmers создана:')
    cursor.close()
except sqlite3.Error as e:
    print('Ошибка подключения к sqlite', e)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print('Подключение закрыто')