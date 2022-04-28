import wx

from customer_add import DialogAddCustomer
from customers_window_db import DialogAllCustomers


class MenuBar(wx.MenuBar):
	""" Создание главного меню приложения """
	def __init__(self, parent, *args, **kwargs):
		super(MenuBar, self).__init__(*args, **kwargs)

		self.parent = parent
#   ----------------------------- Меню -----------------------------------------
		self.main_menu = wx.Menu()
		self.menu_settings = wx.MenuItem(self.main_menu, wx.ID_ANY, 'Настройки')
		self.main_menu.Append(self.menu_settings)
		self.main_menu.AppendSeparator()
		self.menu_exit = wx.MenuItem(self.main_menu, wx.ID_ANY, 'Выход')
		self.main_menu.Append(self.menu_exit)
		self.Append(self.main_menu, "Меню")

		self.Bind(wx.EVT_MENU, self.on_quit, self.menu_exit)
#   ----------------------------- Меню -----------------------------------------
#   ----------------------------- Клиенты --------------------------------------
		self.customers_menu = wx.Menu()
		self.customer_add = wx.MenuItem(self.customers_menu, wx.ID_ANY, 'Добавить')
		self.customers_menu.Append(self.customer_add)
		self.customers_all = wx.MenuItem(self.customers_menu, wx.ID_ANY, 'Все клиенты')
		self.customers_menu.Append(self.customers_all)
		self.Append(self.customers_menu, "&Клиенты")

		self.Bind(wx.EVT_MENU, self.on_customer_add, self.customer_add)
		self.Bind(wx.EVT_MENU, self.on_customers_all, self.customers_all)
#   ----------------------------- Клиенты --------------------------------------
#   ----------------------------- Товары ---------------------------------------
		self.products_menu = wx.Menu()
		self.material_add = wx.MenuItem(self.products_menu, wx.ID_ANY, 'Добавить материал')
		self.products_menu.Append(self.material_add)
		self.materials_all = wx.MenuItem(self.products_menu, wx.ID_ANY, 'Все материалы')
		self.products_menu.Append(self.materials_all)
		self.products_menu.AppendSeparator()
		self.product_add = wx.MenuItem(self.products_menu, wx.ID_ANY, 'Добавить товар')
		self.products_menu.Append(self.product_add)
		self.products_all = wx.MenuItem(self.products_menu, wx.ID_ANY, 'Все товары')
		self.products_menu.Append(self.products_all)
		self.Append(self.products_menu, "Товары")
#   ----------------------------- Товары ---------------------------------------
#   ----------------------------- Помощь ---------------------------------------
		self.help_menu = wx.Menu()
		self.about = wx.MenuItem(self.products_menu, wx.ID_ANY, 'О программе')
		self.help_menu.Append(self.about)
		self.help = wx.MenuItem(self.products_menu, wx.ID_ANY, 'Помощь')
		self.help_menu.Append(self.help)
		self.version = wx.MenuItem(self.products_menu, wx.ID_ANY, 'Версия')
		self.help_menu.Append(self.version)
		self.Append(self.help_menu, "Помощь")
#   ----------------------------- Помощь ---------------------------------------

	def on_quit(self, event):
		""" Закрывает программу """
		self.parent.message_close_program()

	def on_customer_add(self, event):
		""" Добавляет клиента """
		dlg = DialogAddCustomer(self.parent, title="Добавление нового клиента")
		dlg.ShowModal()
		dlg.Destroy()

	def on_customers_all(self, event):
		""" Окно всех клиентов в БД """
		dlg = DialogAllCustomers(self.parent)
		dlg.ShowModal()
		dlg.Destroy()


