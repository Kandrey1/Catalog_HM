import func_program
import window_messages
from base_frame_database import BaseDialogDatabase
from product_add import DialogAddProduct


class DialogAllProducts(BaseDialogDatabase):
    """ Класс создает модальное окно с данными всех изделий в БД """
    def __init__(self, parent, title="База данных изделий"):
        super().__init__(parent, title=title)

        self.__name__ = 'products_database'

        self.create_columns()

        func_program.set_data_in_table(self.__name__, self.main_table)
# ----------------------------- Button start -----------------------------------

    def on_new(self, event):
        """ Вызывает окно добавления нового изделия """
        self.call_window_new_or_redact(mode_redact=False)
        func_program.set_cursor_end_table(self.main_table)

    def on_redact(self, event):
        """ Вызывает окно редактирования данных об изделии из БД """
        id_redact = func_program.get_id_focus_line(self.main_table)
        if not id_redact == -1:
            self.call_window_new_or_redact(mode_redact=True, id_redact=id_redact)

# TODO реализовать общий модуль для поиска -------------------------------------
    def on_search(self, event):
        """ Поиск в базе данных """
        window_messages.message_info_not_realized()

# ----------------------------- Button end -------------------------------------

    def create_columns(self):
        """ Создает колонки в таблице для отображения данных """
        self.main_table.InsertColumn(0, '№', width=40)
        self.main_table.InsertColumn(1, 'ID Изделия', width=0)
        self.main_table.InsertColumn(2, 'Иконка', width=100)
        self.main_table.InsertColumn(3, 'Тип ', width=150)
        self.main_table.InsertColumn(4, 'Модель', width=250)
        self.main_table.InsertColumn(5, 'Стоимость', width=100)
        self.main_table.InsertColumn(6, 'Количество', width=100)
        self.main_table.InsertColumn(7, 'Описание', width=200)
        self.main_table.InsertColumn(8, 'Ширина,см.', width=100)
        self.main_table.InsertColumn(9, 'Высота,см.', width=100)
        self.main_table.InsertColumn(10, 'Глубина,см.', width=100)
        self.main_table.InsertColumn(11, 'Вес,г.', width=100)

    def call_window_new_or_redact(self, mode_redact=False, id_redact=None):
        """ Вызывает окно создающее новую запись об изделие.
            В зависимости от mode_redact решает редактируемая или новая запись
        """
        if mode_redact:
            title_window = "Редактирование данных об изделие"
        else:
            title_window = "Добавление новое изделие"

        dlg = DialogAddProduct(self, title=title_window, id_redact=id_redact)
        dlg.ShowModal()
        dlg.Destroy()

        func_program.refresh_data_in_table(self.__name__, self.main_table)
