import func_database
import func_files
import func_program
import window_messages
from base_frame_database import BaseDialogDatabase
from product_add import DialogAddProduct


class DialogAllProducts(BaseDialogDatabase):
    """ Класс создает модальное окно с данными всех изделий в БД """
    def __init__(self, parent, title="База данных изделий"):
        super().__init__(parent, title=title)

        self.table_db = "products"

        self.refresh_combobox_search()

        self.create_columns()

        func_program.set_data_in_table(self.table_db, self.main_table)
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

    def on_copy(self, event):
        """ Копирует выбранную строку в таблице """
        id_copy = func_program.get_id_focus_line(self.main_table)
        if not id_copy == -1:
            func_database.copy_row_in_table(self.table_db, id_copy)
            self.copy_directory_product(id_copy)
            func_program.refresh_data_in_table(self.table_db, self.main_table)
            func_program.set_cursor_end_table(self.main_table)

    def on_delete(self, event):
        """ Удаляет выбранную строку в таблице и папку изделия в
            каталоге data\\image """
        id_del = func_program.get_id_focus_line(self.main_table)
        if not id_del == -1:
            window_messages.message_delete_record(self, id_del)
            path_del = func_files.File.get_path_miniature_product(id_del)
            path_dir_del = func_files.File.get_dir_path(path_del)
            func_files.File.delete_dir_with_files(path_dir_del)
            func_program.refresh_data_in_table(self.table_db, self.main_table)

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

        func_program.refresh_data_in_table(self.table_db, self.main_table)

    def copy_directory_product(self, id_copy):
        """ Копирует существующую папку с файлами об изделии """
        path_from = func_files.File.get_path_miniature_product(id_copy)
        id_last = func_database.get_id_last_row_in_table(self.table_db)
        func_files.File.create_new_dir_product(id_last)

        if func_files.File.exist_file_miniature(path_from):
            path_in = func_files.File.get_path_miniature_product(id_last)
            func_files.File.copy_file(path_from, path_in)
            func_database.update_path_miniature_product(path_in, id_last)
