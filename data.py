from flask import Blueprint, jsonify, request
from pandas.core.indexes import category

from wrap_backend import Wrap_backend

data = Blueprint('data', __name__)

wrap_obj = Wrap_backend('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', '903e781b4a8c47d9ab4200052231907' ) 

def get_outfits(gender, location, startDay):
    outfits = wrap_obj.get_imageList(gender, location, startDay) #returns a list with strings inside each one being a url a picture
    return outfits

def get_forecast(location, startDay):
    forecast = wrap_obj.getForecast(location, startDay) #returns a list of lists, where each element represents a day with climate, temperature, and rain check.
    return (forecast)