import tkinter as tk
from tkinter import ttk
import model.functions as func
import ui.info as info


class CoordinatesAirports(object):
    def __init__(self, parent):
        """Создает поля для ввода параметров для поиска аэропортов"""
        self.myParent = parent
        self.main_frame = tk.Frame(parent)
        self.main_frame.pack()
        self.info = info.Info()

        self.info_frame = tk.Frame(self.main_frame)
        self.info_frame.pack(side="top",  anchor="e")

        self.information = tk.Label(self.info_frame, text=self.info.search_airports, justify="left")
        self.information.pack(side="top",  anchor="e")

        self.coordinate_frame = tk.Frame(self.main_frame)
        self.coordinate_frame.pack(side="top")

        self.lbl_lat_min = tk.Label(self.coordinate_frame, text=self.info.title_filed["min_lat"])
        self.lbl_lat_min.grid(column=0, row=0)

        self.latitude_min = tk.Entry(self.coordinate_frame)
        self.latitude_min.grid(column=1, row=0)
        self.latitude_min.insert(0, "0")

        self.lbl_lat_max = tk.Label(self.coordinate_frame, text=self.info.title_filed["max_lat"])
        self.lbl_lat_max.grid(column=2, row=0)

        self.latitude_max = tk.Entry(self.coordinate_frame)
        self.latitude_max.grid(column=3, row=0)
        self.latitude_max.insert(0, "0")

        self.lbl_lon_min = tk.Label(self.coordinate_frame, text=self.info.title_filed["min_lon"])
        self.lbl_lon_min.grid(column=0, row=1)

        self.longitude_min = tk.Entry(self.coordinate_frame)
        self.longitude_min.grid(column=1, row=1)
        self.longitude_min.insert(0, "0")

        self.lbl_lat_max = tk.Label(self.coordinate_frame, text=self.info.title_filed["max_lon"])
        self.lbl_lat_max.grid(column=2, row=1)

        self.longitude_max = tk.Entry(self.coordinate_frame)
        self.longitude_max.grid(column=3, row=1)
        self.longitude_max.insert(0, "0")


class Country:
    def __init__(self, parent):
        self.myParent = parent
        self.main_frame = tk.Frame(parent)
        self.main_frame.pack()
        self.info = info.Info()

        self.info_frame = tk.Frame(self.main_frame)
        self.info_frame.pack(side="top",  anchor="e")

        self.information = tk.Label(self.info_frame, text=self.info.search_airlines, justify="left")
        self.information.pack(side="top",  anchor="e")

        self.country_frame = tk.Frame(self.main_frame)
        self.country_frame.pack(side="top")

        self.lbl = tk.Label(self.country_frame, text=self.info.title_column["country"])
        self.lbl.grid(column=0, row=0)

        self.lst_country = ttk.Combobox(self.country_frame, values=func.get_country())
        self.lst_country.grid(column=0, row=1)


class Show:
    __instance = None  # ссылка на экземпляр класса

    def __new__(cls, *args, **kwargs):
        """Не дает возможность создавать больше одного экземпляра,
        возввращает ссылку на класс, если такой существует."""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        """Обнуляет ссылку на класс при удалении"""
        Show.__instance = None

    def __init__(self, parent, flag, result, message):
        self.myParent = parent
        self.flag = flag
        self.result = result
        self.message = message
        self.info = info.Info()

        self.destroy()

        self.main_frame = tk.Frame(parent)
        self.main_frame.pack()

        if flag and len(self.result) != 0:
            self.show_result()
        elif len(self.result) == 0:
            self.message = self.info.errors["empty_result"]
            self.show_error()
        else:
            self.show_error()

    def show_result(self):
        """Создает рамку и выводит последовательно найденные аэропорты"""
        if self.flag:
            self.length_row = len(self.result)
            self.length_column = len(self.result[0])

            # Создается scrollbar для большого списка
            self.frame = tk.Canvas(self.main_frame, width=500)
            self.scrollbar = tk.Scrollbar(self.main_frame, command=self.frame.yview)
            self.frame.config(yscrollcommand=self.scrollbar.set)
            self.scrollbar.grid(row=0, column=5, sticky="ns")
            self.frame.grid(row=0, column=0)

            self.view_frame = tk.Frame(self.frame)
            self.frame.create_window((0, 0), window=self.view_frame, anchor="nw")

            def conf(event):
                self.frame.configure(scrollregion=self.frame.bbox('all'))

            self.frame.bind('<Configure>', conf)

            # выводит найденые результаты
            for index in range(self.length_row):
                for col in range(self.length_column):
                    self.country = tk.Entry(self.view_frame)
                    self.country.grid(column=col, row=index + 1)
                    self.country.insert(0, self.result[index][col])

    def show_error(self):
        """Показывает ошибку, если данные введены некорректно"""
        self.main_frame = tk.Frame(self.myParent)
        self.main_frame.pack()

        self.lbl = tk.Label(self.main_frame, text=self.message)
        self.lbl.grid(column=0, row=0)

    def destroy(self):
        """Удаляет главную рамку, если такая имеется"""
        try:
            self.main_frame.destroy()
        except AttributeError:
            pass



