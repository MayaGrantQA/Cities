from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            # Округляем до 2-х знаков после запятой
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            return lat, lon
        else:
            return 'Город не найден'
    except Exception as e:
        return f"Общая ошибка: {e}"


key = 'df1c31b2072f453d9c74c8d1ffec8900'
city = 'Химки'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')