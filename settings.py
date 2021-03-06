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
                                        " phone, email, address, vkontakte",
                             "col_search": {"фамилия": "last_name",
                                            "имя": "first_name",
                                            "отчество": "middle_name",
                                            "телефон": "phone",
                                            "почта": "email",
                                            "адрес": "address",
                                            "вконтакте": "vkontakte",
                                            }
                             },
                        "materials":
                            {"table": "materials",
                             "pk": "id_material",
                             "columns": "name, unit, vendor",
                             "col_search": {"материал": "name",
                                            "поставщик": "vendor"}
                             },
                        "components":
                            {"table": "components",
                             "pk": "id_component",
                             "columns": "product_id, material_id, number, "
                                        "price_one"
                             },
                        "products":
                            {"table": "products",
                             "pk": "id_product",
                             "columns": "path_ico, type_prod, model, price, "
                                        "number, about, size_width, "
                                        "size_height, size_depth, weigh",
                             "col_search": {"тип": "type_prod",
                                            "модель": "model",
                                            "описание": "about",
                                            }
                             }
                        }
