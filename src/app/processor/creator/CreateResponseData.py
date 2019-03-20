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
    
    loop_max_value = number_of_content - 1
    if loop_max_value < 0:
        loop_max_value = 0

    for i in range(0,number_of_content):  
        contents[i].html_content = ConvertHtml(contents[i].content).to_html()
    
    return Response(None, pager, current_page, contents)

def create_respone_content_data(content):
        
    content[0].html_content = ConvertHtml(content[0].content).to_html()
    
    return Response(None, None, None, content)