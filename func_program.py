import window_messages


def renumber_data_for_set(data):
    """ Получает строки данных из талицы в БД, нумерует их и возвращает
        пронумерованные строки
    """
    data_transform = []
    rows = enumerate(data, 1)
    for row in rows:
        data_temp = [row[0]]
        data_temp.extend(row[1])
        data_transform.append(data_temp)
    return data_transform


def get_id_focus_line(table):
    """ Возвращает id выделенной строки """
    focus_line = table.GetFocusedItem()
    if not focus_line == -1:
        item_line = table.GetItem(focus_line, col=1)
        id_focus = int(item_line.GetText())
        return id_focus
    else:
        window_messages.message_info_no_select_line()
        return -1


def set_cursor_end_table(table):
    """ Ставит курсор и подсвечивает последнюю запись в таблице"""
    count = table.GetItemCount()
    table.Focus(count - 1)
    table.Select(count - 1)
