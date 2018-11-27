'''
Created on 2018/11/18

@author: Tanuki
'''
from flask import session
from flask_restful import Resource

class Login(Resource):
    def post(self):
        session['user_id'] = 'TEST_MAN'
        return 'SUCCESS'