from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    # Relative imports for all the views
    from .views import views
    
    # Blueprint for each of the views, the prefix is set to none, can set to other if need be
    app.register_blueprint(views)
    
    return app
        