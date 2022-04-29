"""
    Файл содержит класс Material для создания материала
    И методы для работы с таблицей Materials
"""
import func_database


class Material:
    """ Класс хранит основные данные о материале """
    def __init__(self, name='', unit='', vendor=''):

        self.name = name
        self.unit = unit
        self.vendor = vendor

        self.sql_new = """
           INSERT INTO materials (id_material, name, unit, vendor )
           VALUES ( NULL, ?, ?, ? ) """

        self.sql_update = """
                  UPDATE materials SET
                      name = ?, unit = ?, vendor = ?
                  WHERE id_material = ? """

    def set_data_in_class(self, data_list):
        """ Заполняет экземпляр класса данными data_set (список)"""
        self.name = data_list[0]
        self.unit = data_list[1]
        self.vendor = data_list[2]

    def write_in_database(self, id_redact=None):
        """
        Записывает данные в таблицу materials БД. Если id_redact не передан,
        то выполняется sql запрос на добавление, если передан, то на изменение
        данных строки id_redact.
        """
        val = [self.name, self.unit, self.vendor]
        sql = self.sql_new
        if id_redact:
            val.append(id_redact)
            sql = self.sql_update

        func_database.set_in_database(sql, val)

# ======================= Общие методы для табл. materials =====================


# TODO использовать методы универсально для всех таблиц(или многих)
def load_all_from_database():
    """ Получает все записи из таблицы materials в БД """
    sql = """ SELECT * FROM materials """
    return func_database.get_from_database(sql)


def delete_line_database(id_del):
    """ Удаляет запись по id_del из таблицы materials в БД """
    sql = "DELETE FROM materials WHERE id_material = ?"
    func_database.get_from_database_with_val(sql, (id_del,))


def get_data_id_focus_line(id_focus):
    """ Возвращает данные выделенной строки по id_focus"""
    sql = "SELECT * FROM materials WHERE id_material = ?"
    return func_database.get_one_line_from_database_with_val(sql, (id_focus,))
