'''
Created on 2018/11/18

@author: Tanuki
'''
from flask_restful import Resource
from flask import Request, json
from app.dto.Response import Response
from app.constant.Url import Url
from app.accessor.Search import Search as proc_serach
from app.processor import CreateResponseData


class Search(Resource):
    def get(self, proc):
        body_json = Request.get_json(self)
        if(proc == Url.SEARCH_TAG):
            return self.search_tag(body_json['tags'], body_json['current_page'])
        elif(proc == Url.SEARCH_TITLE):
            return self.search_title(body_json['title'], body_json['current_page'])
            
    def search_tag(self, tags, current_page):
        proc = proc_serach()
        if(proc.search_tags(tags, current_page)):
            return json.dumps(CreateResponseData.create_respone_contents_data(current_page, proc.get_search_data()))
        else:
            return json.dumps(Response("ERRER")),500
        
    def search_title(self, title, current_page):
        proc = proc_serach()
        if(proc.search_title(title, current_page)):
            return json.dumps(CreateResponseData.create_respone_contents_data(current_page, proc.get_search_data()))
        else:
            return json.dumps(Response("ERRER")),500