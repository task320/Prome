'''
Created on 2018/11/26

@author: Tanuki
'''

from flask import session

def is_authorize():
    if(session['user_id']):
        return True
    else:
        return False