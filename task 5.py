import requests
import json


# Задание 1

print(requests.get('https://api.github.com'))
print(requests.get('https://spb.hh.ru/'))


# Задание 2

id_key = '9624f063104d99a703ba671897a047b2'
url_weather = 'http://api.openweathermap.org/data/2.5/weather?'
city_name = input('Enter city name: ')

url_new = url_weather + 'appid=' + id_key + '&q=' + city_name
resp_weather = requests.get(url_new)

response_weather = resp_weather.json()

if resp_weather.status_code != 404:
    main_response_weather = response_weather['main']

    temperature = round(main_response_weather['temp'] - 273.15)
    pressure = main_response_weather['pressure']
    humidity = main_response_weather['humidity']
    weather_response = response_weather['weather']
    weather_description = weather_response[0]['description']

    print(f'Temperature: {temperature} °C')
    print(f'Atmospheric pressure: {pressure} hPa')
    print(f'Humidity: {humidity} %')
    print(f'Description: {weather_description}')

else:
    print('City not found')


# Задание 3

character_name = input('Enter the full name of the character: ')
url_character = 'https://rickandmortyapi.com/api/character/?name=' + str(character_name.lower())

resp_character = requests.get(url_character)
response_character = resp_character.json()

if resp_character.status_code != 404:
    main_response_character = response_character['results']

    name = main_response_character[0]['name']
    status = main_response_character[0]['status']
    species = main_response_character[0]['species']
    gender = main_response_character[0]['gender']
    origin = main_response_character[0]['origin']['name']

    print(f'Character name: {name}')
    print(f'Character status: {status}')
    print(f'Character species: {species}')
    print(f'Character gender: {gender}')
    print(f'Character origin: {origin}')

else:
    print('Character not found')
