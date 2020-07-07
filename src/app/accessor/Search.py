'''
Created on 2018/11/24

@author: Tanuki
'''
import traceback
from app.accessor.DbConnecter import DbConection
from app.model.Contents import Contents as model_contents
from sqlalchemy.sql import expression
from AppConfig import Config

class Search(DbConection):
    '''
    classdocs
    '''

    __search_data = None

    def __init__(self):
        super.__init__()
        
    def search_tags(self, tags, current_page):
        try:
            target_data = self.session\
                    .query(model_contents)\
                    .filter(model_contents.tags.contains(expression.bindparam(tags)))\
                    .limit(Config.DISPLAY_NUMBER_OF_CONTENTS)\
                    .offset(Config.DISPLAY_NUMBER_OF_CONTENTS * current_page)
            self.__search_data = target_data
            return True
        except:
            traceback.print_exc()
        finally:
            self.session.close()
            
        return False
    
    def search_title(self, title, current_page):
        try:
            target_data = self.session\
                    .query(model_contents)\
                    .filter(model_contents.title.like(expression.bindparam('%' + expression.bindparam(title) + '%')))\
                    .limit(Config.DISPLAY_NUMBER_OF_CONTENTS)\
                    .offset(Config.DISPLAY_NUMBER_OF_CONTENTS * current_page)
            self.__search_data = target_data
            return True
        except:
            traceback.print_exc()
        finally:
            self.session.close()
            
        return False
    
    def get_search_data(self):
        return self.__search_data