"""
    Файл содержит класс
    Component описывающий компонент изделия
"""
import func_database


class Component:
    """ Класс хранит основные данные о компоненте в изделии """
    def __init__(self, product_id='', material_id='', number='', price_one=''):

        self.product_id = product_id
        self.material_id = material_id
        self.number = number
        self.price_one = price_one

        self.sql_new = """
                  INSERT INTO components 
                      (id_component, product_id, material_id, number, price_one)
                  VALUES ( NULL, ?, ?, ?, ?) """

        self.sql_update = """
                  UPDATE components SET
                      product_id = ?, material_id = ?, number = ?, price_one = ?
                  WHERE id_component = ? """

    def write_in_database(self, id_redact=None):
        """ Записывает данные в таблицу components БД. Если id_redact не передан,
            то выполняется sql запрос на добавление, иначе на изменение
            данных строки id_redact. """
        val = [self.product_id, self.material_id, self.number, self.price_one]
        sql = self.sql_new
        if id_redact:
            val.append(id_redact)
            sql = self.sql_update

        func_database.request_make_with_value(sql, val)

    @staticmethod
    def get_data_redact_component(id_redact):
        """ Возвращает данные компонента по id_redact """
        sql = f"""
            SELECT components.id_component, materials.id_material,
                   materials.name, components.number, materials.unit,
                   components.price_one, materials.vendor
            FROM components
                JOIN materials
                    ON  components.material_id = materials.id_material
            WHERE id_component = ? """
        return func_database.request_get_one_row_with_value(sql, (id_redact,))

    @staticmethod
    def get_number_line(id_mat):
        """ Возвращает номер строки материала id_mat """
        sql = f"""
            SELECT Row
            FROM ( SELECT ROW_NUMBER() 
                                OVER(ORDER BY id_material) as Row, id_material
                   FROM materials)
            WHERE id_material = {id_mat} """
        return func_database.request_get_all_rows(sql)[0][0]

    @staticmethod
    def get_all_components_product(id_product):
        """ Возвращает все компоненты изделия из таблицы в БД """
        sql = f""" 
            SELECT * 
            FROM ( SELECT ROW_NUMBER() OVER(ORDER BY id_component) as Row, *
                   FROM ( SELECT components.id_component, materials.id_material,
                                 materials.name, components.number, materials.unit,
                                 components.price_one, materials.vendor
                          FROM components
                                JOIN materials
                                    ON  components.material_id = materials.id_material
                          WHERE product_id = {id_product})
                          ) """
        return func_database.request_get_all_rows(sql)

    @staticmethod
    def get_temp_components():
        """ Возвращает все компоненты где product_id is NULL (временные
            компоненты изделия) """
        sql = f""" 
            SELECT * 
            FROM ( SELECT ROW_NUMBER() OVER(ORDER BY id_component) as Row, *
                   FROM ( SELECT components.id_component, materials.id_material,
                                 materials.name, components.number, materials.unit,
                                 components.price_one, materials.vendor
                          FROM components
                                JOIN materials
                                    ON  components.material_id = materials.id_material
                          WHERE product_id is NULL ) 
                  ) """
        return func_database.request_get_all_rows(sql)

    @staticmethod
    def get_id_temp_components():
        """ Возвращает список временных компонентов """
        sql = f"""  SELECT id_component
                    FROM components
                        JOIN materials
                            ON  components.material_id = materials.id_material
                    WHERE product_id is NULL """
        list_tuples = func_database.request_get_all_rows(sql)
        list_id = []
        for t in list_tuples:
            list_id.append(t[0])
        return list_id

    @staticmethod
    def set_product_id_in_component(id_component, product_id):
        """ Обновляет поле product_id в компоненте """
        val = [product_id, id_component]
        sql = """ UPDATE components SET product_id = ?
                  WHERE id_component = ? """
        func_database.request_make_with_value(sql, val)
