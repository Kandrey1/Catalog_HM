"""
    Файл содержит класс
    Customer описывающий данные клиента
"""
import func_database


class Customer:
    """ Класс хранит основные данные о клиенте """
    def __init__(self, last_name='', first_name='', middle_name='', phone='',
                 email='', address='', vkontakte=''):

        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone = phone
        self.email = email
        self.address = address
        self.vkontakte = vkontakte

        self.sql_new = """
                  INSERT INTO customers 
                      (id_customer, last_name, first_name, middle_name, phone, 
                       email, address, vkontakte)
                  VALUES ( NULL, ?, ?, ? , ?, ?, ?, ?) """

        self.sql_update = """
                  UPDATE customers SET
                      last_name = ?, first_name = ?, middle_name = ?, phone = ?,
                      email = ?, address = ?, vkontakte = ?
                  WHERE id_customer = ? """

    def write_in_database(self, id_redact=None):
        """ Записывает данные в таблицу customers БД. Если id_redact не передан,
            то выполняется sql запрос на добавление, иначе на изменение
            данных строки id_redact. """
        val = [self.last_name, self.first_name, self.middle_name, self.phone,
               self.email, self.address, self.vkontakte]
        sql = self.sql_new
        if id_redact:
            val.append(id_redact)
            sql = self.sql_update

        func_database.request_make_with_value(sql, val)
