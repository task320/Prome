from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.controller.Search import Search
from app.controller.Contents import Contents
from app.controller.User import User
from app.controller.File import File
import Config
import os
from flask_cors.core import get_allow_headers

def create_app(config_name):    
    app = Flask(__name__, instance_relative_config=True)    
    #set Config
    app.config.from_object(Config)
    app.secret_key = os.urandom(32)
    
    api = Api(app)
    CORS(app, 
         resource = {r'/api/*':{"origins":"*"},
                    r'/contents/*':{"origins":"*"}})

    #routing  
    api.add_resource(Search,'/search/<string:proc>')
    api.add_resource(File,'/api/file')
    api.add_resource(Contents,'/contents/<string:proc>')
    api.add_resource(User,'/api/user/<proc>')
    
    return app
    
    
