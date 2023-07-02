import requests

cities = ['london', 'svo', 'cherepovets']

local_params_ru = {
    'nTqmM': '',
    'lang': 'ru',
    }

url_template = 'https://wttr.in/{}'

for city in cities:
    url = url_template.format(city)

    response = requests.get(url, params=local_params_ru)
    response.raise_for_status()

    print(response.text)