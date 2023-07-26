from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#name database
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db.init_app(app)

    with app.app_context():
        import models  # Import the models module here
        db.create_all()  # Create all database tables


    return app
