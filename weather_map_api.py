import requests

api_key = "c69ab9c9561b2cbf754c801a93c2929a"
city = "Orlando"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()

description = json.get("weather")[0].get("description")
print(description)
min_temp = json.get("main").get("min_temp")
print(min_temp)
max_temp = json.get("main").get("max_temp")
print(max_temp)