'''
Created on 2018/11/18

@author: Tanuki
'''

from flask_restful import Resource
from flask import Request, json
from app.dto import Response
from app.accessor.Contents import Contents as dao_contents
from app.processor.creator import CreateResponseData

class Contents(Resource):
    '''
    classdocs
    '''
    
    def get(self):        
        body_json = Request.get_json
        dao = dao_contents()
        if(dao.selectContent(body_json['contents_id'])):
            return json.dumps(CreateResponseData.create_respone_content_data(dao.get_target_content()))
        else:
            return json.dumps(Response("ERRER")),500

    
        