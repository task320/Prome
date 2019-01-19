'''
Created on 2018/11/18

@author: Tanuki
'''
from flask import session
from flask_restful import Resource
from app.constant.Url import Url

class User(Resource):
    def post(self, proc):
        if(proc == Url.USER_LOGIN):
            session['user_id'] = 'TEST_MAN'
        elif(proc == Url.USER_LOGOUT):
            session.pop('user_id', None)
            
        return 'SUCCESS'