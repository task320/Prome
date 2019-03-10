'''
Created on 2018/11/18

@author: Tanuki
'''

from flask_restful import Resource
from flask import Request, json
from app.dto.Response import Response
from app.accessor.Contents import Contents as dao_contents
from app.processor.creator import CreateResponseData
from app.constant.Url import Url

class Contents(Resource, Request):
    '''
    classdocs
    '''
    
    def __init__(self):
        pass
    
    def get(self, proc):
        body_json = self.get_json(True, True, True)
        if(proc == Url.CONTENTS_ONE):
            return self.contents_one(body_json['contents_id'],)
        elif(proc == Url.CONTENTS_ALL):
            if 'current_page' in body_json:
                print("exsist")
            else:
                print("nothing")
            return self.contents_all(body_json['current_page'],)
        
    def contents_one(self, contents_id):        
        dao = dao_contents()
        if(dao.selectContent(contents_id)):
            return json.dumps(CreateResponseData.create_respone_content_data(dao.get_target_content()))
        else:
            return json.dumps(Response("ERRER")),500
        
        
    def contents_all(self, current_page):
        dao = dao_contents()
        if(dao.selectContentAll(current_page)):
            return json.dumps(CreateResponseData.create_respone_contents_data(current_page, dao.get_target_content()))
        else:
            return json.dumps(Response("ERRER")),500 

    
        