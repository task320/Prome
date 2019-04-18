'''
Created on 2018/11/18

@author: Tanuki
'''
from flask_restful import Resource
from flask import request, json
from app.dto.Content import Content
from app.dto.Response import Response
from app.accessor.Contents import Contents
from app.controller.Login import Login
from flask import session
from app.processor.TextReader import TextReader

class File(Resource):

    @classmethod
    def post(self):        
        title = request.form['title']
        tags = json.loads(request.form['tags'])
        upload_file = TextReader(request.files['upload_file'])
        
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
            return
        else:
            return json.dumps(Response("ERRER")),500

    @classmethod
    def put(self):        
        content_id = request.form['content_id']
        title = request.form['title']
        tags = json.loads(request.form['tags'])
        upload_file = TextReader(request.files['upload_file'])
        
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
            return
        else:
            return json.dumps(Response("ERRER")),500

    @classmethod
    def delete(self):        
        content_id = request.form['content_id']       
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
            return
        else:
            return json.dumps(Response("ERRER")),500
        