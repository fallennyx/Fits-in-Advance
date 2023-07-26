from weatherAPI import WeatherReport
from dall_E import Dall_Images
import time

class Wrap_backend:
    
    def __init__(self, dall_key, weather_key):
        self.dall_obj = Dall_Images(dall_key)
        self.weather_obj = WeatherReport(weather_key)

    def get_imageParams(self, location, startDay):
        week_params = []
        forecast = self.weather_obj.get_forecast(location)
        for index in range(startDay, min(startDay + 5, len(forecast))):
            image_param = ""
            temp = forecast[index][0]
            rain_check = forecast[index][2] 
            if (temp <= 62):
                image_param = " winter outfit"
            elif(temp >= 78.8):
                image_param = " summer outfit"
            else:
                image_param = " spring outfit"
            if (rain_check == True):
                image_param = image_param + " with an umbrella"
            week_params.append(image_param)
        return week_params


    def getForecast(self, location, startDay):
        forecast = self.weather_obj.get_forecast(location)
        return forecast[startDay:min(startDay+5, len(forecast))]

    def get_imageList(self, gender, location, startDay):
        dall_input = self.get_imageParams(location, startDay)
        url_list = []
        for index in range(min(5, len(dall_input))):
            image_url = self.dall_obj.get_imageURL(gender + dall_input[index])
            print(f"Day {startDay + index + 1}: {image_url}")
            url_list.append(image_url)
        return url_list
