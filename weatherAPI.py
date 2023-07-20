import requests
import os
key = os.environ.get("weather_key")

#url accepts ip as well as other inputs for location


class WeatherReport:
    def __init__(self, Api_key):
        self.api_key = Api_key
    
    def get_forecast(self, location):
        location = 'porto alegre'
        week_forecast = {}
        response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={location}&days=7&aqi=no&alerts=no')
        weather = response.json()
        for index in range(7):
            #index is the day number, in this case 0 is today
            temp = weather["forecast"]["forecastday"][index]["day"]["avgtemp_f"]
            condition = weather["forecast"]["forecastday"][index]["day"]["condition"]["text"]
            week_forecast[temp] = condition
        return week_forecast

test = WeatherReport(key)
print(test.get_forecast(1))
