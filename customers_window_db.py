import customers
import func_program
import window_messages
from base_frame_database import BaseDialogDatabase
from customer_add import DialogAddCustomer


class DialogAllCustomers(BaseDialogDatabase):
    """ Класс создает модальное окно с данными всех клиентов в БД """
    def __init__(self, parent, title="База данных клиентов"):
        super().__init__(parent, title=title)

        self.__name__ = 'customers_database'

        self.create_columns()

        self.set_data_in_table()
# ----------------------------- Button start -----------------------------------

    def on_new(self, event):
        """ Вызывает окно добавления нового клиента """
        self.call_window_new_or_redact(mode_redact=False)
        func_program.set_cursor_end_table(self.main_table)

    def on_redact(self, event):
        """ Вызывает окно редактирования данных о клиенте из БД """
        id_redact = func_program.get_id_focus_line(self.main_table)
        if not id_redact == -1:
            self.call_window_new_or_redact(mode_redact=True, id_redact=id_redact)

    def on_copy(self, event):
        """ Копирует выбранную запись """
        row = self.get_row_in_focus()
        if row:
            copy_line = customers.Customer()
            copy_line.set_data_in_class(row[1:])
            copy_line.write_in_database()
            self.refresh_data_in_table()
            func_program.set_cursor_end_table(self.main_table)

    def on_delete(self, event):
        """ Удаляет выбранную запись """
        self.id_del = func_program.get_id_focus_line(self.main_table)
        if not self.id_del == -1:
            window_messages.message_delete_record(self)

# TODO реализовать общий модуль для поиска -------------------------------------
    def on_search(self, event):
        """ Поиск в базе данных """
        window_messages.message_info_not_realized()

# ----------------------------- Button end -------------------------------------

    def create_columns(self):
        """ Создает колонки в таблице для отображения данных """
        self.main_table.InsertColumn(0, '№', width=40)
        self.main_table.InsertColumn(1, 'ID Клиента', width=0)
        self.main_table.InsertColumn(2, 'Фамилия', width=100)
        self.main_table.InsertColumn(3, 'Имя ', width=100)
        self.main_table.InsertColumn(4, 'Отчество', width=100)
        self.main_table.InsertColumn(5, 'Телефон', width=100)
        self.main_table.InsertColumn(6, 'Email', width=150)
        self.main_table.InsertColumn(7, 'Адрес', width=150)
        self.main_table.InsertColumn(8, 'Вконтакте', width=100)

    def call_window_new_or_redact(self, mode_redact=False, id_redact=None):
        """ Вызывает окно создающее новую запись о клиенте.
            В зависимости от mode_redact решает редактируемая или новая запись
        """
        if mode_redact:
            title_window = "Редактирование данных о клиенте"
        else:
            title_window = "Добавление нового клиента"

        dlg = DialogAddCustomer(self, title=title_window, id_redact=id_redact)
        dlg.ShowModal()
        dlg.Destroy()

        self.refresh_data_in_table()

    def get_row_in_focus(self):
        """ Получает данные выделенной строки """
        id_focus = func_program.get_id_focus_line(self.main_table)
        if not id_focus == -1:
            row = customers.get_data_id_focus_line(id_focus)
            return row

    def delete_row(self):
        """ Удаляет выбранную запись """
        customers.delete_line_database(self.id_del)
        self.refresh_data_in_table()
