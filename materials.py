"""
    Файл содержит класс
    Material описывающий данные материала
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

        func_database.request_make_with_value(sql, val)
