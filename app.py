import os

from flask_cors import CORS

from data import get_outfits, get_forecast
from flask import Blueprint, render_template, session, request, jsonify, Flask
import json

app = Flask(__name__)
CORS(app)

# Define the views blueprint
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



@views.route("/x", methods=["GET", "POST"])
def get_data_from_results():
    if request.method == "POST":
        try:
            data = request.get_json()  # Use request.get_json() to parse JSON data

            city = data.get("city")
            gender = data.get("gender")

            forecast = get_forecast(city)
            #outfit=get_outfits(gender,location)
            #return outfit too when open ai key fixed
            return (forecast)
        except Exception as e:
            return jsonify({"error": str(e)}), 400
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
