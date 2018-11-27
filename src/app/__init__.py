from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.controller.Search import Search
from app.controller.Contents import Contents
from app.controller.File import File
import Config

def create_app(config_name):    
    app = Flask(__name__, instance_relative_config=True)    
    #set Config
    app.config.from_object(Config)
    
    api = Api(app)
    CORS(app)

    #routing  
    api.add_resource(Search,'/api/search/<proc>')
    api.add_resource(File,'/api/file')
    api.add_resource(Contents,'/api/content')
    
    return app;
    
    
