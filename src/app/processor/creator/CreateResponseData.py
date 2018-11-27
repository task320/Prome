'''
Created on 2018/11/24

@author: Tanuki
'''
from app.dto.Response import Response
from Config import Config
from app.processor.creator.ConvertHtml import ConvertHtml

def create_respone_contents_data(current_page, contents):
    number_of_content =  contents.count()
    
    pager = int(number_of_content / Config.DISPLAY_NUMBER_OF_CONTENTS)
    if((number_of_content % Config.DISPLAY_NUMBER_OF_CONTENTS) > 0):
        pager += 1
    
    for i in (0,contents.count):  
        contents[i].content = ConvertHtml(contents[i].content)
    
    return Response(None, pager, current_page, contents)

def create_respone_content_data(content):
        
    content[0].content = ConvertHtml(content[0].content)
    
    return Response(None, None, None, content)