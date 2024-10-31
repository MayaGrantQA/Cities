from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return 'Город не найден'


key = 'df1c31b2072f453d9c74c8d1ffec8900'
city = 'Ростов-на-Дону'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')