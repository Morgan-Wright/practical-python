import requests


def get_weather_temp():
    api_key = "c69ab9c9561b2cbf754c801a93c2929a"
    city = "Philadelphia"
    url = "http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API}&units=imperial".format(city_name = city, API = api_key)

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    min_temp = json.get("main").get("min_temp")
    max_temp = json.get("main").get("max_temp")
    return {'description': description, 
            'min_temp': min_temp,
            'max_temp': max_temp
            }

def main():
    weather_dict = get_weather_temp()
    print(weather_dict.get('description'))
    print(weather_dict.get('min_temp'))
    print(weather_dict.get('max_temp'))

main()