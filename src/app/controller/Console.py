'''
Created on 2018/11/18

@author: Tanuki
'''
from flask import Response as f_response, request
from app.dto.Response import Response
from app.accessor.Contents import Contents as dao_contents
from app.processor.HtmlRender import HtmlRender


class Console():
    @classmethod
    def main_entrance(cls, proc):
        if(proc == 'list'):
            return cls.list()
        elif(proc == 'edit'):
            return cls.edit()
        else:
            return 'ERROR', 500

    @staticmethod      
    def list():
        contents = dao_contents()
        result = contents.selectContentsList()
        if(result):
            return f_response(
                    HtmlRender.render('console.html', Response(None, None, None, contents.getContentList())),
                    mimetype='text/html',
                    content_type='text/html',
                    status=200
                )
        
        return "ERROR", 500

    @staticmethod      
    def edit():
        content_id = request.args.get('contentId', '')
        contents = dao_contents()
        result = contents.selectContent(content_id)
        if(result):
            return f_response(
                    HtmlRender.render('edit.html', Response(None, None, None, contents.get_target_content())),
                    mimetype='text/html',
                    content_type='text/html',
                    status=200
                )
        
        return "ERROR", 500

    
        