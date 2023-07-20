#!!to use this file you must install openai: pip3 install openai!!
#image sizes: 1024x1024, 512x512, 256x256  ->> smaller = less expensive
import os 
import openai
import requests
from weatherAPI import WeatherReport

class Dall_Images:
    def __init__(self, Api_key):
        openai.api_key = Api_key
    
    def get_imageURL(self, promptInput):
        image = openai.Image.create(prompt = promptInput, n = 1, size = "256x256") #var image is a dictionary with the url's
        return image["data"][0]["url"] #Returns a string with the url

#test = Dall_Images('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')
#print(test.get_imageURL("feminine spring outfit"))
