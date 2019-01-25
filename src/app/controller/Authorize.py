'''
Created on 2018/11/26

@author: Tanuki
'''

from flask import session
from Config import Config

def is_authorize():
    
    if(Config.DEBUG_AUTH):
        session['user_id'] = 'test_user'
        return True
    else:
        if(session['user_id']):
            return True
        else:
            return False
    