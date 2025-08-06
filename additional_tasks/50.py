'''
Additional task 50

'''

# import requests
# import json
#
# def get_weather(city_name, api_key='227f19477ba9ffb549c0681602ca7c51'):
#     base_url = "https://api.openweathermap.org/data/2.5/weather"
#     params = {
#         'q': city_name,
#         'appid': api_key,
#         'units': 'metric',  # температура в Цельсіях
#         'lang': 'ua'        # українська мова
#     }
#
#     response = requests.get(base_url, params=params)
#
#     if response.status_code == 200:
#         data = response.json()
#         temp = data['main']['temp']
#         weather_desc = data['weather'][0]['description']
#         humidity = data['main']['humidity']
#         wind_speed = data['wind']['speed']
#         print(f"🌤 Погода в місті {city_name}:")
#         print(f"Температура: {temp}°C")
#         print(f"Опис: {weather_desc}")
#         print(f"Вологість: {humidity}%")
#         print(f"Швидкість вітру: {wind_speed} м/с")
#     else:
#         print(f"❌ Не вдалося отримати дані. Код помилки: {response.status_code}")
#
# # ==== Використання ====
# # API_KEY = "227f19477ba9ffb549c0681602ca7c51"  # <-- встав сюди свій ключ
# city = input("Введіть назву міста: ")
# get_weather(city)