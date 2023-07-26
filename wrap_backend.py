from weatherAPI import WeatherReport
from dall_E import Dall_Images
from shopping import serAPI
import time

#dallKey = os.environ.get("dall_key")
#weatherKey = os.environ.get("weather_key")

class Wrap_backend:

    def __init__(self, dall_key, weather_key, ser_key):
        self.dall_obj = Dall_Images(dall_key)
        self.weather_obj = WeatherReport(weather_key)
        self.serAPI_obj = serAPI(ser_key)

    def get_imageParams(self, location):
        week_params = []
        forecast = self.getForecast(location)
        for index in range(7):
            image_param = ""
            temp = forecast[index][0]
            rain_check = forecast[index][2]
            if (temp <= 40):
                image_param = " full body winter outfit in " + location +" at temperatures around " + str(temp) + " degrees"
            elif(temp >= 78.8):
                image_param = " full body  view summer outfit in " + location+ " at temperatures around " + str(temp) + " degrees"
            else:
                image_param = "full body spring outfit in " + location+ " at temperatures around " + str(temp) + " degrees"
            if (rain_check == True):
                image_param = image_param + " with an umbrella"
            week_params.append(image_param)
        return week_params

    def getForecast(self, location):
        return self.weather_obj.get_forecast(location)

    def get_imageList(self, gender, location):
        dall_input = self.get_imageParams(location)
        url_list = []
        for index in range(1):
            image_url = self.dall_obj.get_imageURL(gender + dall_input[index])
            time.sleep(10)
            url_list.append(image_url)
        #print(url_list[0])
        return url_list

    def get_shoppingResults(self, gender, location):
        queries = self.get_imageParams(location)
        shopping_results = []
        for index in range(7):
            query = gender + queries[index]
            result = self.serAPI_obj.get_shopping_info(query, location)
            shopping_results.append(result)
        return shopping_results


#test = Wrap_backend(dallKey, weatherKey)
#print(test.get_imageParams("porto alegre"))
#test.get_imageList("masculine" , "porto alegre")