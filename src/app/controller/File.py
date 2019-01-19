'''
Created on 2018/11/18

@author: Tanuki
'''
from flask_restful import Resource
from flask import Request, json
from app.dto import Content, Response
from app.accessor.Contents import Contents
from app.controller import Authorize
from flask import session

class File(Resource):

    def post(self):
        if(not Authorize.is_authorize()):
            return json.dumps(Response("ログインしてください")),500
        
        title = Request.form['title']
        tags = json.loads(Request.form['tags'])
        upload_file = Request.files['upload_file']
        
        content = Content(None,
                          title,
                          tags,
                          upload_file.readlines(),
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

    def put(self):
        if(not Authorize.is_authorize()):
            return json.dumps(Response("ログインしてください")),500
        
        content_id = Request.form['content_id']
        title = Request.form['title']
        tags = json.loads(Request.form['tags'])
        upload_file = Request.files['upload_file']
        
        content = Content(content_id,
                          title,
                          tags,
                          upload_file.readlines(),
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

    def delete(self):
        if(not Authorize.is_authorize()):
            return json.dumps(Response("ログインしてください")),500
        
        content_id = Request.form['content_id']       
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
        