"""
    Файл содержит класс Product для создания клиента
    И методы для работы с таблицей Products
"""
import func_database


class Product:
    """ Класс хранит основные данные об изделии """
    def __init__(self, path_ico='', type_prod='', model='', price='', number='',
                 about='', size_width='', size_height='', size_depth='',
                 weigh=''):

        self.path_ico = path_ico
        self.type_prod = type_prod
        self.model = model
        self.price = price
        self.number = number
        self.about = about
        self.size_width = size_width
        self.size_height = size_height
        self.size_depth = size_depth
        self.weigh = weigh

        self.sql_new = """
           INSERT INTO products 
              (id_product, path_ico, type_prod, model, price, number, about,
               size_width, size_height, size_depth, weigh )
           VALUES ( NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """

        self.sql_update = """
                  UPDATE products SET
                      path_ico = ?, type_prod = ?, model = ?, price = ?, 
                      number = ?, about = ?, size_width = ?, size_height = ?, 
                       size_depth = ?, weigh = ?
                  WHERE id_product = ? """

    def write_in_database(self, id_redact=None):
        """
        Записывает данные в таблицу products БД. Если id_redact не передан,
        то выполняется sql запрос на добавление, если передан, то на изменение
        данных строки id_redact.
        """
        val = [self.path_ico, self.type_prod, self.model, self.price,
               self.number, self.about, self.size_width, self.size_height,
               self.size_depth, self.weigh]
        sql = self.sql_new
        if id_redact:
            val.append(id_redact)
            sql = self.sql_update

        func_database.request_make_with_value(sql, val)
