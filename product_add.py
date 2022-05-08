import wx

import func_database
import func_files
import products
import settings


class DialogAddProduct(wx.Dialog):
    """ Модальное окно для добавления изделия в БД """
    def __init__(self, parent, title, id_redact=None):
        super().__init__(parent, title=title, size=(950, 500))

        size_but_s = settings.size_button_small
        size_but_m = settings.size_button_medium
        size_but_l = settings.size_button_large

        self.path_sys_image_default = settings.path_sys_image_default
        self.path_data_image = settings.path_data_image
        self.parent = parent
        self.id_redact = id_redact
        self.miniature_product = False
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
        self.panel = wx.Panel(self)
        self.main_box = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.main_box)

        self.box_image_materials = wx.BoxSizer(wx.HORIZONTAL)

        self.box_image = wx.BoxSizer(wx.VERTICAL)
        self.image = wx.StaticBitmap(self.panel, wx.ID_ANY)
        self.image.SetBitmap(wx.BitmapFromImage(self.path_sys_image_default))

        self.but_add_image = wx.Button(self.panel, label="Добавить фото",
                                       size=size_but_s)
        self.box_image.Add(self.image, 1, wx.ALIGN_CENTER | wx.ALL, border=5)
        self.box_image.Add(self.but_add_image, 0, wx.ALIGN_CENTER | wx.BOTTOM,
                           border=5)

        self.Bind(wx.EVT_BUTTON, self.on_add_image, self.but_add_image)
# ------------------------------------------------------------------------------
        self.box_buts_materials = wx.BoxSizer(wx.VERTICAL)
        self.but_new = wx.Button(self.panel, label="Добавить", size=size_but_m)
        self.but_redact = wx.Button(self.panel, label="Редактировать",
                                    size=size_but_m)
        self.but_copy = wx.Button(self.panel, label="Копировать",
                                  size=size_but_m)
        self.but_del = wx.Button(self.panel, label="Удалить", size=size_but_m)

        self.box_buts_materials.Add(self.but_new, 0, wx.BOTTOM, border=5)
        self.box_buts_materials.Add(self.but_redact, 0, wx.BOTTOM, border=5)
        self.box_buts_materials.Add(self.but_copy, 0, wx.BOTTOM, border=5)
        self.box_buts_materials.AddSpacer(20)
        self.box_buts_materials.Add(self.but_del, 0, wx.BOTTOM, border=5)

        self.Bind(wx.EVT_BUTTON, self.on_add_material, self.but_new)
        self.Bind(wx.EVT_BUTTON, self.on_redact_material, self.but_redact)
        self.Bind(wx.EVT_BUTTON, self.on_copy_material, self.but_copy)
        self.Bind(wx.EVT_BUTTON, self.on_del_material, self.but_del)

        self.table_materials = wx.ListCtrl(self.panel, wx.ID_ANY,
                                           style=wx.LC_REPORT, size=(-1, 150))
        self.table_materials.SetFont(wx.Font(wx.FontInfo(12)))
        self.table_materials.SetBackgroundColour("#f0f0f0")

        self.table_materials.InsertColumn(0, '№', width=40)
        self.table_materials.InsertColumn(1, 'ID Материала', width=0)
        self.table_materials.InsertColumn(2, 'Материал', width=200)
        self.table_materials.InsertColumn(3, 'Кол-во', width=50)
        self.table_materials.InsertColumn(4, 'Ед.измерения', width=50)
        self.table_materials.InsertColumn(5, 'Стоимость 1 поз.', width=100)
        self.table_materials.InsertColumn(6, 'Поставщик',  width=100)

        self.hbox_materials = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox_materials.Add(self.table_materials, 1, wx.EXPAND | wx.ALL, 5)
        self.hbox_materials.Add(self.box_buts_materials, 0, wx.ALL, 5)

        self.box_image_materials.Add(self.box_image, 0, wx.ALL, 5)
        self.box_image_materials.Add(self.hbox_materials, 1, wx.EXPAND | wx.ALL,
                                     border=5)

        self.main_box.Add(self.box_image_materials, 0, wx.EXPAND | wx.ALL, 5)
        # Разделитель
        self.main_box.Add(wx.StaticLine(self.panel),
                          flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
        self.hbox_datas = wx.BoxSizer(wx.HORIZONTAL)

        self.static_text_type = wx.StaticText(self.panel, label="Тип изделия")
        self.static_text_model = wx.StaticText(self.panel, label="Модель")
        self.static_text_price = wx.StaticText(self.panel, label="Цена")
        self.static_text_about = wx.StaticText(self.panel, label="Описание")
        self.static_text_number = wx.StaticText(self.panel, label="Количество")

        # TODO реализовать возможность создания списка пользователем
        self.links_type = ["Кардхолдер", "Зажим", "Портмоне", "Докхолдер",
                           "Сумка мужская", "Сумка женская"]
        self.combobox_type = wx.ComboBox(self.panel, choices=self.links_type,
                                         style=wx.CB_READONLY)
        self.combobox_type.SetSelection(0)
        self.text_input_model = wx.TextCtrl(self.panel)
        self.text_input_price = wx.SpinCtrl(self.panel, min=0, max=90000000,
                                            initial=0)
        self.text_input_number = wx.SpinCtrl(self.panel, min=0, max=9000000,
                                             initial=0)
        self.text_input_about = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)

        self.box_data = wx.GridBagSizer()
        self.box_data.SetEmptyCellSize(sz=(50, 10))
        self.box_data.Add(self.static_text_type, pos=(0, 0), span=(1, 1),
                          flag=wx.ALL, border=5)
        self.box_data.Add(self.combobox_type, pos=(1, 0), span=(1, 1),
                          flag=wx.ALL | wx.EXPAND, border=5)
        self.box_data.Add(self.static_text_model, pos=(0, 1), span=(1, 1),
                          flag=wx.ALL, border=5)
        self.box_data.Add(self.text_input_model, pos=(1, 1), span=(1, 10),
                          flag=wx.ALL | wx.EXPAND, border=5)
        self.box_data.Add(self.static_text_price, pos=(2, 0), span=(1, 1),
                          flag=wx.ALL, border=5)
        self.box_data.Add(self.text_input_price, pos=(3, 0), span=(1, 1),
                          flag=wx.ALL | wx.EXPAND, border=5)
        self.box_data.Add(self.static_text_number, pos=(4, 0), span=(1, 1),
                          flag=wx.ALL, border=5)
        self.box_data.Add(self.text_input_number, pos=(5, 0), span=(1, 1),
                          flag=wx.ALL | wx.EXPAND, border=5)
        self.box_data.Add(self.static_text_about, pos=(2, 1), span=(1, 1),
                          flag=wx.ALL, border=5)
        self.box_data.Add(self.text_input_about, pos=(3, 1), span=(5, 10),
                          flag=wx.ALL | wx.EXPAND, border=5)

        self.hbox_datas.Add(self.box_data, 0, wx.EXPAND | wx.ALL, 10)

# ------------------------------------------------------------------------------
        self.static_text_width = wx.StaticText(self.panel, label="Ширина,см.")
        self.static_text_height = wx.StaticText(self.panel, label="Высота,см.")
        self.static_text_depth = wx.StaticText(self.panel, label="Глубина,см.")
        self.static_text_weigh = wx.StaticText(self.panel, label="Вес,г.")

        self.text_input_width = wx.SpinCtrl(self.panel, min=0, max=100000,
                                            initial=0)
        self.text_input_height = wx.SpinCtrl(self.panel, min=0, max=100000,
                                             initial=0)
        self.text_input_depth = wx.SpinCtrl(self.panel, min=0, max=100000,
                                            initial=0)
        self.text_input_weigh = wx.SpinCtrl(self.panel, min=0, max=1000000,
                                            initial=0)

        self.box_geometry = wx.GridSizer(rows=4, cols=2, vgap=0, hgap=0)
        self.box_geometry.Add(self.static_text_width, 0, wx.ALL, 5)
        self.box_geometry.Add(self.static_text_height, 0, wx.ALL, 5)
        self.box_geometry.Add(self.text_input_width, 0, wx.ALL, 5)
        self.box_geometry.Add(self.text_input_height, 0, wx.ALL, 5)
        self.box_geometry.Add(self.static_text_depth, 0, wx.ALL, 5)
        self.box_geometry.Add(self.static_text_weigh, 0, wx.ALL, 5)
        self.box_geometry.Add(self.text_input_depth, 0, wx.ALL, 5)
        self.box_geometry.Add(self.text_input_weigh, 0, wx.ALL, 5)

        self.hbox_datas.Add(self.box_geometry, 0, wx.ALL, 5)

        self.main_box.Add(self.hbox_datas, 0, wx.EXPAND | wx.ALL, 5)
        # Разделитель
        self.main_box.Add(wx.StaticLine(self.panel),
                          flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

        self.hbox_button_main = wx.BoxSizer(wx.HORIZONTAL)
        self.button_save = wx.Button(self.panel, label="Сохранить",
                                     size=size_but_l)
        self.button_cancel = wx.Button(self.panel, label="Отмена",
                                       size=size_but_l)
        self.hbox_button_main.Add(self.button_save,   flag=wx.ALL, border=5)
        self.hbox_button_main.Add(self.button_cancel, flag=wx.ALL, border=5)
        self.main_box.Add(self.hbox_button_main, 0,
                          flag=wx.ALIGN_RIGHT | wx.ALL, border=10)

        self.Bind(wx.EVT_BUTTON, self.on_save_product, self.button_save)
        self.Bind(wx.EVT_BUTTON, self.on_close, self.button_cancel)

        if self.id_redact:
            self.load_redact_data()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
    def on_close(self, event):
        """ Закрывает текущее окно"""
        self.Close()

    def on_save_product(self, event):
        """ Сохранение введенных данных об изделии в БД """
        self.save_in_class()
        self.product.write_in_database(self.id_redact)
        id_product = self.id_redact

        if not self.id_redact:
            id_now = func_database.get_id_last_row_in_table("products_database")
            id_product = id_now
            func_files.File.create_new_dir_product(id_product)

        path = self.path_sys_image_default

        if self.miniature_product:
            self.save_mini_pic_product(path, id_product)
            path = func_files.File.get_path_miniature_product(id_product)

        func_database.update_path_miniature_product(path, id_product)

        self.Close()

    def save_in_class(self):
        """ Записывает данные из полей в класс """
        self.product = products.Product()
        self.product.type_prod = self.combobox_type.GetValue()
        self.product.model = self.text_input_model.GetValue()
        self.product.price = self.text_input_price.GetValue()
        self.product.number = self.text_input_number.GetValue()
        self.product.about = self.text_input_about.GetValue()
        self.product.size_width = self.text_input_width.GetValue()
        self.product.size_height = self.text_input_height.GetValue()
        self.product.size_depth = self.text_input_depth.GetValue()
        self.product.weigh = self.text_input_weigh.GetValue()

    def on_add_image(self, event):
        """ Вызывает окно выбора картинки для аватарки изделия """
        path_selected = func_files.File.path_file(self)
        if path_selected:
            self.set_and_save_temp_mini_pic(path_selected)

    def on_add_material(self, event):
        """ Вызывает окно добавление материала """
        pass

    def on_redact_material(self, event):
        """ Вызывает окно редактирования материала """
        pass

    def on_copy_material(self, event):
        """ Копирует выбранный материал в списке матеров в изделии """
        pass

    def on_del_material(self, event):
        """ Удаляет выбранный материал из списка матеров в изделии """
        pass

    def load_redact_data(self):
        """ Загружает данные для редактирования если выбрано редактирование """
        row = func_database.get_data_id_focus_line(self.parent.__name__,
                                                   self.id_redact)
        self.set_in_form_input(row)

    def set_in_form_input(self, data):
        """ Устанавливает данные data в поля окна """
        self.image.SetBitmap(wx.BitmapFromImage(data[1]))
        self.combobox_type.SetValue(data[2])
        self.text_input_model.SetValue(data[3])
        self.text_input_price.SetValue(data[4])
        self.text_input_number.SetValue(data[5])
        self.text_input_about.SetValue(data[6])
        self.text_input_width.SetValue(data[7])
        self.text_input_height.SetValue(data[8])
        self.text_input_depth.SetValue(data[9])
        self.text_input_weigh.SetValue(data[10])

    def save_mini_pic_product(self, path_dir, id_product):
        """ Сохраняет миниатюру в папку изделия """
        path_from = self.path_data_image + "temp_image.jpg"
        self.path_save = func_files.File.get_path_miniature_product(id_product)
        func_files.File.copy_file(path_from, self.path_save)

    def set_and_save_temp_mini_pic(self, path_selected):
        """ Сохраняет выбранное изображение под временным именем и
            устанавливает в качестве миниатюры """
        img_convert = func_files.ConvertImages.resize_mini_pic_product(path_selected)
        path_temp_mini = self.path_data_image + "temp_image.jpg"
        func_files.ConvertImages.save_image(img_convert, path_temp_mini)
        self.miniature_product = True
        self.image.SetBitmap(wx.BitmapFromImage(path_temp_mini))
