'''
Created on 2018/11/20

@author: Tanuki
'''
import traceback
from app.accessor.DbConnecter import DbConection
from sqlalchemy.sql import expression, functions
from app.model.Contents import Contents as model_contents
from Config import Config

class Contents(DbConection):
    
    def __init__(self):
        super().__init__()

    def countContents(self):
        try:
            self.count_contents = self.session\
                            .query(model_contents)\
                            .count()
            return True      
        except:
            traceback.print_exc()
        finally:
            self.session.close()
            
        return False
        
    def selectContent(self, contents_id):
        try:
            self.target_data = self.session\
                            .query(model_contents)\
                            .filter_by(id = contents_id)\
                            .first()
           
            if(self.target_data):
                return True             
        except:
            traceback.print_exc()
        finally:
            self.session.close()
            
        return False
    
    def selectContentAll(self, current_page):
        try:
            self.target_data = self.session\
                            .query(model_contents)\
                            .order_by(model_contents.update_at.desc())\
                            .limit(Config.DISPLAY_NUMBER_OF_CONTENTS)\
                            .offset(Config.DISPLAY_NUMBER_OF_CONTENTS * current_page)\
                            .all()
           
            if(len(self.target_data)):
                return True             
        except:
            traceback.print_exc()
        finally:
            self.session.close()
            
        return False
    
    def get_target_content(self):
        return self.target_data

    def get_count(self):
        return self.count_contents

    def insertContent(self, content):
        try:                
            record = model_contents(title = content.title,
                             tags = content.tags, 
                             content = content.content,
                             users_id = content.users_id,
                             upload_at = functions.current_timestamp(),
                             update_at = functions.current_timestamp(),
                             version = 1
                             )
           
            self.session.add(record)
            self.session.commit()
           
            if(record.id):
                return True                
        except:
            self.session.rollback()
            traceback.print_exc()
        finally:
            self.session.close()
            
        return False
            
    def updateContent(self, content):
        try:
            target_data = self.session\
                            .query(model_contents)\
                            .filter_by(id = content.id)\
                            .first()
                            
            target_data.title = content.title
            target_data.tags =  content.tags
            target_data.content = content.content
            target_data.update_at = functions.current_timestamp()
            target_data.version += 1
           
            self.session.add(target_data)
            self.session.commit()
            return True
        except:
            self.session.rollback
            traceback.print_exc()
        finally:
            self.session.close()
            
        return False
    
    def deleteContent(self, content):
        try:
            target_data = self.session\
                            .query(model_contents)\
                            .filter_by(id = content.id)\
                            .first()
           
            self.session.delete(target_data)
            self.session.commit()
            return True
        except:
            self.session.rollback
            traceback.print_exc()
        finally:
            self.session.close()
            
        return False

    def selectContentsList(self):
        try:
            self.target_data = self.session\
                            .query(model_contents.id, model_contents.title, model_contents.tags, model_contents.update_at, model_contents.upload_at)\
                            .order_by(model_contents.update_at.desc())\
                            .all()
            return True             
        except:
            traceback.print_exc()
        finally:
            self.session.close()
            
        return False

    def getContentList(self):
        return self.target_data
    
    