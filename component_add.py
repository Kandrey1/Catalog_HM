import wx
import search
from components import Component
import func_database
import func_program
import settings


class DialogAddComponent(wx.Dialog):
    """ Класс создает модальное окно для добавления компонента в изделие """
    def __init__(self, parent, title, id_redact=None):
        super().__init__(parent, title=title, size=(880, 370))

        self.table_db = "materials"

        self.parent = parent
        self.id_redact = id_redact
        self.on_select = False

        size_but_s = settings.size_button_small
        size_but_l = settings.size_button_large

        self.panel = wx.Panel(self)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.main_sizer)

        self.box_table_search = wx.BoxSizer(wx.VERTICAL)

        self.table_materials = wx.ListCtrl(self.panel, wx.ID_ANY,
                                           style=wx.LC_REPORT,
                                           size=(720, 130))
        self.table_materials.SetFont(wx.Font(wx.FontInfo(12)))
        self.table_materials.SetBackgroundColour("#f0f0f0")

        self.table_materials.InsertColumn(0, '№', width=40)
        self.table_materials.InsertColumn(1, 'ID Материала', width=0)
        self.table_materials.InsertColumn(2, 'Материал', width=300)
        self.table_materials.InsertColumn(3, 'Ед. измерения', width=80)
        self.table_materials.InsertColumn(4, 'Поставщик', width=300)

        self.box_table_search.Add(self.table_materials, 1,
                                  flag=wx.ALL | wx.EXPAND, border=5)

        self.text_input_search = wx.TextCtrl(self.panel)
        self.button_search = wx.Button(self.panel, label="Поиск",
                                       size=size_but_s)

        self.box_search = wx.BoxSizer(wx.HORIZONTAL)
        self.box_search.Add(self.text_input_search, 1, flag=wx.ALL, border=5)
        self.box_search.Add(self.button_search, 0, flag=wx.ALL, border=5)

        self.box_table_search.Add(self.box_search, 0, flag=wx.ALL | wx.EXPAND,
                                  border=5)

        self.box_table_search_but = wx.BoxSizer(wx.HORIZONTAL)
        self.button_select = wx.Button(self.panel,
                                       label="Выбрать\nэтот\nматериал",
                                       size=(100, 30))
        self.button_select.SetFont(wx.Font(wx.FontInfo(10)))

        self.box_table_search_but.Add(self.box_table_search,  1,
                                      flag=wx.EXPAND | wx.ALL, border=5)
        self.box_table_search_but.Add(self.button_select, 0,
                                      flag=wx.EXPAND | wx.ALL, border=5)

        self.main_sizer.Add(self.box_table_search_but, 0, flag=wx.ALL, border=5)

        # КОМПОНЕНТ
        self.static_text_material = wx.StaticText(self.panel, label="Материал")
        self.static_text_number = wx.StaticText(self.panel, label="Количество")
        self.static_text_unit = wx.StaticText(self.panel,
                                              label="Единицы\nизмерения")
        self.static_text_price_one = wx.StaticText(self.panel,
                                                label="Стоимость\nза единицу")
        self.static_text_vendor = wx.StaticText(self.panel, label="Поставщик")

        self.text_material_out = wx.TextCtrl(self.panel, style=wx.TE_READONLY,
                                             size=(300, 20))
        self.text_input_number = wx.SpinCtrl(self.panel, min=0, max=100000,
                                             initial=1, size=(70, 20))
        self.text_text_unit_out = wx.TextCtrl(self.panel, style=wx.TE_READONLY,
                                              size=(70, 20))
        self.text_input_price_one = wx.SpinCtrl(self.panel, min=0, max=100000,
                                                initial=0, size=(100, 20))
        self.text_text_vendor_out = wx.TextCtrl(self.panel,
                                        style=wx.TE_READONLY, size=(250, 20))

        self.box_component = wx.FlexGridSizer(2, 5, 10, 10)

        self.box_component.Add(self.static_text_material)
        self.box_component.Add(self.static_text_number, flag=wx.EXPAND)
        self.box_component.Add(self.static_text_unit)
        self.box_component.Add(self.static_text_price_one)
        self.box_component.Add(self.static_text_vendor)

        self.box_component.Add(self.text_material_out)
        self.box_component.Add(self.text_input_number)
        self.box_component.Add(self.text_text_unit_out)
        self.box_component.Add(self.text_input_price_one)
        self.box_component.Add(self.text_text_vendor_out)

        self.main_sizer.Add(self.box_component, proportion=0, flag=wx.ALL,
                            border=10)
        # Разделитель
        self.main_sizer.Add(wx.StaticLine(self.panel),
                            flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        # кнопки
        self.box_button = wx.BoxSizer(wx.HORIZONTAL)
        self.button_add = wx.Button(self.panel, label="Добавить компонент",
                                    size=size_but_l)
        self.button_cancel = wx.Button(self.panel, label="Отмена",
                                       size=size_but_l)

        self.box_button.Add(self.button_add, proportion=0, flag=wx.ALL,
                            border=10)
        self.box_button.Add(self.button_cancel, proportion=0, flag=wx.ALL,
                            border=10)

        self.main_sizer.Add(self.box_button, proportion=0, flag=wx.ALIGN_RIGHT,
                            border=10)

        self.Bind(wx.EVT_BUTTON, self.search_in_materials, self.button_search)
        self.Bind(wx.EVT_BUTTON, self.select_material, self.button_select)

        self.Bind(wx.EVT_BUTTON, self.on_save_component, self.button_add)
        self.Bind(wx.EVT_BUTTON, self.on_close, self.button_cancel)

        func_program.set_data_in_table(self.table_db, self.table_materials)

        if self.id_redact != None:
            self.load_redact_data()

    def on_close(self, event):
        """ Закрывает текущее окно """
        self.Close()

    def on_save_component(self, event):
        """ Добавляет компонент в изделие """
        if self.on_select:
            self.save_in_class()
            if self.parent.id_redact_product:
                self.component.product_id = self.parent.id_redact_product
            self.component.write_in_database(self.id_redact)
            self.Close()
        else:
            wx.MessageBox("Выберите материал в таблице.", "Информация", wx.OK)

    def search_in_materials(self, event):
        """ Осуществляет поиск в базе созданных материалов """
        text_find = self.text_input_search.GetValue()
        rows = search.search_in_component(text_find)
        self.table_materials.DeleteAllItems()
        func_program.set_data_in_table(self.table_db, self.table_materials, rows)

    def select_material(self, event):
        """ Кнопка выбора материала. Работает только при выбранной строке """
        id_select = func_program.get_id_focus_line(self.table_materials)
        if not id_select == -1:
            row = func_database.get_data_id_focus_line(self.table_db, id_select)
            self.set_select_in_component(row)
            self.on_select = True

    def set_select_in_component(self, row):
        """ Устанавливает данные выбранной строки в компонент """
        self.id_material = row[0]
        self.text_material_out.SetValue(row[1])
        self.text_text_unit_out.SetValue(row[2])
        self.text_text_vendor_out.SetValue(row[3])

    def save_in_class(self):
        """ Записывает данные из полей в класс """
        product_id = None if not self.id_redact else self.parent.id_redact_product
        self.component = Component()
        self.component.product_id = product_id
        self.component.material_id = self.id_material
        self.component.number = self.text_input_number.GetValue()
        self.component.price_one = self.text_input_price_one.GetValue()

    def load_redact_data(self):
        """ Загружает данные для редактирования если выбрано редактирование """
        row = Component.get_data_redact_component(self.id_redact)
        self.set_redact_data(row)
        func_program.set_cursor_on_row(self.table_materials, row[1])

    def set_redact_data(self, row):
        """ Устанавливает загруженные из БД данные в поля """
        self.text_material_out.SetValue(row[2])
        self.text_input_number.SetValue(row[3])
        self.text_text_unit_out.SetValue(row[4])
        self.text_input_price_one.SetValue(row[5])
        self.text_text_vendor_out.SetValue(row[6])
