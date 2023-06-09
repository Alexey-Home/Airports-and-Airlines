import sqlite3 as sq

path_db = "model/my_data_base.db"

def search_airpotrs(longitude_and_latitude):
    """
    :param longitude_and_latitude: Словарь введеных значений пользователем(максимальная, минимальная долгота и  широта)
    :return: найденные аэропорты из базы данных таблицы "Аэропорты" по введеным данным
    """

    data = (longitude_and_latitude["latitude_min"], longitude_and_latitude["latitude_max"],
            longitude_and_latitude["longitude_min"], longitude_and_latitude["longitude_max"])

    with sq.connect(path_db) as con:
        cur = con.cursor()

        cur.execute("SELECT city, country, latitude, longitude FROM airports "
                    "WHERE latitude BETWEEN ? AND ? AND longitude BETWEEN ? AND ?", data)

        result = cur.fetchall()
        cur.close()

    return result


def get_country():
    """
    Возвращает список стран в таблице 'Airlines
    '"""
    with sq.connect(path_db) as con:
        cur = con.cursor()
        cur.execute("SELECT country FROM airlines")

        result = cur.fetchall()
        cur.close()

    return sorted(set([i[0] for i in result]))


def get_airlines(data):
    """
    :param data Страна для поиска авиакомпаний
    Возвращает список авиакомпаний в выбранной стране
    """
    with sq.connect(path_db) as con:
        cur = con.cursor()

        cur.execute("SELECT name FROM airlines "
                    "WHERE country = ?", data)

        result = cur.fetchall()
        cur.close()

    return result





