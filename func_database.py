import sqlite3 as sq
import settings

path_db = settings.path_database


def get_from_database(sql):
    """ Извлекает данные из БД.
        Функция принимает SQL запрос, возвращает данных списком """
    with sq.connect(path_db) as con:
        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
    return rows


def get_from_database_with_val(sql, val):
    """ Извлекает несколько записей из БД с "условием".
        Функция принимает SQL запрос и кортеж val, возвращает данных списком """
    with sq.connect(path_db) as con:
        cur = con.cursor()
        cur.execute(sql, val)
        rows = cur.fetchall()
    return rows


def get_one_line_from_database_with_val(sql, val):
    """ Извлекает одну запись из БД с "условием".
        Функция принимает SQL запрос и кортеж val, возвращает строку """
    with sq.connect(path_db) as con:
        cur = con.cursor()
        cur.execute(sql, val)
        row = cur.fetchone()
    return row


def set_in_database(sql, val):
    """ Записывает данные в БД.
        Функция принимает SQL запрос и кортеж val содержащий переменные """
    with sq.connect(path_db) as con:
        cur = con.cursor()
        cur.execute(sql, val)
