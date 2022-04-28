import wx

from main_window import MainWindow

app = wx.App()
frame = MainWindow(None, "Каталог рукодельника")
frame.Show()
app.MainLoop()
