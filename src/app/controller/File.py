'''
Created on 2018/11/18

@author: Tanuki
'''
from flask import request, url_for, redirect, session, json
from app.dto.Content import Content
from app.dto.Response import Response
from app.accessor.Contents import Contents
from app.processor.TextReader import TextReader

class File():
    @classmethod
    def main_entrance(cls, proc):
        if(proc == 'post'):
            return cls.post()
        elif(proc == 'put'):
            return cls.put()
        elif(proc == 'delete'):
            return cls.delete()
        else:
            return 'ERROR', 500

    @staticmethod
    def post():        
        title = request.form['title']
        tags = json.loads(request.form['tags'])
        upload_file = TextReader(request.files['uploadFile'])
        
        content = Content(None,
                          title,
                          tags,
                          upload_file.to_utf8(),
                          session['user_id'],
                          None,
                          None,
                          None)
        
        dao = Contents()
        result = dao.insertContent(content)
         
        if(result):
            return redirect(url_for('router.console', proc='list'))
        else:
            return "ERRER", 500

    @staticmethod
    def put():        
        content_id = request.form['contentId']
        title = request.form['title']
        tags = json.loads(request.form['tags'])
        upload_file = TextReader(request.files['uploadFile'])
        
        content = Content(content_id,
                          title,
                          tags,
                          upload_file.to_utf8(),
                          session['user_id'],
                          None,
                          None,
                          None)
        
        dao = Contents()
        result = dao.updateContent(content)
         
        if(result):
            return redirect(url_for('router.console', proc='list'))
        else:
            return "ERRER", 500

    @staticmethod
    def delete():        
        content_id = request.form['contentId']       
        content = Content(content_id,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None,
                          None)
        
        dao = Contents()
        result = dao.deleteContent(content)
         
        if(result):
            return redirect(url_for('router.console', proc='list'))
        else:
            return "ERRER", 500
        