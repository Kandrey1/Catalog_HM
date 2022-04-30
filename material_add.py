import wx

import func_database
import materials
import settings


class DialogAddMaterial(wx.Dialog):
    """ Модальное окно для добавления материала в БД """
    def __init__(self, parent, title, id_redact=None):
        super().__init__(parent, title=title, size=(550, 190))

        self.id_redact = id_redact
        self.parent = parent

        size_but_m = settings.size_button_medium

        self.panel = wx.Panel(self)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.main_sizer)

        self.static_text_name = wx.StaticText(self.panel, label="Материал")
        self.text_input_name = wx.TextCtrl(self.panel)
        self.static_text_vendor = wx.StaticText(self.panel, label="Поставщик")
        self.text_input_vendor = wx.TextCtrl(self.panel)
        self.static_text_unit = wx.StaticText(self.panel,
                                              label="Единицы\nизмерения")
# TODO реализовать возможность пользователем создавать список
        self.combobox_list_unit = [" Выберите ", "м", "дм2", "шт", "мл"]
        self.combobox_unit = wx.ComboBox(self.panel,
                                         choices=self.combobox_list_unit,
                                         style=wx.CB_READONLY)
        self.combobox_unit.SetSelection(0)

        self.flex_sizer = wx.FlexGridSizer(3, 2, 10, 10)

        self.flex_sizer.Add(self.static_text_name)
        self.flex_sizer.Add(self.text_input_name, flag=wx.EXPAND)
        self.flex_sizer.Add(self.static_text_vendor)
        self.flex_sizer.Add(self.text_input_vendor, flag=wx.EXPAND)
        self.flex_sizer.Add(self.static_text_unit)
        self.flex_sizer.Add(self.combobox_unit)

        self.flex_sizer.AddGrowableCol(1)

        self.main_sizer.Add(self.flex_sizer, proportion=0,
                            flag=wx.ALL | wx.EXPAND, border=10)
# ------------------------------------------------------------------------------
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.button_save = wx.Button(self.panel, label="Сохранить",
                                     size=size_but_m)
        self.button_cancel = wx.Button(self.panel, label="Отмена",
                                       size=size_but_m)

        self.hbox.Add(self.button_save, flag=wx.ALL, border=10)
        self.hbox.Add(self.button_cancel, flag=wx.ALL, border=10)

        self.main_sizer.Add(self.hbox, flag=wx.ALIGN_RIGHT)

        self.Bind(wx.EVT_BUTTON, self.on_save_material, self.button_save)
        self.Bind(wx.EVT_BUTTON, self.on_close, self.button_cancel)

        if self.id_redact:
            self.load_redact_data()

        self.Centre()

    def on_close(self, event):
        """ Закрывает текущее окно"""
        self.Close()

    def on_save_material(self, event):
        """ Сохраняет в БД введенные данные о материале """
        self.save_in_class()
        self.material.write_in_database(self.id_redact)
        self.Close()

    def save_in_class(self):
        """ Записывает данные из полей в класс """
        self.material = materials.Material()
        self.material.name = self.text_input_name.GetValue()
        self.material.unit = self.combobox_unit.GetValue()
        self.material.vendor = self.text_input_vendor.GetValue()

    def load_redact_data(self):
        """ Загружает данные для редактирования если выбрано редактирование """
        row = func_database.get_data_id_focus_line(self.parent.__name__,
                                                   self.id_redact)
        self.set_in_form_input(row)

    def set_in_form_input(self, data):
        """ Устанавливает данные data в поля окна """
        self.text_input_name.SetValue(data[1])
        self.combobox_unit.SetValue(data[2])
        self.text_input_vendor.SetValue(data[3])
