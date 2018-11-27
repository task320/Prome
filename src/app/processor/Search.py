'''
Created on 2018/11/24

@author: Tanuki
'''

from app.accessor.Search import Search
from app.processor.creator import CreateResponseData 

class Search:
    '''
    classdocs
    '''  
    
    __output_data = None
    
    def __init__(self):
        pass
    
    def search_tags(self, tags, current_page):
        accessor = Search()
        
        if(not(accessor.search_tags(self, tags, current_page))):
            return False
        
        self.__output_data = CreateResponseData.create_respone_contents_data(current_page, accessor.get_search_data())
        return True       
      
    def search_title(self, title, current_page):
        accessor = Search()
        
        if(not(accessor.search_title(self, title, current_page))):
            return False
        
        self.__output_data = CreateResponseData.create_respone_contents_data(current_page, accessor.get_search_data())
        return True       
        
    def get_output_data(self):
        return self.__output_data
        