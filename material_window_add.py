import func_program
import materials
import window_messages
from base_frame_database import BaseDialogDatabase
from material_add import DialogAddMaterial


class DialogAllMaterials(BaseDialogDatabase):
    """ Класс создает модальное окно с данными материалов в БД """
    def __init__(self, parent, title="База данных материалов"):
        super().__init__(parent, title=title)

        self.__name__ = "materials_database"

        self.create_columns()

        func_program.set_data_in_table(self.__name__, self.main_table)
# ----------------------------- Button start -----------------------------------

    def on_new(self, event):
        """ Вызывает окно добавления нового материала """
        self.call_window_new_or_redact(mode_redact=False)
        func_program.set_cursor_end_table(self.main_table)

    def on_redact(self, event):
        """ Вызывает окно редактирования данных о материале из БД """
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
        self.main_table.InsertColumn(1, 'ID Материала', width=0)
        self.main_table.InsertColumn(2, 'Материал', width=400)
        self.main_table.InsertColumn(3, 'Ед. измерения', width=80)
        self.main_table.InsertColumn(4, 'Поставщик', width=300)

    def call_window_new_or_redact(self, mode_redact=False, id_redact=None):
        """ Вызывает окно создающее новую запись о клиенте.
            Флаг mode_redact определяет редактируемая или новая запись """
        if mode_redact:
            title_window = "Редактирование данных материала"
        else:
            title_window = "Добавление нового материала"

        dlg = DialogAddMaterial(self, title=title_window, id_redact=id_redact)
        dlg.ShowModal()
        dlg.Destroy()

        func_program.refresh_data_in_table(self.__name__, self.main_table)
