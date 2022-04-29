import sqlite3 as sq
import settings

path_db = settings.path_database


def create_table(sql):
    """ Выполняет SQL запрос для создания таблицы """
    with sq.connect(path_db) as con:
        cur = con.cursor()
        cur.executescript(sql)


def create_table_materials():
    """ Таблица материалов для изделия """
    sql = """
			DROP TABLE IF EXISTS materials;
            CREATE TABLE IF NOT EXISTS materials (
            id_material INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            unit TEXT NOT NULL,
            vendor TEXT)
            """
    create_table(sql)
# TODO таблица изделий
# TODO таблица заказов
# TODO таблица покупок


def create_table_customers():
    """ Таблица клиентов """
    sql = """
			DROP TABLE IF EXISTS customers;
            CREATE TABLE IF NOT EXISTS customers (
            id_customer INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            last_name TEXT NOT NULL,
            first_name TEXT ,
            middle_name TEXT,
            phone INTEGER NOT NULL,
            email TEXT,
            address TEXT,
            vkontakte TEXT)            
        """
    create_table(sql)


def create_database_catalog_hm():
    """ Запускает создание таблиц в базе данных"""
    create_table_materials()
    create_table_customers()


create_database_catalog_hm()
