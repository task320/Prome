'''
Created on 2019/01/23

@author: Tanuki
'''

import traceback

class TextReader(object):
    '''
    classdocs
    '''

    __text_file__ = None

    def __init__(self, text_file):
        self.__text_file__ = text_file
            
            
    def to_utf8(self):
        try:
            str_lines = ''
            for line in self.__text_file__.readlines():
                str_lines += line.decode('utf-8')
            return str_lines
        
        except:
            traceback.print_exc()
        
        return None    
