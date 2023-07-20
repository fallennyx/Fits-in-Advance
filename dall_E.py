#!!to use this file you must install openai: pip3 install openai!!
#image sizes: 1024x1024, 512x512, 256x256  ->> smaller = less expensive
import os 
import openai
import requests

class Dall_Images:
    def __init__(self, Api_key):
        openai.api_key = Api_key
    #i can change this function so it sends an array with the url's in case we're going to have more than 1 image
    def get_imageURL(self, promptInput, image_num):
        image = openai.Image.create(prompt = promptInput, n = image_num, size = "256x256") #var image is a dictionary with the url's
        return image["data"][0]["url"] #Returns a string with the url