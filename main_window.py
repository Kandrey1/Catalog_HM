import wx

import settings
from main_panel import MainPanel
from main_menu_bar import MenuBar
from main_toolbar import MainToolbar


class MainWindow(wx.Frame):
    """ Основное окно программы """
    def __init__(self, parent, title):
        width = settings.width_main_window
        height = settings.height_main_window

        super().__init__(parent, title=title, size=(width, height))

        self.SetMenuBar(MenuBar(self))
        self.ToolBar = MainToolbar(self)

        self.status = self.CreateStatusBar()
#        self.status.SetStatusText("Текст в статусной строке")

        self.panel = MainPanel(self)

        sizer = wx.BoxSizer()
        sizer.Add(self.panel, 1, wx.EXPAND | wx.ALL, 0)
        self.SetSizer(sizer)

        self.Centre()

        self.Bind(wx.EVT_CLOSE, self.check_quit)

    def on_quit_program(self):
        """ Закрывает программу """
        self.Destroy()

    def check_quit(self, event):
        """ Вызывает подтверждение закрытия программы, по нажатию 'Х' """
        self.message_close_program()

    def message_close_program(self):
        """ Проверка закрытия программы """
        message = "Вы действительно хотите закрыть программу?"
        caption_close = "Подтверждение закрытия"
        dlg = wx.MessageDialog(self, message, caption_close,
                               wx.YES_NO | wx.NO_DEFAULT | wx.ICON_INFORMATION)
        res = dlg.ShowModal()
        if res == wx.ID_YES:
            self.on_quit_program()
