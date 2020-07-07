'''
Created on 2018/11/18

@author: Tanuki
'''
from flask import session, url_for, redirect
from app.constant.Url import Url

class User():
    def logout(self, proc):
        session.pop('user_id', None)
            
        return redirect(url_for('router.get_all', proc='all', page='1'))