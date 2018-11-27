from flask import Flask
from sqlalchemy import 
from Config import app_config

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy()

class DbConnect():

    def __init__(self):
        app.config.from_object(app_config('development'))
        db.init_app(app)
