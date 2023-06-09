from ui.ui import *
from ui.info import Info
from model.functions import *


class ControllerAirports(CoordinatesAirports):
    def __init__(self, parent):
        super().__init__(parent)
        self.myParent = parent
        self.info = Info()

        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.pack(side="top")

        self.button = tk.Button(self.buttons_frame, text=self.info.title_buttons["search_but"],
                                command=self.search_and_view_airpotrs)
        self.button.grid(column=0, row=3)


    def search_and_view_airpotrs(self):
        """При нажатии кнопки, приимает введеные параметры, проверяет корректность введеных данных, и выводит результат"""
        longitude_and_latitude = {
            "latitude_max": self.latitude_max.get(),
            "latitude_min": self.latitude_min.get(),
            "longitude_max": self.longitude_max.get(),
            "longitude_min": self.longitude_min.get(),
        }
        flag, message, result = self.check_data(longitude_and_latitude)

        if flag:
            result = search_airpotrs(longitude_and_latitude)

        viewer = Show(self.myParent, flag, result, message)


    def check_data(self, data):
        """Проверка на корректность введеных данных"""
        try:
            for key, value in data.items():
                data[key] = float(value)
        except ValueError:
            return False, self.info.errors["valueError"], data
        if data["latitude_max"] < data["latitude_min"]:
            return False, self.info.errors["moreLessLat"], data
        if data["longitude_max"] < data["longitude_min"]:
            return False, self.info.errors["moreLessLon"], data

        return True, None, data


class ControllerAirlines(Country):
    def __init__(self, parent):
        super().__init__(parent)
        self.myParent = parent
        self.info = Info()

        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.pack(side="top")

        self.button = tk.Button(self.buttons_frame, text=self.info.title_buttons["search_but"],
                                command=self.search_and_view_airlines)
        self.button.grid(column=0, row=3)


    def search_and_view_airlines(self):
        """
        При нажатии кнопки, принимает страну для поиска, ищет и выводит название авиакомпаний страны
        :return:
        """
        country = self.lst_country.get()

        result = get_airlines([country])

        if len(result) != 0:
            flag = True
            message = None
        else:
            flag = False
            message = self.info.errors['empty_result']

        viewer = Show(self.myParent, flag, result, message)




