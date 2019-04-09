'''
Created on 2018/11/18

@author: Tanuki
'''
from flask import Response as f_response, request, json
from app.dto.Response import Response
from app.accessor.Contents import Contents as dao_contents
from app.processor.creator import CreateResponseData, HtmlRender
from app.constant.Url import Url


class Contents():
    @classmethod      
    def get(cls, proc):
        if(proc == Url.CONTENTS_ONE):
            contents_id = request.args.get('contents_id')
            return cls.contents_one(contents_id)
        elif(proc == Url.CONTENTS_ALL):
            current_page = int(request.args.get('page'), base=0)
            return cls.contents_all(current_page)
        else:
            return "ERRER",500

    @staticmethod
    def contents_one(contents_id):        
        dao = dao_contents()
        if(dao.selectContent(contents_id)):
            return f_response(
                                HtmlRender.render('index.html', CreateResponseData.create_respone_content_data(dao.get_target_content())),
                                mimetype='text/html',
                                content_type='text/html',
                                status=200
            )
        else:
            return "ERRER",500
    
    @staticmethod
    def contents_all(current_page):
        page_zero_base = current_page - 1
        if(page_zero_base < 0):
            return "ERROR",500

        dao = dao_contents()
        if(dao.countContents() & dao.selectContentAll(page_zero_base)):
            return f_response(
                                HtmlRender.render('index.html', CreateResponseData.create_respone_contents_data(current_page, dao.get_count(), dao.get_target_content())),
                                mimetype='text/html',
                                content_type='text/html',
                                status=200
            )
        else:
            return "ERRER",500 

    
        