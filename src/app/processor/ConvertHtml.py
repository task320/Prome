'''
Created on 2018/11/26

@author: Tanuki
'''
import traceback
from markdown import Markdown as md
from flask import Markup

class ConvertHtml:
    '''
    classdocs
    '''
    
    def __init__(self, source):
        self.source = source
        self.md_processor = md()
       
       
    def to_html(self):
        try:
            return Markup.unescape(self.md_processor.convert(self.source))
        except:
            traceback.print_exc()
            return ''