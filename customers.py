"""
    Файл содержит класс Customer для создания клиента
    И методы для работы с таблицей Customers
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

    def set_data_in_class(self, data_list):
        """ Заполняет экземпляр класса данными data_set (список)"""
        self.last_name = data_list[0]
        self.first_name = data_list[1]
        self.middle_name = data_list[2]
        self.phone = data_list[3]
        self.email = data_list[4]
        self.address = data_list[5]
        self.vkontakte = data_list[6]

    def write_in_database(self, id_redact=None):
        """
        Записывает данные в таблицу customers БД. Если id_redact не передан,
        то выполняется sql запрос на добавление, если передан, то на изменение
        данных строки id_redact.
        """
        val = [self.last_name, self.first_name, self.middle_name, self.phone,
               self.email, self.address, self.vkontakte]
        sql = self.sql_new
        if id_redact:
            val.append(id_redact)
            sql = self.sql_update

        func_database.set_in_database(sql, val)

# ======================= Общие методы для табл. customers =====================


# TODO использовать методы универсально для всех таблиц(или многих)
def load_all_from_database():
    """ Получает все записи из таблицы customers в БД """
    sql = """ SELECT * FROM customers """
    return func_database.get_from_database(sql)


def delete_line_database(id_del):
    """ Удаляет запись по id_del из таблицы customers в БД """
    sql = "DELETE FROM customers WHERE id_customer = ?"
    func_database.get_from_database_with_val(sql, (id_del,))


def get_data_id_focus_line(id_focus):
    """ Возвращает данные выделенной строки по id_focus"""
    sql = "SELECT * FROM customers WHERE id_customer = ?"
    return func_database.get_one_line_from_database_with_val(sql, (id_focus,))
