import wx
import func_database
import settings

dict_search = settings.dict_tables_database


def search_text(table_name=None, column=None, text_find=None):
    """ Поиск по таблице в БД """
    column = dict_search[table_name]["col_search"][column]
    pk = func_database.get_table_pk(table_name)
    sql = f"""    SELECT ROW_NUMBER() OVER(ORDER BY {pk}) as Row, *
                  FROM (  SELECT *
                          FROM {table_name}
                          WHERE {column} LIKE "%{text_find}%" ) """
    return func_database.request_get_all_rows(sql)


def search_in_component(text_find):
    """ Поиск материала при создании компонента """
    if not text_find == "":
        sql = f"""  SELECT ROW_NUMBER() OVER(ORDER BY id_material) as Row, *
                    FROM (  SELECT *
                            FROM materials
                            WHERE name OR vendor LIKE "%{text_find}%" ) """
        return func_database.request_get_all_rows(sql)
    else:
        wx.MessageBox("Вы не ввели текст поиска.", "Информация", wx.OK)


def validation_search(text_find, column):
    """ Проверка на корректность поля ввода текста и выбора колонки поиска """
    if text_find == "Введите текст поиска":
        wx.MessageBox("Вы не ввели текст поиска.", "Информация", wx.OK)
        return False

    if column == "Выберите колонку":
        wx.MessageBox("Вы не выбрали колонку для поиска", "Информация", wx.OK)
        return False
    return True
