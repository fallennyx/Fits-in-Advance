import requests
import os

#url accepts ip as well as other inputs for location


class WeatherReport:
    def __init__(self, Api_key):
        self.api_key = Api_key
    
    def get_forecast(self, location):
        #location = 'porto alegre'
        week_forecast = []
        response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={location}&days=7&aqi=no&alerts=no')
        weather = response.json()
        for index in range(7):
            #index is the day number, in this case 0 is today
            day_forecast = []
            temp = weather["forecast"]["forecastday"][index]["day"]["avgtemp_f"]
            condition = weather["forecast"]["forecastday"][index]["day"]["condition"]["text"]
            rain_check = weather["forecast"]["forecastday"][index]["day"]["daily_will_it_rain"] #returns a bool for a rain check
            day_forecast.append(temp)
            day_forecast.append(condition)
            day_forecast.append(rain_check)
            week_forecast.append(day_forecast)
        return week_forecast #returns a list of lists, where each element is a day with climate, temperature and rain check

#test = WeatherReport(key)
#print(test.get_forecast(1))
