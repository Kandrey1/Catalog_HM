import sqlite3 as sq
import settings

path_db = settings.path_database
dict_tables = settings.dict_tables_database


def request_get_all_rows(sql):
    """ Извлекает все строки из таблицы БД """
    with sq.connect(path_db) as con:
        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
    return rows


# def request_get_rows_with_value(sql, val):
#     """ Извлекает несколько строк из БД с условием (для модуля поиска) """
#     with sq.connect(path_db) as con:
#         cur = con.cursor()
#         cur.execute(sql, val)
#         rows = cur.fetchall()
#     return rows


def request_get_one_row_with_value(sql, val):
    """ Извлекает одну запись из БД с условием """
    with sq.connect(path_db) as con:
        cur = con.cursor()
        cur.execute(sql, val)
        row = cur.fetchone()
    return row


def request_make_with_value(sql, val):
    """ Исполняет запрос в БДс условием """
    with sq.connect(path_db) as con:
        cur = con.cursor()
        cur.execute(sql, val)


# ----------------------- Общие методы -----------------------------------------
def get_table_name(name_db):
    """ Возвращает название таблицы в БД """
    return dict_tables[name_db]["table"]


def get_table_pk(name_db):
    """ Возвращает имя primary key в БД """
    return dict_tables[name_db]["pk"]


def get_table_columns(name_db):
    """ Возвращает строку с названием колонок(кроме primary key) в БД """
    return dict_tables[name_db]["columns"]


def get_all_rows(name_db):
    """ Возвращает все строки из таблицы в БД """
    sql = f" SELECT * FROM {get_table_name(name_db)} "
    return request_get_all_rows(sql)


def get_numeric_all_rows(name_db):
    """ Возвращает пронумерованные строки из таблицы в БД """
    sql = f""" SELECT * 
               FROM ( SELECT ROW_NUMBER() 
                            OVER(ORDER BY {get_table_pk(name_db)}) as Row, *
                      FROM {get_table_name(name_db)}) """
    return request_get_all_rows(sql)


def get_data_id_focus_line(name_db, id_focus):
    """ Возвращает данные выделенной(одной) строки по id_focus """
    sql = f""" SELECT * FROM {get_table_name(name_db)}
               WHERE {get_table_pk(name_db)} = ? """
    return request_get_one_row_with_value(sql, (id_focus,))


def get_id_last_row_in_table(name_db):
    """ Возвращает id последней записи в таблице """
    sql = f""" SELECT MAX({get_table_pk(name_db)})
               FROM {get_table_name(name_db)} """
    row = request_get_all_rows(sql)
    return row[0][0]


def copy_row_in_table(name_db, id_copy):
    """ Копирует строку по id_copy из таблицы БД в конец этой же таблицы """
    sql = f""" INSERT INTO {get_table_name(name_db)} 
                            ({get_table_columns(name_db)})
              SELECT {get_table_columns(name_db)}
              FROM {get_table_name(name_db)} 
              WHERE {get_table_pk(name_db)} = ? """
    request_get_one_row_with_value(sql, (id_copy,))


def delete_row_in_table(name_db, id_del):
    """ Удаляет запись по id_del из таблицы в БД """
    sql = f""" DELETE FROM {get_table_name(name_db)} 
               WHERE {get_table_pk(name_db)} = ? """
    request_make_with_value(sql, (id_del,))


def update_path_miniature_product(path, id_product):
    """ Обновляет путь миниатюры изделия """
    val = [path, id_product]
    sql = """ UPDATE products SET path_ico = ?
              WHERE id_product = ? """
    request_make_with_value(sql, val)
