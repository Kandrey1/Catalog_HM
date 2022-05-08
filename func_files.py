import os
import shutil
import wx
from PIL import Image

import settings

path_data_image = settings.path_data_image


class File:
    """ Класс методов для работы с файлами изображения """
    @staticmethod
    def path_file(parent):
        """ Возвращает полный путь выбранного файла """
        with wx.FileDialog(parent, "Выбрать изображение для аватарки",
                           wildcard="Изображения (*.BMP,JPG,JPEG,PNG)|*.BMP;*.JPG;*.JPEG;*.PNG",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as file:
            if file.ShowModal() == wx.ID_CANCEL:
                return
            pathname = file.GetPath()
            return pathname

    @staticmethod
    def get_dir_path(path):
        """ Разбивает полученный путь файла. Возвращает пук к файлу """
        return os.path.split(path)[0]

    @staticmethod
    def get_name_file(path):
        """ Разбивает полученный путь файла. Возвращает имя файла """
        return os.path.split(path)[1]

    @staticmethod
    def create_dir(new_path):
        """ Создает папку """
        os.mkdir(new_path)

    @staticmethod
    def delete_dir_with_files(path):
        """ Удаляет папку со всеми файлами """
        shutil.rmtree(path)

    @staticmethod
    def copy_file(path_from, path_in):
        """ Копирует файл """
        shutil.copyfile(path_from, path_in)

    @staticmethod
    def copy_dir_with_files(path_from, path_in):
        """ Копирует папку с файлами """
        shutil.copy(path_from, path_in)

    @staticmethod
    def create_new_dir_product(id_product):
        """ Создает новую папку с именем = id_product """
        path_dir_product = path_data_image + str(id_product) + "\\"
        File.create_dir(path_dir_product)

    @staticmethod
    def get_path_miniature_product(id_prod):
        """ Получить путь к миниатюре изделия """
        path_miniature = path_data_image + str(id_prod) + "\\" +"mini_" + str(id_prod) + ".jpg"
        return path_miniature

    @staticmethod
    def exist_file_miniature(path_file):
        """ Проверяет, существует ли файл миниатюры изделия """
        return os.path.isfile(path_file)


class ConvertImages:
    """ Класс методов для редактирования изображения """
    @staticmethod
    def resize_image(image, max_size):
        """ Возвращает уменьшенное изображение полученного image """
        width, height = image.size
        if width > height:
            new_width = max_size
            new_height = int(new_width * height / width)
        else:
            new_height = max_size
            new_width = int(new_height * width / height)
        image_resize = image.resize((new_width, new_height), Image.LANCZOS)
        return image_resize

    @staticmethod
    def resize_mini_pic_product(path_open):
        """ Возвращает miniature вариант image """
        image = Image.open(path_open)
        image_mini_pic = ConvertImages.resize_image(image, 140)
        return image_mini_pic

    @staticmethod
    def save_image(img, path_save):
        """ Сохраняет полученное изображение, в path_save """
        img.save(path_save)
