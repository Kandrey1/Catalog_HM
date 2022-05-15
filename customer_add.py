import wx
import customers
import func_database


class DialogAddCustomer(wx.Dialog):
    """ Модальное окно для добавления клиента в БД """
    def __init__(self, parent, title, id_redact=None):
        super().__init__(parent, title=title, size=(550, 250))

        self.id_redact = id_redact
        self.parent = parent

        self.panel = wx.Panel(self)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.main_sizer)

        self.box_customer = wx.GridBagSizer()
# ------------------------------------------------------------------------------
        self.static_text_last_name = wx.StaticText(self.panel, label="Фамилия")
        self.text_input_last_name = wx.TextCtrl(self.panel)
        self.box_customer.Add(self.static_text_last_name, pos=(0, 0),
                              span=(1, 1), flag=wx.ALL, border=5)
        self.box_customer.Add(self.text_input_last_name, pos=(0, 1),
                              span=(1, 1), flag=wx.ALL, border=5)

        self.static_text_first_name = wx.StaticText(self.panel, label="Имя")
        self.text_input_first_name = wx.TextCtrl(self.panel)
        self.box_customer.Add(self.static_text_first_name, pos=(0, 2),
                              span=(1, 1), flag=wx.ALL, border=5)
        self.box_customer.Add(self.text_input_first_name, pos=(0, 3),
                              span=(1, 1), flag=wx.ALL, border=5)

        self.static_text_middle_name = wx.StaticText(self.panel, label="Отчество")
        self.text_input_middle_name = wx.TextCtrl(self.panel)
        self.box_customer.Add(self.static_text_middle_name, pos=(0, 4),
                              span=(1, 1), flag=wx.ALL, border=5)
        self.box_customer.Add(self.text_input_middle_name, pos=(0, 5),
                              span=(1, 1), flag=wx.ALL, border=5)
    # --------------------------------------------------------------------------
        self.static_text_phone = wx.StaticText(self.panel, label="Телефон")
        self.text_input_phone = wx.TextCtrl(self.panel)
        self.box_customer.Add(self.static_text_phone, pos=(1, 0), span=(1, 1),
                              flag=wx.ALL, border=5)
        self.box_customer.Add(self.text_input_phone, pos=(1, 1), span=(1, 1),
                              flag=wx.ALL, border=5)

        self.static_text_email = wx.StaticText(self.panel, label="Email")
        self.text_input_email = wx.TextCtrl(self.panel)
        self.box_customer.Add(self.static_text_email, pos=(1, 2), span=(1, 1),
                              flag=wx.ALL, border=5)
        self.box_customer.Add(self.text_input_email, pos=(1, 3), span=(1, 3),
                              flag=wx.ALL | wx.EXPAND, border=5)
    # --------------------------------------------------------------------------
        self.static_text_address = wx.StaticText(self.panel, label="Адрес")
        self.text_input_address = wx.TextCtrl(self.panel)
        self.box_customer.Add(self.static_text_address, pos=(2, 0), span=(1, 1),
                              flag=wx.ALL, border=5)
        self.box_customer.Add(self.text_input_address, pos=(2, 1), span=(1, 5),
                              flag=wx.ALL | wx.EXPAND, border=5)
    # --------------------------------------------------------------------------
        self.static_text_vkontakte = wx.StaticText(self.panel, label="Вконтакте")
        self.text_input_vkontakte = wx.TextCtrl(self.panel)
        self.box_customer.Add(self.static_text_vkontakte, pos=(3, 0),
                              span=(1, 1), flag=wx.ALL, border=5)
        self.box_customer.Add(self.text_input_vkontakte, pos=(3, 1),
                              span=(1, 2), flag=wx.ALL | wx.EXPAND, border=5)

        self.main_sizer.Add(self.box_customer, proportion=0, flag=wx.ALL,
                            border=10)
    # --------------------------------------------------------------------------
        self.hbox_button = wx.BoxSizer(wx.HORIZONTAL)
        self.button_save = wx.Button(self.panel, label="Сохранить", size=(120, 28))
        self.button_cancel = wx.Button(self.panel, label="Отмена", size=(120, 28))

        self.hbox_button.Add(self.button_save, flag=wx.ALL, border=10)
        self.hbox_button.Add(self.button_cancel, flag=wx.ALL, border=10)

        self.main_sizer.Add(self.hbox_button, proportion=0,
                            flag=wx.ALL | wx.ALIGN_RIGHT, border=10)

        self.Bind(wx.EVT_BUTTON, self.on_save_customer, self.button_save)
        self.Bind(wx.EVT_BUTTON, self.on_close, self.button_cancel)
# ------------------------------------------------------------------------------

        if self.id_redact:
            self.load_redact_data()

        self.Centre()

    def on_close(self, event):
        """ Закрывает текущее окно"""
        self.Close()

    def on_save_customer(self, event):
        """ Сохраняет в БД введенные данные клиента """
        self.save_in_class()
        self.customer.write_in_database(self.id_redact)
        self.Close()

    def save_in_class(self):
        """ Записывает данные из полей в класс """
        self.customer = customers.Customer()
        self.customer.last_name = self.text_input_last_name.GetValue()
        self.customer.first_name = self.text_input_first_name.GetValue()
        self.customer.middle_name = self.text_input_middle_name.GetValue()
        self.customer.phone = self.text_input_phone.GetValue()
        self.customer.email = self.text_input_email.GetValue()
        self.customer.address = self.text_input_address.GetValue()
        self.customer.vkontakte = self.text_input_vkontakte.GetValue()

    def load_redact_data(self):
        """ Загружает данные для редактирования если выбрано редактирование """
        row = func_database.get_data_id_focus_line(self.parent.table_db,
                                                   self.id_redact)
        self.set_in_form_input(row)

    def set_in_form_input(self, data):
        """ Устанавливает данные data в поля окна """
        self.text_input_last_name.SetValue(data[1])
        self.text_input_first_name.SetValue(data[2])
        self.text_input_middle_name.SetValue(data[3])
        self.text_input_phone.SetValue(str(data[4]))
        self.text_input_email.SetValue(data[5])
        self.text_input_address.SetValue(data[6])
        self.text_input_vkontakte.SetValue(data[7])
