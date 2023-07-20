from weatherAPI import WeatherReport
from dall_E import Dall_Images
import time

#dallKey = os.environ.get("dall_key")
#weatherKey = os.environ.get("weather_key")

class Wrap_backend:
    
    def __init__(self, dall_key, weather_key):
        self.dall_obj = Dall_Images(dall_key)
        self.weather_obj = WeatherReport(weather_key)

    def get_imageParams(self, location):
        week_params = []
        forecast = self.weather_obj.get_forecast(location)
        for index in range(7):
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

    def get_imageList(self, gender, location):
        dall_input = self.get_imageParams(location)
        url_list = []
        for index in range(1):
            image_url = self.dall_obj.get_imageURL(gender + dall_input[index])
            time.sleep(10)
            url_list.append(image_url)
        #print(url_list[0])

#test = Wrap_backend(dallKey, weatherKey)
#print(test.get_imageParams("porto alegre"))
#test.get_imageList("masculine" , "porto alegre")