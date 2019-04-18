import traceback
from app.accessor.DbConnecter import DbConection
from app.model.Users import Users
from sqlalchemy.sql import expression
from Config import Config
from app.processor.Cryptor import Cryptor

class User(DbConection):

    def __init__(self):
        super().__init__()

    def auth(self, user_id, password):
        try:
            hash = Cryptor.output_sha256(user_id, password)
            self.count_users = self.session\
                            .query(Users)\
                            .filter_by(auth_string = hash)\
                            .count()
            return True             
        except:
            traceback.print_exc()
        finally:
            self.session.close()
            
        return False
    
    def get_count_users(self):
        return self.count_users