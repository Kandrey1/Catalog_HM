import wx

import func_database
import func_program
import settings
import window_messages


class BaseDialogDatabase(wx.Dialog):
    """ Шаблон окна базы данных таблицы"""
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(1050, 400))
# ------------------------------------------------------------------------------
        size_but_s = settings.size_button_small
        size_but_m = settings.size_button_medium
        size_but_l = settings.size_button_large

        self.dict_tables_database = settings.dict_tables_database
# ------------------------------------------------------------------------------

        self.panel = wx.Panel(self)
        self.box_main = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.box_main)
        self.hbox_table_button = wx.BoxSizer(wx.HORIZONTAL)
# ------------------------------------------------------------------------------

        self.main_table = wx.ListCtrl(self.panel, wx.ID_ANY, style=wx.LC_REPORT)
        self.main_table.SetFont(wx.Font(wx.FontInfo(12)))
        self.main_table.SetBackgroundColour("#f0f0f0")

        self.box_main_table = wx.BoxSizer()
        self.box_main_table.Add(self.main_table)

        self.hbox_table_button.Add(self.box_main_table, 1,
                                   wx.EXPAND | wx.ALL, 10)

        self.box_button_right = wx.BoxSizer(wx.VERTICAL)

        self.but_new = wx.Button(self.panel, label="Добавить",
                                 size=size_but_m)
        self.but_redact = wx.Button(self.panel, label="Редактировать",
                                    size=size_but_m)
        self.but_copy = wx.Button(self.panel, label="Копировать",
                                  size=size_but_m)
        self.but_delete = wx.Button(self.panel, label="Удалить",
                                    size=size_but_m)

        self.box_button_right.Add(self.but_new, 0, wx.BOTTOM, border=10)
        self.box_button_right.Add(self.but_redact, 0, wx.BOTTOM, border=10)
        self.box_button_right.Add(self.but_copy, 0, wx.BOTTOM, border=10)
        self.box_button_right.AddSpacer(20)
        self.box_button_right.Add(self.but_delete, 0, wx.TOP, border=10)

        self.hbox_table_button.Add(self.box_button_right, 0, wx.EXPAND | wx.ALL,
                                   10)
        self.box_main.Add(self.hbox_table_button, 0, wx.EXPAND | wx.ALL, 10)
        # Разделитель
        self.box_main.Add(wx.StaticLine(self.panel),
                          flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=20)
# ------------------------------------------------------------------------------
        self.box_search = wx.BoxSizer(wx.HORIZONTAL)

        self.input_data_search = wx.TextCtrl(self.panel, size=(400, 20),
                                             value="Введите текст поиска")

# TODO словарь с полями в зависимости от таблицы
#  или выгружать все поля таблицы и заносить в список комбобокса
        self.combobox_list = ["Поиск по колонке", "Поле1", "Поле2", "Поле3"]

        self.combobox_search = wx.ComboBox(self.panel,
                                           choices=self.combobox_list,
                                           style=wx.CB_READONLY)
        self.combobox_search.SetSelection(0)

        self.button_search = wx.Button(self.panel, label="Поиск",
                                       size=size_but_s)
        self.button_search_reset = wx.Button(self.panel, label="Сброс",
                                             size=size_but_s)

        self.box_search.Add(self.input_data_search, 0, wx.ALL, border=10)
        self.box_search.Add(self.combobox_search, 0, wx.ALL, border=10)
        self.box_search.Add(self.button_search, 0, wx.ALL, border=10)
        self.box_search.Add(self.button_search_reset, 0, wx.ALL, border=10)

        self.box_main.Add(self.box_search, 0, wx.EXPAND | wx.ALL, 10)
        # Разделитель
        self.box_main.Add(wx.StaticLine(self.panel),
                          flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=20)
# ------------------------------------------------------------------------------
        self.box_main_button = wx.BoxSizer(wx.HORIZONTAL)

        self.button_help = wx.Button(self.panel, label="Справка",
                                     size=size_but_l)
        self.button_cancel = wx.Button(self.panel, label="Отмена",
                                       size=size_but_l)

        self.box_main_button.Add(self.button_help, 0, wx.ALL, border=20)
        self.box_main_button.Add(self.button_cancel, 0, wx.ALL, border=20)

        self.box_main.Add(self.box_main_button, 1, wx.ALIGN_RIGHT, 10)

# ------------------------------------------------------------------------------
        self.Bind(wx.EVT_BUTTON, self.on_help, self.button_help)
        self.Bind(wx.EVT_BUTTON, self.on_close, self.button_cancel)

        self.Bind(wx.EVT_BUTTON, self.on_new, self.but_new)
        self.Bind(wx.EVT_BUTTON, self.on_redact, self.but_redact)
        self.Bind(wx.EVT_BUTTON, self.on_copy, self.but_copy)
        self.Bind(wx.EVT_BUTTON, self.on_delete, self.but_delete)
        self.Bind(wx.EVT_BUTTON, self.on_search, self.button_search)
        self.Bind(wx.EVT_BUTTON, self.on_search_reset, self.button_search_reset)

# --------------------------- BUTTON start -------------------------------------

        self.Centre()

    def on_new(self, event):
        """ Вызывает окно добавления нового"""
        pass

    def on_redact(self, event):
        """ Вызывает окно редактирования """
        pass

    def on_copy(self, event):
        """ Копирует выбранную строку в таблице """
        pass

    def on_delete(self, event):
        """ Удаляет выбранную строку в таблице """
        pass

    def on_search(self, event):
        """ Запускает поиск по таблице """
        pass

    def on_search_reset(self, event):
        """ Сбрасывает данные полученные по итогам поиска """
        self.refresh_data_in_table()

# TODO ---  всплывающее окно справки   -----------------------------------------
    def on_help(self, event):
        """ Вызывает окно справки """
        window_messages.message_info_not_realized()

    def on_close(self, event):
        """ Закрывает текущее окно"""
        self.Close()

# --------------------------- BUTTON end ---------------------------------------

# ----------------------------- DATA start -------------------------------------
    def get_data_from_database(self):
        """ Получает все строки из таблицы в БД.
            Таблица это значение из словаря dict_table, где ключ
            это self.__name__   """
        sql = f" SELECT * FROM {self.dict_tables_database[self.__name__]} "
        return func_database.get_from_database(sql)

    def set_data_in_table(self, data=None):
        """ Устанавливает полученные записи в таблицу. Если данные не
            передавались(по умолчанию) запрашивает данные из БД    """
        rows = data if data else self.get_data_from_database()
        rows = func_program.renumber_data_for_set(rows)
        for row in rows:
            self.main_table.Append(row)

    def refresh_data_in_table(self):
        """ Обновляет данные в таблице """
        self.main_table.DeleteAllItems()
        self.set_data_in_table()

# ----------------------------- DATA end ---------------------------------------
