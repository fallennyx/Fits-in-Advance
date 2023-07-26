from flask import Blueprint, jsonify, request
from pandas.core.indexes import category

from wrap_backend import Wrap_backend

data = Blueprint('data', __name__)

wrap_obj = Wrap_backend('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','903e781b4a8c47d9ab4200052231907','2769705d67df11795e20d4fc3a8b28f0bbf7e3cf55ef7e716d1ebef6a39d404f')

def get_outfits(gender, location):
    #OLD!gender = category.args.get('gender')
    #OLD!location = category.args.get('location')
    outfits = wrap_obj.get_imageList(gender, location) #returns a list with strings inside each one being a url a picture
    return outfits

def get_forecast(location):
    #OLD!location = category.args.get('location')
    forecast = wrap_obj.getForecast(location) #returns a list of lists, where each element represents a day with climate, temperature, and rain check.
    return (forecast)