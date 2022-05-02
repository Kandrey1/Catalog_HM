import wx
import settings
import window_messages
from customer_add import DialogAddCustomer
from customers_window_db import DialogAllCustomers
from product_add import DialogAddProduct
from product_window_db import DialogAllProducts


class MainToolbar(wx.ToolBar):
    """ Создание toolbar """
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.path_ico = settings.path_sys_image

        self.AddSeparator()
        self.product_add = self.AddTool(wx.ID_ANY, "",
                               wx.Bitmap(self.path_ico + "product_add.png"))
        self.products_all = self.AddTool(wx.ID_ANY, "",
                               wx.Bitmap(self.path_ico + "product_all.png"))
        self.AddSeparator()
        self.AddSeparator()
        self.customer_add = self.AddTool(wx.ID_ANY, "",
                               wx.Bitmap(self.path_ico + "customer_add.png"))
        self.customers_all = self.AddTool(wx.ID_ANY, "",
                               wx.Bitmap(self.path_ico + "customer_all.png"))
        self.AddSeparator()
        self.AddSeparator()
        self.AddSeparator()
        self.AddSeparator()
        self.AddSeparator()
        self.AddSeparator()
        self.bar_test_one = self.AddTool(wx.ID_ANY, "",
                                         wx.Bitmap(self.path_ico + "test1.png"))

        self.Bind(wx.EVT_TOOL, self.on_add_customer, self.customer_add)
        self.Bind(wx.EVT_TOOL, self.on_all_customers, self.customers_all)

        self.Bind(wx.EVT_TOOL, self.on_add_product, self.product_add)
        self.Bind(wx.EVT_TOOL, self.on_all_products, self.products_all)

        self.Bind(wx.EVT_TOOL, self.on_test, self.bar_test_one)

        self.Realize()

    def on_quit(self, event):
        """ Закрывает программу """
        self.parent.message_close_program()

    def on_add_product(self, event):
        """ Вызывает окно добавления нового изделия """
        dlg = DialogAddProduct(self.parent, title="Добавление нового изделия")
        dlg.ShowModal()
        dlg.Destroy()

    def on_all_products(self, event):
        """ Вызывает окно всех изделий в БД """
        dlg = DialogAllProducts(self.parent)
        dlg.ShowModal()
        dlg.Destroy()

    def on_add_customer(self, event):
        """ Вызывает окно добавления нового клиента """
        dlg = DialogAddCustomer(self.parent, title="Добавление нового клиента")
        dlg.ShowModal()
        dlg.Destroy()

    def on_all_customers(self, event):
        """ Вызывает окно всех клиентов в БД """
        dlg = DialogAllCustomers(self.parent)
        dlg.ShowModal()
        dlg.Destroy()

    def on_test(self, event):
        """ Кнопка тест """
        window_messages.message_info_not_realized()
