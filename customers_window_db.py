import func_program
import window_messages
from base_frame_database import BaseDialogDatabase
from customer_add import DialogAddCustomer


class DialogAllCustomers(BaseDialogDatabase):
    """ Класс создает модальное окно с данными всех клиентов в БД """
    def __init__(self, parent, title="База данных клиентов"):
        super().__init__(parent, title=title)

        self.table_db = "customers"

        self.create_columns()

        func_program.set_data_in_table(self.table_db, self.main_table)
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
            Флаг mode_redact определяет редактируемая или новая запись """
        if mode_redact:
            title_window = "Редактирование данных о клиенте"
        else:
            title_window = "Добавление нового клиента"

        dlg = DialogAddCustomer(self, title=title_window, id_redact=id_redact)
        func_program.start_window(dlg)

        func_program.refresh_data_in_table(self.table_db, self.main_table)
