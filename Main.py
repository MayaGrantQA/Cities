from opencage.geocoder import OpenCageGeocode
from tkinter import *


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            # Округляем до 2-х знаков после запятой
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']  # Берем эти параметры из json

            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return f"Широта: {lat},\n Долгота: {lon},\n Страна: {country}.\n Регион: {region}"
            else:
                return f"Широта: {lat},\n Долгота: {lon},\n Страна: {country}"

        return 'Город не найден'
    except Exception as e:
        return f"Возникла ошибка: {e}"


def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f'Координаты города {city}:\n {coordinates}')


key = 'df1c31b2072f453d9c74c8d1ffec8900'

window = Tk()
window.title('Координаты городов')
window.geometry('300x150')
entry = Entry()
entry.pack()
entry.focus_set()
entry.bind('<Return>', show_coordinates)

button = Button(text='Поиск координат', command=show_coordinates)
button.pack()

label = Label(text='Введите город и нажмите на кнопку')
label.pack()

window.mainloop()