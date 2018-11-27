'''
Created on 2018/11/23

@author: Tanuki
'''

class Response:

    def __init__(self, message, pager=None, current_page=None, contents=None):
        self.message = message
        if not(pager is None):
            self.pager = pager
        if not(current_page is None):
            self.current_page = current_page
        if not(contents is None):
            self.contents = contents
        
        