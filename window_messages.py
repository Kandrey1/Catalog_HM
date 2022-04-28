import wx

caption_info = "Информация"
caption_error = "Ошибка"


def message_info_not_realized():
    """ Еще не реализовано """
    message = "Пока не реализовано, но мы стремимся к этому"
    wx.MessageBox(message, caption_info, wx.OK)


def message_error():
    """ Ошибки """
    message = "Что то пошло не по плану.\n Походу придется разбираться " \
              "в том кто все поломал"
    wx.MessageBox(message, caption_error, wx.OK)


def message_info_no_select_line():
    """ Строка в таблице не была выбрана """
    message = "Выберите строку в таблице."
    wx.MessageBox(message, caption_info, wx.OK)


def message_delete_record(parent):
    """ Проверка удаления записи """
    message = "Уверены что хотите удалить эту запись?"
    dlg = wx.MessageDialog(parent, message, caption_info, wx.YES_NO |
                           wx.NO_DEFAULT | wx.ICON_INFORMATION)
    res = dlg.ShowModal()
    if res == wx.ID_YES:
        parent.delete_row()
