from flask import Blueprint, jsonify, request

from wrap_backend import Wrap_backend

data = Blueprint('data', __name__)

wrap_obj = Wrap_backend('dall-e', ' weather',"serp" )

def get_outfits(gender, location, startDay):
    outfits = wrap_obj.get_imageList(gender, location, startDay) #returns a list with strings inside each one being a url a picture
    return outfits

def get_forecast(location, startDay):
    forecast = wrap_obj.getForecast(location, startDay) #returns a list of lists, where each element represents a day with climate, temperature, and rain check.
    return (forecast)
def get_shopping(gender, location,startDay):
    shopResults = wrap_obj.get_shoppingResults(gender, location,startDay)
    return shopResults
