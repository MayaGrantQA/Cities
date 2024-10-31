from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser  # Для открытия ссылки в браузере


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            # Округляем до 2-х знаков после запятой
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']  # Берем эти параметры из json
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}"

            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {"coordinates": f"Широта: {lat},\n Долгота: {lon},\n Страна: {country}.\n Регион: {region}",
                        "map_url": osm_url}
            else:
                return {"coordinates": f"Широта: {lat},\n Долгота: {lon},\n Страна: {country}",
                        "map_url": osm_url}

        return 'Город не найден'
    except Exception as e:
        return f"Возникла ошибка: {e}"


def show_coordinates(event=None):
    global map_url
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text=f'Координаты города {city}:\n {result['coordinates']}')
    map_url = result['map_url']


def show_map():
    if map_url:
        webbrowser.open(map_url)


key = 'df1c31b2072f453d9c74c8d1ffec8900'
map_url = ''

window = Tk()
window.title('Координаты городов')
window.geometry('320x160')
entry = Entry()
entry.pack()
entry.focus_set()
entry.bind('<Return>', show_coordinates)

button = Button(text='Поиск координат', command=show_coordinates)
button.pack()

label = Label(text='Введите город и нажмите на кнопку')
label.pack()

map_button = Button(text='Показать карту', command=show_map)
map_button.pack()

window.mainloop()