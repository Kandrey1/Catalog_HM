import wx


class MainPanel(wx.Panel):
    """ Создание панели для размещения сайзеров """
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.notebook_main = wx.Notebook(self, id=wx.ID_ANY, style=wx.NB_BOTTOM)

# ------------------------------------------------------------------------------
        self.list_note_orders = wx.ListCtrl(self.notebook_main, wx.ID_ANY,
                                            style=wx.LC_REPORT)

        self.list_note_orders.SetFont(wx.Font(wx.FontInfo(12)))
        self.list_note_orders.SetBackgroundColour("#f0f0f0")

        self.list_note_orders.InsertColumn(0, '№', width=50)
        self.list_note_orders.InsertColumn(1, 'ID', width=0)
        self.list_note_orders.InsertColumn(2, '№ Заказа', width=100)
        self.list_note_orders.InsertColumn(3, 'Изделие', width=250)
        self.list_note_orders.InsertColumn(4, 'Заказчик', width=200)
        self.list_note_orders.InsertColumn(5, 'Дата оформления', width=100)
        self.list_note_orders.InsertColumn(6, 'Дата сдачи', width=100)
        self.list_note_orders.InsertColumn(7, 'Стоимость', width=100)
        # заголовок тетради
        self.notebook_main.InsertPage(0, self.list_note_orders, "Текущие заказы")

# ------------------------------------------------------------------------------
        self.list_note_products = wx.ListCtrl(self.notebook_main, wx.ID_ANY,
                                              style=wx.LC_REPORT)
        self.list_note_products.SetFont(wx.Font(wx.FontInfo(12)))
        self.list_note_products.SetBackgroundColour("#f0f0f0")

        self.list_note_products.InsertColumn(0, '№', width=50)
        self.list_note_products.InsertColumn(1, 'ID', width=0)
        self.list_note_products.InsertColumn(2, 'Иконка', width=150)
        self.list_note_products.InsertColumn(3, 'Тип', width=150)
        self.list_note_products.InsertColumn(4, 'Модель', width=200)
        self.list_note_products.InsertColumn(5, 'Стоимость', width=150)
        # заголовок тетради
        self.notebook_main.InsertPage(1, self.list_note_products, "Изделия")
# ------------------------------------------------------------------------------

        self.box_notes = wx.BoxSizer()
        self.box_notes.Add(self.notebook_main, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.box_notes, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(self.sizer)
