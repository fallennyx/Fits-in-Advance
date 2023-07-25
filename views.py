import os
from data import get_outfits, get_forecast
from flask import Blueprint, render_template, session, request, jsonify

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/generator")
def generator():
    return render_template("generator.html")

@views.route("/style")
def style():
    return render_template("style.html")

@views.route("/results")
def results():
    return render_template("results.html")

@views.route("/get_data_from_results", methods=["POST"])
def get_data_from_results():
    data = request.json
    city = data.get("city")
    gender = data.get("gender")

    # Call functions with the input data and get the results
    outfits = get_outfits(gender,city)
    forecast = get_forecast(city)
    result_data = {
           "outfits": outfits,
           "forecast": forecast
       }
    return result_data
