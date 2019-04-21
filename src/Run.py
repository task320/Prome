'''
Created on 2018/11/18

@author: Tanuki
'''
import os
from flask import url_for, Flask, request, session, redirect
from app.controller.Contents import Contents
from app.controller.Search import Search
from app.controller.User import User
from app.controller.File import File
from app.controller.Login import Login
from app.controller.Console import Console
import Config
import os


app = Flask(__name__, 
           instance_relative_config = True)    
#set Config
app.config.from_object(os.getenv('PROME_CONFIG'))
app.secret_key = os.urandom(32)  

@app.route('/contents/<proc>', methods=['GET'])
def get_all(proc):
    return Contents.get(proc)

@app.route('/login', methods=['GET','POST'])
def login():
        return Login.proccess_login()

@app.route('/console/<proc>', methods=['GET'])
def console(proc):
        return Console.main_entrance(proc)

@app.route('/file/<proc>', methods=['POST'])
def file(proc):
        return File.main_entrance(proc)

@app.before_request
def confirmAuthorization():
        endpoint = request.endpoint
        if endpoint == 'console' or endpoint == 'file':
                if not 'user_id' in session:
                        return redirect(url_for('login'))





if __name__ == '__main__':
    app.run(debug=True)
    
    