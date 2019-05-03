'''
Created on 2018/11/18

@author: Tanuki
'''
from flask import Response as f_response, request, redirect, url_for
from app.dto.Response import Response
from app.accessor.Contents import Contents as dao_contents
from app.processor import CreateResponseData
from app.processor.HtmlRender import HtmlRender
from app.constant.Url import Url
from app.processor.ConvertType import ConvertType


class Contents():
    @classmethod      
    def get(cls, proc):
        if(proc == Url.CONTENTS_ONE):
            arg_contents_id = request.args.get('contents_id')
            return cls.contents_one(arg_contents_id)
        elif(proc == Url.CONTENTS_ALL):
            arg_current_page = request.args.get('page')
            return cls.contents_all(arg_current_page)
        else:
            return "ERRER",500

    @staticmethod
    def contents_one(arg_contents_id):                
        if ConvertType.possibleConvertStringToInt(arg_contents_id):
            dao = dao_contents()
            if dao.selectContent(ConvertType.convertStringToInt(arg_contents_id)):
                params = CreateResponseData.create_respone_content_data(dao.get_target_content())
                return f_response(
                    HtmlRender.render('index.html', params),
                    mimetype='text/html',
                    content_type='text/html',
                    status=200
                )
        
        return f_response(
            HtmlRender.render('nothing_content.html', None),
            mimetype='text/html',
            content_type='text/html',
            status=200
        )

    @staticmethod
    def contents_all(arg_current_page):
        if(ConvertType.possibleConvertStringToInt(arg_current_page)):
            current_page = ConvertType.convertStringToInt(arg_current_page)
            page_zero_base = current_page - 1
            if not page_zero_base < 0:
                dao = dao_contents()
                if(dao.countContents() & dao.selectContentAll(page_zero_base)):
                    params = CreateResponseData.create_respone_contents_data(current_page, dao.get_count(), dao.get_target_content())
                    return f_response(
                        HtmlRender.render('index.html', params),
                        mimetype='text/html',
                        content_type='text/html',
                        status=200
                    )
        
        return redirect(url_for('router.get_all', proc='all', page=1))

    
        