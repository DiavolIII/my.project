import requests

def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def display_weather(data):
    if data:
        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        print(f'Погода в {city}:')
        print(f'Температура: {temp}°C')
        print(f'Влажность: {humidity}%')
        print(f'Состояние: {weather_desc}')
        print(f'Скорость ветра: {wind_speed} м/с')
    else:
        print('Ошибка: Не удалось получить данные о погоде.')

def main():
    api_key = 'YOUR_API_KEY'  # Замените на ваш API-ключ OpenWeatherMap
    city = input('Введите название города: ')

    weather_data = get_weather(city, api_key)
    display_weather(weather_data)


if __name__ == '__main__':
    main()