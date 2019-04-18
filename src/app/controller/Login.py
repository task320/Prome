'''
Created on 2018/11/26

@author: Tanuki
'''

from flask import session, request, Response
from app.processor.HtmlRender import HtmlRender
from app.accessor.User import User

class Login():
    @classmethod
    def proccess_login(cls):
        method = request.method
        if method == 'GET':
            return cls.process_get()
        elif  method == 'POST':
            return cls.process_post()

    @staticmethod
    def process_get():
        return Response(
            HtmlRender.render('login.html', None),
            mimetype='text/html',
            content_type='text/html',
            status=200
        )

    @staticmethod
    def process_post():
        user_id = request.form['user_id']
        password = request.form['password']

        user = User()
        proc_result = user.auth(user_id, password)

        if(proc_result):
            if(user.get_count_users() > 0):
                session['auth'] = 1
                return Response(
                    HtmlRender.render('console.html', None),
                    mimetype='text/html',
                    content_type='text/html',
                    status=200
                )
    
        return Response(
            HtmlRender.render('login.html', {'auth_result':'No'}),
            mimetype='text/html',
            content_type='text/html',
            status=200
        )
    