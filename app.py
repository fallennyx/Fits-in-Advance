import os

from flask_cors import CORS

from data import get_outfits, get_forecast, get_shopping
from flask import Blueprint, render_template, session, request, jsonify, Flask, flash
import json
from __init__ import create_app, db
from models import User  # Import the User model from your models.py file

app = create_app()
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


@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        #query the database for user 
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    #render login template
    return render_template("login.html", user=current_user)

#route for logging out
@views.route('/logout')
def logout():
    return "<p>Logout</p>"

#route for signing up
@views.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #query the database for user 
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            #add user to database
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    #render sign up template
    return render_template("sign_up.html", user="Ani")

@views.route("/x", methods=["GET", "POST"])
def get_data_from_results():
    if request.method == "POST":
        try:
            data = request.get_json()  # Use request.get_json() to parse JSON data
            city = data.get("city")
            gender = data.get("gender")
            startDay = data.get("startDay", 0)  # Use 0 as the default value if startDay is not provided
            forecast = get_forecast(city, startDay)
            outfits = get_outfits(gender, city, startDay)
            shopping=get_shopping(gender,city)
            datadic = {"forecast": forecast, "outfits": outfits,"shopping":shopping}
            return jsonify(datadic)
        except Exception as e:
            return jsonify({"error": str(e)}), 400
app.register_blueprint(views, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

