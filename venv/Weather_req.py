import requests 

city = input('Which city do you want the weather info from ?')
url ='http://api.weatherapi.com/v1/current.json?key=5a3c1af145b1411e9cf210101222402&q='+ city +'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_c')
description =weather_json.get('current').get('condition').get('text')

print("Today's weather in", city,"is", description, "and", temp, 'degrees')