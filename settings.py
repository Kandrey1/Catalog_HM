"""
    Настройки программы
"""
width_main_window = 1200
height_main_window = 500

path_database = "data\\database\\catalog_hm.db"
path_data_image = "data\\image\\"

path_sys_image = "sys\\image\\"
path_sys_image_default = "sys\\image\\default_pic.jpg"

size_button_small = (120, 20)
size_button_medium = (120, 30)
size_button_large = (140, 40)

dict_tables_database = {"customers":
                            {"table": "customers",
                             "pk": "id_customer",
                             "columns": "last_name, first_name, middle_name,"
                                        " phone, email, address, vkontakte"
                             },
                        "materials":
                            {"table": "materials",
                             "pk": "id_material",
                             "columns": "name, unit, vendor"
                             },
                        "products":
                            {"table": "products",
                             "pk": "id_product",
                             "columns": "path_ico, type_prod, model, price, "
                                        "number, about, size_width, "
                                        "size_height, size_depth, weigh"
                             }
                        }
