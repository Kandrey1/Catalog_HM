import func_database
import window_messages


def get_id_focus_line(table, column_id=1):
    """ Возвращает id выделенной строки """
    focus_line = table.GetFocusedItem()
    if not focus_line == -1:
        item_line = table.GetItem(focus_line, col=column_id)
        id_focus = int(item_line.GetText())
        return id_focus
    else:
        window_messages.message_info_no_select_line()
        return -1


def set_data_in_table(name_db, table, data=None):
    """ Устанавливает полученные записи в таблицу. Если данные не
        передавались(по умолчанию) запрашивает данные из БД """
    rows = data if data else func_database.get_numeric_all_rows(name_db)
    for row in rows:
        table.Append(row)


def refresh_data_in_table(name_db, table):
    """ Обновляет данные в таблице """
    table.DeleteAllItems()
    set_data_in_table(name_db, table)


def set_cursor_end_table(table):
    """ Ставит курсор и подсвечивает последнюю запись в таблице """
    count = table.GetItemCount()
    table.Focus(count - 1)
    table.Select(count - 1)


def start_window(dlg):
    """ Запускает окно и уничтожает после закрытия """
    dlg.ShowModal()
    dlg.Destroy()
