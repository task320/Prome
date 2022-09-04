'''
Created on 2018/11/24

@author: Tanuki
'''
from app.dto.Response import Response
from app.model.TwitterCardSummary import TwitterCardSummary
from AppConfig import Config
from app.processor.ConvertHtml import ConvertHtml

def create_respone_contents_data(current_page, number_of_content, contents):
        
    pager = int(number_of_content / Config.DISPLAY_NUMBER_OF_CONTENTS)
    if((number_of_content % Config.DISPLAY_NUMBER_OF_CONTENTS) > 0):
        pager += 1
    
    loop_max_value = len(contents)

    for i in range(0,loop_max_value):  
        contents[i].html_content = ConvertHtml(contents[i].content).to_html()
    
    return Response(None, pager, current_page, contents)

def create_respone_content_data(content):
        
    content[0].html_content = ConvertHtml(content[0].content).to_html()
    twitterCard =  TwitterCardSummary(content[0])
    
    return Response(None, None, None, content, twitterCard)

def create_respone_edit_content_data(content):
        
    content[0].html_content = ConvertHtml(content[0].content).to_html()

    return Response(None, None, None, content[0])