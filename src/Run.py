'''
Created on 2018/11/18

@author: Tanuki
'''
import os
from flask import Flask
from Router import router

app = Flask(__name__, 
           instance_relative_config = True)    
#set Config
app.config.from_object(os.getenv('PROME_CONFIG'))
app.register_blueprint(router)
app.secret_key = os.urandom(32)  

if __name__ == '__main__':
    app.run(debug=False)
    
    