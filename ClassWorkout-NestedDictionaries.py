Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> d={}
>>> 
>>> d['list']=list()
>>> d
{'list': []}
>>> 
>>> d['diction']={}
>>> 
>>> d
{'list': [], 'diction': {}}
>>> 
>>> 
>>> # Nested dictionaries
>>> s={
...   "city": {
...     "id": 1253184,
...     "name": "Vijayawada",
...     "coord": {
...       "lon": 80.6167,
...       "lat": 16.5167
...     },
...     "country": "IN",
...     "population": 874587,
    "timezone": 19800
  }}

s
{'city': {'id': 1253184, 'name': 'Vijayawada', 'coord': {'lon': 80.6167, 'lat': 16.5167}, 'country': 'IN', 'population': 874587, 'timezone': 19800}}

# pprint - prettyprint

import pprint
pprint.pprint(s)
{'city': {'coord': {'lat': 16.5167, 'lon': 80.6167},
          'country': 'IN',
          'id': 1253184,
          'name': 'Vijayawada',
          'population': 874587,
          'timezone': 19800}}


s['city']
{'id': 1253184, 'name': 'Vijayawada', 'coord': {'lon': 80.6167, 'lat': 16.5167}, 'country': 'IN', 'population': 874587, 'timezone': 19800}


from pprint import pprint as pp

pp(s['city'])
{'coord': {'lat': 16.5167, 'lon': 80.6167},
 'country': 'IN',
 'id': 1253184,
 'name': 'Vijayawada',
 'population': 874587,
 'timezone': 19800}
s['city']
{'id': 1253184, 'name': 'Vijayawada', 'coord': {'lon': 80.6167, 'lat': 16.5167}, 'country': 'IN', 'population': 874587, 'timezone': 19800}

type(s['city'])
<class 'dict'>


s['city'].get('id')
1253184

s['city'].get('coord')
{'lon': 80.6167, 'lat': 16.5167}
s['city'].get('coord').get('lat')
16.5167




s.keys()
dict_keys(['city'])


s.values()
dict_values([{'id': 1253184, 'name': 'Vijayawada', 'coord': {'lon': 80.6167, 'lat': 16.5167}, 'country': 'IN', 'population': 874587, 'timezone': 19800}])



{
      "dt": 1748241000,
      "sunrise": 1748217881,
      "sunset": 1748264687,
      "temp": {
        "day": 30.94,
        "min": 26.74,
        "max": 32.53,
        "night": 28.33,
        "eve": 27,
        "morn": 28.03
      },
      "feels_like": {
        "day": 37.14,
        "night": 31.47,
        "eve": 27.8,
        "morn": 31.28
      },
      "pressure": 1002,
      "humidity": 69,
      "weather": [
        {
          "id": 501,
          "main": "Rain",
          "description": "moderate rain",
          "icon": "10d"
        }
      ],
      "speed": 4.9,
      "deg": 234,
      "gust": 9.83,
      "clouds": 62,
      "pop": 1,
      "rain": 1.65
    }
{'dt': 1748241000, 'sunrise': 1748217881, 'sunset': 1748264687, 'temp': {'day': 30.94, 'min': 26.74, 'max': 32.53, 'night': 28.33, 'eve': 27, 'morn': 28.03}, 'feels_like': {'day': 37.14, 'night': 31.47, 'eve': 27.8, 'morn': 31.28}, 'pressure': 1002, 'humidity': 69, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'speed': 4.9, 'deg': 234, 'gust': 9.83, 'clouds': 62, 'pop': 1, 'rain': 1.65}


